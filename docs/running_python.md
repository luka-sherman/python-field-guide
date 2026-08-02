# Running Python on your own computer

## Step 0: install Python

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

### Download links

If it's not already installed, then download Python at the link below depending on what kind of computer you have. 
{: .pt-subheading }

</summary>

| OS | Where to get it | Important note |
|----|------------------|------|
| **Windows** | [python.org/downloads](https://python.org/downloads) | Check **"Add python.exe to PATH"** on the first install screen — if you skip this, the terminal won't recognize `python` |
| **macOS** | [python.org/downloads](https://python.org/downloads) | |
| **Linux** | Usually already installed | If `python3 --version` failed, install via your package manager (e.g. `sudo apt install python3`) |

</details>


## Step 1: pick a code editor

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Why a code editor?

A **code editor** or **IDE** ("Integrated Development Environment") is a text editor designed specifically for writing code — it's like Microsoft Word for programming.
{: .pt-subheading }

</summary>

- **Writing code is easier** — syntax highlighting (colored text) makes different parts of your code stand out, so you catch mistakes faster
- **Running code is faster** — click a Run button instead of typing terminal commands every time
- **Code completion** — the editor suggests function names and variables as you type, saving time and reducing typos
- **Error detection** — it warns you about common mistakes before you run the code
- **Debugging** — pause your code mid-run and inspect variables to track down bugs, instead of just reading output after the fact

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

### Debugging

Pause your code mid-run to inspect what's happening and inspect variables —  instead of only reading `print()` outputs at the end. 
{: .pt-subheading }

</summary>

**Step 0: Before running, set "breakpoints"**

A **breakpoint** marks a specific line where you want the program to pause while debugging, so you can inspect it. 

Click in the margin next to a line number (or press F9 in most editors) to set one. You can set as many breakpoints as you want. To remove it, click the same spot again — the red dot toggles off.

*Note for Thonny users: you don't need to set any breakpoints as Thonny's debugger pauses at every step by default, which makes it great for watching exactly how a program runs for the first time.*

**Step 1: Start running to the first breakpoint**

Look for a "Debug" button (often next to the Run button, sometimes a bug icon) instead of the regular Run button. Your program runs normally until it hits the *first* breakpoint, then pauses there.

**Step 2: When at a breakpoint, use these controls to move through your code**

- **Continue/Resume** (often shown as a ▶ play icon) — runs the program until it hits the *next* breakpoint, or finishes if there are none left. This is how you move between breakpoints. Use this when you're done inspecting the current pause point and want to jump ahead to the next one.
- **Step Over** — runs the current line and moves to the next one, without entering any [function](functions.md) it calls. Use this when you trust the function works and don't need to see inside it.
- **Step Into** — if the current line calls a function (a named, reusable block of code — see [Functions](functions.md)), this jumps *inside* that function so you can watch it run line by line — even if there's no breakpoint inside it. Use this when you want to see exactly what a function does.
- **Step Out** — finishes running the rest of the current function all at once, then pauses again back where that function was called from. Use this when you stepped into a function but have seen enough and want to jump back out.
- **Inspect variables** — most editors show you the current value of every variable while paused, often the fastest way to find a bug since you can watch exactly when a variable becomes wrong instead of guessing. 
    - Thonny: shows an always-visible variable inspector panel.
    - VS Code: shows variables in a debug panel.
    - IDLE: shows variables in a more basic debugger window.
    - PyCharm: shows the values of variables in a debug panel or by hovering over the variable in your code.
- **Stop debugging** — look for a Stop button (often a red square) to end the debug session entirely, instead of stepping or continuing all the way through.

**Where's my output?** Debug mode often shows `print()` output in a separate "Debug Console" or "Debug" panel, rather than the regular output panel you see with a normal run.

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

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Reading errors

Red text instead of your expected output? Here's how to read it.
{: .pt-subheading }

```python-ref
Traceback (most recent call last):
  File "hello.py", line 2, in <module>
NameError: name 'name' is not defined
```

</summary>

Errors in Python show up as a **traceback** — don't be intimidated by the wall of text. Read it from the **bottom up**:

- The **last line** tells you the type of error and a short description (e.g. `NameError: name 'name' is not defined`) — this is usually the most useful part.
- The line just above it tells you the **file and line number** where the error happened, so you know exactly where to look in your code.

Fix the issue there, save, and run again. Errors are a normal part of writing code — even experienced programmers see them constantly.

</details>

## Using the terminal (optional)

The terminal is a text-based way to navigate your computer's files and run programs, instead of clicking through folders. It's best for running Python files you've already written — either your own finished scripts, or someone else's — without needing to open them in an editor. It's also handy for quickly re-running the same command over and over while testing.

!!! warning "Be careful what you type"
    The terminal has no undo, and no confirmation prompt for most commands — it does exactly what you type, even if that means deleting or overwriting something permanently. Never paste a command you don't understand, especially from a random webpage or chat, and treat anything involving `rm`, `sudo`, or a file path you didn't type yourself with extra caution.

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Step 1: Navigate to the folder that your Python file is in

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

### Step 2: Run the Python file

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
