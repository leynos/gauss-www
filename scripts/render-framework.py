"""Render the Gauss framework through a sibling df12-www checkout."""

from __future__ import annotations

import argparse
import copy
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML


YAML_LOADER = YAML(typ="safe")


def parse_args() -> argparse.Namespace:
    """Parse command-line paths for the framework renderer.

    Returns
    -------
    argparse.Namespace
        Resolved command-line arguments for the df12 checkout and output tree.

    Examples
    --------
    Render with the conventional sibling checkout::

        python scripts/render-framework.py
    """
    parser = argparse.ArgumentParser(
        description="Render the import-ready Gauss subsite with df12_pages."
    )
    parser.add_argument(
        "--df12-www",
        type=Path,
        default=Path("../df12-www"),
        help="Path to the df12-www checkout.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(".preview/gauss"),
        help="Generated preview output directory.",
    )
    return parser.parse_args()


def load_mapping(path: Path) -> dict[str, Any]:
    """Load one YAML mapping from ``path``.

    Parameters
    ----------
    path : pathlib.Path
        YAML document to read.

    Returns
    -------
    dict[str, Any]
        Parsed top-level mapping.

    Raises
    ------
    ValueError
        Raised when the document does not contain a mapping.
    """
    payload = YAML_LOADER.load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        message = f"Expected a YAML mapping in {path}"
        raise ValueError(message)
    return payload


def compose_config(
    *, repo_root: Path, df12_root: Path, output_dir: Path
) -> dict[str, Any]:
    """Compose an isolated df12 configuration containing the Gauss site.

    Parameters
    ----------
    repo_root : pathlib.Path
        Root of this Gauss framework repository.
    df12_root : pathlib.Path
        Root of the sibling df12-www checkout.
    output_dir : pathlib.Path
        Destination for generated preview files.

    Returns
    -------
    dict[str, Any]
        Complete df12 configuration with the Gauss site injected.
    """
    base = load_mapping(df12_root / "config/pages.yaml")
    fragment = load_mapping(repo_root / "config/gauss.yaml")
    shared_content = base.get("shared_content", {})
    if not isinstance(shared_content, dict):
        message = "df12 config 'shared_content' value must be a mapping"
        raise ValueError(message)
    for shared_page in shared_content.values():
        if isinstance(shared_page, dict) and isinstance(shared_page.get("source"), str):
            shared_page["source"] = str((df12_root / shared_page["source"]).resolve())

    site_payload = fragment.get("gauss")
    if not isinstance(site_payload, dict):
        message = "config/gauss.yaml must contain a 'gauss' mapping"
        raise ValueError(message)

    site = copy.deepcopy(site_payload)
    site["output_dir"] = str(output_dir.resolve())
    site["templates_dir"] = str((repo_root / "templates/gauss").resolve())
    site["static_assets_dir"] = str((repo_root / ".build/gauss/assets").resolve())

    sites = base.setdefault("sites", {})
    if not isinstance(sites, dict):
        message = "df12 config 'sites' value must be a mapping"
        raise ValueError(message)
    sites["gauss"] = site
    return base


def render_framework(repo_root: Path, df12_root: Path, output_dir: Path) -> None:
    """Render the framework with the installed df12 ``pages`` command.

    Parameters
    ----------
    repo_root : pathlib.Path
        Root of this Gauss framework repository.
    df12_root : pathlib.Path
        Root of the sibling df12-www checkout.
    output_dir : pathlib.Path
        Disposable generated preview destination.

    Raises
    ------
    FileNotFoundError
        Raised when the sibling checkout or ``pages`` executable is missing.
    subprocess.CalledProcessError
        Raised when df12_pages rejects the config or templates.
    """
    if not (df12_root / "AGENTS.md").is_file():
        message = f"Not a df12-www checkout: {df12_root}"
        raise FileNotFoundError(message)

    pages_command = shutil.which("pages")
    if pages_command is None:
        message = "The df12_pages 'pages' command is not available on PATH"
        raise FileNotFoundError(message)

    resolved_output = output_dir.resolve()
    if resolved_output.exists():
        shutil.rmtree(resolved_output)
    resolved_output.parent.mkdir(parents=True, exist_ok=True)

    config = compose_config(
        repo_root=repo_root,
        df12_root=df12_root,
        output_dir=resolved_output,
    )
    with tempfile.TemporaryDirectory(prefix="gauss-framework-") as temp_dir:
        config_path = Path(temp_dir) / "pages.yaml"
        yaml_writer = YAML()
        yaml_writer.default_flow_style = False
        yaml_writer.width = 100
        with config_path.open("w", encoding="utf-8") as config_file:
            yaml_writer.dump(config, config_file)
        subprocess.run(
            [
                pages_command,
                "generate",
                "--config",
                str(config_path),
                "--site",
                "gauss",
            ],
            cwd=df12_root,
            check=True,
        )

    print(f"Rendered Gauss framework to {resolved_output}")


def main() -> None:
    """Render the Gauss framework from command-line arguments."""
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    render_framework(repo_root, args.df12_www.resolve(), args.output.resolve())


if __name__ == "__main__":
    main()
