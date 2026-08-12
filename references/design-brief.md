# Gauss website design brief

## 1. Project

Create a product website for **Gauss**, the open-source vector illustration application at `leynos/gauss`, as a new df12 Productions sub-site at `/gauss/`.

Gauss is currently a Phase 0 proof of concept built in Rust with GPUI. The working application supports path drawing and manipulation, SVG import/export, styling, undo/redo, and separate selection history.

The larger product direction is substantially more ambitious: a professional SVG illustration environment in which accessibility, localizability, performance, and pervasive scripting form part of the architecture from the beginning. The roadmap targets Illustrator 10-level breadth while explicitly avoiding a bolt-on approach to accessibility or automation.

The website should therefore present **the product Gauss is becoming without pretending that the roadmap has already shipped**.

---

## 2. Core positioning

### Recommended proposition

> **The document is the interface.**

Gauss should not position itself primarily as “an Illustrator clone written in
Rust”. Illustrator parity is useful as a scope benchmark, but weak as a product
identity.

The product distinction is architectural:

**One vector document, with no privileged way to operate it.**

A pointer, keyboard, assistive technology, script, and eventually an agent
should all reach the same underlying document and command model. “Open source”
matters, but it is evidence rather than the whole position.

The site should unpack three consequences:

1. **Open document**
   SVG is a first-class interchange format rather than an export afterthought.

2. **Open interface**
   Accessibility and keyboard operation belong in the application architecture rather than a compatibility layer added later.

3. **Open automation**
   User-visible operations should gain scriptable equivalents, allowing
   repeatable workflows and eventual agent control without screen-scraping the
   graphical user interface (GUI).

“Vector illustration, open all the way down” remains useful copy for the SVG
and open-stack story. It should not carry the hero alone.

### Suggested hero copy

#### Eyebrow

No eyebrow is required. The wordmark, status rail, and supporting copy already
establish the product and its maturity.

#### Headline

> **The document is the interface.**

#### Supporting copy

> Gauss treats the vector document as the shared centre of drawing,
> accessibility, and automation. Open-source SVG illustration with a command
> model designed for scriptable precision.

#### Primary CTA

`Explore Gauss`

Link to the drawing section so the first action reaches current product
evidence rather than planned architecture.

#### Secondary CTA

`Build from source`

Use `View source on GitHub` as a quieter text link below the two primary
actions.

Below the CTAs, show an explicit status rail:

`Phase 0 proof of concept` · `Rust + GPUI` · `SVG import/export` ·
`Designed for accessibility`

Do not bury the development status in a roadmap page.

---

## 3. Relationship to the existing df12 sites

Gauss should belong unmistakably to df12 without inheriting a generic df12 product template.

The existing product sites establish a useful pattern:

- **Netsuke** turns its build-system concept into tactile Japanese craft, carved wood and careful material detail.
- **Weaver** translates code-agent infrastructure into blueprint, loom and architectural drawing language.
- **mxd** combines protocol engineering with a railway/night-travel visual system and exposes implementation status rather than disguising incomplete compatibility.
- **Stilyagi** uses a highly individual editorial/poster language while organizing substantial technical material underneath it.

The common df12 grammar is therefore not shared colours or interchangeable cards. It is:

**strong metaphor + serious technical substance + unusually specific copy + visible engineering evidence.**

That also fits the parent site, whose stated identity is “Serious tools, playful worlds” and “Fast, elegant, and open by design.”

Gauss should be the **precision instrument** in that collection.

---

## 4. Creative concept: The visible vector

The visual language should combine:

- a professional vector-design studio;
- a clean digital illustration canvas;
- the visible anatomy of Bézier geometry.

Think **illustration tool with its construction exposed**. Gauss is a vector
illustration application, not a computer-aided design (CAD) package, a desktop
publishing system, or a print-production workstation.

The reference to Gauss should remain cultured and oblique. Avoid portraits of
Carl Friedrich Gauss, giant equations, or an endless parade of
normal-distribution curves.

### Existing logo proposal

The current df12 home page contains the starting logo proposal in
`../df12-www/df12_pages/templates/home_page.jinja`: a single arched Bézier, a
filled node at its apex, and a baseline. Adopt that mark rather than inventing a
new `G` or path-and-node icon for the sub-site.

