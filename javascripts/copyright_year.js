(function () {
  function setYear() {
    const el = document.getElementById("copyright-year");
    if (el) el.textContent = new Date().getFullYear();
  }

  if (window.document$) {
    window.document$.subscribe(setYear);
  } else {
    document.addEventListener("DOMContentLoaded", setYear);
  }
})();
