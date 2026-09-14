"""The "Essentials / Advanced" Simplify toggle
(docs/javascripts/essentials_toggle.js, docs/stylesheets/extra.css).

Covers: the default (Advanced) state, that ?simplified=true both hides marked
content and carries the state onto a content page's own heading + TOC entry, and the
link-recovery behavior — a page can still show a *link* to a hidden section (e.g.
collections.md's cheat-sheet table links to #tuples even though the "Tuples" heading
below it is hidden in Essentials mode); clicking it should flip back to Advanced and
reveal the target rather than silently doing nothing.

Browser tier — same setup as test_accessibility_browser.py (`playwright install chromium`).
"""


def test_advanced_content_visible_by_default(page, site_url):
    page.goto(site_url)
    is_simplified = page.evaluate("() => document.body.classList.contains('simplify-active')")
    assert not is_simplified, "Simplify should not be active by default"

    # A row-level marker: the "sets" keyword-link row under Collections.
    hidden = page.evaluate(
        """() => {
            const row = document.querySelector('p[data-advanced="true"]');
            return row ? getComputedStyle(row).display === 'none' : null;
        }"""
    )
    assert hidden is False, "a data-advanced row should be visible when not simplified"


def test_simplified_query_param_hides_marked_row(page, site_url):
    page.goto(f"{site_url}/?simplified=true")
    is_simplified = page.evaluate("() => document.body.classList.contains('simplify-active')")
    assert is_simplified, "?simplified=true should activate Simplify mode"

    hidden = page.evaluate(
        """() => {
            const row = document.querySelector('p[data-advanced="true"]');
            return row ? getComputedStyle(row).display === 'none' : null;
        }"""
    )
    assert hidden is True, "a data-advanced row should be hidden once simplified"


def test_simplified_state_carries_to_content_page_heading_and_toc(page, site_url):
    """functions.md's own '## Decorators { data-advanced="true" }' heading (and its
    integrated-TOC entry) should hide too — carried over from the homepage's marker via
    localStorage, with no need to visit the homepage first in this same test."""
    page.goto(f"{site_url}/functions/?simplified=true")

    result = page.evaluate(
        """() => {
            const heading = document.getElementById('decorators');
            const tocLink = document.querySelector('a.md-nav__link[href$="#decorators"]');
            const tocItem = tocLink ? tocLink.closest('.md-nav__item') : null;
            return {
                headingHidden: heading ? heading.hidden : null,
                tocItemHidden: tocItem ? tocItem.hidden : null,
            };
        }"""
    )
    assert result["headingHidden"] is True, "Decorators heading should be hidden"
    assert result["tocItemHidden"] is True, "Decorators' TOC entry should be hidden too"


def test_admonition_inside_a_hidden_section_is_actually_hidden(page, site_url):
    """Regression: Material's `.md-typeset details { display: flow-root }` beats the
    plain `[hidden] { display: none }` UA rule on specificity, so setting `.hidden = true`
    on an admonition inside a hidden section didn't actually hide it — it stayed on
    screen as a bordered box even though its heading was gone. Fixed with a blanket
    `[hidden] { display: none !important }` in extra.css."""
    page.goto(f"{site_url}/collections/?simplified=true")

    hidden_and_shown = page.evaluate(
        """() => [...document.querySelectorAll('.md-typeset details')]
            .filter((d) => d.hidden)
            .map((d) => getComputedStyle(d).display !== 'none')"""
    )
    assert hidden_and_shown, "expected at least one admonition inside a hidden section"
    assert not any(hidden_and_shown), (
        "an admonition has .hidden = true but still computes a visible display"
    )


def test_link_to_hidden_section_recovers_to_advanced(page, site_url):
    """collections.md's own cheat-sheet table (near the top) links to #tuples even
    while the "Tuples" heading itself is hidden by data-advanced — clicking that visible
    link should flip the toggle back to Advanced and reveal the section, rather than
    landing on a hidden target and doing nothing."""
    page.goto(f"{site_url}/collections/?simplified=true")

    tuples_link = page.locator('table a[href$="#tuples"]')
    assert tuples_link.count() > 0, "expected the cheat-sheet table's #tuples link to exist"

    before = page.evaluate("() => document.getElementById('tuples').hidden")
    assert before is True, "Tuples section should start hidden while simplified"

    tuples_link.first.click()

    after = page.evaluate(
        """() => ({
            tuplesHidden: document.getElementById('tuples').hidden,
            simplifyActive: document.body.classList.contains('simplify-active'),
            toggleActive: document.getElementById('pt-simplify-toggle')?.dataset.active,
            stored: localStorage.getItem('pt-simplify-active'),
        })"""
    )
    assert after["tuplesHidden"] is False, "clicking the link should reveal the Tuples section"
    assert after["simplifyActive"] is False, "clicking the link should turn Simplify off"
    assert after["toggleActive"] == "advanced", "the toggle's own state should flip to Advanced"
    assert after["stored"] == "false", "the flip should persist to localStorage"


def test_link_recovery_ignores_toc_links_to_visible_sections(page, site_url):
    """Sanity check the recovery handler isn't overly broad: clicking an ordinary link to
    a section that's already visible shouldn't touch Simplify state at all."""
    page.goto(f"{site_url}/collections/?simplified=true")

    lists_link = page.locator('a.md-nav__link[href$="#lists"]')
    assert lists_link.count() > 0

    lists_link.first.click()

    still_simplified = page.evaluate(
        "() => document.body.classList.contains('simplify-active')"
    )
    assert still_simplified, "a link to an already-visible section should not flip the toggle"
