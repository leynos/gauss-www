# Gauss site map

## Site proposition

Gauss is an open-source vector illustration application built around one
document model and one command architecture. Direct manipulation, keyboard
operation, accessibility actions, SVG import and export, and future scripting
must meet the same underlying state. No interface gets a private route around
the document.

The public site serves three overlapping audiences:

- illustrators assessing what drawing in Gauss feels like today;
- developers evaluating the model, command, persistence, and platform
  boundaries; and
- accessibility and automation specialists judging whether those concerns are
  structural or retrofitted.

The site must separate evidence from intent. The development roadmap is the
primary source for delivery status; the architecture document and accepted
architectural decision records (ADRs) explain constraints and implemented
foundations; the feature plan describes direction, not current capability.
Every public feature claim is labelled **shipped**, **partial**, or **planned**
and checked against the current code before publication.

Gauss is a vector illustration tool. Its site may use paths, anchors, Bézier
handles, object bounds, and alignment cues when they explain an illustration or
interaction. It must not drift into computer-aided design, desktop publishing,
architectural drawing, or print-production motifs.

## Evidence hierarchy

Public copy uses the references in this order:

1. current Gauss code and tests for claims about shipped behaviour;
2. [`roadmap.md`](../../gauss/docs/roadmap.md) for current delivery status;
3. accepted ADRs for settled architectural constraints;
4. [`gauss-architecture-design.md`](../../gauss/docs/gauss-architecture-design.md)
   for system boundaries and invariants; and
5. [`gauss-feature-plan.md`](../../gauss/docs/gauss-feature-plan.md) for
   long-range product direction.

The references occasionally preserve older status text beside newer completion
notes. The website must resolve those differences against the code rather than
copying the most convenient sentence. In particular, Phase 0 accessibility
chrome wiring is implemented, while broader keyboard and object-level editing
remain incomplete. RustPython scripting remains planned.

### Source references

- [ADR 001: Command and document operation
  roles](../../gauss/docs/adr-001-command-docop-relationship.md)
- [ADR 002: Undo history crate
  selection](../../gauss/docs/adr-002-undo-history-crate-selection.md)
- [ADR 003: Shape and AccessKit identifier
  mapping](../../gauss/docs/adr-003-slotmap-shapeid-accesskit-id-mapping.md)
- [ADR 004: Resource, style, and paint
  model](../../gauss/docs/adr-004-resource-style-store-and-paint-model.md)
- [ADR 005: Gauss metadata
  namespace](../../gauss/docs/adr-005-gauss-metadata-namespace.md)
- [Foundational architecture and guiding
  principles](../../gauss/docs/gauss-architecture-design.md)
- [Feature parity plan](../../gauss/docs/gauss-feature-plan.md)
- [Development roadmap](../../gauss/docs/roadmap.md)

## Information architecture

```text
/gauss/
├── #why
├── #drawing
├── #architecture
├── #file
├── #accessibility
├── #automation
├── #current-state
├── #build
├── roadmap/
├── terms-of-use/
├── privacy-policy/
└── code-of-conduct/
```

The launch site has two authored product routes: the overview and roadmap.
Shared legal pages use Gauss navigation and styling but remain owned by the
parent `df12-www` site. GitHub is an external destination, not a site route.

The following routes are reserved until their subjects earn substantive,
non-duplicative material:

```text
/gauss/drawing/
/gauss/architecture/
/gauss/svg/
/gauss/accessibility/
/gauss/automation/
/gauss/build/
```

## Navigation model

The launch navigation is **Why**, **Drawing**, **Architecture**, **Roadmap**,
and **GitHub**. Why, Drawing, and Architecture target homepage sections.
Roadmap opens the only separate product route. GitHub carries an external-link
cue and names the destination.

The same destinations remain visible on narrow screens without horizontal page
overflow or hover-only disclosure. The Gauss wordmark returns to the overview.
A restrained footer link returns to df12 Productions.

Top-level navigation grows only when a reserved route meets its promotion
criteria. The site must not use a large navigation bar to disguise thin pages.

## Launch page specifications

### 1. Overview — `/gauss/`

**Purpose:** Introduce Gauss, demonstrate the current drawing experience, and
explain the architectural choice that distinguishes it from another SVG editor.

