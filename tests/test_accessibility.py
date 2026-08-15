"""Static regression checks for accessibility issues found by a manual axe-core audit
(see project history) that a browser isn't needed to catch.

This is deliberately narrow: it encodes the *specific pattern* behind one real bug (a
stretched-link card losing its focus ring because `outline: none` was added with no
`:focus`/`:focus-visible` replacement), not a general CSS linter. It won't catch color
contrast, ARIA labeling, or anything else a real browser + axe-core would — that's the
separate, heavier tier in test_accessibility_browser.py (Playwright + axe-core against
rendered pages).
"""

import re

from conftest import REPO_ROOT

EXTRA_CSS = REPO_ROOT / "docs" / "stylesheets" / "extra.css"

RULE_RE = re.compile(r"([^{}]+)\{([^{}]*)\}")
OUTLINE_NONE_RE = re.compile(r"outline\s*:\s*(none|0)\s*(;|$)")


def _rules(css_text: str):
    for selector, body in RULE_RE.findall(css_text):
        yield selector.strip(), body


def test_outline_none_has_a_focus_visible_replacement():
    css_text = EXTRA_CSS.read_text()
    failures = []
    for selector, body in _rules(css_text):
        if "," in selector or not OUTLINE_NONE_RE.search(body):
            continue
        # Every rule in this file that replaces the focus ring does so by appending
        # :focus or :focus-visible directly onto the same selector string (see
        # .pyodide-editor:focus, .pyodide-runner__run-btn:focus-visible,
        # .md-button:focus-visible) — so require that same paired selector to exist.
        replacement_selectors = {f"{selector}:focus", f"{selector}:focus-visible"}
        has_replacement = any(
            other_selector in replacement_selectors
            for other_selector, _ in _rules(css_text)
        )
        if not has_replacement:
            failures.append(selector)
    assert not failures, (
        "These selectors set `outline: none` with no `:focus`/`:focus-visible` "
        "replacement on the same selector — a keyboard user tabbing to them gets no "
        "visible focus indicator (this is exactly how the homepage card-grid links lost "
        "theirs). Add a `<selector>:focus-visible { outline: ...; }` rule:\n"
        + "\n".join(failures)
    )
