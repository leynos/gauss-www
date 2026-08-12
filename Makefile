.PHONY: markdownlint nixie

MDLINT ?= markdownlint-cli2
NIXIE ?= nixie

markdownlint: ## Lint Markdown files
	$(MDLINT) "**/*.md"

nixie: ## Validate Mermaid diagrams
	$(NIXIE) .
