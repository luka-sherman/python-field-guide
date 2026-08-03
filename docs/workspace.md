# Running Python on your own computer

## Step 0: Install Python

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Check if Python is installed

First, check if Python is already installed on your device. 
{: .pt-subheading }

</summary>

Open your terminal application (Terminal on Mac/Linux, Command Prompt or PowerShell on Windows) and run:

```bash
python --version    # try this first
python3 --version   # if it fails try this one
```

✅ If either shows `Python 3.x.x`, Python is installed! Remember which one worked (`python` or `python3`) because that's the command you'll use to run your Python files. You can move onto Step 1.

❌ If both commands fail (you get errors like "command not found"), expand the section below to download Python for your OS:

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Download if not

If it's not already installed, then download Python at the link below depending on what kind of computer you have. 
{: .pt-subheading }

</summary>

| OS | Where to get it | Important note |
|----|------------------|------|
| **Windows** | [python.org/downloads](https://python.org/downloads) | Check **"Add python.exe to PATH"** on the first install screen — if you skip this, the terminal won't recognize `python` |
| **macOS** | [python.org/downloads](https://python.org/downloads) | |
| **Linux** | Usually already installed | If `python3 --version` failed, install via your package manager (e.g. `sudo apt install python3`) |

</details>


## Step 1: Pick a code editor

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Why use a code editor?

A **code editor** or **IDE** ("Integrated Development Environment") is a text editor designed specifically for writing code — it's like Microsoft Word for programming.
{: .pt-subheading }

</summary>

- **Writing code is easier** — syntax highlighting (colored text) makes different parts of your code stand out, so you catch mistakes faster
- **Running code is faster** — click a Run button instead of typing terminal commands every time
- **Code completion** — the editor suggests function names and variables as you type, saving time and reducing typos
- **Error detection** — it warns you about common mistakes before you run the code
- **[Debugging](bugs.md#using-a-debugger)** — pause your code mid-run and inspect variables to track down bugs, instead of just reading output after the fact

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Compare editors

Once Python is installed, pick one of the **free** code editors below based on your priorities, and download it.
{: .pt-subheading }

</summary>

| Code Editor | Best for | Audience | Made by | Download Links |
|--------|----------|---------|---------|---------|
| **Thonny** | <ul><li>🌟 *Never programmed before? Start here* — Designed for Python beginners</li><li>Minimal interface</li><li>Variable inspector visually shows what's happening in your code</li><li>Can walk through your code one line at a time automatically, great for seeing exactly how a program runs</li></ul> | Beginners | Open-source | [Windows](https://thonny.org/) / [macOS](https://thonny.org/) / [Linux](https://thonny.org/) |
| **Visual Studio Code** | <ul><li>Scales well as you grow</li><li>General-purpose code editor</li><li>*NOTE: after installing, download the Python extension from the Extensions marketplace*</li></ul> | Beginners through professionals | Microsoft | [Windows](https://code.visualstudio.com/download) / [macOS](https://code.visualstudio.com/download) / [Linux](https://code.visualstudio.com/download) |
| **IDLE** | <ul><li>Comes with Python — no download needed</li><li>Minimal, doesn't scale well to bigger projects</li><li>*NOTE: no visible Run button — press F5 or use Run → Run Module instead*</li><li>*NOTE: has a debugger, but it's basic — accessed via the Debug menu in the shell window, not built into the editor like the others*</li></ul> | Beginners | Python Software Foundation | Included / Included / `sudo apt install idle3` |
| **PyCharm Community** | <ul><li>Complete Python IDE</li><li>Everything built-in out of the box</li><li>Many panels/menus can feel overwhelming at first</li></ul> | Professionals | JetBrains | [Windows](https://www.jetbrains.com/pycharm/download/) / [macOS](https://www.jetbrains.com/pycharm/download/) / [Linux](https://www.jetbrains.com/pycharm/download/) |

**Note:** Any editor works with any Python library, and your choice doesn't lock you in — you can always switch later.

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Open source

What is "Open Source" software?
{: .pt-subheading }

</summary>

It means the source code is publicly available for anyone to see, modify, and improve. Thonny is maintained by volunteers in the open-source community. VS Code and PyCharm are made by companies but also have open-source elements.

</details>

## Step 2: Write and run a Python file

Now that you have Python installed and a code editor picked, you're ready to write actual Python code.

0. Open your code editor
1. Create a new file (**File → New**) and save it with a `.py` extension, e.g. `hello.py` — the `.py` extension identifies that it's a Python file
2. Type this sample code:
```python-ref
print("Hello, World!")
```
3. Click the **Run button** (usually a green play icon or arrow) — most editors save your file automatically when you click Run, so there's no separate save step. The output appears right there in the editor.

That's it! You've written and run your first Python program. From here, you can modify the code, run it again, and work through the rest of this guide to keep building your Python skills.

See red text instead of your expected output? The [Bugs](bugs.md#reading-errors) page covers how to read it.

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Rules for naming files

A Python filename uses lowercase letters and numbers seperated by hyphens, with .py as the extension.
{: .pt-subheading }

```python-ref
my_script.py     # valid
my-script.py     # invalid — no punctuation other than underscore
2_my_script.py   # invalid — can't start with a number
my script.py     # invalid — no spaces
```

</summary>
- **Ends in .py** - this is what tells your application to treat the file as Python code — the Run button, syntax highlighting, and imports all depend on the extension being there.
- **Only letters, underscores, and numbers** - but it can't start with a number. Standard formatting is to use `snake_case` (all lowercase, separated with underscores). Python is case-sensitive (Species.py and species.py would be two different files).
- **No hyphens** — even though `my-script.py` will run fine on its own, if you need to later `import my-script` it will be invalid syntax becuse Python reads the hyphen as subtraction.
- **No spaces** — it will break imports and makes running the file from the terminal require extra quoting.
- **Don't use a reserved keyword** - There are a handful of "keywords" that are reserved by Python to do specfic things, so they can't be used elsewhere in your code.
    ```python
    print("Run this to get a list of all reserved keywords that you can't name a file: ")
    help("keywords")
    ```
- **Don't use a library's name** — naming a file `random.py` or `math.py` in a project makes `import random` elsewhere in that same project import your file instead of Python's actual `random` library, which is a confusing bug to track down.
    ```python
    print("Run this to get a list of all reserved library names that you can't name a file: ")
    help("modules")
    ```

</details>

## Using the terminal (optional)

The terminal is a text-based way to navigate your computer's files and run programs, instead of clicking through folders. It's best for running Python files you've already written — either your own finished scripts, or someone else's — without needing to open them in an editor. It's also handy for quickly re-running the same command over and over while testing.

!!! warning "Be careful what you type"
    The terminal has no undo, and no confirmation prompt for most commands — it does exactly what you type, even if that means deleting or overwriting something permanently. Never paste a command you don't understand, especially from a random webpage or chat, and treat anything involving `rm`, `sudo`, or a file path you didn't type yourself with extra caution.

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### First, navigate to where your Python file is saved

The four most common terminal commands to move around.
{: .pt-subheading }

```python-ref
pwd                  # where am I right now?
ls                   # what files are here? (use `dir` on Windows)
cd [folder name]     # move into a folder
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

**Shortcut:** Instead of typing `cd Documents`, then `cd my_project`, you can give the full path directly: `cd Documents/my_project`. Or use `~/` (tilde = your home folder) to go directly from anywhere: `cd ~/Documents/my_project`.

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Then, run the Python file

Use whichever command worked during your install check (`python` or `python3`).
{: .pt-subheading }

```bash
python script.py      # if this worked during your version check
python3 script.py     # if this worked during your version check
```

</summary>

Use whichever command worked when you checked your Python version — and stick with it consistently. `cd` into the folder containing your script first (see "Navigate to the folder" above), or provide the full path to the file instead, like `python path/to/script.py`.

**Why two commands?** On Windows, `python` is standard. On Mac/Linux, `python` might not work or might point to an old Python 2, so `python3` is more reliable. They're interchangeable — just pick the one that works for you.

**To stop a running program:** Press **Ctrl+C** (hold Control, press C) — this works on Windows, Mac, and Linux.

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Terminal shortcuts

A few quick tricks to save time and typing.
{: .pt-subheading }

```bash
↑ and ↓         # scroll through command history
Tab             # auto-complete file/folder names
```

</summary>

**Up/down arrow keys:** After you've run a few commands, press the **up arrow** `↑` to see your last command, and press it again to go further back. Use the **down arrow** `↓` to move forward through the history. This saves a lot of typing when you're testing the same command over and over — run it, make a change to your file, then press `↑` to re-run it instantly.

**Tab completion:** Start typing a filename or folder name and press **Tab** — the terminal will auto-complete it for you. For example, if you type `cd Doc` then press Tab, it becomes `cd Documents/`. If there are multiple matches, press Tab again to cycle through them or type more letters.

</details>
