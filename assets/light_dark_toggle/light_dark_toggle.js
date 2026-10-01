(function () {
  // Always-visible two-button light/dark switch, replacing Material's native
  // single-knob palette switch (whose knob was the only clickable spot).
  // Native radios stay in the DOM, hidden; their own JS still applies and
  // persists the scheme via localStorage, we just flip `checked` and
  // dispatch change.

  function readConfig() {
    const script = document.getElementById("light-dark-config");
    if (!script) return null;
    return JSON.parse(script.textContent);
  }

  let toastTimer = null;
  function showToast(text) {
    let toast = document.getElementById("light-dark-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "light-dark-toast";
      toast.className = "light-dark-toast";
      // status + polite: announced to screen readers without interrupting
      // whatever they're already reading, same as a visual toast doesn't
      // steal focus.
      toast.setAttribute("role", "status");
      toast.setAttribute("aria-live", "polite");
      document.body.appendChild(toast);
    }

    toast.textContent = text;

    // The header's own height isn't fixed across breakpoints (taller with
    // a tab bar on tablet/desktop) or over time (Material can hide/reveal
    // it on scroll), so position below it fresh on every call rather than
    // hardcoding an offset in CSS.
    const header = document.querySelector(".md-header");
    const headerBottom = header ? header.getBoundingClientRect().bottom : 0;
    toast.style.top = Math.max(headerBottom, 0) + 12 + "px";

    // Retrigger the transition even if a toast is already showing (rapid
    // clicks): drop the class, force layout, then re-add it, instead of
    // just extending the existing timer.
    toast.classList.remove("light-dark-toast--visible");
    void toast.offsetWidth;
    toast.classList.add("light-dark-toast--visible");

    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      toast.classList.remove("light-dark-toast--visible");
    }, 1400);
  }

  function getOrCreateToggle(config) {
    let container = document.getElementById("light-dark-toggle");
    if (container) return container;

    const paletteForm = document.querySelector('[data-md-component="palette"]');
    if (!paletteForm) return null;

    const lightRadio = paletteForm.querySelector('input[data-md-color-scheme="default"]');
    const darkRadio = paletteForm.querySelector('input[data-md-color-scheme="slate"]');
    if (!lightRadio || !darkRadio) return null;

    paletteForm.hidden = true;

    container = document.createElement("div");
    container.id = "light-dark-toggle";
    container.className = "light-dark-toggle";
    container.setAttribute("role", "group");
    container.setAttribute("aria-label", config.ariaLabel);

    const highlight = document.createElement("span");
    highlight.className = "light-dark-highlight";
    highlight.setAttribute("aria-hidden", "true");

    const dark = document.createElement("button");
    dark.type = "button";
    dark.className = "light-dark-option";
    dark.dataset.scheme = "slate";
    dark.title = config.modes.dark.description;
    dark.setAttribute("aria-label", config.modes.dark.description);

    const light = document.createElement("button");
    light.type = "button";
    light.className = "light-dark-option";
    light.dataset.scheme = "default";
    light.title = config.modes.light.description;
    light.setAttribute("aria-label", config.modes.light.description);

    container.append(highlight, dark, light);
    paletteForm.insertAdjacentElement("beforebegin", container);

    let previousMode = null;
    container.addEventListener("click", function (event) {
      const option = event.target.closest(".light-dark-option");
      if (!option) return;
      const scheme = option.dataset.scheme;
      // Not radio.checked: Material applies the scheme to <body> on init
      // without syncing the matching radio's `checked` property, so that
      // stays false for whichever scheme loaded by default until a real
      // click sets it below.
      if (scheme === document.body.getAttribute("data-md-color-scheme")) return;
      const radio = scheme === "slate" ? darkRadio : lightRadio;
      radio.checked = true;
      radio.dispatchEvent(new Event("change", { bubbles: true }));
      applyState(container);
      const mode = scheme === "slate" ? "dark" : "light";
      if (config.showToast) showToast(config.modes[mode].announcement);
      document.dispatchEvent(
        new CustomEvent("light-dark:modechange", { detail: { mode: mode, previousMode: previousMode } })
      );
      previousMode = mode;
    });

    // Sync to whatever scheme Material's own JS actually lands on, not
    // just what we clicked.
    lightRadio.addEventListener("change", function () {
      applyState(container);
    });
    darkRadio.addEventListener("change", function () {
      applyState(container);
    });

    return container;
  }

  function applyState(container) {
    const scheme = document.body.getAttribute("data-md-color-scheme");
    container.dataset.active = scheme === "slate" ? "dark" : "light";
    container.querySelectorAll(".light-dark-option").forEach(function (option) {
      option.setAttribute("aria-pressed", String(option.dataset.scheme === scheme));
    });
  }

  function setUp() {
    const config = readConfig();
    if (!config) return;
    const toggle = getOrCreateToggle(config);
    if (toggle) applyState(toggle);
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
