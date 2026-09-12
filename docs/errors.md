---
description: >-
  How to read Python error messages and tracebacks, handle them with try/except, and debug
  with print statements or a debugger.
---

# :material-bug-outline:{ .lg .middle } Errors

**Errors** occur when a line of code is impossible to run, so the program stops and displays an error message with information on what went wrong and where. 

**"Bugs"** are the general term for *any* mistake or error in your code, like logic errors. 

They are part of programming, and will happen constantly. Once you know what kind of error you have, you can check for common causes, and try one of these ways of fixing it:

<div class="pt-jump-table" markdown="block">

|  | [Read traceback/error](#reading-a-traceback) | [`try`/`except`](#catch-with-tryexcept) | [Debugging strategies](#debugging-strategies) | [Debugger tool](#debugger-tool) | [Testing](#detect-errors-with-testing) |
|----------|:---:|:---:|:---:|:---:|:---:|
| [Syntax errors](#syntax-errors) | :material-check:{ .pt-icon-success } | :material-close:{ .pt-icon-fail } | :material-close:{ .pt-icon-fail } | :material-close:{ .pt-icon-fail } | :material-close:{ .pt-icon-fail } |
| [Runtime errors](#runtime-errors) | :material-check:{ .pt-icon-success } | :material-check:{ .pt-icon-success } | :material-check:{ .pt-icon-success } | :material-check:{ .pt-icon-success } | :material-check:{ .pt-icon-success } |
| [Logic errors](#logic-errors) | :material-close:{ .pt-icon-fail } | :material-close:{ .pt-icon-fail } | :material-check:{ .pt-icon-success } | :material-check:{ .pt-icon-success } | :material-check:{ .pt-icon-success } |

</div>

## Kinds of errors:

<div class="pfg-section" markdown="block">

### Syntax errors { .pt-fake-h2 }

The code doesn't follow Python's grammar rules, so it can't read or run the file. These errors must be fixed directly.

<div class="pt-jump-table" markdown="block">

| | [Read error message](#reading-a-syntax-error-message) | [`try`/`except`](#catch-with-tryexcept) | [Debugging strategies](#debugging-strategies) | [Debugger tool](#debugger-tool) | [Testing](#detect-errors-with-testing) |
|---|:---:|:---:|:---:|:---:|:---:|
| Ways to fix syntax errors | :material-check:{ .pt-icon-success }<br>Points to what Python couldn't read | :material-close:{ .pt-icon-fail } | :material-close:{ .pt-icon-fail } | :material-close:{ .pt-icon-fail } | :material-close:{ .pt-icon-fail } |

</div>

<div class="pt-checklist-table" markdown="block">

| Kind of syntax error | Happens when | Check for |
|-------|---------------|-----------|
| **`IndentationError`** | Incorrect indentation | <ul><li>Code pasted from somewhere else, with indentation that doesn't match the rest of the file.</li></ul> |
| **`SyntaxError`** | The code isn't valid Python | <ul><li>A missing colon after `if`, `for`, `while`, `def`, `class` etc.</li><li>An unclosed parenthesis, bracket, or quote.</li><li>A line that ends before the expression on it is complete, like a trailing `+`.</li><li>Copying old Python 2 code, like `print "hello"` without parentheses — Python 3 requires `print("hello")`.</li><li>Curly "smart quotes" (`'` `'` `"` `"`) instead of straight ones — copying code out of a Word doc, PDF, or a web page can silently swap them in; Python only recognizes straight quotes. Retype them if this happens.</li><li>A non-breaking space instead of a regular one, from that same kind of copy-paste — also has to be retyped.</li><li>Writing `if x = 5:` instead of `if x == 5:`</li><li>Naming a variable after a reserved keyword, like `class` or `pass`.</li></ul> |
| **`TabError`** | Tabs and spaces mixed in the same block of indentation | <ul><li>Pick one (spaces is Python's convention) and set your editor to use it everywhere — many editors can auto-convert existing tabs to spaces.</li><li>Code pasted in from a source using the other kind of indentation than the rest of the file.</li></ul> |

</div>

</div>

<div class="pfg-section" markdown="block">

### Runtime errors { .pt-fake-h2 }

A **runtime error** happens once a program is already running — the code is grammatically correct, but unable to execute.

Think about what programming concepts the failing line is using (data type, loop, conditional, etc), and revisit that page on this site to confirm you're applying it correctly.

<div class="pt-jump-table" markdown="block">

|  | [Read traceback message](#reading-a-traceback) | [`try`/`except`](#catch-with-tryexcept) | [Debugging strategies](#debugging-strategies) | [Debugger tool](#debugger-tool) | [Testing](#detect-errors-with-testing) |
|---|:---:|:---:|:---:|:---:|:---:|
| Ways to fix runtime errors | :material-check:{ .pt-icon-success }<br>Tells you exactly where it broke | :material-check:{ .pt-icon-success }<br>Use when the failure is expected and outside your control | :material-check:{ .pt-icon-success }<br>Figure out why it failed | :material-check:{ .pt-icon-success }<br>Step through the code to see exactly what's happening | :material-check:{ .pt-icon-success }<br>Lock in the fix to prevent it from happening again |

</div>

<div class="pt-checklist-table" markdown="block">

| Kind of runtime error | Happens when | Check for |
|-------|---------------|-----------|
| **`AttributeError`** | Calling a method or attribute that doesn't exist on that object | <ul><li>Typo in a method name.</li><li>A method that is being called on the wrong type: `"ball".append(...)` fails since `.append()` can only be applied to `list` not `str`.</li><li>A variable holds `None` instead of the object you meant to call a method on — often a function returned None instead of an expected value.</li><li>Reassigning a variable to the result of an in-place list method like `.append()` or `.sort()` — those return `None`, not the changed list.</li><li>A local file named the same as a library you import, see [file naming rules](workspace.md#step-2-write-and-run-a-python-file).</li></ul> |
| **`FileNotFoundError`** | Trying to open a file that doesn't exist at that path | <ul><li>A typo in the filename, path, extension, or case. Open your file browser (Finder/  File Explorer) and check directly.</li><li>The path is relative to your current working directory</li><li>Meant to create a file but opened in read mode `"r"` instead of write mode `"w"` which creates the file if it doesn't exist.</li></ul> |
| **`ImportError`** | Importing a name that doesn't exist in a module that *was* found | <ul><li>The module itself was found, but `from module import name` is asking for something that doesn't exist inside it — a typo in `name`.</li><li>The name exists, but in a different module than the one you're importing it from.</li><li>A local file named the same as a library you import, see [file naming rules](workspace.md#step-2-write-and-run-a-python-file).</li><li>Two of your own files importing from each other — restructure so one of them doesn't need to import the other, often by moving the shared piece into a third file.</li></ul> |
| **`IndexError`** | Looking up an index that doesn't exist — in a list, tuple, or string | <ul><li>Off-by-one — `len(items)` is one past the last valid index; the last item is `items[len(items) - 1]`.</li><li>The sequence is shorter than you assumed.</li><li>Modifying a list while looping over it, so its length changes mid-loop.</li></ul> |
| **`KeyError`** | Looking up a dict key that doesn't exist | <ul><li>The key doesn't exist — check spelling and capitalization against how the [dict](collections.md#dictionaries) was actually built.</li><li>Use `.get(key)` instead of `[key]` when a missing key is expected, so you get `None` back instead of a crash.</li></ul> |
| **`ModuleNotFoundError`** | Importing a module that can't be found| <ul><li>The library isn't installed — `pip install` it into the same environment you're running from.</li><li>A typo in the module name.</li></ul> |
| **`NameError`** | Using a variable that hasn't been assigned yet | <ul><li>Misspelled or mis-cased — Python is case-sensitive, `species` and `Species` are different names.</li><li>Used before the line that assigns it — Python reads top to bottom, so the assignment has to come first.</li><li>Assigned inside a function, but used outside it — see [local vs global variables](functions.md#local-vs-global-variables).</li></ul> |
| **`RecursionError`** | A function calls itself too many times without ever reaching a base case | <ul><li>No [base case](functions.md#recursion) — the function has no condition that ever stops it from calling itself.</li><li>A base case exists, but is unreachable — check that each recursive call actually moves closer to it (the argument shrinks, or grows, toward it every time).</li><li>The recursion is correct, but genuinely deep — Python's default limit is around 1000 calls. Rewriting as a loop is usually the better fix.</li></ul> |
| **`TypeError`** | Using a value the wrong way for its type, or calling a function with the wrong number of arguments | <ul><li>Combining a `str` with a number, like `"length: " + 4.5` — convert first with [`str()`](types.md#convert_2).</li><li>A variable is `None` where you expected a real value — often a function that fell through without hitting a [`return`](functions.md#return-values).</li><li>Called a function without all of its required arguments.</li><li>Missing parentheses on a call — `len` (the function object) instead of `len(species)` (the result), then trying to use it like a number or string.</li><li>Trying to change a character in a string directly (`name[0] = "X"`) — strings are immutable; build a new string instead.</li><li>Sorting, or comparing with `<` or `>`, a [list](collections.md#lists) of mixed, incompatible types, like `[3, "burmese"]`.</li><li>Using a mutable collection (`list`, `dict`, or `set`) as a [dict](collections.md#dictionaries) key or a [set](collections.md#sets) item.</li></ul> |
| **`UnboundLocalError`** | A local variable used before it's assigned | <ul><li>Assigned to that name *later* in the function — Python then treats it as local for the whole function body, so reading it earlier fails instead of falling back to a variable of the same name outside. See [local vs global variables](functions.md#local-vs-global-variables).</li><li>If you actually meant to change the outer variable, add `global name` (or rename the local one).</li></ul> |
| **`ValueError`** | The argument is the right *type*, but not a valid *value* for what's being done with it | <ul><li>Converting a string to a number, but its text doesn't actually look like one — `int("four")` or `float("")`.</li><li>Unpacking the wrong number of values, like `a, b = 1, 2, 3`.</li></ul> |
| **`ZeroDivisionError`** | Dividing by zero | <ul><li>The divisor could be a variable, not a literal `0` (often a count or length that turned out empty).</li><li>Guard with `if divisor != 0:` before dividing, if zero is a value you actually expect sometimes.</li></ul> |

</div>

</div>

<div class="pfg-section" markdown="block">

### Logic errors { .pt-fake-h2 }

A logic error is a bug Python doesn't notice, it finishes running but gives you an **unexpected result** because the reasoning itself was **inaccurate**.

Think about what programming concepts you are using (data types, loops, conditionals, etc.) and revisit those pages on this site to confirm you're applying them correctly.

<div class="pt-jump-table" markdown="block">

|  | [Read traceback/error](#reading-a-traceback) | [`try`/`except`](#catch-with-tryexcept) | [Debugging strategies](#debugging-strategies) | [Debugger tool](#debugger-tool) | [Testing](#detect-errors-with-testing) |
|---|:---:|:---:|:---:|:---:|:---:|
| Ways to fix logic errors? | :material-close:{ .pt-icon-fail }<br>No error message is shown | :material-close:{ .pt-icon-fail }<br>No error is raised | :material-check:{ .pt-icon-success }<br>Helps you find exactly where the code's behavior diverges from what you expected | :material-check:{ .pt-icon-success }<br>Especially useful, since there's no error message to point you anywhere | :material-check:{ .pt-icon-success }<br>State your expected output, so the mistake gets caught automatically next time |

</div>

</div>

## Fixing errors:

<div class="pfg-section" markdown="block">

### Reading a syntax error message { .pt-fake-h2 }

Red text instead of your expected output? Here's how to read it.

```python-ref
  File "hello.py", line 1
    if True
           ^
SyntaxError: expected ':'
```

The code never ran, but Python still points at the problem. Read it from the **bottom up**:

- The **last line** names the problem (`SyntaxError: expected ':'`) — this is usually the most useful part.
- The line above it points at the **file and line number**, with a `^` marking roughly where Python gave up.

Fix the issue there, save, and run again. Errors are a normal part of writing code — even experienced programmers see them constantly.

That pointer isn't always exactly where the mistake is — an unclosed bracket or quote, for example, can get reported many lines later, once Python finally runs out of file without finding the closing character. See [Isolate the problem](#isolate-the-problem) for narrowing down a case like that.

</div>

<div class="pfg-section" markdown="block">

### Reading a traceback { .pt-fake-h2 }

A runtime error follows the same bottom-up pattern — but since the program actually started running, Python can show a full **traceback**: don't be intimidated by the wall of text.

```python-ref
Traceback (most recent call last):
  File "hello.py", line 2, in <module>
NameError: name 'name' is not defined
```

The **last line** and the **file and line** above it still matter most, same as before.

**Longer tracebacks** show one `File` line per function call involved — your code calling a function, which calls another function, and so on. Keep reading bottom to top: the first `File` line naming *your own file* (not a library you imported) is almost always the one worth looking at — the frames above it are usually just the library code that was doing what your code asked, not the actual source of the bug.

```python-ref
Traceback (most recent call last):
  File "hello.py", line 5, in <module>
  File "hello.py", line 3, in describe
  File "/usr/lib/python3.11/random.py", line 449, in choice
IndexError: list index out of range
```

</div>

<div class="pfg-section" markdown="block">

### Catch with try/except { .pt-fake-h2 }

`try`/`except` lets your program handle [runtime errors](#runtime-errors) and then continue without crashing.

```python-ref
try:
    [run this block of code first]  # only the line(s) that could cause the error
except [error name]:  # i.e. KeyError, ValueError, etc
    [if the try block caused the specified error, then continue and run this code]
```

#### When to use it  { .pt-fake-h3 }

!!! success "Handle it with try/except"
    - The failure is genuinely outside your control — a file that might not exist, a network call, user input you can't fully validate ahead of time
    - The failure is an expected, normal outcome — not a mistake
    - You have real alternative logic to run instead, like a fallback value or a retry — not just silencing the error

!!! danger "Fix the code instead"
    - You don't know what is causing the error
    - It is in your control to fix the error
    - Just wanting to make errors stop — often a sign there is a bug

#### Catching multiple exceptions  { .pt-fake-h3 }

List several exception types in one `except` to handle them the same way. Separate `except` blocks work too, if each error type needs different handling — Python checks them top to bottom and runs the first one that matches.

```python-ref
try:
    length = float(lengths[species])
except (KeyError, TypeError):                 #  handle these the same way
    print("couldn't look up that species")
except ValueError:                            # separate for different handling
    print("length on record isn't a number")
```

#### Optional else and finally blocks  { .pt-fake-h3 }

`else` runs only if `try` succeeded, but it won't trigger the `except` block. This isn't commonly used.

`finally` always runs, and is for cleanup that has to happen either way, like closing a file.


```python-ref
try:
    length = lengths[species]         # attempted first
except KeyError:
    print("no length on record")      # runs only on a KeyError
else:
    print(f"found it: {length} ft")   # runs only if try succeeded
finally:
    print("lookup attempt finished")  # always runs
```

??? run "Run a try/except example"
    A case where try/except is the right tool — converting a value that might not be a valid number:

    ```python
    raw_length = "n/a"

    print("trying to read the length")

    try:
        length = float(raw_length)
        print(f"length: {length} ft")
    except ValueError:
        print(f"couldn't read '{raw_length}' as a number")
    ```

</div>

<div class="pfg-section" markdown="block">

### Debugging strategies { .pt-fake-h2 }

These general techniques help close the gap between what you think the code does and what it's actually doing.

#### Read it out loud { .pt-fake-h3 }

Read your code line by line, out loud, saying in plain English what each line does and why. This is often called **rubber duck debugging**: putting each line into words forces you to state assumptions you'd otherwise skim past while reading silently. 

```python-ref
if length < 1 and length > 20:               # "If length is under 1 and length is over 20..." 
    print("that length doesn't look right")  # "impossible condition, should use `or` instead of `and`!"
```

#### Print debugging { .pt-fake-h3 }

```python-ref
print(type(length), length)   # confirm what a value actually is, not what you assumed it was
```

Sprinkle `print()` calls between the lines you suspect, showing a variable's value (and [`type()`](types.md), if you're not sure) at that exact point in the run. This narrows down *where* your assumption about the code stopped matching reality — especially useful when nothing crashes and you're just staring at a wrong final answer, so there's no traceback pointing anywhere. Delete the `print()` calls once you've found the problem.

#### Isolate the problem { .pt-fake-h3 }

Comment out or delete sections of code until you find the smallest version that still shows the problem. Especially useful for syntax errors you can't obviously spot, since the pointer Python gives you isn't always exactly where the mistake is.

#### Flag as TODO/FIXME { .pt-fake-h3 }

```python-ref
# TODO: handle the case where length_ft is negative
length_ft = 4.5

# FIXME: math incorrect
def to_inches(length_ft):
    return length_ft * 10
```

Not every problem gets fixed the moment you spot it — sometimes you're mid-debugging something else and don't want to lose track of it. Marking a comment `TODO` creates a reminder for yourself to "come back to this." `FIXME` is the same idea for something you know is actively broken rather than just unfinished.

??? tip "Collecting TODO/FIXME comments in each editor"
    Some editors collect every `TODO`/`FIXME` in a project into one scannable list.

    === "PyCharm"

        Built-in TODO tool window (**View → Tool Windows → TODO**, or ++alt+6++) collects every `TODO`/`FIXME` in the project into one scannable list.

    === "VS Code"

        No built-in aggregator, but an extension like [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) adds one.

    === "Thonny"

        No built-in equivalent — it still works as a plain comment, just without an aggregated list.

    === "IDLE"

        No built-in equivalent — it still works as a plain comment, just without an aggregated list.

</div>

<div class="pfg-section" markdown="block">

### Debugger tool { .pt-fake-h2 }

A **debugger** is a tool built into most code editors that lets you pause a running program and look around, instead of only seeing what it printed after the fact. Pause your code mid-run to inspect what's happening and inspect variables — instead of only reading `print()` outputs at the end. 

0. **Set breakpoints.** A **breakpoint** marks a specific line where you want the program to pause while debugging, so you can inspect it. You can set as many as you want — set these *before* you start running. Click in the margin next to a line number to set one; click the same spot again to remove it — the red dot toggles off.
1. **Run in debug mode.** Look for a **"Debug"** button instead of the regular Run button. Your program will run normally until it hits the *first* breakpoint, then pauses there.
2. **Use the controls at a breakpoint.** Once paused, these controls move you through your code:

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

</div>

<div class="pfg-section" markdown="block">

### Detect errors with testing { .pt-fake-h2 }

A **test** is a small script that checks your code's behavior automatically, so the mistake gets caught the moment it's introduced.

```python-ref
def get_length(species, lengths):
    return lengths.get(species)

def test_missing_species_returns_none():
    lengths = {"ball python": 4.5, "burmese python": 12}
    assert get_length("reticulated python", lengths) is None
```

[pytest](libraries/pytest.md) is the standard tool for this in Python — a function starting with `test_` is one check, and inside it `assert` states what should be true. Running the file reports exactly which checks passed and which failed, the same way `python` reports which line of your code raised an error.

Tests are especially good at catching [logic errors](#logic-errors) — where the only way to notice something's wrong is comparing the actual output against what you expected. A test does that comparison automatically, instead of relying on you to notice by eye.

They're also useful for [runtime errors](#runtime-errors) — a test can exercise an edge case you wouldn't normally hit every time (an empty input, a missing key, a zero divisor), and `pytest.raises()` even lets you assert that a specific exception *should* fire, so you catch both "this crashes when it shouldn't" and "this doesn't crash when it should."

</div>

