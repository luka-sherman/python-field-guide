"""The Essentials/Advanced content-mode toggle, provided by the
mkdocs-audience-toggle plugin (configured in mkdocs.yml) rather than by
site-local JS — see CLAUDE.md's "Planned extraction" section.

Covers: the default (Advanced) state, that ?mode=essentials both hides marked
content and carries the state onto a content page's own heading + TOC entry, and
the link-recovery behavior — a page can still show a *link* to a hidden section
(e.g. collections.md's cheat-sheet table links to #tuples even though the
"Tuples" heading below it is hidden in Essentials mode); clicking it should flip
back to Advanced and reveal the target rather than silently doing nothing.

Browser tier — same setup as test_accessibility_browser.py (`playwright install chromium`).
"""


def test_advanced_content_visible_by_default(page, site_url):
    page.goto(site_url)
    mode = page.evaluate("() => document.documentElement.getAttribute('data-audience-mode')")
    assert mode == "advanced", "Advanced should be the default mode"

    # A row-level marker: the "sets" keyword-link row under Collections.
    hidden = page.evaluate(
        """() => {
            const row = document.querySelector('p[data-audience-hide~="essentials"]');
            return row ? getComputedStyle(row).display === 'none' : null;
        }"""
    )
    assert hidden is False, "a data-audience-hide=\"essentials\" row should be visible in Advanced"


def test_mode_query_param_hides_marked_row(page, site_url):
    page.goto(f"{site_url}/?mode=essentials")
    mode = page.evaluate("() => document.documentElement.getAttribute('data-audience-mode')")
    assert mode == "essentials", "?mode=essentials should activate Essentials mode"

    hidden = page.evaluate(
        """() => {
            const row = document.querySelector('p[data-audience-hide~="essentials"]');
            return row ? getComputedStyle(row).display === 'none' : null;
        }"""
    )
    assert hidden is True, "a data-audience-hide=\"essentials\" row should be hidden once in Essentials mode"


def test_essentials_state_carries_to_content_page_heading_and_toc(page, site_url):
    """functions.md's own '## Decorators { data-audience-hide="essentials" }' heading (and its
    integrated-TOC entry) should hide too — carried over from the homepage's marker via
    localStorage, with no need to visit the homepage first in this same test."""
    page.goto(f"{site_url}/organization/functions/?mode=essentials")

    result = page.evaluate(
        """() => {
            const heading = document.getElementById('decorators');
            const tocLink = document.querySelector('a.md-nav__link[href$="#decorators"]');
            const tocItem = tocLink ? tocLink.closest('.md-nav__item') : null;
            return {
                headingDisplay: heading ? getComputedStyle(heading).display : null,
                tocItemDisplay: tocItem ? getComputedStyle(tocItem).display : null,
            };
        }"""
    )
    assert result["headingDisplay"] == "none", "Decorators heading should be hidden"
    assert result["tocItemDisplay"] == "none", "Decorators' TOC entry should be hidden too"


def test_admonition_inside_a_hidden_section_is_actually_hidden(page, site_url):
    """Regression (see extra.css's [hidden] override and its history): Material's
    `.md-typeset details { display: flow-root }` used to beat a plain `[hidden] {
    display: none }` UA rule on specificity, so JS-driven hiding of an admonition
    inside a hidden section didn't actually hide it. The plugin sidesteps that class
    of bug entirely by hiding elements with an inline `style.display = "none"`
    instead of the `hidden` attribute — inline style always wins on specificity."""
    page.goto(f"{site_url}/types/collections/?mode=essentials")

    hidden_and_shown = page.evaluate(
        """() => [...document.querySelectorAll('.md-typeset details')]
            .filter((d) => d.style.display === 'none')
            .map((d) => getComputedStyle(d).display !== 'none')"""
    )
    assert hidden_and_shown, "expected at least one admonition inside a hidden section"
    assert not any(hidden_and_shown), (
        "an admonition has style.display = 'none' but still computes a visible display"
    )