**Goal:** Let a visitor understand within five seconds that Gauss is an early,
open-source vector illustration application whose interfaces operate through
one document and command model. The next action should be obvious: inspect the
drawing experience, read the roadmap, or build the current proof of concept.

**Constraints:**

- Lead with “The document is the interface.” Do not ask “open” to carry the
  complete positioning argument.
- Answer what Gauss is, why it differs, whether it is open source, how mature
  it is, and where its code lives in the first viewport.
- Keep the hero's `ARTWORK` / `PATHS` / `SVG` representation switcher as its
  only interaction. The specimen is the subject; application chrome belongs in
  the drawing section.
- State that the specimen grows with Gauss. Every visible technique must be
  reproducible with the current application before it is presented as product
  evidence.
- Use a real application capture for shipped drawing interactions. A framework
  illustration must be labelled as such and replaced before publication.
- Do not imply that shape tools, transform handles, layers, text, gradients,
  effects, symbols, or scripting ship while the roadmap marks them incomplete.
- Treat resource and style stores as implemented architecture, not evidence of
  a shipped gradient or pattern editor.
- Treat Phase 0 accessibility chrome as shipped foundation. Label broader
  keyboard, canvas, and object-level accessibility as partial or planned.
- Label all scripting syntax illustrative until a public RustPython API exists.
- Keep natural-language or large language model control subordinate to the
  scripting boundary. Gauss is not marketed as an artificial intelligence
  product.
- Use a cool white canvas. Avoid unbleached colour, graph-paper rules, crop
  marks, dimensions, registration systems, and blueprint imagery.
- Preserve complete reading order and meaning without JavaScript.

The overview contains the following sections.

#### 1.1 Why Gauss — `#why`

**Purpose:** State the product thesis and its practical consequences.

**Goal:** Establish that direct manipulation, keyboard input, accessibility,
automation, and file interchange are peers at one document boundary.

**Constraints:**

- Describe a shared architectural route, not equal maturity across every
  interface.
- Connect the proposition to the implemented `EngineState` single source of
  truth and Action-to-Command pipeline.
- Keep “open all the way down” for the concrete SVG section.
- Avoid ideological claims about openness that are not demonstrated by source,
  format, or architecture.

**Evidence:** Architecture principles 2.1, 2.2, and 2.5; roadmap guiding
principles 1, 2, and 5; ADR 001.

#### 1.2 Drawing should still feel like drawing — `#drawing`

**Purpose:** Show what using Gauss feels like now.

**Goal:** Give illustrators concrete proof that Gauss is a drawing tool rather
than an architecture thesis which happens to emit paths.

**Constraints:**

- Demonstrate only verified interactions: click-to-place anchors, line and
  auto-smooth cubic segments, path closing, selection of shapes and vector
  anatomy, dragging, basic fill and stroke, pan and zoom, and undo and redo.
- Distinguish current path drawing from the planned Phase 1 Pen upgrade with
  click-drag handle creation.
- Explain historical document undo in user terms only if that behaviour has
  passed interaction testing. The selected `undo_2` crate is implementation
  evidence, not homepage copy.
- Show tool chrome only where it answers a question about drawing. Avoid a
  generic product screenshot gallery.
- Do not broaden “manipulation” into transform handles, rotation, alignment,
  grouping, or marquee selection until those roadmap items ship.

**Evidence:** Roadmap current-state summary and sections 0.3, 0.5, and 1.1 to
1.7; ADRs 001 and 002.

#### 1.3 One document. Every way in — `#architecture`

**Purpose:** Present the shared document model as the centre of Gauss.

**Goal:** Explain an architectural decision already made without presenting
planned interfaces as completed capabilities.

**Constraints:**

- Use a central document-model diagram with direct manipulation, keyboard and
  accessibility, SVG input/output, scripting, and future plug-ins as ports.
- Give every port a written **shipped**, **partial**, or **planned** status.
  Construction-line treatment may reinforce status but cannot carry it alone.
- Show Actions as user intent, Commands as undoable mutations, and document
  operations as atomic changes. Do not collapse the three layers into an
  invented public API.