The proposal carries enough of the Gaussian reference on its own. Keep it
compact and monochrome in the header, favicon, and parent-site card. Do not
enlarge it into the hero or repeat the arch as a decorative bell-curve motif;
the botanical `G` specimen remains the site's expressive centre.

Before finalizing the asset, test the proposal at 16, 24, and 32 CSS pixels,
beside the `Gauss` wordmark, in monochrome, and against both light and dark
surfaces. Preserve the single curve, apex node, and baseline unless those tests
identify a legibility defect.

Use the affordances that belong naturally to vector editing:

- anchor points;
- Bézier handles;
- selected paths;
- alignment and snapping guides;
- bounding boxes;
- control points;
- alignment crosshairs;
- SVG path data;
- layers and object trees.

Do not turn those affordances into a CAD or print metaphor. Avoid graph-paper
grids, measurement-heavy diagrams, crop marks, registration targets, page
furniture, and repeated ruled sections. Every technical mark should describe a
vector object, an interaction, or an alignment relationship.

The website should feel like a vector canvas with its editor overlays left
visible: precise, visual, and made for drawing.

### Design sample

Use `references/design-sample.png` as the visual reference for the launch page.
It establishes several useful directions:

- large editorial serif headings against restrained sans-serif utility copy;
- cobalt selection geometry and vermilion control handles;
- the botanical `G` specimen as the dominant visual object;
- thin outlined controls, sparse cards, and generous white space;
- a dark graphite automation band as the single strong tonal inversion;
- a real application screenshot below the hero, where product chrome has a
  concrete job.

Do not carry over the sample's unbleached background or repeated horizontal
rules. Use a clean white or cool near-white canvas, and separate sections with
spacing, content shifts, and occasional local borders rather than page-wide
ruling.

The browser frame in the sample is presentation context, not part of the site.
Treat the sample as a hierarchy and interaction reference rather than a
fixed-pixel specification. Responsive behaviour, real content, accessible
semantics, and the vector-illustration identity take priority over literal
tracing.

---

## 5. Hero art direction

The hero should contain a **real piece of vector artwork**, not application
chrome. The sample's botanical `G` specimen is the canonical direction: an
editorial mark built from leaves, curves, and visible Bézier anatomy.

Build the specimen using only capabilities genuinely supported by the current
Gauss release: paths, Bézier curves, solid fills, and strokes.

The hero has one interaction:

`ARTWORK` · `PATHS` · `SVG`

Each tab presents the same specimen:

1. `ARTWORK` shows the finished composition;
2. `PATHS` reveals editable curves, anchors, and handles;
3. `SVG` shows the corresponding source with the selected path highlighted.

Do not add an `ACCESSIBILITY` tab until Gauss can demonstrate the corresponding
object-level representation. Do not place application chrome behind the hero
artwork. The actual product screenshot belongs in the drawing section below.

Provide the specimen SVG for download.

State the specimen rule on the page:

> **This drawing grows with Gauss.** Every element in the specimen uses
> capabilities available in the current build. As Gauss learns new techniques,
> the specimen gains them too.

Typography, gradients, compound paths, and effects can enter the artwork only
when those capabilities become real.

That makes the homepage itself a quiet visual changelog.

---

## 6. Signature visual motif

Use an oversized editable curve as the recurrent graphic device.

For example, a broad cobalt curve might enter from the left edge, pass through
two visible nodes, and leave at the lower right. Handles, coordinates, and
alignment marks can appear around it:

`P₀  124,86`
`C₁  212,28`
`C₂  376,240`

The curve can reappear throughout the site in different states:

- raw geometry in technical sections;
- filled shape in visual sections;
- SVG path text in scripting sections;
- highlighted accessible object in accessibility sections.

It becomes a metaphor for the central thesis: **the object is the same even when the interface onto it changes.**

---

## 7. Colour system

Use a mostly light, clean interface. Gauss should contrast with darker
technical product sites without borrowing the colour or texture of unbleached
paper.

### Core palette

#### Canvas white

`#FCFCFD`
Primary background. It should read as a digital canvas, not cream stock,
parchment, or recycled paper.

#### Graphite

`#1E2428`
Primary text, rules and technical marks.

