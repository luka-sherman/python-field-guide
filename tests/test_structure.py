"""Tests for the mechanically-checkable rules in ../STRUCTURE.md.

Scope: this suite only encodes rules that can be verified from the markdown source without
editorial judgment. Several STRUCTURE.md rules are deliberately NOT tested here because no
text-only heuristic can apply them reliably — see the comment above each test (or this list)
for what's out of scope and why:

- Whether an admonition's content is "core enough" to justify `!!!` over `???` (Admonitions).
- Whether a `###`/`####` heading is a genuine "skim target" vs. decorative structure (Headings).
- Whether a numbered list is a step-by-step "walkthrough" (starts at 0) or an enumeration of
  facts/rules (starts at 1) — STRUCTURE.md "Text style conventions".
- Whether a piece of content belongs in prose, an admonition, or a footnote (all three).
"""

import re

import pytest

from conftest import (
    ALL_DOC_FILES,
    DOCS_DIR,
    ATTR_LIST_RE,
    iter_fenced_blocks,
    iter_headings,
    iter_lines,
    rel,
    strip_non_prose,
)

DOC_IDS = [rel(p) for p in ALL_DOC_FILES]


# ============================================================================
# Admonition types are picked from the documented set (STRUCTURE.md "Admonitions")
# ============================================================================

# The table in STRUCTURE.md documents run/tip/warning/note/info/failure/example. success/danger
# aren't in the table but are named explicitly in the surrounding prose as the sanctioned !!!
# pair on errors.md. Anything else showing up here means either new content invented a type
# without updating STRUCTURE.md, or STRUCTURE.md's table needs to grow — either way it's worth
# a look.
DOCUMENTED_ADMONITION_TYPES = {
    "run", "tip", "warning", "note", "info", "failure", "example", "success", "danger", "ai",
    "efficiency",
}

ADMONITION_RE = re.compile(r"^\s*(\?\?\?|!!!)\s+(\w+)\s")


@pytest.mark.parametrize("path", ALL_DOC_FILES, ids=DOC_IDS)
def test_admonition_types_are_documented(path):
    failures = []
    for lineno, raw, in_fence, _ in iter_lines(path):
        if in_fence:
            continue
        m = ADMONITION_RE.match(raw)
        if m and m.group(2) not in DOCUMENTED_ADMONITION_TYPES:
            failures.append(f"{rel(path)}:{lineno}: undocumented admonition type {m.group(2)!r} — {raw.strip()!r}")
    assert not failures, (
        "Admonition type not in STRUCTURE.md's documented set "
        f"{sorted(DOCUMENTED_ADMONITION_TYPES)}:\n" + "\n".join(failures)
    )


# ============================================================================
# md_in_html block wrappers never nest inside a list item or admonition
# ============================================================================

# A `markdown="block"`/`markdown="1"` HTML wrapper (e.g. `<div class="pfg-diagram-frame"
# markdown="block">`) indented under a `- ` list item or a `??? `/`!!! ` admonition has broken
# rendering before: the div got swallowed into a *preceding* code fence's raw text instead of
# being parsed, corrupting the page (confirmed by hand across several pages; fixed by reverting
# those wrappers back to plain, unwrapped HTML). Scoped specifically to the `markdown=`
# attribute, not "any HTML in a list/admonition" — plain raw HTML with no `markdown=` attribute
# (e.g. `.pt-compare`'s `<div class="pt-compare">`, or a bare `<p class="pfg-diagram-caption">`
# caption) already nests inside admonitions/lists safely throughout this site and isn't what
# broke, so it's not flagged here.
MD_IN_HTML_BLOCK_RE = re.compile(r'^(?P<indent>\s+)<\w+[^>]*\bmarkdown="(?:block|1)"')


