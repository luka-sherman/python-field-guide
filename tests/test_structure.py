"""Tests for the mechanically-checkable rules in ../STRUCTURE.md.

Scope: this suite only encodes rules that can be verified from the markdown source without
editorial judgment. Several STRUCTURE.md rules are deliberately NOT tested here because no
text-only heuristic can apply them reliably — see the comment above each test (or this list)
for what's out of scope and why:

- Whether an admonition's content is "core enough" to justify `!!!` over `???` (Admonitions).
- Whether a `###`/`####` heading is a genuine "skim target" vs. decorative structure (Headings).
- Whether a piece of content belongs in prose, an admonition, or a footnote (all three).
Where a rule is *mostly* mechanical but has real exceptions (e.g. not every numbered list is a
"walkthrough"), the exceptions are an explicit, commented allowlist below rather than a fuzzier
heuristic — so a new addition either matches the existing pattern or fails until someone
consciously decides which side of the line it's on.
"""

import re

import pytest

from conftest import (
    ALL_DOC_FILES,
    DOCS_DIR,
    ATTR_LIST_RE,
    FENCE_RE,
    iter_fenced_blocks,
    iter_headings,
    iter_lines,
    rel,
    strip_non_prose,
)

DOC_IDS = [rel(p) for p in ALL_DOC_FILES]


# ============================================================================
# Numbered steps start at 0 (STRUCTURE.md "Text style conventions")
# ============================================================================

# "the first item in any ordered-list walkthrough is 0" — this only applies to lists that are
# actually a sequence of steps the reader performs. Plenty of numbered lists on the site are
# just enumerated facts/rules (order shown for readability, not "do this then this"), and those
# legitimately start at 1. Each entry below is (file, first-item lineno, why it's not a
# walkthrough) — verified by hand against the surrounding prose.
NON_WALKTHROUGH_LISTS = {
    ("foundations.md", 165): "variable naming rules — facts about names, not steps to perform",
    ("foundations.md", 322): "describes what input() does, not steps the reader performs",
    ("foundations.md", 422): "kinds of comments, an enumerated list not a sequence",
    ("conditionals.md", 28): "describes if/elif/else execution order, not reader-performed steps",
    ("style.md", 77): "file layout order, an enumerated structure not a walkthrough",
}

TOP_LEVEL_ORDERED_ITEM_RE = re.compile(r"^(\d+)\.\s+\S")


def _ordered_list_blocks(path):
    """Group top-level (unindented) ordered-list items into blocks.

    A block continues across blank lines and indented continuation/nested content; it ends at
    the next non-blank, non-indented, non-marker line (a paragraph or heading resuming the
    list has ended).
    """
    blocks = []
    current = None
    for lineno, raw, in_fence, _ in iter_lines(path):
        if not in_fence:
            m = TOP_LEVEL_ORDERED_ITEM_RE.match(raw)
            if m:
                if current is None:
                    current = {"first": int(m.group(1)), "lineno": lineno, "text": raw.strip()}
                    blocks.append(current)
                continue
        # Inside a fence, don't look for markers (a code example could contain "1. foo"). A
        # fence is list-item continuation content whether or not it happens to be indented to
        # match the item (some pages indent a nested fence under the item, others don't) — so
        # fence markers/content never break the block, only blank/indented lines do otherwise.
        if in_fence or FENCE_RE.match(raw) or raw.strip() == "" or raw.startswith((" ", "\t")):
            continue
        current = None
    return blocks


@pytest.mark.parametrize("path", ALL_DOC_FILES, ids=DOC_IDS)
def test_numbered_walkthroughs_start_at_zero(path):
    key_file = rel(path)
    failures = []
    for block in _ordered_list_blocks(path):
        if (key_file, block["lineno"]) in NON_WALKTHROUGH_LISTS:
            continue
        if block["first"] != 0:
            failures.append(f"{key_file}:{block['lineno']}: starts at {block['first']} — {block['text']!r}")
    assert not failures, "Numbered walkthroughs must start at 0:\n" + "\n".join(failures)


# ============================================================================
# Admonition types are picked from the documented set (STRUCTURE.md "Admonitions")
# ============================================================================