#### Cobalt

`#2457C5`
Selected paths, active representation tabs, primary actions, and links. Cobalt
must never be the sole link cue; retain underlines or another persistent
affordance where links appear in prose.

#### Vermilion

`#E85131`
Anchor points, warnings and expressive accents. Use decoratively or for large text rather than normal small text on the pale background.

#### Instrument green

`#5FAF72`
Verified `SHIPPED` states and successful checks. Pair the colour with a written
status label.

#### Status amber

Use a restrained amber for `PARTIAL` states. Pair it with interrupted connector
lines and the written label.

#### Construction grey

A family of cool greys for inactive paths, alignment guides, dividers, and
disabled interface elements. Do not assemble them into a page-wide grid.

Avoid rainbow-colouring every feature. The page should feel like an illustration
canvas with a few editor overlays, not a packet of Stabilos detonating.

Dark sections may invert paper and graphite for code or architecture diagrams, but the main page should remain predominantly light.

### Keyboard focus

Focus has its own geometry. Use a high-contrast, 2 px offset double-rule with a
clear gap around the focused element. It must meet WCAG 2.2 contrast and area
requirements against both focused and unfocused states.

Never imitate Gauss selection handles, bounding boxes, or construction guides
for keyboard focus. Selection is cobalt geometry; focus is an offset perimeter.
The distinction must survive greyscale, screenshots, and colour-vision
deficiencies.

---

## 8. Typography

Use three complementary voices.

### Display and editorial

#### STIX Two Text

Use it for major headlines and large pull quotes. Its purpose is expressive
contrast against the application-like interface text, not to turn the site into
a mathematical journal or editorial spread.

### Interface and prose

#### IBM Plex Sans

Neutral, technical and highly legible. Use for body copy, navigation and explanatory labels.

### Code and coordinates

#### IBM Plex Mono

Use for SVG, coordinates, commands, status metadata, and small editor
annotations.

Typography should have the confidence to become very large. A hero with a
72–96 px serif headline beside small 11–12 px path annotations will give the
page the scale contrast seen elsewhere in the df12 family without reproducing
another site's aesthetic. Keep the typography subordinate to the specimen; the
page is not a desktop-publishing demonstration.

---

## 9. Page structure

### A. Navigation

Launch navigation:

`Gauss`
`Why`
`Drawing`
`Architecture`
`Roadmap`
`GitHub`

`Why`, `Drawing`, and `Architecture` are homepage anchors. `Roadmap` may be a
separate route once it has enough substance. `GitHub` is external and must use
both text and an external-link cue.

Do not create thin Accessibility or Automation routes that repeat homepage
copy. Add top-level destinations only when each route has earned its own
material.

A persistent but restrained df12 link should return to the parent site. It may
sit in the footer or wordmark context rather than competing with primary
navigation.

Pair the existing arched-curve mark with a restrained `Gauss` wordmark. Do not
add nodes to the letterforms; the standalone mark already carries the vector
construction idea.

---

### B. Hero

As specified above:

> **The document is the interface.**

Place the copy and actions on the left, and the botanical `G` specimen on the
right. The `ARTWORK` / `PATHS` / `SVG` switcher sits above the headline and is
the hero's only interaction.

The first viewport must answer five questions immediately:

- What is Gauss?
- Why is it different?
- Is it open source?
- How mature is it?
- Where can I inspect the code?

---

### C. Drawing should still feel like drawing

Give the drawing experience its own section directly below the hero. This is
the designer-facing proof that Gauss is a drawing tool, not an architecture
paper which happens to emit paths.

Use a real Gauss application screenshot containing part of the botanical
specimen. Show the current interaction vocabulary:

- place points;
- switch between line and automatic Bézier edges;
- select anchors, segments, and shapes;
- drag and reshape geometry;
- edit fill and stroke;
- reorder objects;
- undo with confidence.

Suggested copy:

> **Drawing should still feel like drawing.** Place points. Shape Bézier curves
> with handles that behave. Edit fill and stroke with clarity. Undo with
> confidence.

The screenshot is evidence, not decoration. Keep its chrome here, where it
answers what using Gauss feels like.

---

### D. One document. Every way in

