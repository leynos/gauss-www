"""Validate the rendered Gauss preview."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

INTERNAL_HREF = re.compile(r'href="(/gauss/[^"#?]*)(?:[#?][^"]*)?"')
FRAGMENT_HREF = re.compile(r'href="(/gauss/[^"#?]*)?#([^"]+)"')
ID_ATTR = re.compile(r'\sid="([^"]+)"')
STATUS_ATTR = re.compile(r'data-status="([^"]+)"')
H1 = re.compile(r"<h1[\s>]")
SKIP_LINK = re.compile(r'class="[^"]*skip-link[^"]*"')
LANG = re.compile(r'<html lang="en-GB"')
IMG = re.compile(r"<img\b[^>]*>")
ALT = re.compile(r'\salt="[^"]*"')

VALID_STATUSES = frozenset({"shipped", "partial", "planned"})
VAGUE_LINK_TEXT = frozenset(
    {"here", "click here", "read more", "more", "learn more", "this", "link"}
)
LINK_TEXT = re.compile(r"<a\b[^>]*>(.*?)</a>", re.S)
TAGS = re.compile(r"<[^>]+>")


def routes_from(preview: Path) -> set[str]:
    """Return every published preview route as a site-absolute path."""
    routes: set[str] = set()
    for page in preview.rglob("index.html"):
        relative = page.parent.relative_to(preview.parent).as_posix()
        routes.add(f"/{relative}/".replace("//", "/"))
    return routes


def route_of(page: Path, preview: Path) -> str:
    """Return the site-absolute route published by ``page``."""
    relative = page.parent.relative_to(preview.parent).as_posix()
    return f"/{relative}/".replace("//", "/")


def check_page(
    page: Path, routes: set[str], preview: Path, ids_by_route: dict[str, set[str]]
) -> list[str]:
    """Return validation problems found in one rendered page."""
    html = page.read_text(encoding="utf-8")
    where = page.parent.relative_to(preview).as_posix() or "."
    problems: list[str] = []

    for href in INTERNAL_HREF.findall(html):
        target = href if href.endswith("/") else f"{href}/"
        if target not in routes and not (preview.parent / href.lstrip("/")).exists():
            problems.append(f"{where}: link to unknown route {href}")

    own_route = route_of(page, preview)
    for path, fragment in FRAGMENT_HREF.findall(html):
        target_route = path if path else own_route
        if not target_route.endswith("/"):
            target_route = f"{target_route}/"
        target_ids = ids_by_route.get(target_route)
        if target_ids is None:
            problems.append(f"{where}: fragment link into unknown route {path}")
        elif fragment not in target_ids:
            problems.append(
                f"{where}: link to missing fragment #{fragment} on {target_route}"
            )

    for status in STATUS_ATTR.findall(html):
        if status not in VALID_STATUSES:
            problems.append(f"{where}: invalid status value {status!r}")

    heading_count = len(H1.findall(html))
    if heading_count != 1:
        problems.append(f"{where}: expected exactly one h1, found {heading_count}")
    if not SKIP_LINK.search(html):
        problems.append(f"{where}: missing skip link")
    if not LANG.search(html):
        problems.append(f"{where}: missing or unexpected html lang attribute")

    duplicates = [
        element
        for element, count in Counter(ID_ATTR.findall(html)).items()
        if count > 1
    ]
    for element in duplicates:
        problems.append(f"{where}: duplicate id {element!r}")

    for tag in IMG.findall(html):
        if ALT.search(tag) is None:
            problems.append(f"{where}: image without an alt attribute")

    for raw in LINK_TEXT.findall(html):
        text = TAGS.sub(" ", raw)
        text = re.sub(r"\s+", " ", text).strip().lower().rstrip(".")
        if text in VAGUE_LINK_TEXT:
            problems.append(f"{where}: uninformative link text {text!r}")

    return problems


def main(argv: list[str] | None = None) -> int:
    """Validate every rendered page under the preview directory."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview", type=Path, default=Path(".preview/gauss"))
    args = parser.parse_args(argv)

    if not args.preview.is_dir():
        print(
            f"No rendered preview at {args.preview}. Run `make preview` first.",
            file=sys.stderr,
        )
        return 1

    routes = routes_from(args.preview)
    pages = sorted(args.preview.rglob("index.html"))
    ids_by_route = {
        route_of(page, args.preview): set(
            ID_ATTR.findall(page.read_text(encoding="utf-8"))
        )
        for page in pages
    }

    problems: list[str] = []
    for page in pages:
        problems.extend(check_page(page, routes, args.preview, ids_by_route))

    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        print(f"\n{len(problems)} problems across {len(pages)} pages.", file=sys.stderr)
        return 1

    print(f"Validated {len(pages)} pages and {len(routes)} routes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
