"""Keyboard-navigation accessibility — what a single axe scan doesn't drive.

axe flags *markup* problems on a static snapshot. These tests use the keyboard the way a
mouse-free user would: the skip link works, this repo's own interactive controls show a
visible focus indicator, nothing hijacks tab order with a positive tabindex, and the palette
toggle is reachable.

Browser tier — same setup as test_accessibility_browser.py (`playwright install chromium`).
"""

import pytest

CHECK_PAGES = ["/", "/types/", "/workspace/"]


@pytest.mark.parametrize("path", CHECK_PAGES)
def test_first_tab_reaches_the_skip_link(page, site_url, path):
    page.goto(f"{site_url}{path}")
    page.keyboard.press("Tab")
    info = page.evaluate(
        """() => {
            const el = document.activeElement;
            return { cls: el.className || '', href: el.getAttribute('href') || '' };
        }"""
    )
    assert "md-skip" in info["cls"], f"first Tab focused {info!r}, not the skip link"
    # Material's instant-nav rewrites internal hrefs to absolute, so match on the
    # fragment rather than a leading '#'.
    assert "#" in info["href"] and info["href"].split("#")[-1], (
        f"skip link should target an in-page anchor, got {info['href']!r}"
    )


def test_skip_link_moves_past_the_navigation(page, site_url):
    page.goto(f"{site_url}/types/")
    page.keyboard.press("Tab")  # focus skip link
    page.keyboard.press("Enter")  # activate it
    moved = page.evaluate(
        """() => {
            const main = document.querySelector('[role=main], .md-content');
            return (main && main.contains(document.activeElement)) || location.hash.length > 1;
        }"""
    )
    assert moved, "activating the skip link did not move focus/scroll into the main content"


@pytest.mark.parametrize("path", CHECK_PAGES)
def test_no_positive_tabindex(page, site_url, path):
    page.goto(f"{site_url}{path}")
    positive = page.evaluate(
        """() => [...document.querySelectorAll('[tabindex]')]
            .map(el => parseInt(el.getAttribute('tabindex'), 10))
            .filter(v => v > 0)"""
    )
    assert not positive, (
        f"{len(positive)} element(s) use a positive tabindex on {path} "
        f"({positive}) — this overrides natural DOM tab order"
    )


def test_palette_toggle_is_keyboard_reachable(page, site_url):
    """The dark/light toggle must be operable without a mouse. Material renders the radios
    visually-hidden behind a styled label; this checks they're still real inputs (not
    `hidden` / `display:none`) and that Tab actually lands on one."""
    page.goto(site_url)
    inputs = page.evaluate(
        """() => [...document.querySelectorAll('input[name=__palette]')].map((i) => ({
            hidden: i.hasAttribute('hidden'),
            display: getComputedStyle(i).display,
        }))"""
    )
    assert len(inputs) >= 2, "expected at least two palette radios (light + dark)"
    assert all(not i["hidden"] and i["display"] != "none" for i in inputs), (
        "a palette radio is hidden from keyboard/AT users entirely"
    )
    for _ in range(25):
        page.keyboard.press("Tab")
        if page.evaluate("() => document.activeElement?.name === '__palette'"):
            return
    raise AssertionError("Tab never reached the palette toggle within 25 stops")


# Interactive things this repo styles itself (as opposed to Material's header/search/palette
# chrome, whose focus treatment is the theme's concern and is guarded statically by
# test_accessibility.py). Each must paint an outline or box-shadow when focused from the
# keyboard — the homepage card links lost theirs exactly this way once before.
# (`.md-button` is only used on 404.md and is already covered statically by
# test_accessibility.py's `.md-button:focus-visible` check, so it's not repeated here.)
REPO_STYLED_CONTROLS = [
    ("/foundations/", ".md-content a[href]"),
    ("/foundations/", ".pyodide-runner__run-btn"),
    ("/foundations/", "details.run > summary"),
    ("/", ".grid.cards a[href]"),
]


@pytest.mark.parametrize("path,selector", REPO_STYLED_CONTROLS)
def test_repo_styled_control_has_a_visible_focus_indicator(page, site_url, path, selector):
    page.goto(f"{site_url}{path}")
    page.evaluate("() => document.querySelectorAll('details').forEach((d) => (d.open = true))")
    target = page.locator(selector).first
    if target.count() == 0:
        pytest.skip(f"no {selector} on {path}")
    # Emulate a keyboard focus so :focus-visible applies, then compare the focused element's
    # own paint against a plain baseline.
    result = page.evaluate(
        """(sel) => {
            const el = document.querySelector(sel);
            el.focus({ focusVisible: true });
            const cs = getComputedStyle(el);
            const outline = cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0;
            const shadow = cs.boxShadow && cs.boxShadow !== 'none';
            return { ok: outline || shadow, focusVisible: el.matches(':focus-visible') };
        }""",
        selector,
    )
    assert result["ok"], (
        f"{selector} on {path} shows no visible focus indicator "
        "(no outline, no box-shadow) when focused"
    )
