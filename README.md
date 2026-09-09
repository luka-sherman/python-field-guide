# [PythonFieldGuide.com breakdown](https://pythonfieldguide.com)

## Table of Contents

- [What this is](#what-this-is)
- [Site generator](#site-generator)
- [Runnable code blocks](#runnable-code-blocks)
- [Styling](#styling)
- [Content conventions](#content-conventions)
- [Running locally](#running-locally)
- [Testing](#testing)
- [Deploying](#deploying)
- [Analytics](#analytics)
- [License](#license)

## What this is

Quick cheatsheet for basic Python.

This is a casual and unpolished personal project, started in Aug '26.

I wrote and built this from scratch — it started as a few quick-reference explanations on loops and lists for high-school intro-Python students working on their first projects, and evolved from there. I couldn't find a resource my students would consistently use that had:

- simple explanations for beginners without technical jargon
- no advanced topics that intimidate or overwhelm beginners
- quick-reference code samples, to browse what functions they could apply to solve their problem
- at-a-glance reminders for students who already knew a concept but needed a refresher on the specifics or syntax
- quick intuitive navigation, see everything in one place
- clean, minimal UI — some sites were visually dated, and less enjoyable for beginners

## Site generator

### MkDocs

MkDocs is a static-site generator, which turns a tree of Markdown files into a documentation website. For bonus points it's written in Python.

### Material for MkDocs

Material for MkDocs is a theme and feature layer for MkDocs. When I found myself overriding too much of the default theme's formatting, I transitioned to this to override less — though I still maintain some custom CSS.

### PyMdown Extensions

PyMdown Extensions is a bundle of Markdown extensions, which adds authoring features on top of plain Markdown. In use here:

- `tabbed` — tabbed content blocks
- `details` — collapsible admonitions
- `keys` — keyboard-key styling
- `caret` — superscript for exponent notation
- `emoji` — `:emoji:` shortcodes rendered as Twemoji SVGs
- `tasklist` — styled task-list checkboxes
- `superfences` — nested fences, and handing Mermaid code blocks off to the renderer
- `snippets` — auto-appends `includes/glossary.md` to every page, a list of `*[term]: definition` entries that the `abbr` extension (plus Material's `content.tooltips`) turns into the hover tooltips on keywords
- `highlight` — set to `use_pygments: false`, so client-side highlight.js does the syntax highlighting instead of build-time Pygments

### Standard Markdown extensions

These ship with Python-Markdown and are enabled alongside the PyMdown set:

- `footnotes` — the `[^1]` reference notes
- `abbr` — the glossary tooltips (fed by `snippets` above)
- `admonition` — the note/warning callout boxes
- `attr_list` — `{ .class #id }` attributes on elements, e.g. the homepage buttons
- `md_in_html` — Markdown parsed inside raw HTML blocks, e.g. the card grids
- `tables` — pipe tables

## Runnable code blocks

### Pyodide

Pyodide is CPython compiled to WebAssembly, which runs Python in the browser with no download or install. It powers the runnable blocks, so readers can execute and tweak an example inline. The runtime is pulled from a CDN on demand the first time someone clicks Run.

### CodeJar

CodeJar is a ~2KB code editor, which makes an element editable in place with live syntax highlighting. It wraps each Pyodide block so you can change a value and rerun without leaving the page.

### highlight.js

highlight.js is a syntax highlighter, which colors code in the browser. It handles both the static examples and whatever a reader types into a CodeJar block. Pygments, MkDocs's usual build-time highlighter, is switched off in favor of it.

## Styling

### Mermaid

Mermaid is a diagram renderer, which draws flowcharts and diagrams from a plain-text description. A small config shim themes them to the site palette.

### Google Fonts

Google Fonts is a web-font host, which serves font files to the page from its CDN. It provides the two typefaces — Source Serif 4 for text, JetBrains Mono for code — wired in through Material's native font config.

## Content conventions

[STRUCTURE.md](STRUCTURE.md) is the reference for authoring or editing pages. It covers:

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

Install the browser binary once, then run the suite:

```bash
source .venv/bin/activate
playwright install chromium   # one-time, downloads a browser binary for the accessibility tests
pytest
```

### pytest

pytest is the standard Python test runner, which discovers `test_*` functions across the repo and reports what passed. It's the single entry point for the whole suite:

- `tests/test_structure.py` checks `docs/*.md` against the mechanically-verifiable rules in
  STRUCTURE.md. See its docstring/comments for what's covered and what's deliberately left out
  because it needs editorial judgment a text-only check can't make.
- `tests/test_accessibility.py` is a static (no-browser) regression check for a specific
  accessibility bug pattern (an `outline: none` with no `:focus-visible` replacement).
- `tests/test_accessibility_browser.py` renders real pages with Playwright and runs
  axe-core against them — the heaviest check in the suite, since it needs
  `playwright install chromium` above and launches a real browser per run.

### Playwright

Playwright is a browser-automation library, which drives a real browser from code to load pages and read back the rendered result. Here it launches a headless Chromium so the accessibility pass sees each page exactly as a browser builds it.

### axe-core

[axe-core](https://github.com/dequelabs/axe-core) is an accessibility rule engine, which scans a rendered page's DOM for WCAG violations. It runs inside the Playwright browser against every fully rendered page.

## Deploying

### GitHub Actions

GitHub Actions is GitHub's built-in CI/CD runner, which executes a workflow of commands on their servers in response to repo events like a push. Here, [.github/workflows/deploy.yml](.github/workflows/deploy.yml) runs on every push to `main`. It installs `requirements.txt` and runs `mkdocs gh-deploy --force`, which builds the site and pushes the static output to the `gh-pages` branch. No manual deploy step is needed — just push to `main`. A push is usually live within a few minutes.

### GitHub Pages

GitHub Pages is GitHub's free static-site host, which serves the files on a chosen branch of a repo as a website. Here it serves the built site from the `gh-pages` branch at my custom domain.

### Purchased .com domain

The domain is set up via the [docs/CNAME](docs/CNAME) file (`pythonfieldguide.com`), which MkDocs copies into every build so Pages keeps serving there. On my registrar I added apex `A` records pointing at GitHub's Pages IPs.

## Analytics

Google Analytics (GA4) is wired in through Material's built-in support. I immediately noticed the library pages drawing more traffic than the rest of the site, so I built those out further.

## License

The content and code in this repo are not licensed for reuse — see [LICENSE](LICENSE).
