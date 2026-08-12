# :material-bug-outline:{ .lg .middle } Errors

Your code had an error or didn't do what you expected — here are tools for figuring out why. 

## Reading errors

An **error** is Python's way of telling you it couldn't do what your code asked — a typo it can't parse, a variable that doesn't exist, dividing by zero, and so on. When Python hits one, it stops the program right there. That's not a sign you've broken something unrecoverable — it's Python pointing at the exact spot to look.

Errors are part of programming, and will happen constantly. 

### How to read a traceback

Red text instead of your expected output? Here's how to read it.

```python-ref
Traceback (most recent call last):
  File "hello.py", line 2, in <module>
NameError: name 'name' is not defined
```

Errors in Python show up as a **traceback** — don't be intimidated by the wall of text. Read it from the **bottom up**:

- The **last line** tells you the type of error and a short description (e.g. `NameError: name 'name' is not defined`) — this is usually the most useful part.
- The line just above it tells you the **file and line number** where the error happened, so you know exactly where to look in your code.

Fix the issue there, save, and run again. Errors are a normal part of writing code — even experienced programmers see them constantly.

**Longer tracebacks** show one `File` line per function call involved — your code calling a function, which calls another function, and so on. Keep reading bottom to top: the first `File` line naming *your own file* (not a library you imported) is almost always the one worth looking at — the frames above it are usually just the library code that was doing what your code asked, not the actual source of the bug.

```python-ref
Traceback (most recent call last):
  File "hello.py", line 5, in <module>
  File "hello.py", line 3, in describe
  File "/usr/lib/python3.11/random.py", line 449, in choice
IndexError: list index out of range
```

## Handling errors

`try`/`except` lets your program handle an error instead of crashing.

```python-ref
try:
    [run this block of code first]
except [specific error]:
    [if the above block failed due to the specific error named in the except, then run this code]
```

!!! success "Handle it with try/except"
    - A failure that's expected and outside your control, even when the code is correct
    - Catch the specific exception type you expect, not a bare `except:`
    - Keep the `try` block small — only the line that can actually fail

!!! danger "Fix the code instead"
    - Typos, bugs, incorrect logic 
    - Catching several unrelated exception types just to make errors stop — often a sign one of them is actually a bug

An **exception** is Python's formal name for the type of error that was raised — `KeyError`, `ValueError`, and so on are all exceptions, and it's the technical term for what `except` actually matches against. Matching `except` to a specific exception type (rather than catching everything) means your program only handles the failure you actually expected, and still crashes loudly on a genuine bug — which is usually what you want while learning.

```python-ref
lengths = {"ball python": 4.5, "burmese python": 12}

try:
    print(lengths["reticulated python"])
except KeyError:
    print("no length on record for that species")
```

### Common exception types

The name in the traceback's last line tells you which of these went wrong.

**Runtime errors** — valid Python that fails only once that specific line actually executes. These are the ones `except` can catch.

| Exception | Happens when |
|-----------|---------------|
| `NameError` | Using a variable that hasn't been assigned yet |
| `TypeError` | Using a value the wrong way for its type, or calling a function with the wrong number of arguments |
| `ValueError` | The type is right, but the value doesn't make sense — `int("banana")`, or unpacking the wrong number of values (`a, b = 1, 2, 3`) |
| `KeyError` | Looking up a dict key that doesn't exist |
| `IndexError` | Looking up a list index that doesn't exist |
| `ZeroDivisionError` | Dividing by zero |
| `AttributeError` | Calling a method that doesn't exist on that object — often a typo, or calling a method on `None` |
| `FileNotFoundError` | Trying to open a file that doesn't exist at that path |
| `ImportError` (or `ModuleNotFoundError`) | Importing something that doesn't exist, or a library that isn't installed |

**Parse-time errors** — Python can't even finish reading the file, so nothing runs at all. `except` can't catch this — it has to be fixed.

| Exception | Happens when |
|-----------|---------------|
| `SyntaxError` | The code isn't valid Python at all — a missing colon, mismatched parentheses |
| `IndentationError` | A specific kind of `SyntaxError` for inconsistent or incorrect indentation |

??? tip "Catching multiple exceptions"
    List several exception types in one `except` to handle them the same way. Separate `except` blocks work too, if each error type needs different handling — Python checks them top to bottom and runs the first one that matches.

    ```python-ref
    try:
        print(lengths[species])
    except (KeyError, TypeError):
        print("couldn't look up that species")
    ```

