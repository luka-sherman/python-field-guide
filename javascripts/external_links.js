(function () {
  // Any link whose hostname differs from the site's own opens in a new tab —
  // covers python.org, GitHub, docs for third-party libraries, etc.
  function markExternalLinks() {
    const currentHost = window.location.hostname;

    document.querySelectorAll(".md-content a[href]").forEach((link) => {
      let url;
      try {
        url = new URL(link.getAttribute("href"), window.location.href);
      } catch (err) {
        return;
      }

      if (url.hostname && url.hostname !== currentHost) {
        link.target = "_blank";
        link.rel = "noopener noreferrer";
      }
    });
  }

  // Material's navigation.instant swaps page content via JS without a full
  // reload, so DOMContentLoaded only ever fires once. document$ is Material's
  // own observable that emits on every page change, instant or not.
  if (window.document$) {
    window.document$.subscribe(markExternalLinks);
  } else {
    document.addEventListener("DOMContentLoaded", markExternalLinks);
  }
})();
