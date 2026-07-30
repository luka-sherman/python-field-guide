# Running Python On Your Own Computer

Every example on this site runs here in your browser, powered by Pyodide — no setup needed. But once you start writing your own `.py` files, you'll use a **code editor** — a program that combines a text editor, a Run button, and a place to see your program's output, all in one window.

Pick one of the code editors below and click the download link for your operating system:

| Code Editor | Best for | Download Links |
|--------|----------|---------|
| **VS Code** | <ul><li>Lightweight and simple</li><li>Huge ecosystem of extensions</li><li>Works on all platforms</li><li>After installing, add the Python extension from the Extensions marketplace</li></ul> | [Windows](https://code.visualstudio.com/download) / [macOS](https://code.visualstudio.com/download) / [Linux](https://code.visualstudio.com/download) |
| **PyCharm Community** | <ul><li>Complete Python IDE</li><li>Everything built-in out of the box</li><li>Best if you don't mind a bigger download</li></ul> | [Windows](https://www.jetbrains.com/pycharm/download/) / [macOS](https://www.jetbrains.com/pycharm/download/) / [Linux](https://www.jetbrains.com/pycharm/download/) |
| **Thonny** | <ul><li>Designed specifically for beginners</li><li>Simplest setup and interface</li><li>Great for learning Python fundamentals</li></ul> | [Windows](https://thonny.org/) / [macOS](https://thonny.org/) / [Linux](https://thonny.org/) |
| **IDLE** | <ul><li>Comes bundled with Python</li><li>No extra download needed</li><li>Minimal but functional</li></ul> | Included / Included / `sudo apt install idle3` |

**Note:** Any editor works with any Python library. Your choice now doesn't lock you into anything — if you later decide to do data science, web development, or something else, you can always switch editors then. Pick whichever one sounds easiest to start with.

## Installing Python

Before you can run your own `.py` files, Python needs to actually be on your computer — check the sections above only cover *running* code, not getting Python itself.

| OS | Where to get it | Note |
|----|------------------|------|
| **Windows** | [python.org/downloads](https://python.org/downloads) | Check **"Add python.exe to PATH"** on the first install screen — skip it and the terminal won't recognize `python` |
| **macOS** | [python.org/downloads](https://python.org/downloads) | The system doesn't reliably include Python 3 anymore — don't rely on what's already there |
| **Linux** | Usually already installed | Run `python3 --version` to check; if missing, install via your package manager (e.g. `sudo apt install python3`) |

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### "python is not recognized"

The most common install error, and almost always the same fix.
{: .pt-subheading }

```bash
python --version    # if this fails, Python isn't on PATH
python3 --version    # try this instead — may work even when `python` doesn't
```

</summary>

This means Python installed, but your terminal doesn't know where to find it — usually because "Add to PATH" was left unchecked during a Windows install. The fix is to re-run the installer and check that box (or reinstall from scratch), then open a **new** terminal window, since existing windows won't pick up the change.

</details>

## Checking Your Python Version

Once Python is installed, check which version you have and where it's located — this affects how you run scripts in the terminal.

```bash
python --version     # Windows, or Mac/Linux with only Python 3
python3 --version    # Mac/Linux, to check if Python 3 is available
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Why version matters

Different Python versions need different terminal commands.
{: .pt-subheading }

```bash
python script.py     # Python 3 only (Windows, or Mac/Linux without Python 2)
python3 script.py    # Python 3 (Mac/Linux, when both Python 2 and 3 exist)
```

</summary>

On **Windows**, `python` always points to Python 3 (if you installed it correctly), so use `python script.py`. On **Mac/Linux**, many systems have both Python 2 (old, obsolete) and Python 3 still installed — `python` might point to the old version, so `python3` is safer. You can check which one you have by running the commands above; whichever one gives you a `3.x` version is what you should use.

</details>

## Using the Terminal

The terminal is a text-based way to navigate your computer's files and run programs, instead of clicking through folders.

!!! warning "Be careful what you type"
    The terminal has no undo, and no confirmation prompt for most commands — it does exactly what you type, even if that means deleting or overwriting something permanently. Never paste a command you don't understand, especially from a random webpage or chat, and treat anything involving `rm`, `sudo`, or a file path you didn't type yourself with extra caution.

```bash
pwd
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Step 1: Navigate to the folder that your python file is in

The four most common terminal commands to move around.
{: .pt-subheading }

```python-ref
pwd                  # where am I right now?
ls                   # what files are here? (use `dir` on Windows)
cd species_notes     # move into a folder
cd ..                # move up one level
```

</summary>

`pwd` is a good first command any time you're not sure where the terminal currently "is" — every other command (like running a script) acts relative to that location. `cd` ("change directory") is how you move between folders; `cd ..` is the one beginners forget, and it's how you back out of a folder you moved into by mistake.

Here's what this looks like in practice:

```bash
$ pwd
/Users/luka
$ ls
Desktop    Documents    Downloads
$ cd Documents
$ ls
my_project    other_stuff
$ cd my_project
$ ls
my_python_file.py
$ pwd
/Users/luka/Documents/my_project
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Step 2: Run the python file

`python script.py` runs a file, using whatever folder the terminal is currently in.
{: .pt-subheading }

```bash
python script.py      # Windows, or Mac/Linux with only Python 3 installed
python3 script.py     # Mac/Linux, when both Python 2 and 3 are present
```

</summary>

If `python` runs an old Python 2 installation (or isn't recognized at all) on Mac or Linux, try `python3` instead — many systems keep both commands around, with `python3` guaranteed to point at a modern version. `cd` into the folder containing your script first (see above), or provide the full path to the file instead, like `python path/to/script.py`.

</details>
