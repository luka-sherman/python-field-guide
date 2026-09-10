"""Accessibility of the custom Pyodide runnable code block feature.

The runner is hand-wired in docs/javascripts/pyodide_runner.js — Material and MkDocs know
nothing about it — so nothing else in the suite covers whether the JS-injected controls are
usable with a keyboard or announced to a screen reader.

These tests render a page that has runnable blocks and check the injected DOM directly. They
do NOT execute Python: that needs the Pyodide runtime (a CDN fetch and ~10MB of WASM). What
they check is the always-present scaffolding — accessible names, roles, keyboard focus order,
the output live region — plus axe-core over the output panel forced into its visible state.
"""

from conftest import format_violations, run_axe

# A core content page that carries several ```python runnable blocks.
RUNNABLE_PAGE = "/foundations/"


def _open(page, site_url):
    page.goto(f"{site_url}{RUNNABLE_PAGE}")
    # `.pyodide-runner` is injected synchronously by initPage(); wait for it attached
    # (not visible — the blocks sit inside collapsed `??? run` admonitions).
    page.wait_for_selector(".pyodide-runner", state="attached")
    # A reader opens the block before using it; expand every <details> so the injected
    # controls are actually rendered/visible for the keyboard + focus checks.
    page.evaluate("() => document.querySelectorAll('details').forEach((d) => (d.open = true))")
    page.wait_for_selector(".pyodide-runner__run-btn", state="visible")
    return page


def test_page_actually_has_runnable_blocks(page, site_url):
    _open(page, site_url)
    assert page.locator(".pyodide-runner").count() > 0, (
        f"{RUNNABLE_PAGE} has no runnable blocks — pick a different page for these tests"
    )


def test_run_buttons_have_an_accessible_name(page, site_url):
    _open(page, site_url)
    buttons = page.locator(".pyodide-runner__run-btn")
    for i in range(buttons.count()):
        btn = buttons.nth(i)
        assert btn.get_attribute("type") == "button"
        assert (btn.inner_text() or "").strip() == "Run"
        assert btn.locator("svg").get_attribute("aria-hidden") == "true", (
            "the play icon must be aria-hidden so it doesn't double up the label"
        )


def test_editors_are_labelled_textboxes(page, site_url):
    _open(page, site_url)
    editors = page.locator(".pyodide-editor")
    assert editors.count() > 0
    for i in range(editors.count()):
        ed = editors.nth(i)
        assert ed.get_attribute("role") == "textbox"
        assert ed.get_attribute("aria-multiline") == "true"
        assert (ed.get_attribute("aria-label") or "").strip(), "editor has no aria-label"


def test_editors_are_keyboard_focusable(page, site_url):
    _open(page, site_url)
    page.locator(".pyodide-editor").first.focus()
    assert page.evaluate(
        "() => document.activeElement.classList.contains('pyodide-editor')"
    ), "the editable code block did not accept keyboard focus"


def test_run_button_is_keyboard_focusable_and_activates(page, site_url):
    # NOTE: we don't assert Tab *from the editor* lands on the Run button — CodeJar binds
    # Tab to indentation once it loads, so focus doesn't leave the editor that way. That's
    # standard code-editor behavior but a known keyboard-trap caveat worth remembering.
    _open(page, site_url)
    btn = page.locator(".pyodide-runner__run-btn").first
    btn.focus()
    assert page.evaluate(
        "() => document.activeElement.classList.contains('pyodide-runner__run-btn')"
    ), "the Run button did not accept keyboard focus"
    btn.press("Enter")
    # The click handler flips disabled + relabels before its first await, so a keyboard
    # activation that reached the handler shows up immediately.
    page.wait_for_function(
        """() => {
            const b = document.querySelector('.pyodide-runner__run-btn');
            return b.disabled || b.textContent.trim() !== 'Run';
        }""",
        timeout=3000,
    )


def test_output_panel_is_a_live_region(page, site_url):
    _open(page, site_url)
    outputs = page.locator(".pyodide-runner__output")
    assert outputs.count() > 0
    for i in range(outputs.count()):
        out = outputs.nth(i)
        assert out.get_attribute("role") == "status"
        assert out.get_attribute("aria-live") == "polite"


def test_axe_passes_with_output_panels_visible(page, site_url):
    """Reveal every output panel (normal + error text) without running Python, so axe
    checks the panel's contrast and markup in the state a reader sees after clicking Run."""
    _open(page, site_url)
    page.evaluate(
        """() => {
            document.querySelectorAll('.pyodide-runner__output').forEach((o, i) => {
                o.hidden = false;
                if (i % 2) {
                    o.classList.add('pyodide-runner__output--error');
                    o.textContent = 'Traceback (most recent call last):\\n  NameError: name \\'x\\' is not defined';
                } else {
                    o.textContent = 'hello, field guide';
                }
            });
        }"""
    )
    # Scope the scan to the runner subtrees — this test is about the output panel's own
    # markup/contrast, not a re-audit of the whole page.
    violations = run_axe(page, context=".pyodide-runner")
    assert not violations, (
        "axe-core violations with runnable output panels visible:\n"
        + format_violations(violations)
    )
