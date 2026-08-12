# Gauss website design brief

## 1. Project

Create a product website for **Gauss**, the open-source vector illustration application at `leynos/gauss`, as a new df12 Productions sub-site at `/gauss/`.

Gauss is currently a Phase 0 proof of concept built in Rust with GPUI. The working application supports path drawing and manipulation, SVG import/export, styling, undo/redo, and separate selection history.

The larger product direction is substantially more ambitious: a professional SVG illustration environment in which accessibility, localizability, performance, and pervasive scripting form part of the architecture from the beginning. The roadmap targets Illustrator 10-level breadth while explicitly avoiding a bolt-on approach to accessibility or automation.

The website should therefore present **the product Gauss is becoming without pretending that the roadmap has already shipped**.

---

## 2. Core positioning

### Recommended proposition

> **Vector illustration, open all the way down.**

Gauss should not position itself primarily as “an Illustrator clone written in Rust”. Illustrator parity is useful as a scope benchmark, but weak as a product identity.

The stronger idea is:

**One vector document, with no privileged way to operate it.**

A pointer, keyboard, assistive technology, script, and eventually an agent should all address the same underlying document and command model.

That gives Gauss three unusually coherent promises:

1. **Open document**
   SVG is a first-class interchange format rather than an export afterthought.

2. **Open interface**
   Accessibility and keyboard operation belong in the application architecture rather than a compatibility layer added later.

3. **Open automation**
   User-visible operations should have scriptable equivalents, allowing repeatable workflows and eventual agent control without screen-scraping the GUI.

The site should repeatedly return to this idea.

### Suggested hero copy

#### Eyebrow

`OPEN-SOURCE VECTOR ILLUSTRATION · PHASE 0`

#### Headline

> **Vector illustration, open all the way down.**

#### Supporting copy

> Gauss is an open-source SVG editor being built so direct manipulation, keyboard and assistive technology, and scripts can operate on the same document model. Precision drawing without a privileged input method.

#### Primary CTA

`Explore Gauss`

#### Secondary CTA

`View source on GitHub`

Below the CTAs, show an explicit status rail:

`Phase 0 proof of concept` · `Rust + GPUI` · `SVG import/export` · `ISC licensed`

Do not bury the development status in a roadmap page.

---

## 3. Relationship to the existing df12 sites

Gauss should belong unmistakably to df12 without inheriting a generic df12 product template.

The existing product sites establish a useful pattern:

* **Netsuke** turns its build-system concept into tactile Japanese craft, carved wood and careful material detail.
* **Weaver** translates code-agent infrastructure into blueprint, loom and architectural drawing language.
* **mxd** combines protocol engineering with a railway/night-travel visual system and exposes implementation status rather than disguising incomplete compatibility.
* **Stilyagi** uses a highly individual editorial/poster language while organizing substantial technical material underneath it.

The common df12 grammar is therefore not shared colours or interchangeable cards. It is:

**strong metaphor + serious technical substance + unusually specific copy + visible engineering evidence.**

That also fits the parent site, whose stated identity is “Serious tools, playful worlds” and “Fast, elegant, and open by design.”

Gauss should be the **precision instrument** in that collection.

---

## 4. Creative concept: The Coordinate Atelier

The visual language should combine:

* a professional vector-design studio;
* an engineering drawing board;
* mathematical typesetting;
* plotter and registration graphics;
* the visible anatomy of Bézier geometry.

Think **drafting table rather than mathematics department**.

The reference to Gauss should remain cultured and oblique. Avoid portraits of Carl Friedrich Gauss, giant equations, or an endless parade of normal-distribution curves. A bell curve as the principal logo would make the application look like statistics software.

Instead, use the visual artefacts that vector artists and engineers already share:

* anchor points;
* Bézier handles;
* coordinate grids;
* rulers;
* dimensions;
* snapping guides;
* bounding boxes;
* control points;
* registration marks;
* crop marks;
* SVG path data;
* layers and object trees.

The website should feel as though somebody has temporarily left a beautifully typeset technical drawing open on a vector workstation.

---

## 5. Hero art direction

The hero should contain a **real piece of vector artwork**, not merely a screenshot of application chrome.

Ideally, create a canonical abstract “Gauss specimen” using only capabilities that Gauss genuinely supports at launch: paths, Bézier curves, solid fills and strokes.

Then:

1. render the finished artwork prominently;
2. expose several selected paths, handles and anchor points around part of it;
3. place the actual Gauss application around or behind the artwork;
4. optionally let visitors switch between `ARTWORK`, `PATHS`, `SVG` and later `ACCESSIBILITY` views.