- Explain that document history belongs to `EngineState`, while selection
  history remains a separate editor concern.
- Keep diagrams close to vector editing: paths, nodes, handles, and selected
  objects. Avoid conventional cloud architecture, floor plans, and drafting
  sheets.

**Evidence:** ADRs 001 and 002; architecture sections 3, 5, 6, and 7; roadmap
sections 0.1 to 0.6.

#### 1.4 The file is already yours — `#file`

**Purpose:** Demonstrate SVG as the current native and interchange format.

**Goal:** Show that artwork, editable vector anatomy, and source are three
representations of the same document.

**Constraints:**

- Pair a selected visual object with its corresponding SVG path data.
- Claim the implemented subset precisely. Current path import supports
  absolute `M`, `L`, `C`, and `Z` commands; broader element support remains
  planned.
- Explain that Gauss metadata uses the canonical
  `https://gauss.dev/ns/metadata/1` namespace and does not alter visible
  rendering in standard SVG viewers.
- Distinguish editable Gauss SVG from web-ready export, which strips the Gauss
  namespace, `gauss:*` attributes, and persisted metadata blocks.
- State that gradients, patterns, and symbols have typed resource storage and
  round-trip foundations without claiming that their editing interfaces ship.
- Do not claim unrestricted, perfect, or lossless round-tripping beyond tested
  SVG fixtures and supported syntax.

**Evidence:** ADRs 004 and 005; architecture section 10; roadmap sections 0.2.3,
0.4, and 1.7.

#### 1.5 Accessibility is an architecture decision — `#accessibility`

**Purpose:** Explain how accessibility enters the application architecture.

**Goal:** Let accessibility specialists distinguish implemented foundations
from the work still required for keyboard-complete, object-level editing.

**Constraints:**

- Show the route from application command to semantic action, AccessKit, and
  the platform accessibility API.
- Describe stable accessibility node identity through the explicit
  `ShapeId`-to-AccessKit mapping settled in ADR 003.
- State that the Phase 0 shell publishes stable chrome semantics, incremental
  tree updates, and supported chrome action routing.
- State just as clearly that comprehensive keyboard parity, canvas semantics,
  object navigation, and screen-reader validation remain active work.
- Never use “fully accessible”, an unqualified compliance badge, or a blanket
  platform-support claim.
- Demonstrate keyboard focus with the Gauss offset double-rule. Selection and
  keyboard focus must remain visually distinct.

**Evidence:** ADR 003; architecture sections 2.4 and 11; roadmap current-state
summary and sections 0.6 and 1.9.

#### 1.6 If it can be clicked, it should be callable — `#automation`

**Purpose:** Explain why scripting is designed through the command model.

**Goal:** Show that future automation will use the same semantic actions as the
interface rather than driving pixels or bypassing document rules.

**Constraints:**

- Present Action-to-Command routing as implemented architecture.
- Present the RustPython host and `gauss.app`, `gauss.doc`,
  `gauss.commands`, `gauss.selection`, `gauss.export`, and `gauss.events`
  modules as proposals.
- Mark terminal commands, Python calls, and result mappings as illustrative
  until they run against a released API.
- Do not promise plug-ins, macro recording, asynchronous jobs, event
  subscriptions, or large language model control as shipped features.
- Keep automation deterministic, undoable, and observable in the explanation.

**Evidence:** ADR 001; architecture sections 2.1, 7, and 13; roadmap migration
notes and section 1.11.

#### 1.7 Current state — `#current-state`

**Purpose:** Give a compact, honest account of what works, what is being built,
and where Gauss is headed.

**Goal:** Let visitors calibrate maturity without reading the complete
engineering roadmap.

**Constraints:**

- Use hand-curated **working now**, **in progress**, and **direction** groups.
- Source “working now” from current code and tests, not unchecked roadmap prose.
- Keep architecture foundations separate from user-visible editor features.
- Group future work by user capability: core drawing, document organization,
  typography, path operations, appearance, reuse, automation, accessibility,
  localization, performance, and platform coverage.
- Do not import live GitHub issue titles as product copy.
- Link to the roadmap for detail and show the date on which status was last
  reviewed.

**Evidence:** Complete roadmap, with the feature plan used only to name
long-range capability groups.

