# Site structure & content conventions

Documentation of how this site's content is built, for anyone authoring or editing pages:
runnable code blocks, the shape every content page follows, house style for prose, and where a
given piece of information belongs (heading, admonition, glossary, or footnote).
[CLAUDE.md](CLAUDE.md) covers everything else (theme/CSS internals, commands, link maintenance).

The rules that can be checked mechanically (numbered-list start, heading case, admonition
types, `python-ref` comment format, homepage keyword-link coverage, and a clean `mkdocs build`)
are enforced by `pytest` — see [tests/test_structure.py](tests/test_structure.py). Rules that
need editorial judgment (is this content core enough for `!!!`, is this subheading a real skim
target) aren't and can't be — that file's docstring says which is which.

## Pyodide runnable code blocks

The "runnable code block" feature is entirely hand-wired in
[docs/javascripts/pyodide_runner.js](docs/javascripts/pyodide_runner.js) — Pyodide itself is
just a Python-in-WebAssembly runtime with a JS API, no DOM awareness or UI of its own.

- **Detection** — on `DOMContentLoaded`, scans for `pre > code.language-python`, the class
  MkDocs' `fenced_code` extension gives ordinary ` ```python ` blocks. No custom Markdown
  extension needed — any fenced Python block in `docs/*.md` gets a Run button automatically.
- **Lazy load** — Pyodide's JS runtime (`pyodide.js`) loads from the jsdelivr CDN only on first
  Run click, not on page load, so normal page loads stay fast.
- **Output capture** — stdout/stderr are captured via `pyodide.setStdout`/`setStderr` batched
  callbacks and written into an injected `<pre class="pyodide-runner__output">` panel.
