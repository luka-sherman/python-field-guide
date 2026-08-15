"""Browser-based accessibility checks: render real pages with Playwright, run axe-core.

Complements test_accessibility.py (static, no browser). This tier catches what static
analysis can't — ARIA labeling, color contrast, focus visibility, scrollable-region keyboard
access — the same kinds of issues a manual axe-core audit found real bugs with. It's also the
heavier tier: needs a one-time `playwright install chromium` (see README.md's Testing
section), and every run launches a real headless browser against a real `mkdocs build`.
"""

from pathlib import Path

import pytest

# Vendored rather than fetched from a CDN at test time, so a run doesn't depend on network
# access to a third party. Pinned to axe-core 4.10.2 — to update, download a newer
# axe.min.js from https://github.com/dequelabs/axe-core/releases over this file.
VENDOR_AXE_JS = Path(__file__).parent / "vendor" / "axe.min.js"

# Issues that live in Material for MkDocs' own theme templates, not this repo's code —
# confirmed by manual audit to be present even on an otherwise-clean page. Excluded here
# rather than chased, since fixing them means patching Material's own partials, not this
# repo's CSS/JS/content. If a Material upgrade ever fixes these upstream, this set (and the
# rules it silences) should shrink accordingly.
KNOWN_UPSTREAM_RULES = {
    "aria-dialog-name",  # Material's search dialog (.md-search) has no accessible name
    "landmark-unique",  # Material's code-block toolbar landmark collides on multi-code pages
}

# Issues that ARE this repo's own doing but are a deliberate design choice, not a bug — kept
# separate from KNOWN_UPSTREAM_RULES because the fix (if ever wanted) lives here, not upstream.
KNOWN_ACCEPTED_RULES = {
    # index.md's hidden <h1> (site branding) is followed by #### category headings with no
    # ##/### between them — the #### level is used for its CSS sizing, not to claim h2/h3's
    # place in the outline. Confirmed as an accepted tradeoff, not something to fix here.
    "heading-order",
}

DISABLED_RULES = KNOWN_UPSTREAM_RULES | KNOWN_ACCEPTED_RULES

# One representative page per distinct kind of content on the site, not all ~28 pages, to
# keep this fast — but enough to cover the site's actual variety: the homepage (card grid,
# FAQ tabs), a content page with a wide comparison table, a page built from numbered
# walkthroughs and tabbed OS instructions, one dense with admonitions, and a library page
# full of images.
PAGES = ["/", "/types/", "/workspace/", "/collections/", "/libraries/pillow/"]


def _run_axe(page):
    page.add_script_tag(path=str(VENDOR_AXE_JS))
    result = page.evaluate(
        """(disabledRules) => axe.run(document, {
            rules: Object.fromEntries(disabledRules.map((id) => [id, { enabled: false }]))
        })""",
        list(DISABLED_RULES),
    )
    return result["violations"]


def _format_violations(violations):
    lines = []
    for v in violations:
        targets = [n["target"] for n in v["nodes"][:5]]
        lines.append(
            f"[{v['impact']}] {v['id']}: {v['help']} ({len(v['nodes'])} node(s)) — {targets}"
        )
    return "\n".join(lines)


@pytest.mark.parametrize("path", PAGES)
def test_page_has_no_axe_violations(page, site_url, path):
    page.goto(f"{site_url}{path}")
    violations = _run_axe(page)
    assert not violations, f"axe-core violations on {path}:\n" + _format_violations(violations)


def test_homepage_has_no_axe_violations_in_dark_mode(page, site_url):
    page.goto(site_url)
    # Material's palette toggle is a radio input its own CSS keeps out of the
    # normal visibility flow (the visible control is a styled sibling label),
    # so Playwright's actionability checks never see it as clickable. A real
    # user's click reaches it via that label; dispatching the click directly
    # in the page gets the same "input change fires, Material's own JS reacts"
    # result without depending on which label happens to be visible when.
    page.evaluate('document.querySelector(\'input[data-md-color-scheme="slate"]\').click()')
    page.wait_for_timeout(200)  # let the palette CSS variables settle before scanning
    violations = _run_axe(page)
    assert not violations, (
        "axe-core violations on homepage (dark mode):\n" + _format_violations(violations)
    )
