"""Shared fixtures for the test suite.

test_structure.py checks the *mechanically verifiable* rules in ../STRUCTURE.md — things like
"numbered walkthroughs start at 0" or "every python-ref line ends in a comment". Rules that
require editorial judgment (e.g. "is this admonition core enough to be always-open") are not
encoded here; see the comments in test_structure.py for what's deliberately out of scope.

test_accessibility.py and test_accessibility_browser.py check for accessibility regressions —
the former statically (no browser), the latter by actually rendering pages with Playwright and
running axe-core against them. Both build on the `built_site` fixture below.
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