#### 1.8 Build Gauss — `#build`

**Purpose:** Give contributors and experimenters a truthful route into the
current application.

**Goal:** Move a technically prepared visitor from interest to a successful
local build or a useful repository contribution.

**Constraints:**

- Use build commands and platform requirements from the current Gauss
  repository. Do not duplicate commands that cannot be tested during the site
  release.
- Address contributors and experimenters until packaged releases justify a
  consumer download path.
- Provide three clear actions: build from source, read the roadmap, and browse
  the repository.
- Do not imply stable installers, production support, or complete
  cross-platform coverage.

**Evidence:** Current Gauss README and developer guide, plus the roadmap's
cross-platform UI work.

### 2. Roadmap — `/gauss/roadmap/`

**Purpose:** Translate the engineering roadmap into a maintained product-status
view without discarding links to implementation detail.

**Goal:** Let designers, contributors, and technical evaluators see what is
working, what comes next, and which architectural foundations constrain later
features.

**Constraints:**

- Show a visible “Last reviewed” date. A stale roadmap should look stale.
- Open with the verified current state and Phase 0 maturity, not the final
  Illustrator 10 parity ambition.
- Separate completed foundations from shipped user workflows. A resource store
  does not make a gradient editor available.
- Organize the public roadmap by capability rather than reproducing every
  numbered engineering task.
- Retain deep links to the canonical roadmap, architecture document, feature
  plan, and relevant ADRs for contributors who need implementation detail.
- Treat the feature plan's phase outcomes as targets. Do not write future-tense
  outcomes as present product claims.
- Explain that scripting, typography, advanced paths, appearance, symbols,
  data-driven graphics, and final parity work remain future phases.
- Flag scope changes and postponed work directly. Do not silently move an item
  between “next” and “later”.
- Curate “in progress” copy by hand. GitHub issues may provide evidence but not
  page headings.

**Proposed data-driven elements:** A status summary; capability groups with
status, phase, evidence link, and last-reviewed fields; a foundation timeline;
and links to accepted ADRs. One status record should drive both this route and
the homepage summary.

