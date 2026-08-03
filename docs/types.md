# :material-shape-outline:{ .lg .middle } Basic data types

Every value in Python has a **type**, which determines what operations it supports and how it behaves — Python figures this out from the value itself, since you never declare a type explicitly. A basic (or "scalar") data type holds a single, indivisible value, as opposed to a [collection](collections.md), which groups many values together. The basic types are also all **immutable**: once created, the value itself can never be changed in place — only replaced with a different value.

| Type | Example | Use it for |
|------|---------|------------|
| `int` | `5` | <ul><li>Counts — how many of something there are, like items in a list</li><li>Indexes — the position of an item in a sequence, like `species[2]`</li><li>IDs — a unique whole-number identifier, like a user or record ID</li></ul> |
| `float` | `4.5` | <ul><li>Measurements, ratios — anything with a decimal</li><li>Binary rounding errors mean `0.1 + 0.2 != 0.3`</li></ul> |
| `str` | `"ball python"` | <ul><li>Text — names, labels, messages</li><li>Ordered and indexable like a list, but immutable — `.upper()`, `.replace()`, etc. return a *new* string</li></ul> |
| `bool` | `True` | <ul><li>Flags, yes/no switches, comparison results (`length > 3`)</li><li>Secretly a subclass of `int` — `True + True == 2`</li></ul> |
| `None` | `None` | <ul><li>Marking "no value yet" — a default placeholder, or what a function returns if it falls through without a `return`</li><li>Compare with `is None`, not `== None`</li><li>`not thing` also catches `None`, but it's true for any falsy value (`0`, `""`, `[]`) too — use `is None` when you mean *specifically* "no value"</li></ul> |

??? tip "Check any variable's type"
    If you're not sure what type a value is — because it came from user input, a function's return value, or somewhere else you didn't set it yourself — you can ask Python directly instead of guessing. `type()` shows the exact type; `isinstance()` checks whether a value is that type, and also matches a subclass, which is usually why it's the better choice inside an `if`. Works the same way for any type on this page.

    ```python-ref
    type(5)              # <class 'int'>
    isinstance(5, int)   # True
    ```

??? note "Any type can act as True ("truthy") or False ("falsy")"
    You'll often see code like `if my_list:` instead of `if len(my_list) > 0:` — that works because Python doesn't require an `if` condition to actually be a `bool`. Every value counts as either "truthy" or "falsy" when used somewhere a `bool` is expected, not just actual `True`/`False` values.

    ```python-ref
    bool(0)       # False
    bool("")      # False
    bool([])      # False
    bool(None)    # False
    bool("ball")  # True
    bool(5)       # True
    ```

    Zero, empty strings, empty collections, and `None` are all falsy; almost everything else — including any non-empty string or nonzero number — is truthy.

## Integers

An integer (`int`) is a whole number — positive, negative, or zero — with no decimal point.

```python-ref
length = 5
```

### Arithmetic

The standard math operators, with one that surprises beginners: `/` always returns a float. `/` (true division) always returns a `float`, even when the numbers divide evenly — use `//` (floor division) if you want an `int` result.

```python-ref
length + 3     # 8
length - 2     # 3
length * 2     # 10
length / 2     # 2.5  (/ always returns a float)
length // 2    # 2    (floor division — drops the remainder)
length % 2     # 1    (modulo — the remainder)
length ** 2    # 25   (exponent)
```

### Convert to integer

`int()` converts a string of digits, or truncates a float toward zero. It cuts off the decimal — it does not round.

```python-ref
int("5")      # 5
int(5.9)      # 5   (cuts off decimal, doesn't round)
int(True)     # 1
```

??? run "Run an integer example"
    All the examples above, combined into one script:

    ```python
    length = 5

    print(length + 3)
    print(length - 2)
    print(length * 2)
    print(length / 2)
    print(length // 2)
    print(length % 2)
    print(length ** 2)

    print(int("5"))
    print(int(5.9))
    print(int(True))
    ```

## Floats

A float is a number with a decimal point — for anything that isn't a whole number.

```python-ref
weight = 4.5
weight    # 4.5
```

### Arithmetic

