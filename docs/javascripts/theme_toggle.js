(function () {
  // Light/dark toggle: two always-visible options with a sliding highlight,
  // next to the palette toggle. Replaces Material's native single-knob
  // switch, whose knob was the only clickable spot. Native radios stay in
  // the DOM (hidden); their own JS still applies and persists the scheme,
  // we just flip `checked` and dispatch change.
  //
  // The Essentials/Advanced content toggle used to live in this file too;
  // it's now the mkdocs-audience-toggle plugin (see mkdocs.yml and
  // CLAUDE.md's "Planned extraction" section) and no longer touches this
  // code. This file keeps only the one bit that plugin can't own:
  // recomputing --library-span (the add-on-library boxes' grid span) once
  // the plugin hides some of their cards — see updateLibrarySpans below.

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
  function setUpLibrarySpanRecompute() {
    if (window.__librarySpanObserverBound) return;
    window.__librarySpanObserverBound = true;
    new MutationObserver(updateLibrarySpans).observe(document.documentElement, {
      attributeFilter: ["data-audience-mode"],
    });
    updateLibrarySpans();
  }

  // Disappearing confirmation toast — shows what a click on the light/dark
  // toggle just changed, since the button itself only shows the current
  // state, not what changed.
  //
  // `iconAttrs` is the dataset to put on the icon span, e.g. {scheme:
  // "slate"} — matched in extra.css by .pt-mode-icon[data-scheme] to the
  // same sun/moon icons the toggle itself uses. `body` is optional; pass ""
  // for a one-line toast (this toggle's own message is self-explanatory).
  let toastTimer = null;
  function showToast(label, iconAttrs, body) {
    let toast = document.getElementById("pt-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "pt-toast";
      toast.className = "pt-toast";
      // status + polite: announced to screen readers without interrupting
      // whatever they're already reading, same as a visual toast doesn't
      // steal focus.
      toast.setAttribute("role", "status");
      toast.setAttribute("aria-live", "polite");
      document.body.appendChild(toast);
    }

    toast.innerHTML = "";

    const title = document.createElement("div");
    title.className = "pt-toast__title";
    const icon = document.createElement("span");
    icon.className = "pt-mode-icon";
    Object.keys(iconAttrs).forEach(function (key) {
      icon.dataset[key] = iconAttrs[key];
    });
    icon.setAttribute("aria-hidden", "true");
    title.append(icon, " " + label);
    toast.append(title);

    if (body) {
      const bodyEl = document.createElement("div");
      bodyEl.className = "pt-toast__body";
      bodyEl.textContent = body;
      toast.append(bodyEl);
    }

    // The header's own height isn't fixed across breakpoints (taller with
    // the tab bar on tablet/desktop) or over time (Material can hide/reveal
    // it on scroll), so position below it fresh on every call rather than
    // hardcoding an offset in CSS.
    const header = document.querySelector(".md-header");
    const headerBottom = header ? header.getBoundingClientRect().bottom : 0;
    toast.style.top = Math.max(headerBottom, 0) + 12 + "px";

    // Retrigger the transition even if a toast is already showing (rapid
    // clicks): drop the class, force layout, then re-add it, instead of
    // just extending the existing timer.
    toast.classList.remove("pt-toast--visible");
    void toast.offsetWidth;
    toast.classList.add("pt-toast--visible");

    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      toast.classList.remove("pt-toast--visible");
    }, 1400);
  }

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
      const scheme = option.dataset.scheme;
      const radio = scheme === "slate" ? darkRadio : lightRadio;
      if (radio.checked) return;
      radio.checked = true;
      radio.dispatchEvent(new Event("change", { bubbles: true }));
      applyThemeState(container);
      showToast(scheme === "slate" ? "Lights off" : "Lights on", { scheme: scheme }, "");
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

  function setUp() {
    const themeToggle = getOrCreateThemeToggle();
    if (themeToggle) applyThemeState(themeToggle);
    setUpLibrarySpanRecompute();
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
