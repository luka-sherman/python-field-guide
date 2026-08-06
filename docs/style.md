# :material-palette-outline:{ .lg .middle } Style

Code that works isn't automatically code that's easy to read, debug, or hand off to someone else — these conventions are about writing Python that stays clear as a file grows past a few lines.

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

## Imports

Imports go at the very top of the file, grouped in order: Python's own standard library first, then third-party packages, then your own local files — with a blank line between each group.

```python-ref
import random                    # standard library

import requests                  # third-party — installed separately

import snake_data                # your own file
```

Avoid `from module import *` — it pulls in every name from that module without saying which ones, so it's unclear later where a given name actually came from.

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

Covered in full on the [Foundations](foundations.md#multiline-comments-with) page — a triple-quoted string as the first line of a function, class, or file, documenting what it does.

## Main function

`if __name__ == "__main__":` controls what runs only when a file is executed directly — not when it's imported into another file.

```python-ref
def describe(species):
    return f"a {species} python"

if __name__ == "__main__":
    print(describe("ball"))
```

`__name__` is a variable Python sets automatically: `"__main__"` when the file is run directly, or the file's own module name when it's imported elsewhere instead. Wrapping your "do the actual work" code in this check means another file can `import` yours — to reuse a function, say — without that code running as a side effect.

## Order

A Python file conventionally follows the same layout, top to bottom:

1. **Module docstring** — what the file does
2. **Imports** — standard library, then third-party, then local
3. **Constants** — `ALL_CAPS` values used throughout the file
4. **Functions and classes** — the file's actual logic
5. **The `if __name__ == "__main__":` guard** — the code that runs when the file is executed

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

Not every file needs every piece — a short script might skip constants or classes entirely — but when a piece is present, this is the order readers expect to find it in.