Make this an architecture diagram, not a three-panel capability demo. The
shared document model is the large central object. Interfaces plug into it as
ports:

- direct manipulation;
- keyboard and accessibility;
- scripting API;
- SVG import and export;
- future plug-ins.

Status belongs to the diagram's construction language:

- `SHIPPED` ports use solid lines and complete sockets;
- `PARTIAL` ports use interrupted lines and partially resolved geometry;
- `PLANNED` ports use ghosted anchors or unfilled sockets.

Always include written status labels. Colour supports the meaning but does not
carry it.

The launch baseline should be treated as:

- direct manipulation – `SHIPPED`;
- keyboard and accessibility – `PARTIAL`;
- scripting API – `PLANNED`;
- SVG import and export – `SHIPPED`;
- plug-ins – `PLANNED`.

Verify every label against the current Gauss repository before publication.
The labels in `design-sample.png` demonstrate the visual grammar, not product
evidence.

The proposition is architectural: every interface must meet the same document
and command model. The diagram can become progressively live as each port
ships, without changing the page's argument.

---

## 10. The file is already yours

Use “Vector illustration, open all the way down” as a quiet eyebrow or section
line here, where “open” has concrete evidence.

> **The file is already yours.**

Follow the sample's side-by-side composition:

- artwork on the left;
- formatted SVG on the right;
- a highlighted `<path>` corresponding to the selected visual object;
- a line connecting the selected node to its `d=` path data.

Copy should emphasize interoperability and legibility rather than ideological purity.

Gauss already imports and exports SVG in the proof of concept, so this is something the site can demonstrate rather than merely promise.

Avoid claims such as “perfect SVG round-tripping” unless tests and implementation actually justify them.

---

## 11. Accessibility section

Suggested headline:

> **Accessibility is an architecture decision.**

This is an architecture claim, not a declaration of complete object-level
accessibility. Keep it prominent without presenting planned work as shipped.

Visually show several layers:

`APPLICATION COMMAND`
↓
`SEMANTIC ACTION`
↓
`ACCESSKIT`
↓
`PLATFORM ACCESSIBILITY API`

Beside it, show keyboard navigation and the offset double-rule focus treatment
in the actual UI. Do not reuse cobalt selection geometry for focus.

Key messages:

- semantic roles and labels begin with the UI foundation;
- keyboard-only operation is a design constraint;
- platform accessibility comes through AccessKit;
- object-level accessible editing can expand progressively as the document model grows;
- localization follows the same principle of being structural rather than retrofitted.

This is a much more credible claim than plastering the page with WCAG logos.

The website itself must exemplify this standard. Treat the sample's “Designed
for accessibility” status-rail item as intent; every public capability claim
still requires evidence from the current build.

---

## 12. Automation and scripting section

Suggested headline:

> **If you can click it, you should be able to call it.**

This is the future-facing section and the sample's single dark graphite band.
The tonal shift distinguishes planned command architecture from the shipped
drawing and SVG demonstrations above it.

Show a left-to-right mapping:

`COMMAND` → `SEMANTIC ACTION` → `RESULT`

Include a compact terminal or command column only when it can be tied to real
commands. Until a scripting API exists, label all syntax `ILLUSTRATIVE` and
avoid presenting invented Python as documentation.

Explain that scriptability should emerge from the command architecture itself.
Future natural-language or agent control can then sit above a deterministic
API rather than operating the GUI by imitation.

Do not market Gauss as “AI-powered”. The interesting architectural choice is that an AI does **not** need privileged access.

---

## 13. Architecture section

Suggested headline:

> **How Gauss is built.**

This section deepens the document-model diagram rather than repeating it. Show:

`GPUI application shell`

→ command/controller boundary

→ document model

→ SVG import/export

with cross-cutting rails for:

`AccessKit`
`localization`
`scripting`
`history`

Draw the relationships with the same paths, nodes, handles, and alignment cues
used elsewhere on the page. Avoid blueprint styling, building-plan notation,
measurement grids, and conventional cloud-architecture boxes.

A compact technology rail can identify:

`Rust` · `GPUI` · `AccessKit` · `SVG`

Avoid making the implementation language the hero. “Written in Rust” supports the story of a responsive and maintainable native application, but users do not choose a drawing program because Cargo.toml is particularly fetching.

