(function () {
  // Material wraps wide tables in .md-typeset__scrollwrap (and, on narrow
  // viewports, the FAQ tab-label row in .tabbed-labels) to scroll them
  // horizontally, but neither element ships with a tabindex — a keyboard-only
  // user has no way to focus and scroll them. Add one ourselves.
  function makeScrollRegionsFocusable() {
    document.querySelectorAll(".md-typeset__scrollwrap, .tabbed-labels").forEach((el) => {
      if (!el.hasAttribute("tabindex")) {
        el.setAttribute("tabindex", "0");
      }
    });
  }

  // pymdownx.tasklist (style.md's checklist) renders each `- [ ]` as a real
  // <input type="checkbox" disabled> wrapped in its own <label>, but that
  // label contains only the checkbox itself — the item's actual text sits
  // outside it as a plain sibling — so the checkbox has no accessible name
  // (axe: "Form elements must have labels"). It's also disabled and never
  // toggles, so it's not a real control a screen reader user can act on;
  // hiding it from the accessibility tree lets that text be read on its own
  // instead of prefixed with a confusing, non-interactive "checkbox" role.
  function hideDecorativeTaskListCheckboxes() {
    document.querySelectorAll(".task-list-control > input[type=checkbox]").forEach((el) => {
      el.setAttribute("aria-hidden", "true");
    });
  }

  function initA11yPatches() {
    makeScrollRegionsFocusable();
    hideDecorativeTaskListCheckboxes();
  }

  // Material's navigation.instant swaps page content via JS without a full
  // reload, so DOMContentLoaded only ever fires once. document$ is Material's
  // own observable that emits on every page change, instant or not.
  if (window.document$) {
    window.document$.subscribe(initA11yPatches);
  } else {
    document.addEventListener("DOMContentLoaded", initA11yPatches);
  }
})();
