# :material-palette-outline:{ .lg .middle } Style

Code that works isn't automatically code that's easy to live with — following a shared set of conventions is what keeps a Python file manageable as it grows past a few lines.

- **Consistency** — code that follows the same conventions everywhere reads the same, no matter who wrote which part
- **Faster to learn** — a new file feels familiar instead of like starting over, since the same patterns keep repeating
- **Easier to debug** — a predictable layout means you already know where to look when something breaks
- **Easier for others to work with** — working on a collaborative project means others **review** your code before approving it and **merge** it in with everyone else's changes; consistent style means they can focus on what you actually changed, instead of different formatting choices

## Checklist

A few things worth double-checking before calling a script finished — each links to the full rule further down this page. Run a [linter](#linter-tool) first, since it catches most of this automatically; what's left afterward has to be checked by eye.

- [ ] **[Run a linter check](#linter-tool)** — catches many of the following automatically, but it can be good practice to check manually instead to get familiar with writing it correctly from the start:
    - [ ] **[File Order](#file-order)** — standardized file layout
    - [ ] **[Mutable default arguments](#common-patterns)** — a default list/dict shared across every call
    - [ ] **[`is None` instead of `== None`](#common-patterns)** — a real correctness risk, not just style
    - [ ] **[`with open(...)` instead of manual `open()`/`close()`](#common-patterns)** — avoids a file left open if something goes wrong
    - [ ] **[Catch specific exceptions](#catch-specific-exceptions)** — no bare `except:` swallowing errors you didn't expect
    - [ ] **[Naming](#naming)** — does every variable and function name say what it holds?
    - [ ] **[Docstrings](#docstrings)** — does every function and file explain what it does?
    - [ ] **[Truthy checks instead of `len(x) > 0`](#common-patterns)** — test a collection directly
    - [ ] **[`enumerate()` instead of `range(len(...))`](#common-patterns)** — loop with both index and item at once
    - [ ] **[Indentation](#indentation)** — 4 spaces per level, never tabs
    - [ ] **[Blank lines](#blank-lines)** — two around top-level functions/classes, one between methods
    - [ ] **[Whitespace](#whitespace)** — spaces around operators, but not around a keyword argument's `=`
    - [ ] **[Comments](#comments)** — two spaces before an inline `#`, one space after
- [ ] **[Keep functions focused](#keep-functions-focused)** — does each function do just one job, with no repeated logic a [linter](#linter-tool) won't flag on its own?
- [ ] **[Constants](#constants)** — are unchanging numbers pulled out into named `ALL_CAPS` values?
- [ ] **[Quote style](#quote-style)** — one quote style used consistently throughout the file
- [ ] **[Type hints](#type-hints)** — used on a function signature where the types aren't obvious?
- [ ] **[Tuple unpacking instead of a temporary variable](#common-patterns)** — swapping two variables directly
- [ ] **[File names](workspace.md#step-2-write-and-run-a-python-file)** — `snake_case.py`, no hyphens or spaces
- [ ] **[Readable print output](#readable-print-output)** — `\n`/`\t` and separator rows used to space out console output

## Linter tool

A **linter** is a tool that scans your code and flags issues like [PEP 8](#pep-8-style-guide), Python's official style guide, and [Pythonic](#pythonic-patterns) idioms automatically. It reads your file, checks it against its rule set, and prints a report: one line per violation, giving the file, line number, a rule code, and a short message. 

It can't catch a bug that only shows up when the code actually runs, since it never runs it. 

A **formatter** tool (either separate, or a combined linter+formatter), actually rewrites your file on its own fixing the errors. However, it can be helpful to manually fix the issues on your own, so you learn to write them correctly for next time.  

**Comparing different tools**

| Tool | Type | Best for |
|------|------|----------|
| PyCharm's built-in inspections | Linter | No setup needed — catches most PEP 8 violations and several Pythonic issues automatically |
| Pylint | Linter | Comprehensive checks — catches complex logical errors, not just formatting |
| Ruff | Linter & Formatter | Speed — large projects or CI pipelines where Pylint's speed becomes noticeable |
| Black | Formatter | Eliminating style debates entirely — rewrites the file to a consistent style automatically, instead of just flagging issues |

**Get started in your environment**

| Environment | Installing third party tools | Using a linter | Using a formatter |
|-------------|-----------------------------------|-----------------|--------------------|
| PyCharm | `Settings > Plugins >` tool name, then restart | Built-in inspections run automatically, no setup needed; plugins do too, once installed. Underlines issues, hover for full message. Full issue list in `View > Tool Windows > Problems`. | `Code > Format Code` |
| VS Code | `View > Extensions >` tool name | Underlines issues, hover for full message. Full issue list in `View > Problems`. | Trigger via `Format Document`, or set it as the default formatter in `settings.json` |
| Outside of an IDE | Send in terminal: `pip install` [tool name] | print report in the terminal:<ul><li>`pylint your_file.py`</li><li>`ruff check your_file.py`</li></ul> | rewrite the file directly:<ul><li>`black your_file.py`</li><li>`ruff format your_file.py`</li></ul>|

## PEP 8 Style Guide

[**PEP 8** is Python's official style guide](https://peps.python.org/pep-0008/) — a document written by Python's own core developers covering formatting, naming, and organizing code. "PEP" stands for Python Enhancement Proposal.

Python runs styled and unstyled code identically, so following PEP 8 doesn't make a script more *correct* — it makes it more *predictable* to read. Anyone who's used Python before recognizes the shape of PEP 8-styled code, so sticking to it means less friction reading someone else's code, and less friction when someone else reads yours.

### File Order

A Python file conventionally follows the same layout, top to bottom.[^order-pep8]

1. **Module docstring** — what the file does
2. **[Imports](modules.md#importing-modules)** — standard library, then third-party, then local
3. **Constants** — `ALL_CAPS` values used throughout the file
4. **Functions and classes** — the file's actual logic
5. **[The `if __name__ == "__main__":` guard](modules.md#the-main-guard)** — the code that runs when the file is executed

[^order-pep8]: The first three steps are PEP 8. Where functions/classes and the main guard fall isn't PEP 8 — but it is the convention the rest of the Python community has settled on.

```python-ref
"""
snake_survey.py

Tracks species and lengths recorded during the spring snake survey.

Author: Jordan Lee
Date: 2024-03-15
"""

import csv

MAX_TYPICAL_LENGTH_FT = 5

def is_unusually_long(length_ft):
    """Check whether a snake is unusually long for its species."""
    return length_ft > MAX_TYPICAL_LENGTH_FT

class Snake:
    """A single snake recorded during the survey."""

    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

if __name__ == "__main__":
    ball = Snake("ball python", 4.5)
    print(is_unusually_long(ball.length_ft))
```

### Naming

A variable name should say what it holds — `length_ft` over `l`, `species_list` over `data`. `snake_case` and the other naming rules are covered on the [Foundations](foundations.md#naming-variables) page; this is about picking a *meaningful* name within those rules, not just a valid one.

```python-ref
l = 4.5                # what is l?
length_ft = 4.5        # clear at a glance
```

A short name is fine when its scope is short too — `for s in species:` is common, since `s` only exists for the one line inside the loop.

### Constants

A **constant** is a variable whose value isn't meant to change while the program runs — written in `ALL_CAPS` by convention, so it's easy to tell apart from a regular variable at a glance. Defining one instead of repeating a raw number (a "magic number") gives that number a name explaining what it means.

```python-ref
if length_ft > 5:                    # what's special about 5?
    print("unusually long")

MAX_TYPICAL_LENGTH_FT = 5            # named once, explains itself
if length_ft > MAX_TYPICAL_LENGTH_FT:
    print("unusually long")
```

Constants are usually defined near the top of a file, so they're easy to find and adjust later — see [File Order](#file-order) above.

### Quote style

Python treats `'single'` and `"double"` quotes identically for strings — PEP 8 doesn't prefer one over the other, just pick one as your default and stick with it throughout a file, rather than mixing both without reason. (This site uses double quotes.) The one except&zwnj;ion: switch to the other quote character for a string that itself contains a quote, rather than escaping it with a backslash.

```python-ref
print("it's a ball python")    # no backslash needed
print('it\'s a ball python')   # works, but harder to read
```

### Docstrings

A triple-quoted string as the first line of a function or a file documents what it does — the underlying trick is the same [multi-line comment](foundations.md#multi-line-comments-with) covered on Foundations, just placed specifically as the first line.

```python-ref
def is_unusually_long(length_ft):
    """Check whether a snake is unusually long for its species."""
    return length_ft > 5
```

For a function whose parameters or return value need explaining, spell them out with a standard `Args`/`Returns` format instead of a one-line summary:

```python-ref
def is_unusually_long(species, length_ft):
    """
    Check whether a snake is unusually long for its species.

    Args:
        species (str): the snake's species name.
        length_ft (float): the snake's measured length, in feet.

    Returns:
        bool: True if length_ft is unusually long for species.
    """
    return length_ft > 5
```

Full rules on the [Functions](functions.md#docstrings) page.

Placed as the very first line of a file instead, the same trick becomes a **module docstring** — documenting the file as a whole rather than a single function, and a common place to note who wrote it and when.

```python-ref
"""
snake_survey.py

Tracks species and lengths recorded during the spring snake survey.

Author: Jordan Lee
Date: 2024-03-15
"""

species = "ball python"
length_ft = 4.5
```

### Indentation

Python uses indentation, not braces, to mark a block — PEP 8's rule is 4 spaces per level, never tabs (mixing the two causes real errors, not just style complaints).

```python-ref
def describe(species):
  return f"a {species} python"      # 2 spaces — works, but not PEP 8

def describe(species):
    return f"a {species} python"    # 4 spaces — PEP 8
```

### Blank lines

Two blank lines separate top-level function and class definitions; one blank line separates methods inside a class.

```python-ref
def parse_entry(text):
    ...
def save_entry(entry):    # only one blank line — not PEP 8
    ...


def parse_entry(text):
    ...


def save_entry(entry):    # two blank lines — PEP 8
    ...
```

### Whitespace

Put a single space around most operators (`=`, `==`, `+`, `>`), but drop it around `=` when it's a keyword argument rather than an assignment.

```python-ref
length_ft=4.5                              # missing spaces — not PEP 8
length_ft = 4.5                            # PEP 8

def describe(species, length_ft = 4.5):    # spaces around a keyword default — not PEP 8
    ...

def describe(species, length_ft=4.5):      # PEP 8
    ...
```

### Comments

An inline comment needs at least two spaces before the `#` and one space after it; a block comment on its own line follows the same one-space-after rule.

```python-ref
length_ft = 4.5 #too short         # not PEP 8 — no spacing
length_ft = 4.5  # too short       # PEP 8 — two spaces before, one after

#check length                      # not PEP 8
# check length                     # PEP 8
```

## Pythonic patterns

**Pythonic** code uses Python's own built-in features and standard patterns, instead of verbose work arounds. 

There's no single tool that reliably flags all "unpythonic" code the way PEP 8 has a document to check against. The real habit is asking *"does Python already have a built-in way to do this?"* before writing a manual loop, counter, or flag — an instinct built over time to recognize the built-in pattern.

Other programming langues have different features and patterns, so if code is translated from another langauge into Python it might not be written very clearly. Pythonic code tends to be less buggy and faster.

### Common patterns

A few of these a beginner tends to write out longhand before learning the built-in shortcut, roughly most to least common:

- **Truthy checks instead of `len(x) > 0`** — test a collection directly; a non-empty list is already truthy

    ```python-ref
    if len(species) > 0:    # works, but not Pythonic
        print("found some")

    if species:              # Pythonic — a non-empty list is already truthy
        print("found some")
    ```

- **`enumerate()` instead of `range(len(...))`** — loop with both the index and the item at once, instead of indexing into the list by hand

    ```python-ref
    for i in range(len(species)):        # manual indexing
        print(i, species[i])

    for i, s in enumerate(species):      # Pythonic — enumerate() hands back both
        print(i, s)
    ```

- **`with open(...)` instead of a manual `open()`/`close()` pair** — a context manager guarantees the file gets closed even if something goes wrong partway through

    ```python-ref
    file = open("notes.txt")           # works, but there's a risk of locking the file in a buffer
    contents = file.read()
    file.close()

    with open("notes.txt") as file:    # Pythonic — closes automatically, even on error
        contents = file.read()
    ```

- **`is None` instead of `== None`** — checking against `None` is a check of identity, not equality, so `is` is the correct tool

    ```python-ref
    length_ft = None
    if length_ft == None:                # works, but not Pythonic
        print("unknown length")

    if length_ft is None:                # Pythonic — `is` is the correct tool for a None check
        print("unknown length")
    ```

- **Avoid mutable default arguments** — a default list or dict is created once, when the function is defined, and reused across every call — so items appended in one call are still there the next time, unless the default is `None` instead

    ```python-ref
    def add_snake(species, tracked=[]):     # works, but tracked is shared across every call
        tracked.append(species)
        return tracked

    def add_snake(species, tracked=None):   # Pythonic — a fresh list every call
        if tracked is None:
            tracked = []
        tracked.append(species)
        return tracked
    ```

- **Tuple unpacking instead of a temporary variable** — swap two variables directly, rather than juggling a spare variable to hold one during the swap

    ```python-ref
    a, b = "ball python", "boa"
    temp = a                             # manual swap using a spare variable
    a = b
    b = temp

    a, b = b, a                          # Pythonic — tuple unpacking swaps directly
    ```

## Additional best practices

### Keep functions focused

A function should do one thing. If you find yourself describing it with "and" — "parses the input *and* saves it *and* prints a summary" — it's probably three functions.

```python-ref
def parse_and_save(text):    # doing too much
    ...

def parse_entry(text):       # one job each
    ...

def save_entry(entry):
    ...
```

Repeating the same few lines in multiple places is a sign to pull them into their own function instead — commonly called **DRY** ("don't repeat yourself"). It also means a fix only has to happen in one place, instead of every place the lines were copied to.

??? tip "Guard clauses: return early instead of nesting"
    Handle the exception case first and return, rather than wrapping the rest of the function in an `else`. It keeps the normal path at the lowest indentation level, instead of nested one level deeper for every added check.

    ```python-ref
    def describe(length_ft):
        if length_ft > 0:
            return f"{length_ft} ft"
        else:
            return "unknown length"
    ```

    ```python-ref
    def describe(length_ft):
        if length_ft <= 0:
            return "unknown length"
        return f"{length_ft} ft"
    ```

    Both versions do the same thing — the second reads top to bottom without having to track which `if` branch you're inside.

### Catch specific exceptions

Catch the exact exception you expect (`except ValueError:`) instead of a bare `except:` — a bare `except` also silently swallows errors you didn't anticipate, including a typo in your own code, and even catches things like a keyboard interrupt (++ctrl+c++) that usually shouldn't be caught at all. Full `try`/`except` mechanics are covered on the [Errors](errors.md#handling-errors) page.

```python-ref
try:
    length_ft = float(user_input)
except:                    # catches everything, even mistakes you didn't expect
    print("invalid input")

try:
    length_ft = float(user_input)
except ValueError:         # only catches what you actually expect
    print("invalid input")
```

### Type hints

A **type hint** annotates a parameter or return value with the type it's expected to be — `species: str`, `length_ft: float`, `-> bool` — without Python enforcing it at runtime; it's documentation an editor or a separate type checker (like `mypy`) can check for you.

```python-ref
def is_unusually_long(species: str, length_ft: float) -> bool:
    return length_ft > 5
```

A wrong type still runs — Python doesn't stop you from calling `is_unusually_long("ball python", "4.5")` with a string instead of a `float` — the hint only helps a tool catch the mismatch before you do, and helps a reader (or their editor) see what's expected without reading the function body.

### Readable print output

`\n` and `\t` are **escape sequences** — `\n` inserts a line break, `\t` a tab — so a single `print()` call can space out multi-line or columned output.

```python
print(f"species: burmese\nlength: 10 ft\n")
print("species\t\tlength_ft")
print("ball python\t4.5")
```

A row of repeated characters makes a quick visual separator between sections of console output, useful for breaking up a long script's output into readable chunks.

```python
print("survey results")
print("=" * 40)
```

??? tip "Be creative with ASCII art"
    Write in the terminal with bubble letters or draw images through creative character use.

    ```bash
    ============================
                                    ,----,                                       
    ,-.----.                      ,/   .`|       ,--,    ,----..            ,--. 
    \    /  \                   ,`   .'  :     ,--.'|   /   /   \         ,--.'| 
    |   :    \         ,---,  ;    ;     /  ,--,  | :  /   .     :    ,--,:  : | 
    |   |  .\ :       /_ ./|.'___,/    ,',---.'|  : ' .   /   ;.  \,`--.'`|  ' : 
    .   :  |: | ,---, |  ' :|    :     | |   | : _' |.   ;   /  ` ;|   :  :  | | 
    |   |   \ :/___/ \.  : |;    |.';  ; :   : |.'  |;   |  ; \ ; |:   |   \ | : 
    |   : .   / .  \  \ ,' '`----'  |  | |   ' '  ; :|   :  | ; | '|   : '  '; | 
    ;   | |`-'   \  ;  `  ,'    '   :  ; '   |  .'. |.   |  ' ' ' :'   ' ;.    ; 
    |   | ;       \  \    '     |   |  ' |   | :  | ''   ;  \; /  ||   | | \   | 
    :   ' |        '  \   |     '   :  | '   : |  : ; \   \  ',  / '   : |  ; .' 
    :   : :         \  ;  ;     ;   |.'  |   | '  ,/   ;   :    /  |   | '`--'   
    |   | :          :  \  \    '---'    ;   : ;--'     \   \ .'   '   : |       
    `---'.|           \  ' ;             |   ,/          `---`     ;   |.'       
    `---`            `--`              '---'                     '---'         
    ============================
    Welcome to the program!
    Press Enter:
    ```

    [ascii text resource](https://patorjk.com/software/taag/#p=display&f=Isometric1&t=Type+Something+&x=none&v=4&h=4&w=80&we=false)

    [ascii art resource](https://www.asciiart.eu/#google_vignette)