**Internal links:** [Overview](#1-overview--gauss),
[Drawing](#12-drawing-should-still-feel-like-drawing--drawing),
[Architecture](#13-one-document-every-way-in--architecture),
[SVG](#14-the-file-is-already-yours--file),
[Accessibility](#15-accessibility-is-an-architecture-decision--accessibility),
and [Automation](#16-if-it-can-be-clicked-it-should-be-callable--automation).

### 3. Terms of use — `/gauss/terms-of-use/`

**Purpose:** Present the parent site's terms within Gauss navigation and visual
context.

**Goal:** Keep legal terms reachable from every Gauss page without maintaining
a divergent product-specific copy.

**Constraints:**

- Source the prose from `df12-www/config/shared/terms-of-use.md`.
- Do not duplicate or amend legal text in Gauss templates.
- Preserve one page heading, ordered heading levels, and a route back to Gauss.
- Keep the effective or reviewed date supplied by the shared source.

### 4. Privacy policy — `/gauss/privacy-policy/`

**Purpose:** Present the parent site's privacy policy within Gauss navigation
and visual context.

**Goal:** Explain the applicable data-handling position without inventing
Gauss-specific collection or telemetry.

**Constraints:**

- Source the prose from `df12-www/config/shared/privacy-policy.md`.
- Do not claim that the desktop application collects, stores, or avoids data
  unless current application behaviour and policy support the statement.
- Keep third-party resources off the published site so the implementation
  matches the policy position.
- Preserve one page heading, ordered heading levels, and a route back to Gauss.

### 5. Code of Conduct — `/gauss/code-of-conduct/`

**Purpose:** State the conduct expected in Gauss community spaces.

**Goal:** Give contributors a clear behavioural baseline and route for handling
conduct concerns.

**Constraints:**

- Source the prose from `df12-www/config/shared/code-of-conduct.md`.
- Do not fork community standards inside the Gauss template layer.
- Keep reporting instructions and contact routes current and explicit.
- Preserve one page heading, ordered heading levels, and a route back to Gauss.

## Reserved route specifications

Reserved routes are not launch deliverables. Each remains a homepage section
until it meets the promotion criteria below.

### Drawing — `/gauss/drawing/`

**Purpose:** Become the evidence-led guide to current drawing workflows.

**Goal:** Help an illustrator decide whether the available tools support a real
piece of work.

**Constraints:** Promote only when Gauss has multiple stable workflows beyond
the Phase 0 path demonstration, current application captures, and enough
interaction detail to avoid repeating the homepage. Every workflow must name
its limitations and keyboard route.

### Architecture — `/gauss/architecture/`

**Purpose:** Explain the core engine, tool, command, persistence, rendering,
accessibility, and platform boundaries at an evaluative level.

**Goal:** Let contributors understand why the boundaries exist before entering
the exhaustive repository design document.

**Constraints:** Promote only when the page can provide maintained component
status, concise diagrams with text equivalents, an ADR index, and concrete
examples from the current crate structure. Keep implementation detail in the
repository documentation.

### SVG and files — `/gauss/svg/`

**Purpose:** Document supported SVG import, save, round-trip, metadata, and
web-ready export behaviour.

**Goal:** Let illustrators and toolchain authors judge interoperability without
guessing which SVG features Gauss understands.

**Constraints:** Promote only with a generated or tested support matrix, sample
files, explicit unsupported syntax, and stable user-facing file commands. Never
generalize from path fixtures to the complete SVG specification.

### Accessibility — `/gauss/accessibility/`

**Purpose:** Publish the application's accessibility support matrix and design
constraints.

**Goal:** Give disabled users and accessibility specialists testable details
about keyboard access, semantic controls, canvas navigation, object access, and
platform adapters.

**Constraints:** Promote only when evidence extends beyond the homepage's
architecture account. Each claim needs a tested platform, assistive technology,
version, scope, and known limitation. Avoid compliance theatre.

### Automation — `/gauss/automation/`

**Purpose:** Document the released scripting and command surface.

**Goal:** Let developers automate a real document edit using stable,
copyable examples.

**Constraints:** Promote only after RustPython integration or another public
automation boundary ships. Examples must execute in validation, call public
Actions or Commands rather than internal Rust state, report failures, and
preserve undo semantics.

### Build and contribute — `/gauss/build/`

**Purpose:** Provide a maintained contributor onboarding path for the desktop
application.

**Goal:** Get a supported host from clone to verified build, test, and first
small contribution.

**Constraints:** Promote only when the route can improve on the repository
README through platform-specific prerequisites, verified commands,
troubleshooting, and contribution paths. The repository remains authoritative;
generated website instructions must be checked in the same release.

## Shared content model

The following records should live in structured configuration and be reused
across the overview and roadmap:

- capability identifier and public label;
- **shipped**, **partial**, or **planned** status;
- user-facing description;
- architecture foundation versus user-visible capability;
- canonical evidence link;
- roadmap phase or work-item identifier;
- last-reviewed date; and
- homepage visibility.

Navigation, calls to action, accepted ADR summaries, and technology names also
belong in shared data where they recur. Jinja templates should render those
records rather than maintaining parallel status prose.

## Site-wide constraints

- Publish beneath `/gauss/` through the `df12-www` generator. Generated HTML is
  disposable output.
- Use semantic HTML, ahead-of-time Tailwind CSS v4, daisyUI v5 components, and
  Gauss semantic classes. The site must not depend on a browser-side CSS
  compiler or frontend runtime.
- Meet WCAG 2.2 AA, including landmarks, heading order, descriptive links,
  keyboard-visible focus, contrast, target size, zoom, reduced motion, forced
  colours, and narrow-screen reflow.
- Keep the page useful without JavaScript. Enhancement failure must not hide
  copy, status, navigation, or specimen provenance.
- Self-host required assets. External project and evidence links are explicit
  navigations, not third-party requests made on page load.
- Use British English with Oxford spelling. Keep claims short, technical, and
  sourced.
- Do not use Adobe Illustrator as a visual template or imply trademarked
  product endorsement. The feature plan's parity target is roadmap context,
  not the public proposition.
- Do not create documentation routes merely to mirror repository files. A web
  page must answer a visitor need that raw engineering documentation does not.
