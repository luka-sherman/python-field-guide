"""Shared fixtures for the test suite.

test_structure.py checks the *mechanically verifiable* rules in ../STRUCTURE.md — things like
"numbered walkthroughs start at 0" or "every python-ref line ends in a comment". Rules that
require editorial judgment (e.g. "is this admonition core enough to be always-open") are not
encoded here; see the comments in test_structure.py for what's deliberately out of scope.

The accessibility checks are tiered:
  - test_accessibility.py — static, no browser (a specific `outline: none` CSS bug pattern).
  - test_accessibility_browser.py — Playwright + axe-core over representative pages, in light
    and dark mode and at mobile / tablet widths.
  - test_accessibility_runnable.py — the hand-wired Pyodide runnable code block feature:
    accessible names, keyboard focus order, the output live region.
  - test_accessibility_keyboard.py — keyboard navigation: skip link, visible focus on every
    tab stop, no positive tabindex, palette toggle operable.
The browser tiers share `built_site` / `site_url` and the axe helpers (`run_axe`,
`format_violations`, `DISABLED_RULES`) defined below.
"""

import functools
import http.server
import re
import subprocess
import sys
import threading
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"

ALL_DOC_FILES = sorted(DOCS_DIR.rglob("*.md"))


def rel(path: Path) -> str:
    return path.relative_to(DOCS_DIR).as_posix()


FENCE_RE = re.compile(r"^(?P<indent>\s*)```(?P<lang>\S*)\s*$")


def iter_lines(path: Path):
    """Yield (lineno, raw_line, in_fence, fence_lang) for every line.

    `in_fence` reflects whether the line's *content* sits inside a fenced code block —
    the fence delimiter lines themselves report False, since they're markdown syntax,
    not code/heading content.
    """
    in_fence = False
    fence_lang = None
    for lineno, raw in enumerate(path.read_text().splitlines(), start=1):
        m = FENCE_RE.match(raw)
        if m:
            in_fence = not in_fence
            fence_lang = m.group("lang") if in_fence else None
            yield lineno, raw, False, None
            continue
        yield lineno, raw, in_fence, fence_lang


def iter_fenced_blocks(path: Path, lang: str | None = None):
    """Yield (start_lineno, end_lineno, indent, content_lines) per fenced code block.

    content_lines have the fence's own indentation stripped (fences nested inside an
    admonition are indented to match the admonition body).
    """
    blocks = []
    in_fence = False
    cur_lang = None
    cur_indent = 0
    start = None
    content: list[str] = []
    for lineno, raw in enumerate(path.read_text().splitlines(), start=1):
        m = FENCE_RE.match(raw)
        if m:
            if not in_fence:
                in_fence = True
                cur_lang = m.group("lang")
                cur_indent = len(m.group("indent"))
                start = lineno
                content = []
            else:
                in_fence = False
                if lang is None or cur_lang == lang:
                    blocks.append((start, lineno, cur_indent, content))
            continue
        if in_fence:
            content.append(raw[cur_indent:] if len(raw) >= cur_indent else raw.lstrip())
    return blocks


# --- prose-stripping helpers, for checks that must ignore code/links/icons ---

HTML_CODE_RE = re.compile(r"<(code|pre)[^>]*>.*?</\1>", re.S)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
LINK_TARGET_RE = re.compile(r"\]\([^)]*\)")
ICON_SHORTCODE_RE = re.compile(r":[\w-]+:")
ATTR_LIST_RE = re.compile(r"\{[^}]*\}")


def strip_non_prose(text: str) -> str:
    """Strip code spans/blocks-as-HTML, link targets, icon shortcodes, and attr_list blocks.

    Leaves link *text* and heading words intact so callers can still scan the remaining prose.
    """
    text = HTML_CODE_RE.sub(" ", text)
    text = INLINE_CODE_RE.sub(" ", text)
    text = LINK_TARGET_RE.sub("]", text)
    text = ICON_SHORTCODE_RE.sub(" ", text)
    text = ATTR_LIST_RE.sub(" ", text)
    return text


HEADING_RE = re.compile(r"^(#{1,4})\s+(.*?)\s*$")