- **Editable, not just runnable** — the `<code>` element is wired up with
  [CodeJar](https://github.com/antonmedv/codejar) (CDN, ES module), using the page's own
  highlight.js instance so edited text re-highlights with the same theme as the static block.
- **Styling** lives in [docs/stylesheets/extra.css](docs/stylesheets/extra.css) under the
  `pyodide-runner__*` BEM class names — edit there to restyle, not the JS.
- **Wiring** — both files sit under `docs/` (MkDocs' `docs_dir`, where non-Markdown files get
  copied through as-is) and are pulled in via `extra_css`/`extra_javascript` in
  [mkdocs.yml](mkdocs.yml).
- **Why hand-rolled** — chosen over the existing `pyodide-mkdocs-theme` package (ACE Editor +
  jQuery Terminal + a macros-based plugin architecture) in favor of a minimal, fully
  custom-stylable implementation. If richer needs come up later (in-browser editing, `input()`
  support, exercise correctors), that package is the reference for a more complete but more
  opinionated approach.

### `python-ref` blocks — non-runnable cheat-sheet previews

A second fence language, ` ```python-ref `, also handled by `pyodide_runner.js`
(`buildReference()`): same dark panel + highlight.js coloring as a runnable block, but no Run
button and no CodeJar editing — for code meant to be read, not executed. Used specifically for
the always-visible preview inside a collapsible section's `<summary>` (see "Content page
structure" below) — every content page's per-concept sections open with one. Conventions:

- **One line per concept** covered in the collapsed dropdown below it — a `python-ref` block is
  a table of contents for that section's examples, not a worked example itself.
- **Continue from the page's already-defined variable** (e.g. `species`, set up in the page's
  top-level runnable block) rather than redeclaring a fresh throwaway list — keeps the block
  reading as a continuation of the same story instead of a new one.
- **End each line with a `# ...` comment showing the output** — the literal return value for
  read-only expressions (`species[0]  # "burmese"`), or the resulting state for mutating calls
  that return `None` (`species.sort()  # ["angolan", "ball", ...]`). Truncate long unchanged
  portions with `...` rather than dropping the comment.
- **Compute comments by hand** against the actual current value of the shared variable (or run
  it in a scratch shell) — a stale comment is worse than no comment.

## Content page structure

Every content page follows the same shape:

1. An intro paragraph.
2. One `##` section per concept, each with an intro sentence + a simple top-level runnable
   `python` block.
3. Zero or more collapsible subsections (`??? type "..."` admonitions — see "Admonitions"
   below) digging into specific operations.

Other notes:

- Read one of the more recently added pages' raw Markdown as the fastest way to pick up the
  convention before adding another.
- Several pages open with a small comparison or glossary table before the first `##` section —
  see "Glossary" below for when that's the right tool versus a single inline glossary term.
- Each concept section (or subsection) pairs a `python-ref` preview with prose notes and
  exactly one combined runnable `python` block covering every example mentioned in those notes
  — one Run button per section, not one per example.
- Subsection (`###`/`####`) headings are kept short — 1-2 words, or a single keyword/method
  name — since `toc.integrate` mirrors heading text verbatim into the sidebar TOC, and a long
  sentence-style heading would make that list unreadable. The fuller "why open this"
  explanation goes in the first sentence of the section's body instead.

## Text style conventions

Apply across every page's prose, headings, and `mkdocs.yml` nav labels:

- **"Python" is always capitalized** in prose (never "python" as a word). Other technical
  proper nouns follow their own standard capitalization too (NumPy, Pillow, JSON, CSV) — check
  the library's own convention if unsure. Doesn't apply inside fenced code blocks, inline code
  spans, or fenced code language tags (` ```python ` stays lowercase — it's syntax, not prose).
- **Headings use sentence case**, not Title Case — only the first word and proper
  nouns/keywords capitalized. Applies to `#`/`##`/`###`/`####` headings.
- **Full sentences end with a period.** Intro paragraphs and section-opening sentences get a
  trailing period if missing. Bare keyword/noun-phrase headings (`### int`, `### Lists`) stay
  short per the subsection convention above — don't lengthen into full sentences or add a
  period to a non-sentence heading.
- **Numbered steps start at 0**, not 1 — the first item in any ordered-list walkthrough is `0.`
  (Markdown honors the literal starting number of the first list item).
- **"Step X:" headings capitalize the first word after the colon**, then sentence case from
  there — `## Step 0: Install Python`, not `## Step 0: install Python`. The one exception to
  plain sentence case, since "Step 0:" reads as a label prefix, not the heading's first word.

## Content structure rules

Rules for deciding *where a piece of information goes* on a page — heading level, admonition,
glossary, or footnote. Guiding principle:

**A page should be as minimal as possible for a beginner to follow straight through, while
staying accurate — everything not required to understand the core concept moves out of the
main reading path (into an admonition, a footnote, or another page via a link) rather than
staying inline.**

### Headings

- **`#`** — the page title. One per page.
- **`##`** — one per top-level concept. The unit a page is built from (e.g. Integers, Floats,
  Strings on `types.md`) and the level `toc.integrate` uses for the sidebar outline. If a chunk
  of content doesn't map to a distinct concept a reader might jump straight to, it isn't a `##`.
- **`###`** / **`####`** — a subheading under the level above it, used when at least one of
  these is true:
    - **Skim target** — a reader scanning for one specific definition or operation (e.g. "how
      do I round a float?") should find it as a heading, not have to read a paragraph first.
    - **Standalone/modular** — the content works as its own self-contained mini-topic someone
      could link to or read in isolation.
    - **Breaks down the level above it** — the parent heading covers enough ground that named
      pieces are easier to follow than one long undivided section.
  Don't add one just to look structured — if none of the three apply, keep it as prose or a
  list under the parent heading instead.
- **Keep subheading text short** — 1-2 words or a method/keyword name — since `toc.integrate`
  mirrors it verbatim into the sidebar. The fuller "why open this" context belongs in the first
  sentence under the heading, not the heading itself.
- **No backticks in heading text** — even for a heading that's naming a piece of syntax (e.g.
  `#### *args tuple`, not `` #### `*args` tuple ``). Backticks are fine, and expected, in the
  body prose under the heading. **Exception:** an identifier containing a double underscore
  (`__init__`, `__repr__`, any dunder) needs its backticks kept — Markdown reads bare `__` as
  bold/emphasis markup, not literal underscores, so `### Overriding __init__()` renders (and
  slugifies) as "Overriding **init**()" with the underscores silently eaten. Confirm any heading
  change like this against the real built HTML, not just the source Markdown.
- **`####` is a normal fourth level**, used under the same three conditions as `###` above, for
  when a `###` section itself needs breaking down further (e.g. `types.md`'s `### int`/`### float`
  each splitting into `#### Arithmetic`, `#### Convert`, etc.). Used throughout content pages, not
  just `index.md`'s homepage category boxes or library pages.

### Cheatsheet flags (`index.md`, `libraries/index.md`)

The card grids on `index.md` and `libraries/index.md` are generated by the
[mkdocs-cheatsheet](https://github.com/luka-sherman/mkdocs-cheatsheet) plugin from flags on each
content page's headings. Neither index file lists links by hand; each holds a
`<!-- cheatsheet -->` placeholder. `libraries/index.md` has its own placeholder, so the homepage
shows library pages as title-and-description cards only, and their links appear only on
`libraries/index.md`.

- **Flag syntax.** Append the marker inside the heading's attr_list braces:
  `## Integers { cs="integers" }`. `{ cs }` uses the heading text. Several comma-separated labels
  each become a link to the same heading: `#### Add item { cs="append, extend, insert" }`.
- **What each level becomes.** Labels on the `#` title show at the top of the card and link to the
  top of the page (e.g. `isinstance`, `type`). A flagged `##` starts a bold "label:" line; its
  extra labels become links in that line. Flagged `###`/`####` headings become the links under
  the nearest `##`. A `##` line only shows its bold label when the `##` itself is flagged.
- **What to flag.** Flag headings that name a concrete concept or piece of syntax a reader would
  look up by name. Leave narrative headings ("What do you see when a program runs?", "Going
  further") unflagged. Syntax taught in prose without its own heading (e.g. `dict.get()`) goes on
  the nearest heading whose content covers it, as an extra label. Only flag what a page actually
  teaches; `print()` appearing as an example on `errors.md` isn't taught there.
- **Order.** `##` lines keep page order. Links within a line sort alphabetically
  (`sort: alphabetical` in `mkdocs.yml`), symbols before letters.
- **Card text.** Each page's front matter sets `cheatsheet_description` (falling back to
  `description`), plus `cheatsheet_title`, `cheatsheet_icon` or `cheatsheet_title_suffix` (the
  built-in/third-party badge on library cards) where the defaults don't fit.
- **Essentials mode.** A flagged heading that carries `data-fcm-hide="essentials"` passes it to
  its cheatsheet line or link, so the audience toggle hides both together. A whole card is
  hidden with `cheatsheet_attrs: {data-fcm-hide: essentials}` in front matter.
- **Verify with a real build.** A renamed heading moves its flag with it, so the cheatsheet can't
  go stale, but `mkdocs build` still prints a `WARNING` for any broken link elsewhere.
- **Marking content "advanced" for the Essentials/Advanced toggle** — the header's segmented
  control is provided by the `mkdocs-audience-toggle` plugin (configured under `plugins:` in
  `mkdocs.yml`) and hides content marked `data-fcm-hide="essentials"`. On a content page, append
  `{ data-fcm-hide="essentials" }` to the heading line (e.g. `functions.md`'s
  `## Decorators { data-fcm-hide="essentials" }`). This hides that heading, everything up to the
  next heading of the same or higher level, and its sidebar entry. The cheatsheet picks the
  marker up from the heading, so there's no second place to tag.
  Which spots to mark, and what counts as advanced/niche vs. core, is a per-editor judgment call
  — there's no test enforcing it either way. See the `mkdocs-audience-toggle` plugin's own
  README for the toggle mechanism itself. A page can still show a *link* to a hidden section (e.g.
  `collections.md`'s own cheat-sheet table links to `#tuples` even though the "Tuples" heading is
  hidden) — following such a link automatically switches back to Advanced and reveals the target,
  so this doesn't need special-casing when adding new advanced content.

### Admonitions (`??? type "..."`)

Admonitions are for **helpful-but-not-necessary branches** — content a reader benefits from but
doesn't need to understand the concept on first pass. If removing it would leave a gap in
understanding *how the core concept works*, it belongs in main prose, not an admonition.

Use them for:

- **Further reading** — a related idiom, a shortcut, "here's another way to do this."
- **Branching** — an edge case, gotcha, or "this also works but here's when it breaks," that
  only matters once someone hits it.

Pick the existing type that matches the branch, don't invent new ones without a reason:

| Type | Use for |
|---|---|
| `??? run` | The section's one combined runnable example — either a worked script combining every snippet shown above it ("All the examples above, combined into one script"), or, on pages that call for practice (e.g. `collections.md`), fill-in exercises with a hidden "Show solutions" block. Always collapsed. |
| `??? tip` | An optional aside — alternate approach, shortcut, related technique. |
| `??? warning` | A concrete "this will bite you" failure mode, not a generic caveat. |
| `??? note` | A conceptual clarification that isn't a warning or a tip. |
| `??? info` | Defining a term/concept adjacent to the page but not the topic itself. |
| `??? failure` | The negative counterpart to a `success` branch — "this didn't work, here's what to do about it" (e.g. workspace.md's "download Python here" branch when `python --version` doesn't show 3.x.x). |
| `??? ai` | Opinion/meta content specifically about learning with or around AI (e.g. index.md's FAQ tabs on whether/how to use AI while learning) — not used for teaching content about Python itself. |
| `??? efficiency` | A runtime/space aside naming the cost behind a choice already shown in prose (e.g. list vs. set membership, `sort()` vs. `sorted()`) — usually a Big O difference, occasionally a constant-factor one (`.get()` vs. two hash lookups, vectorized NumPy vs. a Python loop) where it's still worth flagging but doesn't change the O(...) class. Wrap it in `<div data-fcm-hide="essentials" markdown="block">` on a page that participates in the Essentials/Advanced toggle (skip it on a page that doesn't, like the library reference pages), and close with a link to [style.md's "Efficiency"](docs/practices/style.md#efficiency) section. Formalizes a tradeoff the surrounding prose already states in plain language; doesn't introduce the tradeoff for the first time. |
| `!!! example` | An always-open side-by-side comparison the reader is meant to see without a click, not a branch — e.g. "how to loop each type," showing every collection type's loop pattern in one visible table. |

Default to collapsed (`???`), not always-open (`!!!`) — an always-open admonition competes with
the main prose for attention. Use `!!!` only when both are true:

- The content is **core**, not an optional branch — the box itself carries weight the
  surrounding prose needs.
- The admonition format is **genuinely the clearest way** to present it — e.g. `errors.md`'s
  paired `!!! success` / `!!! danger` boxes contrasting "handle it with try/except" against
  "fix the code instead," where the visual side-by-side split does real work a paragraph
  wouldn't.

This should still be rare — most core content belongs in plain prose, not any admonition.

### Glossary

- **Single technical term** an absolute beginner might not know → add it to
  [includes/glossary.md](includes/glossary.md) as `*[term]: definition` (the `abbr` extension,
  auto-appended to every page via `pymdownx.snippets`) instead of explaining it inline or in an
  admonition. Every occurrence of that exact term anywhere on the site then gets a dotted
  underline and hover tooltip automatically — no per-page wiring. Use for a term that's just a
  name for a concept (`exception`, `mutable`, `subclass`, `docstring`) where one sentence fully
  defines it.
- **Term needs more than one sentence**, or needs comparing against sibling terms (`int` vs
  `float` vs `str`, `for` vs `while`) → a **comparison table** instead, at the top of a page
  before the first `##` (e.g. `types.md`'s type-comparison table, `loops.md`'s `for` vs `while`
  table, `oop.md`'s term table). Table rules:
    - Skip a "Pros/Cons" framing unless there's a genuine tradeoff — a single "Use it for"
      column reads better than forcing artificial pro/con pairs.
    - Cut jargon the table hasn't taught yet, or replace it with the concrete consequence.
    - A row needing more than one fact gets an inline `<ul><li>` list in the cell; a row that's
      one clean sentence stays plain text.
    - These are reference/comparison, not tutorial — link out to the page's own `##`/`###`
      section for the full explanation rather than duplicating it in the cell.

### Footnotes

Enabled via `markdown_extensions: [footnotes, ...]` in `mkdocs.yml`. Use `[^label]` inline and
`[^label]: ...` for the definition.

Footnotes are for content that is **too minor for an admonition, but still worth saying**:

- A **clarification** not important enough to interrupt the sentence or justify its own
  admonition — the kind of aside currently wedged into prose with an em-dash ("...which is
  technically X, but Y in practice").
- An **"actually, here's why this works"** dip into a more advanced explanation a beginner does
  **not need in order to use the feature**, but that helps build a correct mental model if
  curious (e.g. why `bool` being an `int` subclass matters, why a triple-quoted comment is
  actually a discarded string literal).

If the aside is something a reader is likely to actively want to branch into and read (a
worked-out further example, a related technique), it's a `??? tip`, not a footnote — footnotes
are for the reader who's fine never clicking the marker at all.

- **Admonition** = a branch — has its own weight, could stand alone.
- **Footnote** = a whisper — a few words, meant to be read in the flow of the sentence's
  superscript, not sought out.

### Cross-linking

Pages should stand alone — a reader landing on one page shouldn't have to hop to another just
to follow it. Whether to link or restate depends on what the concept actually belongs to:

- **Restate** when the concept is a real, load-bearing part of more than one page, just not big
  enough to deserve its own page — e.g. `break`/`continue` genuinely belongs to both
  `conditionals.md` and `loops.md` (loop control is driven by a conditional check), so both
  pages explain it in place rather than one deferring to the other.
- **Link** when the concept has its own dedicated page — e.g. `oop.md` linking to
  `functions.md` for how functions work, rather than re-explaining functions, since Functions
  is the canonical page for that topic. Link to the specific heading (`[text](page.md#anchor)`)
  rather than the page root.

If unsure which case applies: is there already a page whose whole job is to explain this? If
yes, link to it. If it's a shared building block no single page owns, restate it in each page
it's actually part of.
