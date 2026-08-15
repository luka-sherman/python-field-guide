---
description: >-
  How to install Python, pick a code editor, and run your first .py file — a step-by-step
  setup guide.
---

# :material-monitor:{ .lg .middle } Workspace Setup

## Step 0: Install Python

0. Open your Terminal application *(Terminal on Mac/Linux, Command Prompt or PowerShell on Windows)* 

1. Type this command and press ++return++ to "run" it:

    ```bash
    python --version
    ```

    ??? success "If it shows `Python 3.x.x`, Python is installed!"
        If you ever decide to run your files from the Terminal later you'll use the command `python`. 

        Skip to Step 1: Pick a code editor. 

    ??? info "If you see `Python 2.x.x`"
        Python 2 is installed. Python 2 reached end of life in 2020 and is no longer maintained.

2. If you didn't see `Python 3.x.x` after running the last command, run this one:
        ```bash
        python3 --version
        ```

    ??? success "If it shows `Python 3.x.x`, Python is installed!"
        If you ever decide to run your files from the Terminal later you'll use the command `python3`.

    ??? failure "If you see anything else, download Python here."

        === "macOS"

            [python.org/downloads](https://python.org/downloads)
        
        === "Windows"

            [python.org/downloads](https://python.org/downloads)

            Check **"Add python.exe to PATH"** on the first install screen — if you skip this, the terminal won't recognize `python`
        
        === "Linux"

            Usually already installed. If `python3 --version` failed, install via your package manager (e.g. `sudo apt install python3`)



## Step 1: Pick an application to write code in

A **code editor** or an **IDE** ("Integrated Development Environment") is a text editor designed specifically for writing code — it's like Microsoft Word for programming.

- **Makes code easier to read** — syntax highlighting uses different colors for different parts of your code
- **Running code is easier** — click a Run button from your IDE instead of typing Terminal commands every time
- **Code completion** — the editor suggests function names and variables as you type, saving time and reducing typos
- **Error detection** — it warns you about common mistakes before you run the code
- **[Debugging](errors.md#using-a-debugger)** — pause your code mid-run and inspect variables to track down bugs, instead of only reading output after the fact

Download one of the **free** code editors below. You can always switch later.

| Code Editor | Best for | Audience | Made by | Download Links |
|--------|----------|---------|---------|---------|
| **Thonny** | <ul><li>*Never programmed before? Start here* — Designed for Python beginners</li><li>Only has the essentials</li><li>Variable inspector visually shows what's happening in your code</li><li>Can walk through your code one line at a time automatically, great for seeing exactly how a program runs</li></ul> | Beginners | Open-source | [Windows](https://thonny.org/) / [macOS](https://thonny.org/) / [Linux](https://thonny.org/) |
| **Visual Studio Code** | <ul><li>Scales well as you grow</li><li>General-purpose code editor</li><li>*NOTE: after installing, download the Python extension from the Extensions marketplace*</li></ul> | Beginners through professionals | Microsoft | [Windows](https://code.visualstudio.com/download) / [macOS](https://code.visualstudio.com/download) / [Linux](https://code.visualstudio.com/download) |
| **IDLE** | <ul><li>Comes with Python — no download needed</li><li>Minimal, doesn't scale well to bigger projects</li><li>*NOTE: no visible Run button — press ++f5++ or use Run → Run Module instead*</li><li>*NOTE: has a debugger, but it's basic — accessed via the Debug menu in the shell window, not built into the editor like the others*</li></ul> | Beginners | Python Software Foundation | Included / Included / `sudo apt install idle3` |
| **PyCharm Community** | <ul><li>Complete Python IDE</li><li>Everything built-in out of the box</li><li>Many panels/menus can feel overwhelming at first</li></ul> | Professionals | JetBrains | [Windows](https://www.jetbrains.com/pycharm/download/) / [macOS](https://www.jetbrains.com/pycharm/download/) / [Linux](https://www.jetbrains.com/pycharm/download/) |

??? info "What does "open-source" mean?"
    The source code that it is built from is publicly available for anyone to see, modify, and improve. 
    
    *Thonny* is maintained by volunteers in the open-source community. *VS Code* and *PyCharm* are made by companies but also have open-source elements.

## Step 2: Write and run a Python file

Now that you have Python installed and a code editor picked, you're ready to write actual Python code.

0. Open your code editor
1. Create a new file (**File → New**) and call it `hello.py`. The `.py` extension identifies that it's a Python file
2. Type this code:
```python-ref
print("Hello, World!")
```
3. Click the **Run button** (usually a green play icon or arrow) — most editors save your file automatically when you click Run, so there's no separate save step. 
4. Find the output window in the application where it says `Hello, World!`, it should pop up on its own. 

That's it! You've written and run your first Python program. From here, you can modify the code, run it again, and [work through the rest of this guide](foundations.md#tips-for-getting-started) to keep building your Python programming skills.

??? tip "Rules for naming Python files"
    **A Python filename uses lowercase letters and numbers separated by hyphens, with .py as the extension.**

    ```python-ref
    my_script.py     # valid
    my-script.py     # invalid — no punctuation other than underscore
    2_my_script.py   # invalid — can't start with a number
    my script.py     # invalid — no spaces
    ```

    1. **Ends in .py** 
    
        This is what tells your application to treat the file as Python code — the Run button, syntax highlighting, and imports all depend on the extension being there.
    
    2. **Only letters, underscores, and numbers** — but it can't start with a number. 
    
        Standard formatting is to use `snake_case` (all lowercase, separated with underscores). Python is case-sensitive (Species.py and species.py would be two different files).
    
    3. **No hyphens** 
    
        Even though `my-script.py` will run fine on its own, if you need to later `import my-script` it will be invalid syntax because Python reads the hyphen as subtraction.
    
    4. **No spaces** 
    
        They will break imports and makes running the file from the terminal require extra quoting.
    
    5. **Don't use a reserved keyword** 
    
        There are a handful of "keywords" that are reserved by Python to do specific things, so they can't be used elsewhere in your code. Run this code to get a list of all reserved keywords:

        ```python
        help("keywords")
        ```
    
    6. **Don't use a library's name** 
    
        Naming a file `random.py` or `math.py` in a project makes `import random` elsewhere in that same project import your file instead of Python's actual `random` library, which is a confusing bug to track down. Run this code to get a list of all reserved library names:
        
        ```python
        help("modules")
        ```
        
??? tip "Reading error messages"

    When you see red error text, the [Errors](errors.md#reading-errors) page covers how to read it.

## Using the terminal *(optional)*

The terminal is a text-based way to navigate your computer's files and run programs. 

It's good for running Python files that are already finished — either your own, or someone else's — without needing to open them in an editor. It's also handy for quickly re-running the same command over and over while testing.

0. Open the terminal 

    You can either use a dedicated terminal application (Terminal on Mac/Linux, Command Prompt or PowerShell on Windows), or if your code editor application has a terminal window you can use that. 

1. Navigate to the folder ("location") your Python file is saved in using these commands:

    ```bash
    pwd                  # What is my current location? Good to send first, or if you get lost
    ls                   # what folders and files are at my current location? (use `dir` on Windows)
    cd [folder name]     # move into a folder that is at my current location
    cd ..                # move back one level, into the parent location
    ```

    Here's an example:
    
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

2. Run the Python file

    Use whichever below command showed 3.x.x. when you checked your Python version above.

    ```bash
    python script.py
    python3 script.py
    ```

3. To stop a running program: ++ctrl+c++ 

4. You can now run a Python file again, or a different command.      

!!! warning "Be careful what you send in the terminal"
    The terminal has no undo, and no confirmation prompt for most commands — it does exactly what you type, even if that means deleting or overwriting something permanently. Never paste a command you don't fully understand, especially from a random webpage or AI.
    
    Use **extreme caution** with `rm`, `sudo`, or a file path you didn't type yourself.

??? tip "Terminal shortcuts"

    1. **Auto-complete file/folder names:** 
    
        Start typing a file or folder name and press ++tab++ — the terminal will autoc-omplete it for you. For example, if you type `cd Doc` then press Tab, it becomes `cd Documents/`. 
        
        If there are multiple matches, press ++tab++ again to cycle through them, or type more letters so that there is only one option it could be and then ++tab++ again.

    2. **Auto-fill previous commands:** 
    
        ++up++ shows your last command, and press it again to go further back. 
        
        ++down++ then moves forward through the history. 
        
        You can this press return to send that command without needing to type it out. This saves typing when you want to send the same command(s) multiple times.

    3. **Give the full path in one command:**

        `~/` aka "tilde" = your home folder. 
        
        Specify the complete path with `cd ~/Documents/my_folder/my_project`.

        You can also run the file with one command: `python path/to/script.py`.
    
    4. **Stop a running Python file:**

        ++ctrl+c++ 