# The table in STRUCTURE.md documents run/tip/warning/note/info/failure/example. success/danger
# aren't in the table but are named explicitly in the surrounding prose as the sanctioned !!!
# pair on errors.md. Anything else showing up here means either new content invented a type
# without updating STRUCTURE.md, or STRUCTURE.md's table needs to grow — either way it's worth
# a look.
DOCUMENTED_ADMONITION_TYPES = {
    "run", "tip", "warning", "note", "info", "failure", "example", "success", "danger",
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


# Default to collapsed (???); !!! should be rare and deliberate (STRUCTURE.md: "Use !!! only
# when... This should still be rare"). Whether a *given* use is justified is a judgment call
# (is the content core, is the admonition format genuinely clearest) that this suite can't make
# — but unreviewed growth in !!! usage is worth a conscious decision each time. This allowlist
# is every !!! in the docs as of this test's introduction; a new one fails here until someone
# adds it deliberately (which is the point — it forces the "is this rare and justified" check
# STRUCTURE.md asks for, rather than letting !!! quietly become the default).
ALWAYS_OPEN_ALLOWLIST = {
    ("errors.md", 55),  # the documented success/danger pair
    ("errors.md", 60),
    ("workspace.md", 187),
    ("foundations.md", 453),
    ("conditionals.md", 103),
    ("loops.md", 202),
    ("loops.md", 437),
}


@pytest.mark.parametrize("path", ALL_DOC_FILES, ids=DOC_IDS)
def test_always_open_admonitions_are_reviewed(path):
    failures = []
    for lineno, raw, in_fence, _ in iter_lines(path):
        if in_fence:
            continue
        m = re.match(r"^\s*!!!\s+\w+\s", raw)
        if m and (rel(path), lineno) not in ALWAYS_OPEN_ALLOWLIST:
            failures.append(f"{rel(path)}:{lineno}: new !!! admonition not in ALWAYS_OPEN_ALLOWLIST — {raw.strip()!r}")
    assert not failures, (
        "New always-open (!!!) admonition(s). STRUCTURE.md wants these rare and deliberate — "
        "confirm this one is core content where the box format genuinely earns its keep, then "
        "add it to ALWAYS_OPEN_ALLOWLIST in test_structure.py:\n" + "\n".join(failures)
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
CHECKED_PAGES_FOR_PYTHON_REF_COMMENTS = {"types.md", "collections.md"}

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
# mkdocs build has no WARNINGs (STRUCTURE.md "Link maintenance" / "Homepage keyword deep-links")
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


# ============================================================================
# index.md's keyword deep-links cover every ##/### heading (STRUCTURE.md "Homepage
# keyword deep-links")
# ============================================================================

# A heading opts out of (or customizes) this check from the source markdown itself, via
# attr_list (already enabled — see mkdocs.yml — and already used elsewhere for exactly this
# kind of per-element metadata, e.g. `{ .pt-homepage-heading }`):
#
#   ## Heading text { data-card-link="skip" }
#       — this heading is narrative/descriptive, not a reusable keyword (STRUCTURE.md's own
#         examples: "What do you see when a program runs?"). No index.md entry required.
#
#   ## Heading text { data-card-link="your preferred link text" }
#       — index.md must link to this heading's anchor using exactly that text. Catches the
#         two ways this can drift: the link is missing, or it exists with different text than
#         what's declared here.
#
#   ## Heading text                              (no attribute)
#       — default: index.md must link to this heading's anchor, any text.
#
# attr_list attributes land directly on the rendered heading tag, so this reads straight off
# the built HTML alongside id/text — no separate markdown-source parsing needed.
PAGES_SKIPPED_FOR_COVERAGE = {"index.md", "404.md", "about.md", "privacy.md", "thanks.md", "libraries/index.md"}

LINK_RE = re.compile(r"\[([^\]]*)\]\(([\w./-]+\.md)(#[\w-]+)?\)")
BUILT_HEADING_RE = re.compile(r'<h([23])\s+([^>]*)>(.*?)</h\1>', re.S)
ATTR_VALUE_RE = re.compile(r'(\w[\w-]*)="([^"]*)"')
TAG_RE = re.compile(r"<[^>]+>")
LINK_TEXT_DECORATION_RE = re.compile(r"[`*]")


def _normalize_link_text(text: str) -> str:
    return LINK_TEXT_DECORATION_RE.sub("", text).strip()


def _index_links():
    """page.md -> {anchor: link text (markdown decoration stripped)}, for every #anchor link."""
    index_text = (DOCS_DIR / "index.md").read_text()
    linked: dict[str, dict[str, str]] = {}
    for text, page, anchor in LINK_RE.findall(index_text):
        if anchor:
            linked.setdefault(page, {})[anchor[1:]] = _normalize_link_text(text)
    return linked


def _html_path_for(built_site, md_rel: str):
    site_dir = built_site["site_dir"]
    if md_rel == "index.md":
        return site_dir / "index.html"
    return site_dir / md_rel[: -len(".md")] / "index.html"


@pytest.mark.parametrize("path", ALL_DOC_FILES, ids=DOC_IDS)
def test_homepage_keyword_links_cover_all_headings(built_site, path):
    md_rel = rel(path)
    if md_rel in PAGES_SKIPPED_FOR_COVERAGE:
        pytest.skip("not a content page covered by the homepage card grid")

    html_file = _html_path_for(built_site, md_rel)
    assert html_file.exists(), f"no build output for {md_rel} at {html_file}"

    linked = _index_links().get(md_rel, {})
    failures = []
    for level, attrs_raw, text in BUILT_HEADING_RE.findall(html_file.read_text()):
        attrs = dict(ATTR_VALUE_RE.findall(attrs_raw))
        anchor_id = attrs.get("id")
        if not anchor_id:
            continue
        declared = attrs.get("data-card-link")
        if declared == "skip":
            continue

        clean_text = TAG_RE.sub("", text).strip()
        actual_text = linked.get(anchor_id)
        if actual_text is None:
            suffix = f" — declared text: {declared!r}" if declared else ""
            failures.append(f"{md_rel}#{anchor_id} (h{level} {clean_text!r}) has no index.md keyword link{suffix}")
        elif declared and declared != actual_text:
            failures.append(
                f"{md_rel}#{anchor_id} (h{level} {clean_text!r}) linked as {actual_text!r}, "
                f"but the heading declares {declared!r}"
            )
    assert not failures, (
        "Every ##/### heading needs its own index.md keyword deep-link (STRUCTURE.md "
        "'Homepage keyword deep-links: Coverage'). Add the link, or mark the heading "
        '`{ data-card-link="skip" }` if it\'s intentionally not a reusable keyword:\n'
        + "\n".join(failures)
    )
