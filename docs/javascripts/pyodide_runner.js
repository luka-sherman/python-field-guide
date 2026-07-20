(function () {
  const PYODIDE_CDN = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js";
  const CODEJAR_CDN = "https://cdn.jsdelivr.net/npm/codejar@4.3.0/dist/codejar.js";

  let pyodideReadyPromise = null;

  function loadPyodideRuntime() {
    if (pyodideReadyPromise) return pyodideReadyPromise;
    pyodideReadyPromise = new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = PYODIDE_CDN;
      script.onload = async () => {
        try {
          resolve(await loadPyodide());
        } catch (err) {
          reject(err);
        }
      };
      script.onerror = () => reject(new Error("Failed to load the Pyodide runtime."));
      document.head.appendChild(script);
    });
    return pyodideReadyPromise;
  }

  // highlight.js 11 marks an element data-highlighted="yes" and refuses to
  // re-highlight it. Clear that flag before every pass so edits stay colored.
  function highlightWithExistingTheme(editor) {
    delete editor.dataset.highlighted;
    window.hljs.highlightElement(editor);
  }

  function makeEditable(codeBlock) {
    codeBlock.classList.add("pyodide-editor");
    import(CODEJAR_CDN).then(({ CodeJar }) => {
      CodeJar(codeBlock, highlightWithExistingTheme, {
        tab: "    ",
        indentOn: /[({\[:]$/,
      });
    });
  }

  function buildRunner(codeBlock) {
    const pre = codeBlock.parentElement;

    const wrapper = document.createElement("div");
    wrapper.className = "pyodide-runner";

    const toolbar = document.createElement("div");
    toolbar.className = "pyodide-runner__toolbar";

    const runButton = document.createElement("button");
    runButton.type = "button";
    runButton.className = "pyodide-runner__run-btn";
    runButton.textContent = "Run";
    toolbar.appendChild(runButton);

    const output = document.createElement("pre");
    output.className = "pyodide-runner__output";
    output.hidden = true;

    pre.insertAdjacentElement("beforebegin", wrapper);
    wrapper.appendChild(pre);
    wrapper.appendChild(toolbar);
    wrapper.appendChild(output);

    makeEditable(codeBlock);

    runButton.addEventListener("click", async () => {
      const originalLabel = runButton.textContent;
      runButton.disabled = true;
      runButton.textContent = "Loading…";
      output.hidden = false;
      output.textContent = "";
      output.classList.remove("pyodide-runner__output--error");

      try {
        const pyodide = await loadPyodideRuntime();
        runButton.textContent = "Running…";

        let buffer = "";
        pyodide.setStdout({ batched: (s) => { buffer += s + "\n"; } });
        pyodide.setStderr({ batched: (s) => { buffer += s + "\n"; } });

        await pyodide.runPythonAsync(codeBlock.textContent);
        output.textContent = buffer || "(no output)";
      } catch (err) {
        output.classList.add("pyodide-runner__output--error");
        output.textContent = String(err);
      } finally {
        runButton.disabled = false;
        runButton.textContent = originalLabel;
      }
    });
  }

  // Reference-only blocks (` ```python-ref `): syntax-highlighted like real
  // Python, but no Run button — for cheat-sheet-style annotated snippets
  // where the `# result` comment is the point, not execution.
  function buildReference(codeBlock) {
    const pre = codeBlock.parentElement;
    const wrapper = document.createElement("div");
    wrapper.className = "pyodide-reference";
    pre.insertAdjacentElement("beforebegin", wrapper);
    wrapper.appendChild(pre);

    if (window.hljs) {
      const result = window.hljs.highlight(codeBlock.textContent, { language: "python" });
      codeBlock.innerHTML = result.value;
    }
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("pre > code.language-python").forEach(buildRunner);
    document.querySelectorAll("pre > code.language-python-ref").forEach(buildReference);
  });
})();
