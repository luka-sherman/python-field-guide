"""Browser-based accessibility checks: render real pages with Playwright, run axe-core.

Complements test_accessibility.py (static, no browser). This tier catches what static
analysis can't — ARIA labeling, color contrast, focus visibility, scrollable-region keyboard
access — the same kinds of issues a manual axe-core audit found real bugs with. It's also the
heavier tier: needs a one-time `playwright install chromium` (see README.md's Testing
section), and every run launches a real headless browser against a real `mkdocs build`.

Sibling browser tiers, sharing conftest's `site_url` + axe helpers:
  - test_accessibility_runnable.py — the Pyodide runnable code block feature
  - test_accessibility_keyboard.py — keyboard navigation
"""

import pytest

from conftest import format_violations, run_axe

# One representative page per distinct kind of content on the site, not all ~28 pages, to
# keep this fast — but enough to cover the site's actual variety: the homepage (card grid,
# FAQ tabs), a content page with a wide comparison table, a page built from numbered
# walkthroughs and tabbed OS instructions, one dense with admonitions, and a library page
# full of images.
PAGES = ["/", "/types/basics/", "/start/workspace/", "/types/collections/", "/libraries/pillow/"]

# The pages whose palette does the most work — card grid, wide truth tables — re-checked
# with the dark scheme active. (Material lists `slate` first, so dark is already the
# default the PAGES run above scans; this forces the *other* direction explicitly too.)
LIGHT_MODE_PAGES = ["/", "/types/collections/"]

MOBILE_VIEWPORT = {"width": 375, "height": 812}
# Between Material's own tab-bar breakpoint (~1220px) and extra.css's override that pulls
# it back down to 45em (~720px): a width where the custom media query keeps the tab bar
# visible when stock Material would have collapsed it to the hamburger.
TABLET_VIEWPORT = {"width": 800, "height": 1024}


def _select_scheme(page, scheme):
    """Flip Material's palette to `scheme` ('default' = light, 'slate' = dark).

    docs/javascripts/essentials_toggle.js replaces the visible light/dark control with its
    own buttons and hides Material's native radio entirely, so Playwright can't click it
    as a normal user control. Clicking it directly still fires the same input change that
    Material's own JS (and our buttons) rely on to apply and persist the scheme.
    """
    page.evaluate(
        "(s) => document.querySelector(`input[data-md-color-scheme=\"${s}\"]`).click()",
        scheme,
    )
    page.wait_for_timeout(200)  # let the palette CSS variables settle before scanning


@pytest.mark.parametrize("path", PAGES)
def test_page_has_no_axe_violations(page, site_url, path):
    page.goto(f"{site_url}{path}")
    violations = run_axe(page)
    assert not violations, f"axe-core violations on {path}:\n" + format_violations(violations)


@pytest.mark.parametrize("path", LIGHT_MODE_PAGES)
def test_page_has_no_axe_violations_in_light_mode(page, site_url, path):
    page.goto(f"{site_url}{path}")
    _select_scheme(page, "default")
    violations = run_axe(page)
    assert not violations, (
        f"axe-core violations on {path} (light mode):\n" + format_violations(violations)
    )


def test_homepage_has_no_axe_violations_in_dark_mode(page, site_url):
    page.goto(site_url)
    _select_scheme(page, "slate")
    violations = run_axe(page)
    assert not violations, (
        "axe-core violations on homepage (dark mode):\n" + format_violations(violations)
    )


@pytest.mark.parametrize("path", ["/", "/types/collections/"])
def test_page_has_no_axe_violations_on_mobile(page, site_url, path):
    page.set_viewport_size(MOBILE_VIEWPORT)
    page.goto(f"{site_url}{path}")
    violations = run_axe(page)
    assert not violations, (
        f"axe-core violations on {path} at {MOBILE_VIEWPORT['width']}px:\n"
        + format_violations(violations)
    )


def test_mobile_nav_drawer_has_no_axe_violations(page, site_url):
    """The hamburger drawer is a different DOM subtree than the desktop tab nav."""
    page.set_viewport_size(MOBILE_VIEWPORT)
    page.goto(f"{site_url}/types/collections/")
    page.evaluate(
        """() => {
            const drawer = document.getElementById('__drawer');
            drawer.checked = true;
            drawer.dispatchEvent(new Event('change'));
        }"""
    )
    page.wait_for_timeout(150)
    violations = run_axe(page)
    assert not violations, (
        "axe-core violations with the mobile nav drawer open:\n" + format_violations(violations)
    )


def test_tablet_width_has_no_axe_violations(page, site_url):
    page.set_viewport_size(TABLET_VIEWPORT)
    page.goto(f"{site_url}/types/basics/")
    violations = run_axe(page)
    assert not violations, (
        f"axe-core violations at {TABLET_VIEWPORT['width']}px (custom tab-bar breakpoint):\n"
        + format_violations(violations)
    )
