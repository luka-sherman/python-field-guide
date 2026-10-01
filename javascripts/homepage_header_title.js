(function () {
  // Material's header shows the current top-level nav tab's label in place
  // of the site title once you scroll past the tab bar. The homepage's nav
  // entry is labeled "All" (to fit the tab bar as the first tab), which
  // reads oddly as a page title — so on the homepage specifically, force
  // that label back to the site name instead.
  function fixHomepageHeaderTitle() {
    const isHomepage = window.location.pathname.replace(/index\.html$/, "") === "/";
    if (!isHomepage) return;

    const topic = document.querySelector('[data-md-component="header-topic"] .md-ellipsis');
    if (topic) topic.textContent = "Python Field Guide";
  }

  // Material's navigation.instant swaps page content via JS without a full
  // reload, so DOMContentLoaded only ever fires once. document$ is Material's
  // own observable that emits on every page change, instant or not.
  if (window.document$) {
    window.document$.subscribe(fixHomepageHeaderTitle);
  } else {
    document.addEventListener("DOMContentLoaded", fixHomepageHeaderTitle);
  }
})();
