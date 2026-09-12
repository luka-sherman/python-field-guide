"""Typo check over the site's prose sources, via codespell.

codespell flags known misspellings (e.g. "teh", "recieve", "langauge") rather than
unrecognized words, so it doesn't choke on the site's snake species names, Python
jargon, or Pyodide/mkdocs terminology the way a dictionary-based spellchecker would.

If a future false positive does show up (a real word codespell's dictionary treats as
a typo), add it to IGNORE_WORDS below rather than editing the file to dodge it.
"""

import subprocess
import sys

from conftest import REPO_ROOT

# Words codespell's dictionary flags that are intentional here — add to this set
# (lowercase) rather than rewording a page to avoid a false positive.
IGNORE_WORDS: set[str] = set()

# Prose sources to check: page content plus the repo's own editorial docs.
CHECK_PATHS = ["docs", "includes", "STRUCTURE.md", "README.md"]


def test_no_typos():
    args = [sys.executable, "-m", "codespell_lib", *CHECK_PATHS]
    if IGNORE_WORDS:
        args += ["-L", ",".join(sorted(IGNORE_WORDS))]
    proc = subprocess.run(args, cwd=REPO_ROOT, capture_output=True, text=True)
    # codespell exits 0 for no findings, >0 (non-usage-error) for findings.
    assert proc.returncode == 0, (
        "codespell found possible typos (fix the text, or add a genuine false "
        "positive to IGNORE_WORDS in tests/test_typos.py):\n" + proc.stdout + proc.stderr
    )
