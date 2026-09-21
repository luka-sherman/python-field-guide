(function () {
  // "Essentials / Advanced" toggle: hides data-advanced content. On a
  // homepage row, data-advanced="true" hides that row; the same attribute
  // on a content page's own heading (e.g. functions.md's `## Decorators`)
  // hides that section plus its TOC entry — marked independently in each
  // place, no shared map. data-advanced="card" hides a whole homepage
  // card (see extra.css); no content-page equivalent, since it marks a
  // linked page rather than a section. Shows on every page; state
  // persists via localStorage.
  const STORAGE_KEY = "pt-simplify-active";

  // pt-lib--N sizes each library box for its full card count; hiding cards
  // in Essentials mode leaves boxes too wide. Recompute the visible count
  // into --pt-lib-span so extra.css can override pt-lib--N while active.
  function updateLibrarySpans() {
    document.querySelectorAll(".pt-category--wide").forEach(function (box) {
      const cards = box.querySelectorAll(".grid.cards > ul > li");
      let visible = 0;
      cards.forEach(function (li) {
        if (getComputedStyle(li).display !== "none") visible++;
      });
      if (visible > 0) box.style.setProperty("--pt-lib-span", Math.min(visible, 4));
    });
  }

  // Hides/restores a heading and its whole section — every sibling up to
  // the next heading of the same or higher level.
  function setSectionHidden(heading, hidden) {
    heading.hidden = hidden;
    const level = Number(heading.tagName[1]);
    let el = heading.nextElementSibling;
    while (el && !(/^H[1-6]$/.test(el.tagName) && Number(el.tagName[1]) <= level)) {
      el.hidden = hidden;
      el = el.nextElementSibling;
    }

    // Many pages wrap a whole ## section in <div class="pfg-section"> for
    // its own card-style border/background (raw HTML in the markdown, not
    // generated). Hiding the heading and its siblings above leaves that
    // wrapper behind as an empty card, so hide it too when the heading is
    // its first child.
    const wrapper = heading.parentElement;
    if (wrapper && wrapper.classList.contains("pfg-section") && wrapper.firstElementChild === heading) {
      wrapper.hidden = hidden;
    }
  }

  // toc.integrate puts headings in the same nav as site links — hide the
  // matching <li> too, so there's no dead link to hidden content.
  function setTocEntryHidden(id, hidden) {
    // href gets rewritten to a full URL after hydration; match by suffix.
    document.querySelectorAll('a.md-nav__link[href$="#' + id + '"]').forEach(function (link) {
      const item = link.closest(".md-nav__item");
      if (item) item.hidden = hidden;
    });
  }

  function applyAdvancedHeadings(active) {
    document.querySelectorAll('.md-typeset [data-advanced="true"]').forEach(function (el) {
      if (!/^H[1-6]$/.test(el.tagName)) return;
      setSectionHidden(el, active);
      if (el.id) setTocEntryHidden(el.id, active);
    });
  }

  function applyState(container, active) {
    document.body.classList.toggle("simplify-active", active);
    updateLibrarySpans();
    applyAdvancedHeadings(active);
    container.dataset.active = active ? "simplified" : "advanced";
    container.querySelectorAll(".pt-simplify-option").forEach(function (option) {
      option.setAttribute("aria-pressed", String(option.dataset.mode === container.dataset.active));
    });
  }

  // Two always-visible options with a sliding highlight, not one button
  // whose text changes.
  function getOrCreateToggle() {
    let container = document.getElementById("pt-simplify-toggle");
    if (container) return container;

    const paletteForm = document.querySelector('[data-md-component="palette"]');
    if (!paletteForm) return null;

    container = document.createElement("div");
    container.id = "pt-simplify-toggle";
    container.className = "pt-simplify-toggle";
    container.setAttribute("role", "group");
    container.setAttribute("aria-label", "Content level");

    const highlight = document.createElement("span");
    highlight.className = "pt-simplify-highlight";
    highlight.setAttribute("aria-hidden", "true");

    const essentials = document.createElement("button");
    essentials.type = "button";
    essentials.className = "pt-simplify-option";
    essentials.dataset.mode = "simplified";
    essentials.title = "Show only what you need to write your first programs";
    const essentialsLabel = document.createElement("span");
    essentialsLabel.className = "pt-simplify-label";
    essentialsLabel.textContent = "Essentials";
    essentials.append(essentialsLabel);

    const advanced = document.createElement("button");
    advanced.type = "button";
    advanced.className = "pt-simplify-option";
    advanced.dataset.mode = "advanced";
    advanced.title = "Show all site content";
    const advancedLabel = document.createElement("span");
    advancedLabel.className = "pt-simplify-label";
    advancedLabel.textContent = "Advanced";
    advanced.append(advancedLabel);

    container.append(highlight, advanced, essentials);
    paletteForm.insertAdjacentElement("beforebegin", container);

    container.addEventListener("click", function (event) {
      const option = event.target.closest(".pt-simplify-option");
      if (!option) return;
      const next = option.dataset.mode === "simplified";
      localStorage.setItem(STORAGE_KEY, String(next));
      applyState(container, next);
    });

    return container;
  }

  // Light/dark, same two-option format as above — replaces Material's
  // native single-knob switch, whose knob was the only clickable spot.
  // Native radios stay in the DOM (hidden); their own JS still applies
  // and persists the scheme, we just flip `checked` and dispatch change.
  function getOrCreateThemeToggle() {
    let container = document.getElementById("pt-theme-toggle");
    if (container) return container;

    const paletteForm = document.querySelector('[data-md-component="palette"]');
    if (!paletteForm) return null;

    const lightRadio = paletteForm.querySelector('input[data-md-color-scheme="default"]');
    const darkRadio = paletteForm.querySelector('input[data-md-color-scheme="slate"]');
    if (!lightRadio || !darkRadio) return null;

    paletteForm.hidden = true;

    container = document.createElement("div");
    container.id = "pt-theme-toggle";
    container.className = "pt-simplify-toggle pt-theme-toggle";
    container.setAttribute("role", "group");
    container.setAttribute("aria-label", "Color theme");

    const highlight = document.createElement("span");
    highlight.className = "pt-simplify-highlight";
    highlight.setAttribute("aria-hidden", "true");

    const light = document.createElement("button");
    light.type = "button";
    light.className = "pt-simplify-option pt-theme-option";
    light.dataset.scheme = "default";
    light.title = "Switch to light mode";
    light.setAttribute("aria-label", "Switch to light mode");

    const dark = document.createElement("button");
    dark.type = "button";
    dark.className = "pt-simplify-option pt-theme-option";
    dark.dataset.scheme = "slate";
    dark.title = "Switch to dark mode";
    dark.setAttribute("aria-label", "Switch to dark mode");

    container.append(highlight, dark, light);
    paletteForm.insertAdjacentElement("beforebegin", container);

    container.addEventListener("click", function (event) {
      const option = event.target.closest(".pt-theme-option");
      if (!option) return;
      const radio = option.dataset.scheme === "slate" ? darkRadio : lightRadio;
      if (!radio.checked) {
        radio.checked = true;
        radio.dispatchEvent(new Event("change", { bubbles: true }));
      }
      applyThemeState(container);
    });

    // Sync to whatever scheme Material's own JS actually lands on, not
    // just what we clicked.
    lightRadio.addEventListener("change", function () {
      applyThemeState(container);
    });
    darkRadio.addEventListener("change", function () {
      applyThemeState(container);
    });

    return container;
  }

  function applyThemeState(container) {
    const scheme = document.body.getAttribute("data-md-color-scheme");
    container.dataset.active = scheme === "slate" ? "dark" : "light";
    container.querySelectorAll(".pt-theme-option").forEach(function (option) {
      option.setAttribute("aria-pressed", String(option.dataset.scheme === scheme));
    });
  }

  // A visible link can point at a hidden section (e.g. collections.md's
  // cheat-sheet table links to #tuples while "Tuples" itself is hidden) —
  // reveal the target instead of landing on nothing.
  //
  // Uses hashchange rather than a click listener: a real mouse click on an
  // anchor races with, and in Chromium beats, a capturing click handler —
  // it worked for a scripted .click() in manual testing but silently
  // failed for an actual pointer click. hashchange fires after the
  // navigation commits either way.
  function revealHashTargetIfHidden() {
    if (!location.hash || !document.body.classList.contains("simplify-active")) return;

    const target = document.getElementById(location.hash.slice(1));
    if (!target || !target.hidden) return;

    const container = document.getElementById("pt-simplify-toggle");
    if (!container) return;
    localStorage.setItem(STORAGE_KEY, "false");
    applyState(container, false);
  }

  function setUpAdvancedLinkRecovery() {
    if (window.__ptHashRecoveryBound) return;
    window.__ptHashRecoveryBound = true;
    window.addEventListener("hashchange", revealHashTargetIfHidden);
  }

  function setUpSimplifyToggle() {
    const container = getOrCreateToggle();
    if (!container) return;

    setUpAdvancedLinkRecovery();

    const themeToggle = getOrCreateThemeToggle();
    if (themeToggle) applyThemeState(themeToggle);

    // ?simplified=true/false on a link forces and saves that state, e.g.
    // sharing a pre-simplified link.
    const override = new URLSearchParams(window.location.search).get("simplified");
    if (override !== null) localStorage.setItem(STORAGE_KEY, override !== "false" ? "true" : "false");

    applyState(container, localStorage.getItem(STORAGE_KEY) === "true");

    // Also covers loading a URL whose hash already points at a hidden
    // section, not just navigating there via a same-page click.
    revealHashTargetIfHidden();
  }

  // navigation.instant swaps page content via JS without a full reload, so
  // DOMContentLoaded only fires once. document$ is Material's own
  // observable that emits on every page change, instant or not.
  if (window.document$) {
    window.document$.subscribe(setUpSimplifyToggle);
  } else {
    document.addEventListener("DOMContentLoaded", setUpSimplifyToggle);
  }
})();