def iter_headings(path: Path, levels=(1, 2, 3, 4)):
    """Yield (lineno, level, raw_heading_text) for ATX headings outside code fences."""
    for lineno, raw, in_fence, _ in iter_lines(path):
        if in_fence:
            continue
        m = HEADING_RE.match(raw)
        if m and len(m.group(1)) in levels:
            yield lineno, len(m.group(1)), m.group(2)


# --- one real `mkdocs build`, shared by every test that needs it ---


@pytest.fixture(scope="session")
def built_site(tmp_path_factory):
    """Run `mkdocs build` once and share the output across tests.

    STRUCTURE.md calls this out directly: "Verify with a real build, not by eye — mkdocs
    build prints a WARNING for any link/anchor MkDocs can't resolve; treat that warning as
    a checklist." This fixture is that build, reused by the warnings check and the homepage
    keyword-link coverage check so we only pay the build cost once per test run.
    """
    site_dir = tmp_path_factory.mktemp("site")
    proc = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--site-dir", str(site_dir), "--clean"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
    )
    return {
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "site_dir": site_dir,
    }


@pytest.fixture(scope="session")
def site_url(built_site):
    """Serve the built site over local HTTP for Playwright to navigate to.

    A plain file:// URL mostly works for MkDocs output but some relative-asset assumptions
    behave differently than a real deployment; a local HTTP server matches production closely
    enough to trust the results without the overhead of a full `mkdocs serve`.
    """
    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler, directory=str(built_site["site_dir"])
    )
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        thread.join()


# --- shared axe-core plumbing for the browser-based a11y tiers ---
#
# test_accessibility_browser.py, test_accessibility_runnable.py, and
# test_accessibility_keyboard.py all inject the same vendored axe build and
# silence the same rule set, so it lives here rather than being copied.

# Vendored rather than fetched from a CDN at test time, so a run doesn't depend on
# network access to a third party. Pinned to axe-core 4.10.2 — to update, download a
# newer axe.min.js from https://github.com/dequelabs/axe-core/releases over this file.
VENDOR_AXE_JS = Path(__file__).parent / "vendor" / "axe.min.js"

# Rules that fire on Material for MkDocs' own theme templates, not this repo's code —
# confirmed by manual audit to be present even on an otherwise-clean page. Silenced
# rather than chased, since fixing them means patching Material's own partials. If a
# Material upgrade fixes these upstream, this set should shrink accordingly.
KNOWN_UPSTREAM_RULES = {
    "aria-dialog-name",  # Material's search dialog (.md-search) has no accessible name
    "landmark-unique",  # Material's code-block toolbar landmark collides on multi-code pages
}

# Issues that ARE this repo's own doing but are a deliberate design choice, not a bug.
# Kept separate from KNOWN_UPSTREAM_RULES because the fix, if ever wanted, lives here.
KNOWN_ACCEPTED_RULES = {
    # index.md's hidden <h1> (site branding) is followed by #### category headings with
    # no ##/### between them — the #### level is used for its CSS sizing, not to claim
    # h2/h3's place in the outline. Accepted tradeoff, not something to fix here.
    "heading-order",
}

DISABLED_RULES = KNOWN_UPSTREAM_RULES | KNOWN_ACCEPTED_RULES


def run_axe(page, extra_disabled=(), context=None):
    """Inject the vendored axe-core and return its violations for the page's current DOM.

    `extra_disabled` adds to DISABLED_RULES for one call — e.g. a test that deliberately
    puts the page in a state where an unrelated rule would otherwise noise up the result.
    `context` is an optional CSS selector to scope the scan to (axe's include context), for
    a test that's only about one component rather than the whole page.
    """
    page.add_script_tag(path=str(VENDOR_AXE_JS))
    disabled = sorted(set(DISABLED_RULES).union(extra_disabled))
    result = page.evaluate(
        """([disabledRules, ctx]) => axe.run(ctx || document, {
            rules: Object.fromEntries(disabledRules.map((id) => [id, { enabled: false }]))
        })""",
        [disabled, context],
    )
    return result["violations"]


def format_violations(violations):
    """Render axe violations as a short, greppable block for an assertion message."""
    lines = []
    for v in violations:
        targets = [n["target"] for n in v["nodes"][:5]]
        lines.append(
            f"[{v['impact']}] {v['id']}: {v['help']} ({len(v['nodes'])} node(s)) — {targets}"
        )
    return "\n".join(lines)