??? tip "else and finally"
    `else` runs only if `try` succeeded; `finally` always runs, whether it succeeded or not. `else` is a good place for code that should only run after a successful `try`, without risking it accidentally triggering the `except` block itself. `finally` is for cleanup that has to happen either way, like closing a file — it runs even if the `try` block succeeded, failed, or the `except` block itself raised a new error.

    ```python-ref
    try:
        length = lengths[species]      # attempted first
    except KeyError:
        print("no length on record")   # runs only on a KeyError
    else:
        print(f"found it: {length} ft")  # runs only if try succeeded
    finally:
        print("lookup attempt finished")  # always runs
    ```

??? run "Run a try/except example"
    All the examples above, combined into one script:

    ```python
    lengths = {"ball python": 4.5, "burmese python": 12}

    try:
        print(lengths["reticulated python"])
    except KeyError:
        print("no length on record for that species")

    lengths = {"ball python": 4.5, "burmese python": 12}
    species = "reticulated python"

    try:
        print(lengths[species])
    except KeyError:
        print("no length on record for that species")
    except TypeError:
        print("species should be text, not a number")

    lengths = {"ball python": 4.5, "burmese python": 12}
    species = "ball python"

    try:
        length = lengths[species]      # attempted first
    except KeyError:
        print("no length on record")   # runs only if the try block raised a KeyError
    else:
        print(f"found it: {length} ft")  # runs only if the try block succeeded
    finally:
        print("lookup attempt finished")  # always runs, no matter what happened above
    ```

## Using a debugger

A **debugger** is a tool built into most code editors that lets you pause a running program and look around, instead of only seeing what it printed after the fact. Pause your code mid-run to inspect what's happening and inspect variables — instead of only reading `print()` outputs at the end. 

### Step 0: Set "breakpoints"

A **breakpoint** marks a specific line where you want the program to pause while debugging, so you can inspect it. You can set as many breakpoints as you want. Set these *before* you start running. 

Click in the margin next to a line number to set one. To remove it, click the same spot again — the red dot toggles off.

### Step 1: Run in debug mode 

Your program will run normally until it hits the *first* breakpoint, then it pauses there.

Look for a **"Debug"** button instead of the regular Run button. 

### Step 2: What you can do at a breakpoint

When it gets to a breakpoint it will pause, and you can use these controls to move through your code:

| Control | What it does | Use it when |
|---------|---------------|-------------|
| **Inspect variables** | Shows the current value of every variable while paused | You want to watch exactly when a variable becomes wrong, instead of guessing |
| **Step Into** | Jumps inside the [function](functions.md) being called, so you can watch it run line by line | You want to see exactly what a function does |
| **Step Over** | Runs the current line, then pauses on the next one, without entering any function it calls | You trust the function works and don't need to see inside it |
| **Step Out** | Finishes the current function, then pauses back where it was called from | You stepped into a function but have seen enough and want to jump back out |
| **Continue/Resume** (▶) | Runs until the next breakpoint, or finishes if there are none left | You're done inspecting the current pause point and want to jump ahead |
| **Stop debugging** | Ends the debug session entirely | You're done, instead of stepping or continuing all the way through |

??? tip "Where debugging controls are in each editor"
    Where to find the debugger, and what it calls things, varies by editor.

    === "Thonny"

        - **Debug button:** Bug icon in the main toolbar
        - **Step controls:** Inline in the main toolbar
        - **Stop button:** Same toolbar
        - **Where output shows:** Same Shell panel as a normal run
        - **Inspecting variables:** Always-visible Variables panel

        You don't need to set any breakpoints — Thonny's debugger pauses at every step by default, which is great for watching exactly how a program runs the first time.

    === "VS Code"

        - **Debug button:** "Run and Debug" in the sidebar, or the dropdown next to the Run button
        - **Step controls:** A floating toolbar
        - **Stop button:** Red square, same floating toolbar
        - **Where output shows:** Separate "Debug Console" panel
        - **Inspecting variables:** Variables section in the Run and Debug sidebar

    === "IDLE"

        - **Debug button:** Debug menu in the Shell window (turn on before running)
        - **Step controls:** A separate popup window
        - **Stop button:** "Quit" button, same popup window
        - **Where output shows:** Same Shell window as a normal run
        - **Inspecting variables:** Same popup Debug Control window

        Most basic of the four.

    === "PyCharm"

        - **Debug button:** Bug icon next to the Run button
        - **Step controls:** The bottom Debug tool window
        - **Stop button:** Red square, same tool window
        - **Where output shows:** Same "Debug" tool window
        - **Inspecting variables:** Same tool window, or hover over a variable in the editor
