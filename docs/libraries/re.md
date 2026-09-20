---
description: >-
  Regular expressions in Python with the re module: searching, extracting groups, replacing,
  and splitting text, with runnable examples.
---

# :material-regex:{ .lg .middle } re library

[re documentation :material-open-in-new:](https://docs.python.org/3/library/re.html){ .md-button target="_blank" }

The **`re`** module works with regular expressions — patterns that describe text to search for, extract, or replace, more flexible than plain string methods like `.find()` or `.replace()`.

<div class="pfg-section" markdown="block">

## Setup { data-card-link="skip" }

`re` ships with Python's standard library — nothing to install. The whole module is used through the `re.` prefix, so a plain import is all you need. Patterns are written as **raw strings** (`r"..."`), so a backslash like `\d` is passed straight to `re` instead of Python trying to interpret it as a string escape sequence first.

```python-ref
import re
```

| Function | Does | Returns |
|----------|------|---------|
| `search(pattern, text)` | Finds the first match anywhere in `text` | A `Match`, or `None` |
| `findall(pattern, text)` | Finds every match | A list of strings (or tuples, with groups) |
| `sub(pattern, repl, text)` | Replaces every match | A new string |
| `split(pattern, text)` | Splits `text` wherever the pattern matches | A list of strings |

| Pattern syntax | Matches |
|-----------------|---------|
| `\d` `\w` `\s` | A digit, a word character, whitespace |
| `.` | Any single character |
| `*` `+` `?` | 0 or more, 1 or more, 0 or 1 of the thing before it |
| `{n,m}` | Between `n` and `m` repeats |
| `[...]` | Any one character from the set |
| `^` `$` | Start, end of the text |
| `(...)` | A capturing group |

</div>

<div class="pfg-section" markdown="block">

## Searching for a pattern

`re.search()` scans the text and returns a `Match` object for the first hit, or `None` if the pattern never occurs. `.group()` reads the actual matched text back out of it.

```python-ref
import re

note = "the burmese python measured 12ft at last checkup"
match = re.search(r"\d+ft", note)

print(match.group())
```

??? tip "Reusing a pattern with re.compile"
    Compiling a pattern once with `re.compile()` and calling `.search()`/`.findall()`/etc. on the result is faster than passing the same pattern string to `re.*` repeatedly — worth it once a pattern is reused across many pieces of text.

    ```python-ref
    length_pattern = re.compile(r"\d+ft")
    length_pattern.search(note).group()    # "12ft"
    ```

??? efficiency "For efficiency, compile the pattern once with re.compile()"
    | | Compilation cost (over a loop of n calls) |
    |---|---|
    | Recompiled every pass | <span class="pt-bigo pt-bigo--ok">O(n)</span> |
    | Compiled once, reused | <span class="pt-bigo pt-bigo--good">O(1)</span> |

    Calling `re.search()` (or `.findall()`, `.sub()`, etc.) with a raw pattern string repeats the same compilation work internally on every call, even when the pattern never changes — across a loop of n calls, that's n compilations of the same pattern. Compiling it once with `re.compile()` above the loop and calling `.search()` on the result instead does that work exactly once, however many times the loop runs.

    See [Efficiency](../style.md#efficiency) for why this distinction matters.

??? run "Run a searching example"
    All the examples above, combined into one script:

    ```python
    import re

    note = "the burmese python measured 12ft at last checkup"
    match = re.search(r"\d+ft", note)

    print(match.group())

    import re

    length_pattern = re.compile(r"\d+ft")
    match = length_pattern.search(note)

    print(match.group())
    ```

</div>

<div class="pfg-section" markdown="block">

## Finding all matches

`re.findall()` returns every match in the text as a list, instead of stopping at the first one.

```python-ref
import re

notes = "ball: 4ft, burmese: 12ft, boa: 8ft"

print(re.findall(r"\d+ft", notes))
```

### Groups

Parentheses in a pattern mark a **capturing group** — a piece of the match to pull out on its own. With groups in the pattern, `findall()` returns a list of tuples, one tuple of group values per match, instead of a list of whole matches.

```python-ref
notes = "ball: 4ft, burmese: 12ft, boa: 8ft"
re.findall(r"(\w+): (\d+)ft", notes)    # [("ball", "4"), ("burmese", "12"), ("boa", "8")]
```

??? tip "Naming a group"
    `(?P<name>...)` gives a group a name instead of a position, so it can be read back with `.group("name")` on a `Match` — clearer than counting parentheses when a pattern has several groups.

    ```python-ref
    match = re.search(r"(?P<species>\w+): (?P<length>\d+)ft", notes)
    match.group("species")    # "ball"
    match.group("length")     # "4"
    ```

??? run "Run a finding all matches example"
    All the examples above, combined into one script:

    ```python
    import re

    notes = "ball: 4ft, burmese: 12ft, boa: 8ft"

    print(re.findall(r"\d+ft", notes))

    import re

    notes = "ball: 4ft, burmese: 12ft, boa: 8ft"
    print(re.findall(r"(\w+): (\d+)ft", notes))

    import re

    notes = "ball: 4ft, burmese: 12ft, boa: 8ft"
    match = re.search(r"(?P<species>\w+): (?P<length>\d+)ft", notes)

    print(match.group("species"), match.group("length"))
    ```

</div>

<div class="pfg-section" markdown="block">

## Replacing text

`re.sub()` replaces every match with a new string. `\1` in the replacement refers back to the first capturing group in the pattern, so part of each match can be kept while the rest changes.

```python-ref
import re

notes = "ball: 4ft, burmese: 12ft, boa: 8ft"

print(re.sub(r"(\d+)ft", r"\1 feet", notes))
```

??? run "Run a replacing text example"
    All the examples above, combined into one script:

    ```python
    import re

    notes = "ball: 4ft, burmese: 12ft, boa: 8ft"

    print(re.sub(r"(\d+)ft", r"\1 feet", notes))
    ```

</div>

<div class="pfg-section" markdown="block">

## Splitting on a pattern

`re.split()` breaks text apart wherever the pattern matches, similar to `str.split()` but able to split on more than one exact separator at once.

```python-ref
import re

species_list = "ball, burmese; boa,   blood"

print(re.split(r"[,;]\s*", species_list))
```

??? run "Run a splitting example"
    All the examples above, combined into one script:

    ```python
    import re

    species_list = "ball, burmese; boa,   blood"

    print(re.split(r"[,;]\s*", species_list))
    ```

</div>
