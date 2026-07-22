# Python Field Guide

A hands-on reference for learning Python — run every example on this site without installing anything.

This is **NOT** a comprehensive guide, it was designed for entry-level programmers to have a quick reference guide when first learning to program Python. 

## What's inside

- **[Basic Data Types](basic_data_types.md)** — the scalar building blocks (`int`, `float`, `str`, `bool`) that hold a single value.
- **[Collections of Data](collections_of_data.md)** — `list`, `tuple`, `dict`, and `set`, for grouping multiple values together.
- **[Conditionals](conditionals.md)** — `if`/`elif`/`else` statements that run code only when a condition is `True`.
- **[Loops](loops.md)** — `for` and `while` loops for repeating a block of code.
- **[OOP](oop.md)** — classes and objects, for bundling data together with the behavior that belongs to it.
- **[Pillow](pillow.md)** — opening, editing, and saving image files.
- **[Tkinter](tkinter.md)** — Python's built-in toolkit for building desktop GUI applications.

## Try it yourself

```python
# run this code below
discoveries = ["write a comment"]
discoveries.append("create a list")

print("Field journal created.\n")
print("Explorer begins their first expedition into Python.\n")
discoveries.append("print console output")

print("Discoveries so far:")

discoveries.append("iterate through a list with a for loop")
discoveries.append("string concatenation")
for discovery in discoveries: 
    print("-\t"+discovery)
```