def test_pfg_section_wrapper_is_hidden_with_its_heading(page, site_url):
    """Regression: many pages wrap a whole ## section in raw
    `<div class="pfg-section">` for its own card-style border/background (not
    generated — written directly in the markdown). Configured via the plugin's own
    `wrapper_class: [pfg-section]` option (mkdocs.yml) — without it, only the
    heading and its flow siblings *inside* that wrapper would hide, leaving the
    wrapper itself on screen as an empty bordered card."""
    page.goto(f"{site_url}/types/collections/?mode=essentials")

    result = page.evaluate(
        """() => {
            const heading = document.getElementById('tuples');
            const wrapper = heading.closest('.pfg-section');
            return {
                wrapperFound: !!wrapper,
                wrapperDisplay: wrapper ? getComputedStyle(wrapper).display : null,
            };
        }"""
    )
    assert result["wrapperFound"], "expected #tuples to sit inside a .pfg-section wrapper"
    assert result["wrapperDisplay"] == "none", "the wrapper is still rendering as an empty card"


def test_whole_homepage_card_hides(page, site_url):
    """A page with `cheatsheet_attrs: {data-audience-hide: essentials}` in its front matter
    gets the marker on its cheatsheet card's <li>, which the audience toggle hides."""
    page.goto(f"{site_url}/?mode=essentials")

    card_display = page.evaluate(
        """() => {
            const card = document.querySelector('.md-cheatsheet__card[data-audience-hide~="essentials"]');
            return card ? getComputedStyle(card).display : null;
        }"""
    )
    assert card_display == "none", "a card marked via cheatsheet_attrs should fully hide"


def test_link_to_hidden_section_recovers_to_advanced(page, site_url):
    """collections.md's own cheat-sheet table (near the top) links to #tuples even
    while the "Tuples" heading itself is hidden by data-audience-hide="essentials" — clicking
    that visible link should flip the toggle back to Advanced and reveal the
    section, rather than landing on a hidden target and doing nothing."""
    page.goto(f"{site_url}/types/collections/?mode=essentials")

    tuples_link = page.locator('table a[href$="#tuples"]')
    assert tuples_link.count() > 0, "expected the cheat-sheet table's #tuples link to exist"

    before = page.evaluate("() => getComputedStyle(document.getElementById('tuples')).display")
    assert before == "none", "Tuples section should start hidden while in Essentials mode"

    tuples_link.first.click()

    # hashchange (which drives the recovery) always fires as a separate queued
    # task, never synchronously with the click — so the reveal can still be
    # pending right after .click() returns. Wait for it instead of assuming it
    # already happened (this was flaky in CI for exactly that reason).
    page.wait_for_function(
        "() => getComputedStyle(document.getElementById('tuples')).display !== 'none'"
    )

    after = page.evaluate(
        """() => ({
            tuplesDisplay: getComputedStyle(document.getElementById('tuples')).display,
            mode: document.documentElement.getAttribute('data-audience-mode'),
            toggleActive: document.getElementById('audience-toggle')?.dataset.active,
            stored: localStorage.getItem('audience-mode'),
        })"""
    )
    assert after["tuplesDisplay"] != "none", "clicking the link should reveal the Tuples section"
    assert after["mode"] == "advanced", "clicking the link should flip the mode to Advanced"
    assert after["toggleActive"] == "advanced", "the toggle's own state should flip to Advanced"
    assert after["stored"] == "advanced", "the flip should persist to localStorage"


def test_link_recovery_ignores_toc_links_to_visible_sections(page, site_url):
    """Sanity check the recovery handler isn't overly broad: clicking an ordinary link to
    a section that's already visible shouldn't touch the content mode at all."""
    page.goto(f"{site_url}/types/collections/?mode=essentials")

    # Material renders a page's TOC twice: once for real in the secondary
    # (right-hand) sidebar, and once inert (visibility:collapse) inside the
    # primary nav's copy of the current page's entry — scope to the visible
    # one so .first doesn't land on the inert copy and time out.
    lists_link = page.locator('.md-sidebar--secondary a.md-nav__link[href$="#lists"]')
    assert lists_link.count() > 0

    lists_link.first.click()

    still_essentials = page.evaluate(
        "() => document.documentElement.getAttribute('data-audience-mode')"
    )
    assert still_essentials == "essentials", "a link to an already-visible section should not flip the mode"