This gives the site a wonderful piece of dogfooding:

> **Made with Gauss.**

Provide the specimen SVG for download.

As Gauss grows, the specimen can grow with it. Typography, gradients, compound paths and effects can visibly enter the artwork when those capabilities become real.

That makes the homepage itself a quiet visual changelog.

---

## 6. Signature visual motif

Use an oversized editable curve as the recurrent graphic device.

For example, a broad cobalt curve might enter from the left edge, pass through two visible nodes and leave at the lower right. Handles, coordinates and dimensions can appear around it:

`P₀  124,86`
`C₁  212,28`
`C₂  376,240`

The curve can reappear throughout the site in different states:

* raw geometry in technical sections;
* filled shape in visual sections;
* SVG path text in scripting sections;
* highlighted accessible object in accessibility sections.

It becomes a metaphor for the central thesis: **the object is the same even when the interface onto it changes.**

---

## 7. Colour system

Use a mostly light, paper-like interface. Gauss should contrast with darker technical product sites without becoming sterile.

### Core palette

#### Plotter paper

`#F4F0E6`
Primary background.

#### Graphite

`#1E2428`
Primary text, rules and technical marks.

#### Cobalt

`#2457C5`
Primary interactive colour, selected paths, links and focus states.

#### Vermilion

`#E85131`
Anchor points, warnings and expressive accents. Use decoratively or for large text rather than normal small text on the pale background.

#### Instrument green

`#5FAF72`
Successful checks, accessibility states and secondary plotted geometry.

#### Construction grey

A family of low-contrast cool greys for grids, rulers and inactive guides.

Avoid rainbow-colouring every feature. The page should feel like a working drawing with a few annotation inks, not a packet of Stabilos detonating.

Dark sections may invert paper and graphite for code or architecture diagrams, but the main page should remain predominantly light.

---

## 8. Typography

Use three complementary voices.

### Display and editorial

#### STIX Two Text

It brings mathematical publishing DNA without turning the site into faux-Victorian scholarship. Use it for major headlines, large pull quotes and occasional mathematical labels.

### Interface and prose

#### IBM Plex Sans

Neutral, technical and highly legible. Use for body copy, navigation and explanatory labels.

### Code and coordinates

#### IBM Plex Mono

Use for SVG, coordinates, commands, status metadata, figure numbering and small engineering annotations.

Typography should have the confidence to become very large. A hero with a 72–96 px serif headline beside small 11–12 px coordinate annotations will give the page the scale contrast seen elsewhere in the df12 family without reproducing another site's aesthetic.

---

## 9. Page structure

### A. Navigation

Suggested top-level navigation:

`Gauss`
`Why`
`Interface`
`Accessibility`
`Automation`
`Roadmap`
`GitHub`

A persistent but restrained `← df12` link should return to the parent site.

The Gauss wordmark itself should contain a small vector-path motif, perhaps the terminal of the `G` or one `s` shown with two subtle nodes.

---

### B. Hero

As specified above:

> **Vector illustration, open all the way down.**

Large specimen artwork, visible vector anatomy, explicit Phase 0 status and GitHub CTA.

The first viewport must answer five questions immediately:

* What is Gauss?
* Why is it different?
* Is it open source?
* How mature is it?
* Where can I inspect the code?

---

### C. “One document. Every way in.”

This should be the conceptual centrepiece.

Show the same object through three synchronized representations.

#### 01 · Draw

A fragment of the Gauss canvas with selected anchor points.

##### Direct manipulation

> Draw, select and reshape vectors without surrendering the underlying geometry.

#### 02 · Navigate

An abstract representation of the accessible object/interface tree with keyboard focus moving through it.

##### Accessible interaction

> Commands, controls and document structure should remain operable without requiring pixel-perfect pointer interaction.

Do not claim that the complete canvas is screen-reader accessible before the corresponding object-level accessibility work lands. The roadmap explicitly treats that as an evolving capability.

#### 03 · Script

A compact Python API concept alongside the same selected object.

##### Programmable workflow

> The architecture is being designed so user-facing commands can also become scripting primitives.

Mark this panel `ROADMAP` until RustPython integration exists.

The visual punchline is that all three panels connect to a single central document model.

---

## 10. “SVG is not the export format”

Suggested headline:

> **The file is already yours.**

Show:

* artwork on the left;
* formatted SVG on the right;
* a highlighted `<path>` corresponding to the selected visual object;
* perhaps a line connecting the selected node to its `d=` path data.

Copy should emphasize interoperability and legibility rather than ideological purity.

