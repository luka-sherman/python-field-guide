(function () {
  // Explicit "Cheatsheet" text shortcut to the homepage (already this
  // site's compact quick-reference dashboard — see README), replacing the
  // logo image in the header's top-left slot rather than sitting next to
  // it — the logo already linked home with no other purpose, so the pill
  // takes over that exact role instead of duplicating it. Styled in
  // extra.css to match the Essentials/Advanced toggle's own active/
  // inactive look. The logo itself is hidden via CSS (.md-header__button
  // .md-logo { display: none }), not removed here, so this script only
  // owns inserting the pill.
  function render() {
    const existing = document.querySelector(".pt-cheatsheet-link");
    if (existing) existing.remove();

    const title = document.querySelector(".md-header__title");
    const logo = document.querySelector(".md-header__button.md-logo");
    if (!title || !logo) return;

    const link = document.createElement("a");
    link.className = "pt-cheatsheet-link";
    link.href = logo.getAttribute("href");
    link.textContent = "Cheatsheet";

    // Same homepage check as homepage_header_title.js — kept independent
    // rather than shared, since one more `===` comparison isn't worth a
    // cross-file dependency between two otherwise-unrelated scripts.
    const isHomepage = window.location.pathname.replace(/index\.html$/, "") === "/";
    if (isHomepage) {
      link.classList.add("pt-cheatsheet-link--active");
      link.setAttribute("aria-current", "page");
    }

    title.insertAdjacentElement("beforebegin", link);
  }

  if (window.document$) {
    window.document$.subscribe(render);
  } else {
    document.addEventListener("DOMContentLoaded", render);
  }
})();
