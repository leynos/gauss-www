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

lint:
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