Gauss already imports and exports SVG in the proof of concept, so this is something the site can demonstrate rather than merely promise.

Avoid claims such as “perfect SVG round-tripping” unless tests and implementation actually justify them.

---

## 11. Accessibility section

Suggested headline:

> **Accessibility is an architecture decision.**

This should be one of the most prominent sections rather than a footer badge.

Visually show several layers:

`APPLICATION COMMAND`
↓
`SEMANTIC ACTION`
↓
`ACCESSKIT`
↓
`PLATFORM ACCESSIBILITY API`

Beside it, show keyboard navigation and focus treatment in the actual UI.

Key messages:

* semantic roles and labels begin with the UI foundation;
* keyboard-only operation is a design constraint;
* platform accessibility comes through AccessKit;
* object-level accessible editing can expand progressively as the document model grows;
* localization follows the same principle of being structural rather than retrofitted.

This is a much more credible claim than plastering the page with WCAG logos.

The website itself must exemplify this standard.

---

## 12. Automation and scripting section

Suggested headline:

> **If you can click it, you should be able to call it.**

This is the future-facing section.

Use a split view:

**left:** a design operation taking place visually;
**right:** its conceptual scripting equivalent.

For example:

```python
circle = doc.ellipse(cx=240, cy=180, rx=64, ry=64)
circle.fill = "#2457c5"
circle.translate(x=24, y=0)
```

The actual API shown here must follow the implemented API once scripting lands. Before then, label all syntax **illustrative** rather than presenting invented code as documentation.

Explain that scriptability should emerge from the command architecture itself. Future natural-language or agent control can then sit above a deterministic API rather than operating the GUI by imitation.

Do not market Gauss as “AI-powered”. The interesting architectural choice is that an AI does **not** need privileged access.

---

## 13. Architecture section

Suggested headline:

> **A drawing application you can reason about.**

A clean technical diagram should show:

`GPUI application shell`

→ command/controller boundary

→ document model

→ SVG import/export

with cross-cutting rails for:

`AccessKit`
`localization`
`scripting`
`history`

Use the visual style of an instrument schematic rather than conventional cloud-architecture boxes.

A compact technology rail can identify:

`Rust` · `GPUI` · `AccessKit` · `SVG`

Avoid making the implementation language the hero. “Written in Rust” supports the story of a responsive and maintainable native application, but users do not choose a drawing program because Cargo.toml is particularly fetching.

---

## 14. Current state and roadmap

Borrow mxd's admirable refusal to pretend incomplete work is complete.

Create a visually explicit matrix:

### Working now

Use only verified capabilities from the current repository, such as:

* drawing paths;
* line and automatic Bézier modes;
* shape and anchor manipulation;
* fill and stroke;
* SVG import/export;
* document and selection history.

### In progress

Populate from current issues and active execution plans at build/update time.

### Direction

* broader Illustrator-class editing functionality;
* richer typography;
* advanced geometry;
* pervasive scripting;
* deeper document accessibility;
* expanded platform coverage.

Do not turn the roadmap into a feature-checkbox arms race. Group it by product capability.

---

## 15. Getting started

Because Gauss remains early-stage software, this section should be aimed at **contributors and experimenters**, not pretend there is already a frictionless consumer installer.

Suggested copy:

> **Try the instrument while we're still building it.**

Show the actual build/run command from the current repository and supported host requirements. The README currently identifies macOS and Linux as GPUI's supported targets for the proof of concept.

CTAs:

`Build Gauss`
`Read the roadmap`
`Browse the source`

Eventually this becomes `Download Gauss` when packaged releases justify it.

---

## 16. Motion and interaction

Motion should reveal structure rather than decorate the page.

Good uses:

* hovering or focusing the hero specimen reveals vector handles;
* switching representation tabs moves selection between artwork, SVG and semantic structure;
* diagram arrows draw themselves once on entry;
* selected nodes gently enlarge when focused;
* rulers or coordinate labels update as the pointer moves over a demonstration region.

Never require animation to understand content.

Respect `prefers-reduced-motion`, provide keyboard equivalents for every interactive demonstration, and make all hidden representations available in the DOM rather than painting inaccessible spectacle onto a canvas.

---

## 17. Responsive behaviour

Desktop can lean into the drafting-board metaphor with marginal coordinates, generous whitespace and asymmetrical compositions.

Tablet should preserve the same hierarchy while moving annotations closer to their subject.

Mobile should become a clean editorial column. Do not attempt to preserve every decorative ruler and dimension mark on a 390 px screen.

The core visual specimen should remain visible, but auxiliary technical markings can disappear progressively.