@pytest.mark.parametrize("path", ALL_DOC_FILES, ids=DOC_IDS)
def test_md_in_html_blocks_are_not_indented(path):
    failures = []
    for lineno, raw, in_fence, _ in iter_lines(path):
        if in_fence:
            continue
        if MD_IN_HTML_BLOCK_RE.match(raw):
            failures.append(f"{rel(path)}:{lineno}: {raw.strip()!r}")
    assert not failures, (
        "A markdown=\"block\"/\"1\" HTML wrapper is indented, meaning it's nested inside a list "
        "item or admonition — this exact pattern has broken rendering before (see the comment "
        "above this test). Move the wrapper to the top level, or if it must live in a list/"
        "admonition, drop the `markdown=` attribute and use plain HTML instead:\n"
        + "\n".join(failures)
    )


# ============================================================================
# Headings use sentence case (STRUCTURE.md "Text style conventions" / "Headings")
# ============================================================================

# Scoped to ##/###/#### only. # (page titles) mix in icon shortcodes and, in a couple of
# cases, function as branding/proper-name text (the site's own name, a page's own product
# name) rather than ordinary prose headings — that's a different judgment call than the one
# this heuristic makes, so page titles are left for a human to review.
#
# Heuristic: a heading word is "pure title case" if it starts uppercase and everything after
# is lowercase (`Style`, `Guide`, `Libraries`). Mixed-case identifiers (NumPy, OpenCV,
# DataFrame, ImageOps) and ALL-CAPS acronyms (JSON, PEP, OOP) don't match this pattern and are
# exempt automatically. Pure title-case words that are still legitimate (proper nouns not
# expressible as mixed-case/acronym) need an explicit allowlist entry below.
PROPER_NOUNS = {"Python", "Image", "None", "Pillow", "Tkinter"}

# "Step X:" headings capitalize the word right after the colon (STRUCTURE.md's own exception).
STEP_PREFIX_RE = re.compile(r"^(?:Step \d+|\d+):\s*(\S+)")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]*")
PURE_TITLE_CASE_RE = re.compile(r"^[A-Z][a-z'-]*$")


def _heading_case_violations(heading_text: str) -> list[str]:
    text = strip_non_prose(heading_text)
    text = ATTR_LIST_RE.sub("", text).strip()
    words = WORD_RE.findall(text)
    if not words:
        return []
    allowed_extra = set()
    m = STEP_PREFIX_RE.match(text)
    if m:
        allowed_extra.add(m.group(1).strip(".,:;"))
    violations = []
    for i, word in enumerate(words):
        if i == 0:
            continue
        if word in PROPER_NOUNS or word in allowed_extra:
            continue
        if word.isupper():
            continue
        if PURE_TITLE_CASE_RE.match(word):
            violations.append(word)
    return violations


@pytest.mark.parametrize("path", ALL_DOC_FILES, ids=DOC_IDS)
def test_headings_use_sentence_case(path):
    failures = []
    for lineno, level, text in iter_headings(path, levels=(2, 3, 4)):
        bad_words = _heading_case_violations(text)
        if bad_words:
            failures.append(f"{rel(path)}:{lineno}: {text!r} — Title Case word(s) {bad_words}")
    assert not failures, "Headings should use sentence case, not Title Case:\n" + "\n".join(failures)


# ============================================================================
# "Python" is always capitalized in prose (STRUCTURE.md "Text style conventions")
# ============================================================================

# The site's snake-species theme means "python" is *also* a real, correctly-lowercase word
# here (ball python, burmese python, ...) — those aren't violations of this rule, they're a
# different noun entirely. Excluded via the same species-adjective vocabulary CLAUDE.md itself
# uses (ball python, burmese, boa, ...) plus every adjective actually used with it on the site.
SPECIES_PYTHON_RE = re.compile(r"\b(ball|burmese|blood|reticulated|boa)\s+python\b", re.I)
FILENAME_PYTHON_RE = re.compile(r"\bpython\.\w+")
LOWERCASE_PYTHON_RE = re.compile(r"\bpython\b")


FENCE_MARKER_RE = re.compile(r"^\s*```")


