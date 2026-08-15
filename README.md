# [Python Field Guide](pythonfieldguide.com)

## What it is 

Quick cheatsheet for basic Python.

I built this from scratch — it started as a few quick-reference explanations for highschool intro python students working on their first programs, and evolved into a fairly comprehensive site. I couldn't find a resource my students would consistently use that had:

- simple explanations for beginners without technical jargon
- no advanced topics that intimidate or overwhelm beginners
- quick-reference code samples, to browse what functions they could apply to solve their problem
- at-a-glance reminders for students who already knew a concept but needed a refresher on the specifics or syntax
- quick intuitive navigation
- clean, minimal UI

## Stack 

**MkDocs** is a lightweight Markdown library, for bonus points it's written in Python.

**Pyodide** blocks let users execute code in the browser with no download/install to instantly experiment with concepts.

**Material for MkDocs theme** - When I found myself overriding too much of the native theme, I switched over to this so I could stop reinventing the wheel.

## Content conventions

See [STRUCTURE.md](STRUCTURE.md) for how pages are built — runnable code blocks, page shape,
house style, and the rules for where a given piece of information belongs (heading, admonition,
glossary, or footnote).

## Running locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

mkdocs serve   # live-reloading dev server at http://127.0.0.1:8000
```

## Testing

```bash
source .venv/bin/activate
playwright install chromium   # one-time, downloads a browser binary for the accessibility tests
pytest
```

- `tests/test_structure.py` checks `docs/*.md` against the mechanically-verifiable rules in
  STRUCTURE.md. See its docstring/comments for what's covered and what's deliberately left out
  because it needs editorial judgment a text-only check can't make.
- `tests/test_accessibility.py` is a static (no-browser) regression check for a specific
  accessibility bug pattern (an `outline: none` with no `:focus-visible` replacement).
- `tests/test_accessibility_browser.py` renders real pages with Playwright and runs
  [axe-core](https://github.com/dequelabs/axe-core) against them — the heaviest check in the
  suite, since it needs `playwright install chromium` above and launches a real browser per run.

## Deploying

Pushes to `main` are automatically built and published to GitHub Pages by
[.github/workflows/deploy.yml](.github/workflows/deploy.yml), which runs `mkdocs gh-deploy`
to push the built site to the `gh-pages` branch. No manual deploy step is needed — just push
to `main`.

The repo's GitHub Pages source (Settings → Pages) needs to point at the `gh-pages` branch for
this to take effect.

## License

The content and code in this repo are not licensed for reuse — see [LICENSE](LICENSE).