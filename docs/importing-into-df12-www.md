# Importing the Gauss framework into df12-www

## Purpose

The framework uses the same source layers as a native `df12_pages` subsite.
Importing it adds one dedicated ahead-of-time Tailwind entrypoint, not a second
renderer or browser runtime.

## Source mapping

| This repository | df12-www destination | Role |
| --- | --- | --- |
| `config/gauss.yaml` | `config/pages.yaml` beneath `sites:` | Routes, navigation, and template variables |
| `templates/gauss/` | `templates/gauss/` | Homepage, roadmap, shared chrome, and legal wrapper |
| `src/styles/gauss.css` | `src/styles/gauss.css` | Tailwind v4 and daisyUI v5 entrypoint |
| `src/static/gauss/` | `src/static/gauss/` | Logo and future self-hosted assets |

The configuration file contains the `gauss:` mapping itself. Merge it beneath
the existing `sites:` mapping in `config/pages.yaml`.

## Parent build integration

Add a Gauss CSS build beside the existing mxd entrypoint in
`df12-www/package.json`:

```json
{
  "scripts": {
    "build:css": "bunx tailwindcss -i ./src/styles/site.css -o ./public/assets/site.css --minify && bun run build:css:mxd && bun run build:css:gauss",
    "build:css:gauss": "bunx tailwindcss -i ./src/styles/gauss.css -o ./public/gauss/assets/tailwind.css --minify"
  }
}
```

The stylesheet uses CSS-first Tailwind v4 configuration, explicit `@source`
discovery for Jinja, and a custom daisyUI v5 theme. Do not add a
`tailwind.config.js` or a browser CDN.

## Import procedure

1. Copy `templates/gauss/` into `df12-www/templates/gauss/`.
2. Copy `src/styles/gauss.css` into `df12-www/src/styles/gauss.css`.
3. Copy `src/static/gauss/` into `df12-www/src/static/gauss/`.
4. Merge `config/gauss.yaml` beneath `sites:` in
   `df12-www/config/pages.yaml`.
5. Add the `build:css:gauss` parent script described above.
6. Confirm `terms-of-use`, `privacy-policy`, and `code-of-conduct` remain
   defined in the parent shared-content mapping.
7. Build through the normal parent pipeline:

   ```bash
   bun run build
   uv run pages generate --site gauss
   ```

8. Inspect `public/gauss/` at narrow and wide viewports, then run the parent
   template, JavaScript, accessibility, Markdown, and repository gates.

## Local contract preview

With `../df12-www` available:

```bash
make preview
```

The build compiles CSS to `.build/`, composes temporary parent configuration,
and renders to `.preview/gauss/`. It does not modify `../df12-www` or write to a
tracked generated tree.

Serve the result with:

```bash
make serve-preview
```

For continuous rebuilds with the same watcher/server topology as the parent:

```bash
make dev
```

Override the default port with `DF12_PORT=8090 make dev`.

## Framework boundaries

- Semantic HTML, daisyUI components, Tailwind utilities, and Gauss semantic
  wrappers form the style stack.
- Required assets are local. The published site makes no third-party browser
  request.
- Shared legal prose remains owned by df12 and renders through Gauss chrome.
- Navigation and content remain complete without JavaScript.
- `.build/`, `.preview/`, and parent `public/` trees are generated output.
