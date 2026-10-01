(function () {
  // Recomputes --library-span (the add-on-library boxes' grid span) once the
  // mkdocs-audience-toggle plugin hides some of their cards in Essentials
  // mode — the one bit of library-grid behavior no plugin owns, since it's
  // specific to this site's own card layout.

  // The cheatsheet plugin's --cards-N class sizes each library box for its full card count; hiding cards
  // in Essentials mode leaves boxes too wide. Recompute the visible count
  // into --library-span so extra.css can override --cards-N while active.
  function updateLibrarySpans() {
    document.querySelectorAll(".library-grid > .md-cheatsheet__group").forEach(function (box) {
      const cards = box.querySelectorAll(".grid.cards > ul > li");
      let visible = 0;
      cards.forEach(function (li) {
        if (getComputedStyle(li).display !== "none") visible++;
      });
      if (visible > 0) box.style.setProperty("--library-span", Math.min(visible, 4));
    });
  }

  // The plugin hides content (and sets html[data-audience-mode]) synchronously
  // from its own script; a MutationObserver callback always fires as a
  // separate microtask after that synchronous work finishes, so this stays
  // correctly ordered regardless of which script's DOMContentLoaded/
  // document$ subscriber happens to run first.
  function setUp() {
    if (window.__librarySpanObserverBound) return;
    window.__librarySpanObserverBound = true;
    new MutationObserver(updateLibrarySpans).observe(document.documentElement, {
      attributeFilter: ["data-audience-mode"],
    });
    updateLibrarySpans();
  }

  // navigation.instant swaps page content via JS without a full reload, so
  // DOMContentLoaded only fires once. document$ is Material's own
  // observable that emits on every page change, instant or not.
  if (window.document$) {
    window.document$.subscribe(setUp);
  } else {
    document.addEventListener("DOMContentLoaded", setUp);
  }
})();