@pytest.mark.parametrize("path", ALL_DOC_FILES, ids=DOC_IDS)
def test_python_is_capitalized_in_prose(path):
    failures = []
    for lineno, raw, in_fence, _ in iter_lines(path):
        if in_fence or FENCE_MARKER_RE.match(raw):
            continue  # fence language tags (```python-ref) are syntax, not prose
        text = strip_non_prose(raw)
        text = SPECIES_PYTHON_RE.sub("", text)
        text = FILENAME_PYTHON_RE.sub("", text)
        for m in LOWERCASE_PYTHON_RE.finditer(text):
            failures.append(f"{rel(path)}:{lineno}: lowercase 'python' — {raw.strip()!r}")
    assert not failures, "'Python' should be capitalized in prose:\n" + "\n".join(failures)


# ============================================================================
# python-ref cheat-sheet lines end with a `# ...` output comment (STRUCTURE.md
# "python-ref blocks")
# ============================================================================

# This rule ("one line per concept... end each line with a # comment showing the output") is
# documented for one specific use: the short always-visible preview opening a content section.
# In practice python-ref is *also* used site-wide for longer worked examples that can't run
# under Pyodide (Tkinter/Pillow/OpenCV GUI and file/camera side effects, error tracebacks,
# docstring displays) — those never had per-line output comments and STRUCTURE.md doesn't
# claim they should. No text-only heuristic reliably tells the two apart (checked: neither
# control-flow-keyword presence nor block length is a clean signal — both produce dozens of
# false positives against the library pages). So this check is deliberately scoped to the two
# pages that are the clearest, most literal examples of the documented convention. Extending it
# to more pages would need either a markup convention to mark "this block follows the cheat
# sheet rule" or a per-page editorial pass — worth doing, but a separate task from this suite.
CHECKED_PAGES_FOR_PYTHON_REF_COMMENTS = {"types/basics.md", "types/collections.md"}

_CONTROL_FLOW_RE = re.compile(
    r"^(if |elif |else|while |for |def |class |try|except|finally|with |return|import |from |@|match |case )"
)
_BARE_ASSIGN_RE = re.compile(r"^[A-Za-z_]\w*\s*=(?!=)")


@pytest.mark.parametrize("path", ALL_DOC_FILES, ids=DOC_IDS)
def test_python_ref_teaser_lines_have_output_comments(path):
    if rel(path) not in CHECKED_PAGES_FOR_PYTHON_REF_COMMENTS:
        pytest.skip("python-ref comment convention only checked on the canonical teaser pages")

    failures = []
    for start, _end, _indent, content in iter_fenced_blocks(path, lang="python-ref"):
        lines = list(enumerate(content, start=start + 1))
        block_text = [c for _, c in lines]
        if any(_CONTROL_FLOW_RE.match(c.strip()) for c in block_text):
            # Syntax being demonstrated for its shape (if/for/match/...), not a flat list of
            # one-output-per-line expressions — out of scope for this rule.
            continue
        for lineno, content_line in lines:
            stripped = content_line.strip()
            if stripped == "" or content_line.startswith((" ", "\t")):
                continue
            if _BARE_ASSIGN_RE.match(stripped):
                continue  # establishing/reusing a variable, not showing output
            if "#" in content_line:
                continue
            failures.append(f"{rel(path)}:{lineno}: missing output comment — {content_line!r}")
    assert not failures, "python-ref lines should end with a `# ...` output comment:\n" + "\n".join(failures)


# ============================================================================
# mkdocs build has no WARNINGs (STRUCTURE.md "Link maintenance")
# ============================================================================


def test_mkdocs_build_has_no_warnings(built_site):
    warning_lines = [
        line for line in built_site["stderr"].splitlines() if line.strip().startswith("WARNING")
    ]
    assert built_site["returncode"] == 0, built_site["stderr"]
    assert not warning_lines, (
        "mkdocs build printed warnings — STRUCTURE.md treats these as a checklist, not just "
        "informational output:\n" + "\n".join(warning_lines)
    )