Floats support the same operators as integers. Notably, `/` always returns a `float` — even `10 / 2`, which divides evenly, gives `5.0`, not `5`.

```python-ref
weight + 1.5    # 6.0
weight / 2      # 2.25
10 / 2          # 5.0  (still a float, even though it divides evenly)
```

### Rounding

`round()` rounds to the nearest whole number, or to a given number of decimal places. With no second argument it rounds to the nearest whole number — but Python uses "round half to even" (banker's rounding), so `round(4.5)` is `4`, not `5`. Pass a second argument to round to that many decimal places instead.

```python-ref
round(weight)         # 4  (Python rounds .5 to the nearest *even* number)
round(4.567, 2)        # 4.57
```

### Convert to float

`float()` converts an integer or a numeric string into a float.

```python-ref
float(5)         # 5.0
float("4.5")      # 4.5
```

??? warning "Floating-point precision"
    Tiny rounding errors creep in, since most decimal fractions can't be stored exactly in binary.

    ```python-ref
    0.1 + 0.2    # 0.30000000000000004
    ```

    This is a property of floating-point math in virtually every programming language, not a Python bug. If you need exact decimal arithmetic (for money, for example), use the `decimal` module instead of `float`.

??? run "Run a float example"
    All the examples above, combined into one script:

    ```python
    weight = 4.5

    print(weight + 1.5)
    print(weight / 2)
    print(10 / 2)

    print(round(weight))
    print(round(4.567, 2))

    print(float(5))
    print(float("4.5"))

    print(0.1 + 0.2)
    print(round(0.1 + 0.2, 2))
    ```

## Strings

A string stores text — a sequence of characters — inside a single variable.

Strings have three defining traits:

- **Ordered** — characters keep the position they're written in.
- **Immutable** — unlike a list, a string can't be changed in place; every "modification" actually builds a new string.
- **Indexable** — since a string is a sequence, it supports the same `[]` indexing and slicing as a list.

```python-ref
name = "burmese python"
name    # "burmese python"
```

### Access characters

Strings use the same index and slice syntax as lists. `0` is the first character, negative indexes count from the end, and `start:end` slices out a substring.

```python-ref
name[0]      # "b"
name[-1]     # "n"
name[0:7]    # "burmese"
```

### Concatenate & repeat

`+` joins strings end to end; `*` repeats a string a given number of times.

```python-ref
"ball" + " " + "python"    # "ball python"
"ball" * 3                  # "ballballball"
```

### Format strings

An f-string lets you embed variables directly inside `{}`. An f-string is a string literal prefixed with `f`, and it can embed expressions too, without manually joining pieces with `+`.

```python-ref
f"the {species} python is about {length} feet long"    # "the ball python is about 5 feet long"
```

### Comma, +, or f-string?

Three ways to combine text and values — each fits a different situation.

| Method | Example | Use it for |
|--------|---------|------------|
| `,` in `print()` | `print(species, length_ft)` | Quickly displaying values on one line — no separate string is created |
| `+` | `species + " python"` | Building an actual string value to store or reuse — every piece must already be a string |
| f-string | `f"{species} is {length_ft} ft"` | Embedding variables inside a sentence — converts values to strings automatically |

`,` only works inside `print()` (or similar functions) — it can't be saved to a variable, since it isn't actually building a string, just printing several values side by side. `+` builds a real string you can store, but every piece must already be text — `species + length_ft` raises a `TypeError` since `length_ft` is a number, not a string, and needs `str(length_ft)` first. An f-string sidesteps that entirely, converting values to text automatically, which is why it's usually the clearest choice once a sentence has more than one or two variables in it.

### Modify strings

Since strings are immutable, these all return a **new** string rather than changing the original. `upper()`, `lower()`, and `title()` change letter case. `strip()` removes leading and trailing whitespace. `replace()` swaps every occurrence of one substring for another.

```python-ref
name.upper()          # "BURMESE PYTHON"
name.title()          # "Burmese Python"
"  ball  ".strip()    # "ball"
name.replace("burmese", "ball")   # "ball python"
```

### Split & join

`split()` breaks a string into a list; `join()` glues a list of strings back together. `split()` uses whitespace as the separator by default. `join()` uses the string it's called on as the separator between each item.

```python-ref
name.split()                          # ["burmese", "python"]
"-".join(["burmese", "python"])       # "burmese-python"
```

### Check substring

`in` checks whether one string contains another. `find()` returns the index where a substring first appears, or `-1` if it's not found. `count()` counts how many times a substring appears.

```python-ref
"python" in name          # True
name.find("python")       # 8
name.count("p")           # 1
```

### Convert to string

`str()` converts almost any value into its text representation. Handy any time you need to combine a number with text, since `+` can't join a string and a number directly.

```python-ref
str(5)      # "5"
str(4.5)    # "4.5"
str(True)   # "True"
```

??? run "Run a string example"
    All the examples above, combined into one script:

    ```python
    name = "burmese python"

    print(name[0])
    print(name[-1])
    print(name[0:7])
    print(name[8:])

    species = "ball"
    name = species + " " + "python"
    print(name)

    print(species * 3)

    species = "ball"
    length = 5
    sentence = f"the {species} python is about {length} feet long"
    print(sentence)

    species = "ball"
    length_ft = 4.5

    print(species, length_ft)                    # comma — fine for a quick printout

    name = species + " " + str(length_ft)         # + — needs str() to include a number
    print(name)

    print(f"{species} is {length_ft} ft")         # f-string — no manual conversion needed

    name = "burmese python"

    print(name.upper())
    print(name.title())

    padded = "  ball python  "
    print(padded.strip())

    print(name.replace("burmese", "ball"))

    name = "burmese python"
    parts = name.split()
    print(parts)

    rejoined = "-".join(parts)
    print(rejoined)

    name = "burmese python"

    print("python" in name)
    print("cobra" in name)

    print(name.find("python"))
    print(name.count("p"))

    print(str(5))
    print(str(4.5))
    print(str(True))
    ```

## Booleans

A boolean (`bool`) holds one of exactly two values, `True` or `False` — used to represent yes/no, on/off, or the result of a comparison.

```python-ref
venomous = False
venomous    # False
```

### Comparisons return booleans

Every comparison operator evaluates to a `bool`. `>`, `<`, `>=`, `<=`, `==`, `!=` — this is what powers every `if` statement.

```python-ref
length = 5
length > 3     # True
length == 5    # True
length != 5    # False
```

### Combine booleans

`and`, `or`, and `not` combine or invert boolean values. `and` is `True` only if both sides are; `or` is `True` if either side is; `not` flips a boolean.

```python-ref
is_python and is_venomous    # True and False → False
is_python or is_venomous     # True or False  → True
not is_venomous              # not False      → True
```

??? note "Bool is a subclass of int"
    `True` behaves like `1` and `False` behaves like `0` in arithmetic.

    ```python-ref
    isinstance(True, int)    # True
    True + True               # 2
    ```

    `bool` is technically a subclass of `int`, though it's rare to rely on this on purpose.

??? run "Run a boolean example"
    All the examples above, combined into one script:

    ```python
    length = 5

    print(length > 3)
    print(length == 5)
    print(length != 5)

    is_python = True
    is_venomous = False

    print(is_python and is_venomous)
    print(is_python or is_venomous)
    print(not is_venomous)

    print(isinstance(True, int))
    print(True + True)
    ```

## None

`None` represents the absence of a value — Python's way of saying "nothing here," distinct from `0`, `False`, or an empty string.

```python-ref
venomous = None
venomous    # None
```

### Check for None

Always compare to `None` with `is` / `is not`, not `==` / `!=`. `is` checks that it's the *exact same object*, which is what you want for a singleton value like `None`.

```python-ref
venomous is None        # True
venomous is not None    # False
```

### Functions return None by default

If a function runs to the end without hitting a `return` statement, it returns `None` automatically. This is what you get back if a lookup silently "doesn't find" anything.

```python-ref
result = find_species("cobra")    # None — the function fell through without a return
```

??? run "Run a None example"
    All the examples above, combined into one script:

    ```python
    venomous = None

    print(venomous is None)
    print(venomous is not None)

    def find_species(name):
        if name == "ball":
            return "found it"
        # falls through here for anything else — implicitly returns None

    result = find_species("cobra")
    print(result)
    print(result is None)
    ```
