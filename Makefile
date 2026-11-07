.DEFAULT_GOAL := check

DF12_WWW ?= ../df12-www
PYTHON ?= python3

MDLINT ?= markdownlint-cli2
NIXIE ?= nixie

# `make fmt` and `make check-fmt` call mdtablefix directly. `--git` selects the
# Markdown files Git tracks and `--include-untracked` adds the untracked files
# Git does not ignore, so a new document is formatted before it is staged.
# Both modes need mdtablefix 0.6.1 or later.
MDTABLEFIX ?= mdtablefix
MDTABLEFIX_SELECT = --git --include-untracked
MDTABLEFIX_RULES = --wrap --renumber --breaks --ellipsis --fences

.PHONY: build check check-fmt dev fmt install-dev lint markdownlint nixie \
	preview serve-preview typecheck validate

check: check-fmt lint typecheck markdownlint nixie build validate

build:
	bun run build

install-dev:
	bun install --frozen-lockfile
	uv sync --project $(DF12_WWW) --group dev --locked

dev: install-dev
	bun run dev

check-fmt:
	bun run check:fmt
	$(MDTABLEFIX) --check $(MDTABLEFIX_SELECT) $(MDTABLEFIX_RULES)

fmt:
	bun run fmt
	$(MDTABLEFIX) --in-place $(MDTABLEFIX_SELECT) $(MDTABLEFIX_RULES)
	$(MDLINT) --fix "**/*.md"

# The repository's Python is the site renderer and validator under scripts/.
# Interrogate scans each target recursively, subject to its default exclusions.
INTERROGATE_VERSION ?= 1.7.0
INTERROGATE_TARGETS ?= scripts
# Level 2 prints a MISSED row per undocumented definition, which the
# `interrogate` recipe below looks for: the rounded percentage alone can pass a
# lone gap.
INTERROGATE_FLAGS ?= -vv --fail-under 100
INTERROGATE ?= uv tool run --python 3.13 --from 'interrogate==$(INTERROGATE_VERSION)' interrogate

# Interrogate rounds its percentage to one decimal, so `--fail-under 100` alone
# can pass a lone gap in a large repository. This recipe also fails when `grep`
# finds a MISSED row in the report on standard output, which `-vv` or higher
# prints for each undocumented definition.
.PHONY: interrogate
interrogate: ## Enforce complete Python docstring coverage
	@report="$$($(INTERROGATE) $(INTERROGATE_FLAGS) $(INTERROGATE_TARGETS))"; \
	  status=$$?; \
	  printf '%s\n' "$$report"; \
	  test "$$status" -eq 0 || exit "$$status"; \
	  if printf '%s\n' "$$report" | grep -q '| *MISSED *|'; then \
	    printf '%s\n' 'interrogate: undocumented definitions remain; see the MISSED rows above' >&2; \
	    exit 1; \
	  fi

lint:
	$(MAKE) --no-print-directory interrogate
	bun run lint

typecheck:
	bun run typecheck

markdownlint: ## Lint Markdown files
	bun run markdownlint

nixie: ## Validate Mermaid diagrams
	$(NIXIE) .

preview: build
	uv run --project $(DF12_WWW) python scripts/render-framework.py \
		--df12-www $(DF12_WWW)

validate: preview
	$(PYTHON) scripts/validate_site.py

serve-preview: preview
	$(PYTHON) -m http.server 8080 --directory .preview
