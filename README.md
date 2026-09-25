# [PythonFieldGuide.com](https://pythonfieldguide.com)

[![Live site](https://img.shields.io/badge/live-pythonfieldguide.com-2e7d32)](https://pythonfieldguide.com)
[![Deploy](https://github.com/luka-sherman/python-field-guide/actions/workflows/deploy.yml/badge.svg)](https://github.com/luka-sherman/python-field-guide/actions/workflows/deploy.yml)
[![Built with Material for MkDocs](https://img.shields.io/badge/built%20with-Material%20for%20MkDocs-526cfe?logo=materialformkdocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![Runnable code via Pyodide](https://img.shields.io/badge/runnable%20code-Pyodide-3776ab?logo=python&logoColor=white)](https://pyodide.org)
[![Accessibility tested with axe-core](https://img.shields.io/badge/a11y-axe--core%20tested-663399)](https://github.com/dequelabs/axe-core)

## Table of Contents

- [What this is](#what-this-is)
- [Content](#content)
- [Site generator](#site-generator)
- [Client-side rendering](#client-side-rendering)
- [New open source](#new-open-source)
- [Theme](#theme)
- [Content conventions](#content-conventions)
- [Running locally](#running-locally)
- [Testing](#testing)
- [Deploying](#deploying)
- [Analytics](#analytics)
- [License](#license)

## What this is

Quick cheatsheet for basic Python.

**This is a casual and unpolished personal project, started in Aug '26.**

I wrote and built this from scratch, not as a complete Python language reference, but as a **visualization of my mental model** of how Python works.

It started as a few quick-reference explanations on loops and lists for high-school intro-Python students working on their first independent projects, and evolved from there. I couldn't find a resource my students would consistently use that had:

- simple explanations for beginners without technical jargon
- no advanced topics that intimidate or overwhelm beginners
- quick-reference code samples, to browse what functions they could apply to solve their problem
- at-a-glance reminders for students who already knew a concept but needed a refresher on the specifics or syntax
- quick intuitive navigation, see everything in one place
- clean, minimal UI — some sites were visually dated, and less enjoyable for beginners

## Content

Pages are hand-written by me *(very much a work in progress)*.

On the homepage there is a compacted quick reference cheatsheet that includes most python keywords that are covered on that page. As this content evolved so did the structure, it was an immense amount of technical writing and information architecture. 

**Core Python**

- **Get started** — Workspace setup, Foundations
- **Data types** — Scalars (int, float, str, bool, None), Collections (list, dict, tuple, set)
- **Control flow** — Conditionals, Loops
- **Code organization** — Functions, Classes
- **External files and resources** — Modules & imports, Reading & writing files
- **Robust programming practices** — Style, Errors

**Add-on libraries** 

- **Utilities** — collections, datetime, math, random, re, time
- **Data analysis** — csv, matplotlib, NumPy, pandas
- **APIs** — json, requests
- **Image editing** — Pillow
- **Computer vision** — OpenCV
- **Desktop UIs** — Tkinter
- **Games** — turtle
- **Testing** — pytest

## Site generator

### [MkDocs](https://www.mkdocs.org/)

A static-site generator, which turns a tree of Markdown files into a documentation website. For bonus points it's written in Python.

### [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

A theme and feature layer for MkDocs. When I found myself overriding too much of the default theme's formatting, I transitioned to this to rewrite less — though I still maintain some custom CSS.

### [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/):

- `tabbed` — tabbed content blocks
- `details` — collapsible admonitions
- `keys` — keyboard-key styling
- `caret` — superscript for exponent notation
- `emoji` — `:emoji:` shortcodes rendered as Twemoji SVGs
- `tasklist` — styled task-list checkboxes
- `superfences` — nested fences, and handing Mermaid code blocks off to the renderer
- `snippets` — auto-appends `includes/glossary.md` to every page, a list of `*[term]: definition` entries that the `abbr` extension (plus Material's `content.tooltips`) turns into the hover tooltips on keywords
- `highlight` — set to `use_pygments: false`, so client-side highlight.js does the syntax highlighting instead of build-time Pygments

### [Python-Markdown extensions](https://python-markdown.github.io/):

- `footnotes` 
- `abbr` — the glossary tooltips (fed by `snippets` above)
- `admonition` — the note/tip/warning callout boxes that can be collapsible
- `attr_list` — `{ .class #id }` attributes on elements, e.g. the homepage buttons
- `md_in_html` — Markdown parsed inside raw HTML blocks, e.g. the card grids on the homepage
- `tables` — pipe tables, in use at the top of some pages to compare components

## Client-side rendering

Things MkDocs doesn't produce at build time — JavaScript turns them into their final form in the reader's browser.

### [Pyodide](https://pyodide.org/)

CPython compiled to WebAssembly, which runs Python in the browser with no download or install. It powers the runnable blocks, so readers can execute and tweak an example inline. The runtime is pulled from a CDN on demand the first time someone clicks Run.

### [CodeJar](https://medv.io/codejar/)

A ~2KB code editor, which makes an element editable in place with live syntax highlighting. It wraps each Pyodide block so you can change a value and rerun without leaving the page.

### [highlight.js](https://highlightjs.org/)

A syntax highlighter, which colors code in the browser. It handles both the static examples and whatever a reader types into a CodeJar block. Pygments, MkDocs's usual build-time highlighter, is switched off in favor of it.

### [Mermaid](https://mermaid.js.org/)

A diagram renderer, which draws flowcharts and diagrams from a plain-text description. Fenced `mermaid` blocks in the Markdown are rendered to SVG on page load.

### Essentials / Advanced toggle

A two-option [switch](docs/javascripts/essentials_toggle.js) that lets a reader hide everything beyond a first-pass beginner curriculum. Content is opted into hiding by marking it `data-advanced="true"`:

- On a `##`/`###` heading inside a content page (e.g. functions.md's `## Decorators`), it hides that heading plus every sibling up to the next heading of the same or higher level, and removes the matching entry from the `toc.integrate` sidebar — so there's no dead nav link to something that's hidden.
- On a homepage card-grid row, it hides just that row; `data-advanced="card"` hides an entire homepage card instead, for a whole linked page rather than one section.

Each marking is independent — there's no shared list of "advanced" topics to keep in sync, just the attribute at each spot in the Markdown. State persists in `localStorage` and applies on every page (also settable via a `?simplified=true`/`false` URL param, for sharing a pre-set link). If a visible link points at a heading that's currently hidden (e.g. collections.md's cheat-sheet table linking to `#tuples`), following it flips the toggle back to Advanced and reveals the target instead of landing on nothing.

Some examples of content that is hidden while in "Essentials" mode, while a student is first learning to program:

- Collection types a beginner can often get by without (tuples, sets)
- OOP features past a basic class (method decorators, multiple inheritance, polymorphism, encapsulation, operator overloading, dataclasses, abstract base classes). OOP can already be a challenging topic, and they should first have a strong understanding of it before adding these features.
- Function features (type hints, positional-only/keyword-only parameters, recursion, decorators, generators)
- File-handling edge cases (seek and tell, the `"x"` create mode)
- Styling suggestions that aren't critical (file order, constants, quote style, indentation, comments, the truthy-check and `enumerate()` idioms)
- Workspace/tooling topics as most students are using an IDE (using the terminal, virtual environments)
- Efficiency, awareness of space and time resources, Big O notation

## New open source

### [mkdocs-nested-tabs](https://pypi.org/project/mkdocs-nested-tabs/)

I published a new mkdocs plugin to add functionality I wanted for this site. 

A multi-level two row header — every top-level category shown with all of its child pages
listed underneath. An enhancement to Material's native tabs (which only reveal a category's children via a hover dropdown, one at a time) — started as site-specific JavaScript here, then got extracted into its own published PyPi plugin.

```bash
pip install mkdocs-nested-tabs
```

```yaml
theme:
  features:
    - navigation.tabs
plugins:
  - nested-tabs
```

I extracted it because it fills a real, previously-requested gap — someone asked for exactly this in a [Material for MkDocs discussion](https://github.com/squidfunk/mkdocs-material/discussions/4765) and the maintainer's answer was horizontal scroll, not an expanded layout — and nothing on PyPI already does it (checked against the existing nav/dropdown/sidebar plugins first). It reads a site's `nav:` tree directly at runtime, so it needs no plugin-specific configuration for the common case, and falls back to Material's own theme variables for styling so it looks reasonable on any palette out of the box. This site is its first real consumer — see `mkdocs.yml`'s `plugins:` list and `extra.css`'s `--md-nested-tabs-*` overrides for how it's wired in here.

## Theme

### Custom CSS

Styling, primarily centered on making the homepage a compact all-in-one dashboard view. 

### [Google Fonts](https://fonts.google.com/)

Serves font files to the page. It provides the two typefaces — Source Serif 4 for text, JetBrains Mono for code — wired in through Material's native font config.

## Content conventions

I found myself writing so much content for this, and needing to jump between different pages so frequently while I was editing, that I created a structure guide to help the site stay consistent as it grows over time. [STRUCTURE.md](STRUCTURE.md) is the reference for authoring or editing pages. It covers:

- **Runnable code blocks** — how the Pyodide/CodeJar feature is wired (detection of
  ` ```python ` fences, lazy CDN load, stdout capture, editable re-highlighting), and the
  `python-ref` fence used for the non-runnable cheat-sheet preview at the top of each concept
  section.
- **Page shape** — every content page is an intro paragraph, then one `##` per concept (each
  with an intro sentence and a single combined runnable block), then optional `???` collapsible
  subsections for specific operations.
- **Text style** — "Python" always capitalized in prose, sentence-case headings, full sentences
  end with a period, numbered walkthroughs start at `0.`, short (1–2 word) subheadings because
  `toc.integrate` mirrors them verbatim into the sidebar.
- **Where information goes** — the decision rules for heading level vs. admonition vs. glossary
  entry vs. footnote, with a table of which `??? type` to use for what, plus how the homepage
  keyword deep-links in `index.md` have to cover every heading.

The mechanically-checkable subset of these rules (heading case, list-start number, admonition
types, `python-ref` comment format, homepage link coverage, clean `mkdocs build`) is enforced
by `tests/test_structure.py`; the rest need editorial judgment.

## Running locally

Create the virtualenv, install the dependencies, and start the dev server:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

mkdocs serve   # live-reloading dev server at http://127.0.0.1:8000
```

## Testing

The site's main features are integrations of client-side libraries, plus a custom CSS layered over
Material. This test suite covers
the invariants nothing else checks: the runnable code blocks still execute in a browser, the
palette clears WCAG AA contrast in light and dark mode, the custom CSS doesn't trap keyboard
focus or swallow clicks, and every content page keeps the structure the homepage cards link to.

### [pytest](https://docs.pytest.org/)

The standard Python test runner, which discovers `test_*` functions across the repo and reports what passed. It's the single entry point for the whole suite:

- `tests/test_structure.py` checks `docs/*.md` against the mechanically-verifiable rules in
  STRUCTURE.md. See its docstring/comments for what's covered and what's deliberately left out
  because it needs editorial judgment a text-only check can't make.
- `tests/test_accessibility.py` is a static (no-browser) regression check for a specific
  accessibility bug pattern (an `outline: none` with no `:focus-visible` replacement).
- `tests/test_typos.py` runs [codespell](#codespell) over the site's prose sources.
- The browser-based accessibility tier (`test_accessibility_browser.py`,
  `test_accessibility_runnable.py`, `test_accessibility_keyboard.py`) renders real pages with
  Playwright and checks: axe-core over representative pages in light/dark mode and at
  mobile/tablet widths; the hand-wired Pyodide runnable blocks (accessible names, keyboard
  focus order, the output live region); and keyboard navigation (skip link, a visible focus
  ring on every tab stop, no positive tabindex, palette toggle reachable). It's the heaviest
  part of the suite — needs `playwright install chromium` above and launches a real browser.
- `tests/test_essentials_toggle.py` is a browser test (same Playwright setup) for the
  Essentials/Advanced toggle described above: the default (Advanced) state, that
  `?simplified=true` hides marked content and carries onto a page's own heading + TOC entry,
  and the link-recovery behavior for a visible link into hidden content.

### [Playwright](https://playwright.dev/)

A browser-automation library, which drives a real browser from code to load pages and read back the rendered result. Here it launches a headless Chromium so the accessibility pass sees each page exactly as a browser builds it.

### [axe-core](https://github.com/dequelabs/axe-core)

An accessibility rule engine, which scans a rendered page's DOM for WCAG violations. It runs inside the Playwright browser against every fully rendered page.

### [codespell](https://github.com/codespell-project/codespell)

A spell checker aimed at source code and prose, which flags known misspellings against a fixed list rather than words simply missing from a dictionary. `tests/test_typos.py` runs it over the site's page content and editorial docs.

### Continuous integration

1. Work is done on the `development` branch.
2. A `development` -> `main` pull request is opened.
3. [`test.yml`](.github/workflows/test.yml) runs the full `pytest` suite in GitHub Actions against the pull request.
4. Merging into `main` publishes the site: [`deploy.yml`](.github/workflows/deploy.yml) builds it and pushes the output to GitHub Pages.

### Running the tests locally

```bash
source .venv/bin/activate
playwright install chromium   # one-time, downloads a browser binary for the accessibility tests
pytest
```

## Deploying

### [GitHub Actions](https://github.com/features/actions)

GitHub's built-in CI/CD runner, which executes a workflow of commands on their servers in response to repo events like a push. Here, [.github/workflows/deploy.yml](.github/workflows/deploy.yml) runs on every push to `main`. It installs `requirements.txt` and runs `mkdocs gh-deploy --force`, which builds the site and pushes the static output to the `gh-pages` branch. No manual deploy step is needed — just push to `main`. A push is usually live within a few minutes.

### [GitHub Pages](https://pages.github.com/)

GitHub's free static-site host, which serves the files on a chosen branch of a repo as a website. Here it serves the built site from the `gh-pages` branch at my custom domain.

### Purchased .com domain

The domain is set up via the [docs/CNAME](docs/CNAME) file, which MkDocs copies into every build so Pages keeps serving there. On my registrar I then added apex `A` records pointing at GitHub's Pages IPs.

## Analytics

[Google Analytics](https://marketingplatform.google.com/about/analytics/) (GA4) is wired in through Material's built-in support. I immediately noticed the library pages drawing more traffic than the rest of the site, so I built those out further.

## License

The content and code in this repo are not licensed for reuse — see [LICENSE](LICENSE).