---

## 14. Current state and roadmap

Borrow mxd's admirable refusal to pretend incomplete work is complete.

Create a visually explicit matrix:

### Working now

Use only verified capabilities from the current repository, such as:

- drawing paths;
- line and automatic Bézier modes;
- shape and anchor manipulation;
- fill and stroke;
- SVG import/export;
- document and selection history.

### In progress

Write this by hand as product copy and review it with each site release. Link to
active GitHub issues for detail, but do not import issue titles into the page.
Issue labels and titles are implementation records, not durable product
language.

### Direction

- broader Illustrator-class editing functionality;
- richer typography;
- advanced geometry;
- pervasive scripting;
- deeper document accessibility;
- expanded platform coverage.

Do not turn the roadmap into a feature-checkbox arms race. Group it by product capability.

Show a visible “Last reviewed” date if the roadmap has its own route. Stale
status must be obvious rather than quietly masquerading as current state.

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

Present these as the three closing actions shown in the sample. Use descriptive
link labels – `Build Gauss from source`, `Read the Gauss roadmap`, and `Browse
Gauss on GitHub` – rather than repeating generic “Learn more” links.

Eventually this becomes `Download Gauss` when packaged releases justify it.

---

## 16. Motion and interaction

Motion should reveal structure rather than decorate the page.

Good uses:

- hovering or focusing the hero specimen reveals vector handles;
- switching representation tabs preserves the same selected object across
  artwork, paths and SVG;
- port lines resolve as status changes, when that transition teaches the
  architecture;
- selected nodes gently enlarge when focused;
- alignment indicators or coordinate labels update as the pointer moves over a
  demonstration region.

Never require animation to understand content.

Respect `prefers-reduced-motion`, provide keyboard and touch equivalents for
every interactive demonstration, and make all representations available in the
document object model (DOM) rather than painting inaccessible spectacle onto a
canvas.

---

## 17. Responsive behaviour

Desktop can lean into a spacious vector-workspace composition with local path
annotations, generous white space, and asymmetry around the specimen.

Tablet should preserve the same hierarchy while moving annotations closer to their subject.

Mobile should become a clean visual column. Do not preserve every alignment
mark or path annotation on a 390 px screen.

Keep the headline, supporting copy, primary action, and status visible before
the specimen on narrow screens. The representation tabs remain a single
accessible tab list; they may scroll within their own labelled region if
necessary.

The core visual specimen should remain visible, but auxiliary technical
markings can disappear progressively. Stack the architecture ports around the
document model or replace the visual diagram with an equivalent ordered text
view. Never shrink labels below a readable size to preserve the desktop
composition.

No horizontal scrolling should be required for the page itself. Code examples may scroll within their own labelled region.

---

## 18. Accessibility requirements for the website

The Gauss site has less licence than most sites to get this wrong.

Minimum requirements:

- WCAG AA contrast for ordinary text and UI;
- a 2 px offset double-rule `:focus-visible` treatment with at least 3:1
  contrast against focused and adjacent colours;
- semantic headings and landmarks;
- no colour-only encoding;
- descriptive alternative text for every informative technical illustration;
- empty alternative text for purely decorative editor overlays;
- textual equivalents for interactive diagrams;
- complete keyboard operation;
- reduced-motion handling;
- at least 24 × 24 CSS pixel targets, with 44 × 44 practical touch targets for
  primary controls where the layout permits;
- SVG diagrams with meaningful accessible names or adjacent equivalent prose;
- no bespoke fake controls where native controls will work.

The hero's `ARTWORK` / `PATHS` / `SVG` control must use real tab semantics,
support arrow-key movement, preserve a logical focus order, and expose the same
information without motion. The architecture diagram needs adjacent prose that
states every port and status; its lines and colours are supplementary.

The accessibility section should itself work exceptionally well with a screen reader. That detail will say more than any manifesto paragraph.

---

## 19. Things to avoid

### Do not imitate Illustrator

Illustrator 10 parity is a roadmap benchmark, not an invitation to reproduce Adobe's trade dress.

Gauss should look like Gauss.

### Do not extend the Gaussian reference beyond the logo

The existing arched-curve mark is the permitted visual nod to Gauss. Do not
echo it as charts, distribution curves, background patterns, or hero artwork.
The identity should still read as vector illustration rather than statistics
software.

