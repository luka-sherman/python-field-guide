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

  function initA11yPatches() {
    makeScrollRegionsFocusable();
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
