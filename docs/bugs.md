# Bugs

Something's not working — this page covers every tool for figuring out why, whether Python threw an error at you or your code just quietly did the wrong thing.

## Reading errors

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Reading a traceback

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

## Handling errors

`try`/`except` lets your program handle an error instead of crashing — attempt some code in `try`, and if it fails, run the code in `except` instead.

```python
lengths = {"ball python": 4.5, "burmese python": 12}

try:
    print(lengths["reticulated python"])
except KeyError:
    print("no length on record for that species")
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Common exception types

The name in the traceback's last line tells you which of these went wrong.
{: .pt-subheading }

| Exception | Happens when |
|-----------|---------------|
| `NameError` | Using a variable that hasn't been assigned yet |
| `TypeError` | Using a value the wrong way for its type, like adding a string and a number |
| `ValueError` | The type is right, but the value doesn't make sense, like `int("banana")` |
| `KeyError` | Looking up a dict key that doesn't exist |
| `IndexError` | Looking up a list index that doesn't exist |
| `ZeroDivisionError` | Dividing by zero |

</summary>

Matching `except` to a specific exception type (rather than catching everything) means your program only handles the failure you actually expected, and still crashes loudly on a genuine bug — which is usually what you want while learning.

```python
try:
    length = int("banana")
except ValueError:
    print("that's not a valid number")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("can't divide by zero")
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Catching multiple exception types

List several exception types in one `except` to handle them the same way.
{: .pt-subheading }

```python-ref
try:
    print(lengths[species])
except (KeyError, TypeError):
    print("couldn't look up that species")
```

</summary>

Separate `except` blocks work too, if each error type needs different handling — Python checks them top to bottom and runs the first one that matches.

```python
lengths = {"ball python": 4.5, "burmese python": 12}
species = "reticulated python"

try:
    print(lengths[species])
except KeyError:
    print("no length on record for that species")
except TypeError:
    print("species should be text, not a number")
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### else and finally

`else` runs only if `try` succeeded; `finally` always runs, whether it succeeded or not.
{: .pt-subheading }

```python-ref
try:
    length = lengths[species]
except KeyError:
    print("no length on record")
else:
    print(f"found it: {length} ft")
finally:
    print("lookup attempt finished")
```

</summary>

`else` is a good place for code that should only run after a successful `try`, without risking it accidentally triggering the `except` block itself. `finally` is for cleanup that has to happen either way, like closing a file — it runs even if the `try` block succeeded, failed, or the `except` block itself raised a new error.

```python
lengths = {"ball python": 4.5, "burmese python": 12}
species = "ball python"

try:
    length = lengths[species]
except KeyError:
    print("no length on record")
else:
    print(f"found it: {length} ft")
finally:
    print("lookup attempt finished")
```

</details>

## Debugging

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Using a debugger

Pause your code mid-run to inspect what's happening and inspect variables — instead of only reading `print()` outputs at the end. 
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