No horizontal scrolling should be required for the page itself. Code examples may scroll within their own labelled region.

---

## 18. Accessibility requirements for the website

The Gauss site has less licence than most sites to get this wrong.

Minimum requirements:

* WCAG AA contrast for ordinary text and UI;
* highly visible `:focus-visible` states;
* semantic headings and landmarks;
* no colour-only encoding;
* descriptive alternative text for every technical illustration;
* textual equivalents for interactive diagrams;
* complete keyboard operation;
* reduced-motion handling;
* minimum 44 px practical touch targets where appropriate;
* SVG diagrams with meaningful accessible names or adjacent equivalent prose;
* no bespoke fake controls where native controls will work.

The accessibility section should itself work exceptionally well with a screen reader. That detail will say more than any manifesto paragraph.

---

## 19. Things to avoid

### Do not imitate Illustrator

Illustrator 10 parity is a roadmap benchmark, not an invitation to reproduce Adobe's trade dress.

Gauss should look like Gauss.

### Do not build the identity around a bell curve

The name already contains the reference. One tiny Gaussian easter egg is charming; turning the site into statistics clip-art is not.

### Avoid generic SaaS aesthetics

No glowing orb behind a laptop.
No endless purple-to-blue gradients.
No floating glass cards containing meaningless graphs.
No “Revolutionize your creative workflow”.

Gauss is a precision drawing instrument. Let it look specific.

### Do not overclaim accessibility

“Accessibility from day one” is a defensible architectural statement. “Fully accessible professional vector editing” is a product claim that must wait for implementation evidence.

### Do not overclaim scripting

Until the scripting layer ships, explain the architecture and roadmap rather than presenting mock Python as a current API.

### Avoid AI-first positioning

Potential LLM control belongs downstream of the scripting model. The site's story should remain about open, deterministic interfaces.

---

## 20. df12 integration

The existing df12 home configuration already contains a Gauss card described as:

> “Accessible SVG illustration with scriptable precision. Illustrator for the open web.”

and currently links directly to GitHub.

Once the site ships:

* change the target to `/gauss/`;
* change the CTA from `View on GitHub` to `Learn more`;
* mark it as an internal link.

I would also consider revising **“Illustrator for the open web”**. Gauss is a native application built around open formats, and “for the open web” can imply a browser-based editor.

A cleaner card line would be:

> **Accessible SVG illustration with scriptable precision. Vector editing without a privileged input method.**

or, more compactly:

> **Accessible, scriptable SVG illustration. Precision drawing on an open stack.**

---

## 21. Implementation approach

Implement Gauss as a first-class df12 sub-site rather than a standalone microsite.

The df12 generator already treats sub-site templates and product-specific static assets separately: templates live beneath `templates/<site>/`, while hand-crafted assets mirror their published paths under `src/static/`.

Recommended shape:

```text
templates/gauss/
    _layout.jinja
    home_page.jinja
    pages/
        why.jinja
        accessibility.jinja
        automation.jinja
        architecture.jinja
        roadmap.jinja

src/static/gauss/
    assets/
        images/
        js/
        icons/

src/styles/
    gauss.css
```

Prefer the current build-time CSS pipeline rather than copying the older Tailwind-CDN arrangement used by Netsuke and Weaver. The df12 developer guide specifically calls out those older sub-sites' CDN-related cascade quirks.

Keep JavaScript progressive and small. The hero should still communicate the product if all enhancement scripts fail.

---

## 22. Initial deliverables

For the first implementation, produce:

1. `/gauss/` homepage;
2. product wordmark and simple path/node icon;
3. canonical Gauss specimen SVG;
4. actual application screenshot containing that specimen;
5. responsive hero;
6. “One document. Every way in.” representation;
7. SVG/document section;
8. accessibility architecture section;
9. scripting roadmap section;
10. current-state/roadmap matrix;
11. build-from-source CTA;
12. parent df12 integration;
13. complete responsive and accessibility pass.

Deeper Architecture, Accessibility and Automation routes can initially reuse and expand material introduced on the homepage rather than requiring a large documentation estate before launch.

---

## 23. Desired impression

A visitor should leave thinking:

> **This is not merely another open-source drawing program. Someone is reconsidering what the interface to a vector document ought to be.**

The site should feel precise, visually literate and slightly obsessive about structure.

A designer should want to try it.

A developer should want to inspect the architecture.

An accessibility specialist should recognize that they have been invited into the design process before the concrete has set.

And the whole thing should still have enough df12 peculiar charm to avoid resembling software procured by a committee that has recently discovered rounded rectangles.
