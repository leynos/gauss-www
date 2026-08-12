.DEFAULT_GOAL := check

DF12_WWW ?= ../df12-www
PYTHON ?= python3

MDLINT ?= markdownlint-cli2
NIXIE ?= nixie

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

fmt:
	bun run fmt

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