### Do not mistake precision for CAD or print production

Keep deconstructed vectors, handles, nodes, alignment marks, and snapping
guides. Remove graph-paper backgrounds, drawing dimensions, architectural
notation, crop marks, registration systems, and desktop-publishing page
furniture.

Avoid unbleached cream backgrounds and repeated horizontal rules. Gauss works
on a digital illustration canvas, not a roll of plotter paper or a specimen
sheet waiting for the press.

### Avoid generic SaaS aesthetics

No glowing orb behind a laptop.
No endless purple-to-blue gradients.
No floating glass cards containing meaningless graphs.
No “Revolutionize your creative workflow”.

Gauss is a precision drawing instrument. Let it look specific.

### Do not turn the hero into a product screenshot

Application chrome belongs in the drawing section, where it demonstrates real
interaction. The hero belongs to the specimen and its three representations.

### Do not confuse the sample with product evidence

The design sample demonstrates layout, visual language, and status grammar.
Every `SHIPPED`, `PARTIAL`, or `PLANNED` label must be checked against the
current Gauss repository before release.

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

- change the target to `/gauss/`;
- change the CTA from `View on GitHub` to `Explore Gauss`;
- mark it as an internal link.

Replace **“Illustrator for the open web”**. Gauss is a native application built
around open formats, and “for the open web” incorrectly suggests a browser
editor.

Use:

> **Accessible, scriptable SVG illustration. Precision drawing on an open stack.**

“Vector illustration without a privileged interface” may become a strong short
descriptor once the product identity has enough context. It should not
introduce the concept cold on the parent grid.

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
        roadmap.jinja

src/static/gauss/
    assets/
        images/
            gauss-logo.svg
            gauss-specimen.svg
            gauss-application.webp
        js/
        icons/

src/styles/
    gauss.css
```

Prefer the current build-time CSS pipeline rather than copying the older Tailwind-CDN arrangement used by Netsuke and Weaver. The df12 developer guide specifically calls out those older sub-sites' CDN-related cascade quirks.

Keep `Why`, `Drawing`, and `Architecture` as homepage sections at launch. Add
new templates only when their routes contain material that does more than
repeat the homepage.

Keep JavaScript progressive and small. The hero should still communicate the
product if all enhancement scripts fail. Without JavaScript, show the artwork
representation first and provide direct links to the specimen SVG and source.

---

## 22. Initial deliverables

For the first implementation, produce:

1. `/gauss/` homepage;
2. production-ready SVG of the existing arched-curve logo proposal and its
   wordmark lock-up;
3. canonical Gauss specimen SVG;
4. responsive hero with `ARTWORK` / `PATHS` / `SVG` representations;
5. public “This drawing grows with Gauss” provenance statement;
6. actual application screenshot and drawing-experience section;
7. document-model architecture diagram with verified status ports;
8. SVG/document section;
9. accessibility architecture section;
10. automation architecture band with clearly labelled illustrative syntax;
11. deeper implementation architecture section;
12. hand-curated current-state and roadmap material;
13. closing build, roadmap, and source actions;
14. parent df12 integration;
15. complete responsive and accessibility pass;
16. five-second, first-click, keyboard-only, greyscale, 200% zoom, and
    reduced-motion checks.

Do not create placeholder deep routes for Architecture, Accessibility, or
Automation. Their homepage sections should earn those routes through
substantive future material.

---

## 23. Desired impression

The five-second reading should be:

> **Gauss is an early open-source vector editor built around one document model,
> not one privileged interface.**

A visitor should leave thinking:

> **This is not merely another open-source drawing program. Someone is reconsidering what the interface to a vector document ought to be.**

The site should feel precise, visually literate, and slightly obsessive about
structure.

A designer should want to draw with it because the page shows real interaction,
not only architecture.

A developer should want to inspect the architecture.

An accessibility specialist should recognize that they have been invited into the design process before the concrete has set.

The primary first click should be `Explore Gauss`; `Build from source` and
GitHub remain obvious alternatives for contributors.

The whole thing should still have enough df12 peculiar charm to avoid
resembling software procured by a committee that has recently discovered
rounded rectangles.
