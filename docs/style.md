# :material-palette-outline:{ .lg .middle } Style

Code that works isn't automatically code that's easy to read, debug, or hand off to someone else — these conventions are about writing Python that stays clear as a file grows past a few lines.

## PEP 8

**PEP 8** is Python's official style guide — a document written by Python's own core developers covering formatting, naming, and organizing code. ("PEP" stands for Python Enhancement Proposal, the same process used to propose changes to the language itself.) Several of the conventions on this page — naming, quote style, import order — come directly from it.

Python runs styled and unstyled code identically, so following PEP 8 doesn't make a script more *correct* — it makes it more *predictable* to read. Anyone who's used Python before recognizes the shape of PEP 8-styled code, so sticking to it means less friction reading someone else's code, and less friction when someone else reads yours.

PEP 8 itself is just a document — it doesn't check anything on its own. A **linter** like Pylint is a separate tool that actively scans your code against it, catching style violations, likely bugs, and structural issues automatically instead of you having to spot them by eye.

| Editor | PEP 8 checking |
|--------|-----------------|
| PyCharm Community | Built in — violations are underlined automatically, no setup needed |
| VS Code | Install the *Pylint* extension |
| Thonny | No built-in PEP 8 checking |
| IDLE | No built-in PEP 8 checking |

??? info "What does "Pythonic" mean?"
    Using Python's own built-in features and standard patterns, instead of writing code that just works but reads like it was translated from another language. Two pieces of code can do the exact same thing while only one is Pythonic.

    ```python-ref
    if len(species) > 0:    # works, but not Pythonic
        print("found some")

    if species:              # Pythonic — a non-empty list is already truthy
        print("found some")
    ```

    It's worth the effort for real reasons, not just to match convention:

    - **Readable** — other Python developers recognize the pattern instantly, without having to puzzle through it
    - **Fewer bugs** — the standard way is usually the safest way; `with open(...)` guarantees a file gets closed even if something goes wrong, where a manual `open()`/`close()` pair is easy to get wrong
    - **Faster** — built-in patterns like comprehensions are implemented in C under the hood, quicker than the hand-written equivalent
    - **Works with the language, not against it** — instead of carrying over patterns from another language that Python already has a built-in way of doing

## Naming

A variable name should say what it holds — `length_ft` over `l`, `species_list` over `data`. `snake_case` and the other naming rules are covered on the [Foundations](foundations.md#naming-variables) page; this is about picking a *meaningful* name within those rules, not just a valid one.

```python-ref
l = 4.5                # what is l?
length_ft = 4.5        # clear at a glance
```

A short name is fine when its scope is short too — `for s in species:` is common, since `s` only exists for the one line inside the loop.

## Constants

A **constant** is a variable whose value isn't meant to change while the program runs — written in `ALL_CAPS` by convention, so it's easy to tell apart from a regular variable at a glance. Defining one instead of repeating a raw number (a "magic number") gives that number a name explaining what it means.

```python-ref
if length_ft > 5:                    # what's special about 5?
    print("unusually long")

MAX_TYPICAL_LENGTH_FT = 5            # named once, explains itself
if length_ft > MAX_TYPICAL_LENGTH_FT:
    print("unusually long")
```

Constants are usually defined near the top of a file, so they're easy to find and adjust later — see [Order](#order) below.

## Keep functions focused

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

## Comprehensions vs. loops

A comprehension can replace a short loop that just builds a new list, but it's a readability trade — reach for a regular `for` loop instead once the logic doesn't fit comfortably on one line.

```python-ref
lengths = []
for s in species:
    lengths.append(len(s))

lengths = [len(s) for s in species]    # same result, one line
```

## Quote style

Python treats `'single'` and `"double"` quotes identically for strings — pick one as your default and stick with it throughout a file, rather than mixing both without reason. (This site uses double quotes.)

## Docstrings

A triple-quoted string as the first line of a function or a file documents what it does — the underlying trick is the same [multi-line comment](foundations.md#multi-line-comments-with) covered on Foundations, just placed specifically as the first line. Function docstrings are covered on the [Functions](functions.md#docstrings) page.

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

??? tip "ASCII art in comments"
    A comment doesn't have to be plain text — a small banner or diagram can make a long file easier to scan, or sketch out something a sentence can't easily convey.

    ```python-ref
    """
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
    """
    def describe(species):
        ...
    ```

    Handy for marking the major sections of a long file, or roughing out a small diagram (a tree, a grid, a state machine) that's genuinely clearer drawn than described. Keep it small and easy to update, though — an elaborate piece of ASCII art goes stale the moment the code around it changes, turning into more comment to maintain than value it adds.

    [ascii text](https://patorjk.com/software/taag/#p=display&f=Isometric1&t=Type+Something+&x=none&v=4&h=4&w=80&we=false)
    [ascii art](https://www.asciiart.eu/#google_vignette)

## Order

A Python file conventionally follows the same layout, top to bottom:

1. **Module docstring** — what the file does
2. **[Imports](modules.md#importing-libraries)** — standard library, then third-party, then local
3. **Constants** — `ALL_CAPS` values used throughout the file
4. **Functions and classes** — the file's actual logic
5. **[The `if __name__ == "__main__":` guard](modules.md#the-main-guard)** — the code that runs when the file is executed

```python-ref
"""
snake_survey.py

Tracks species and lengths recorded during the spring snake survey.
"""

import csv

MAX_TYPICAL_LENGTH_FT = 5

def is_unusually_long(length_ft):
    return length_ft > MAX_TYPICAL_LENGTH_FT

class Snake:
    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

if __name__ == "__main__":
    ball = Snake("ball python", 4.5)
    print(is_unusually_long(ball.length_ft))
```

## Checklist

A few things worth double-checking before calling a script finished:

- **Function docstrings** — does every function explain what it does? Full rules on the [Functions](functions.md#docstrings) page.
- **Variable and function names** — meaningful, specific, `snake_case` format. Full rules on the [Foundations](foundations.md#naming-variables) page.
- **File names** — `snake_case.py`, no hyphens or spaces. Full rules on the [Workspace](workspace.md#step-2-write-and-run-a-python-file) page.

Not every file needs every piece — a short script might skip constants or classes entirely — but when a piece is present, this is the order readers expect to find it in.
