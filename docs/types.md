# :material-shape-outline:{ .lg .middle } Basic data types

Every value in Python has a **type**, which determines what operations it supports and how it behaves — Python figures this out from the value itself, since you never declare a type explicitly. A basic (or "scalar") data type holds a single, indivisible value, as opposed to a [collection](collections.md), which groups many values together. The basic types are also all **immutable**: once created, the value itself can never be changed in place — only replaced with a different value.

<div class="pt-jump-table" markdown="block">

| Type | Example | Use it for |
|------|---------|------------|
| <a href="#integers">**`int`**</a> | `5` | <ul><li>Counts — how many of something there are, like items in a list</li><li>Indexes — the position of an item in a sequence, like `species[2]`</li><li>IDs — a unique whole-number identifier, like a user or record ID</li></ul> |
| <a href="#floats">**`float`**</a> | `4.5` | <ul><li>Measurements, ratios — anything with a decimal</li><li>Binary rounding errors mean `0.1 + 0.2 != 0.3`</li></ul> |
| <a href="#strings">**`str`**</a> | `"ball python"` | <ul><li>Text — names, labels, messages</li><li>Ordered and indexable like a list, but immutable — `.upper()`, `.replace()`, etc. return a *new* string</li></ul> |
| <a href="#booleans">**`bool`**</a> | `True` | <ul><li>Flags, yes/no switches, comparison results (`length > 3`)</li><li>Secretly a subclass of `int` — `True + True == 2`</li></ul> |
| <a href="#none">**`None`**</a> | `None` | <ul><li>Marking "no value yet" — a default placeholder, or what a function returns if it falls through without a `return`</li><li>Compare with `is None`, not `== None`</li><li>`not thing` also catches `None`, but it's true for any falsy value (`0`, `""`, `[]`) too — use `is None` when you mean *specifically* "no value"</li></ul> |

</div>

??? tip "Check what type a variable is"

    `type()` shows the data type
    
    `isinstance()` checks whether a value is that type.

    ```python-ref
    weight = 5

    type(weight)        # <class 'int'>

    isinstance(5, int)  # True
    isinstance(5, str)  # False
    ```

## Integers

An integer (`int`) is a whole number — positive, negative, or zero — with no decimal point.

```python-ref
length = 5
```

### Integer operations

#### Arithmetic

- The standard math operators — **`+`, `-`, `*`, `/`, `**`**. One surprise for beginners: `/` (true division) always returns a `float`, even when the numbers divide evenly.

    ```python-ref
    length + 3     # 8
    length - 2     # 3
    length * 2     # 10
    length / 2     # 2.5  (/ always returns a float)
    length ** 2    # 25   (exponent)
    ```

- **Combine** any of these with `=` for an augmented assignment — it does the calculation on the variable, and sets it equal to the variable, doing two things with one operation.

    ```python-ref
    length += 1    # same as length = length + 1
    ```

#### Floor division & modulo

- **floor division `//`** divides two numbers and keeps only the whole-number part, dropping anything after the decimal — like asking "how many whole groups of 2 fit into 7?" 

    ```python-ref
    7 // 2    # 3    (7 split into groups of 2 makes 3 full groups)
    ```

- **modulo `%`** returns the remainder after that floor division — the part `//` throws away. `//` and `%` are a pair: one tells you how many whole groups fit, the other tells you what's left afterward.

    ```python-ref
    7 % 2     # 1    (7 split into groups of 2 leaves 1 behind)
    ```

- **`divmod()`** does both at once, returning `(quotient, remainder)` as a tuple — the same two values `//` and `%` give you separately, in one call.

    ```python-ref
    divmod(7, 2)    # (3, 1) — same as (7 // 2, 7 % 2)
    ```

#### Absolute value

- **`abs()`** returns a number with its sign dropped — negative becomes positive, positive stays unchanged.

    ```python-ref
    abs(-5)      # 5
    abs(5)       # 5
    abs(-4.5)    # 4.5
    ```

#### Convert

- **`int()`** converts a string of digits, or truncates a float toward zero. It cuts off the decimal — it does not round.

    ```python-ref
    int("5")      # 5
    int(5.9)      # 5   (cuts off decimal, doesn't round)
    int(True)     # 1
    ```

### Boolean expressions

- **Truthy:** any nonzero integer

- **Falsy:** `0`

```python-ref
if length:                 # runs — length isn't 0
    print("has a length")

while length:              # loops until length reaches 0
    length -= 1
```

??? run "Practice with integers"
    
    ```python
    length = 5

    print(length + 3)
    print(length - 2)
    print(length * 2)
    print(length / 2)
    print(length // 2)
    print(length % 2)
    print(divmod(length, 2))
    print(length ** 2)

    length += 1
    print(length)

    print(abs(-5))
    print(abs(5))

    print(int("5"))
    print(int(5.9))
    print(int(True))

    length = 5
    if length:
        print("has a length")

    while length:
        length -= 1
    print(length)
    ```

## Floats

A float is a number with a decimal point — for anything that isn't a whole number.

```python-ref
weight = 4.5
weight    # 4.5
```

### Float operations

#### Arithmetic

- Floats support the same operators as integers. Notably, `/` always returns a `float` — even `10 / 2`, which divides evenly, gives `5.0`, not `5`.

    ```python-ref
    weight + 1.5    # 6.0
    weight / 2      # 2.25
    10 / 2          # 5.0  (still a float, even though it divides evenly)
    ```

- **Combine** any of these with `=` for an augmented assignment — it does the calculation on the variable, and sets it equal to the variable, doing two things with one operation.

    ```python-ref
    weight += 1.5    # same as weight = weight + 1.5
    ```

#### Floor division & modulo

- **floor division `//`** divides two numbers and keeps only the whole-number part, dropping anything after the decimal — like asking "how many whole groups of 2 fit into 7?" 

    ```python-ref
    7.0 // 2    # 3.0    (7.0 split into groups of 2 makes 3 full groups)
    ```

- **modulo `%`** returns the remainder after that floor division — the part `//` throws away. `//` and `%` are a pair: one tells you how many whole groups fit, the other tells you what's left afterward.

    ```python-ref
    7.0 % 2     # 1.0    (7.0 split into groups of 2 leaves 1 behind)
    ```

- **`divmod()`** does both at once, returning `(quotient, remainder)` as a tuple — the same two values `//` and `%` give you separately, in one call.

    ```python-ref
    divmod(7.0, 2.0)    # (3.0, 1.0) — same as (7.0 // 2.0, 7.0 % 2.0)
    ```

#### Adjust

- **`abs()`** works the same way it does on an `int` — drops the sign, negative becomes positive.

    ```python-ref
    abs(-4.5)    # 4.5
    ```

- **`round()`** rounds to the nearest whole number, or to a given number of decimal places. With no second argument it rounds to the nearest whole number — but Python uses "round half to even" (banker's rounding), so `round(4.5)` is `4`, not `5`. Pass a second argument to round to that many decimal places instead.

    ```python-ref
    round(weight)          # 4  (Python rounds .5 to the nearest *even* number)
    round(4.567, 2)        # 4.57
    ```

#### Convert

- **`float()`** converts an integer or a numeric string into a float.

    ```python-ref
    float(5)         # 5.0
    float("4.5")      # 4.5
    ```

### Boolean expressions

- **Truthy:** any nonzero float

- **Falsy:** `0.0`

```python-ref
if weight:                  # runs — weight isn't 0.0
    print("has a weight")
```

??? warning "Floating-point precision"
    Tiny rounding errors creep in, since most decimal fractions can't be stored exactly in binary.

    ```python-ref
    0.1 + 0.2    # 0.30000000000000004
    ```

    This is a property of floating-point math in virtually every programming language, not a Python bug. If you need exact decimal arithmetic, use the `decimal` library instead of `float`.

??? run "Practice with floats"

    ```python
    weight = 4.5

    print(weight + 1.5)
    print(weight / 2)
    print(10 / 2)

    weight += 1.5
    print(weight)
    weight = 4.5

    print(weight // 2)
    print(weight % 2)

    print(round(weight))
    print(round(4.567, 2))

    print(float(5))
    print(float("4.5"))

    if weight:
        print("has a weight")

    print(0.1 + 0.2)
    print(round(0.1 + 0.2, 2))
    ```

## Strings

A string stores text — a sequence of characters — inside a single variable.[^str-collection]

[^str-collection]: Structurally, a string is a collection — it's iterable, indexable, and has a length, the same as a list. It's covered here rather than on the [Collections](collections.md) page because of how it's normally *used*: as one indivisible piece of text, not as a group of separate items you add to or remove from one at a time.

Strings have three defining traits:

- **Ordered** — characters keep the position they're written in.
- **Immutable** — unlike a list, a string can't be changed in place; every "modification" actually builds a new string.
- **Indexable** — since a string is a sequence, it supports the same `[]` indexing and slicing as a list.

```python-ref
name = "burmese python"
name    # "burmese python"
```

### String operations

#### Access characters

Strings use the same index and slice syntax as lists. `0` is the first character, negative indexes count from the end, and `start:end` slices out a substring.

- Index with `name[index]`.

    ```python-ref
    name[0]      # "b"
    name[-1]     # "n"
    ```

- A **slice** `name[start:end]` returns a substring from `start` up to (but not including) `end`.

    ```python-ref
    name[0:7]    # "burmese"
    ```

- A **step** `name[start:end:step]` skips characters instead of taking every one — leave `start`/`end` off to apply it to the whole string. A step of `-1` walks backward, which is the standard trick for reversing a string.

    ```python-ref
    name[::2]     # "breepto"  — every 2nd character
    name[::-1]    # "nohtyp esemrub"  — reversed
    ```

#### Inspect

- **`len()`** returns how many characters are in a string.

    ```python-ref
    len(name)              # 15
    ```

#### Combine

- **`,` in `print()`** separates multiple values with a space, converting non-strings automatically — but it only works inside `print()` (or similar functions), since it isn't actually building a string, just printing values side by side.

    ```python-ref
    print(species, length_ft)    # ball 4.5 — quick, but can't be saved to a variable
    ```

- **`+`** joins strings end to end, building a real string you can store — but every piece must already be text, so joining a string with a number raises a `TypeError` unless you convert the number with `str()` first.

    ```python-ref
    "ball" + " " + "python"    # "ball python"
    ```

- **`*`** repeats a string a given number of times.

    ```python-ref
    "ball" * 3    # "ballballball"
    ```

- **Combine** `+` or `*` with `=` for an augmented assignment — it does the calculation on the variable, and sets it equal to the variable, doing two things with one operation.

    ```python-ref
    name = "ball"
    name += " python"    # same as name = name + " python"
    ```

- **`.join()`** glues a list of strings back together, using the string it's called on as the separator between each item.

    ```python-ref
    "-".join(["burmese", "python"])       # "burmese-python"
    ```

#### f-strings

- An **f-string** lets you embed variables directly inside `{}` and is a good choice once a string has multiple variables in it. Put a variable's name inside the `{}` and the variable's value will be inserted inside. 

    ```python-ref
    species = "ball"
    length = 5

    print(f"{species} is {length} feet")  # "ball is 5 feet"
    ```

- A **format spec** is an optional add-on *inside* one `{}` placeholder — it goes after the `value:` and controls how that value is displayed. It's built from **one or more optional** pieces, stacked together in this order: 

    `{ value : [align] [sign] [width] [thousand separator ,] [.precision] [type] }`

    - **align** — `<` left, `>` right, or `^` center, aligns *within* the width, so it requires a specificed width too.

        ```python-ref
        f"{length:<6}"    # "5     " — left-aligned in 6 characters
        f"{length:>6}"    # "     5" — right-aligned in 6 characters
        f"{length:^6}"    # "  5   " — centered in 6 characters
        ```

    - **sign** — `-` is the default where only negative numbers get a sign, `+` forces a sign on every number, `=` forces the sign to the very front, before any zero-padding.

        ```python-ref
        f"{5:+}"      # "+5" — always shows a sign
        f"{-5:+}"     # "-5"
        f"{5:=+06}"   # "+00005" — sign forced to the front, before the zero-padding
        ```

    - **width** — a plain number `width` pads the result to at least that many characters.

        ```python-ref
        f"{length:6}"    # "     5" — padded to 6 characters wide
        ```

    - **thousands separator** - a `,` adds a comma to group every 3 digits.

        ```python-ref
        f"{1234567.5:,}"    # "1,234,567.5"
        ```

    - **precision** — a `.` followed by a number `.digits` sets how many digits appear after the decimal point in a `f` and `%` type (detailed below), without a precision they default to 6 decimal places.

        ```python-ref
        f"{length_ft:.2f}"    # "4.50" — 2 digits after the decimal
        ```

    - **type** — a letter at the very end — tells Python how to display the value: `d` for an integer, `f` for fixed-point notation (displayed with decimal places), `%` for a percentage.

        ```python-ref
        f"{length:d}"        # "5" — treated as an integer
        f"{length_ft:.2f}"   # "4.50" — fixed-point notation, 2 decimal places
        f"{length_ft:f}"     # "4.500000" — no precision given, defaults to 6 digits
        f"{0.25:.1%}"        # "25.0%" — treated as a percentage
        ```

#### Modify

Since strings are immutable, these all return a **new** string rather than changing the original.

- **`.upper()`, `.lower()`, `.title()`, `.capitalize()`** change letter case. `.upper()`/`.lower()` change every character; `.title()` capitalizes every word; `.capitalize()` capitalizes only the first character and lowercases the rest.

    ```python-ref
    name.upper()          # "BURMESE PYTHON"
    name.lower()          # "burmese python"
    name.title()          # "Burmese Python"
    name.capitalize()     # "Burmese python"
    ```

- **`.strip()`** removes leading and trailing whitespace.

    ```python-ref
    "  ball  ".strip()    # "ball"
    ```

- **`.replace()`** swaps every occurrence of one substring for another.

    ```python-ref
    name.replace("burmese", "ball")   # "ball python"
    ```

#### Search

- **`in`** checks whether one string contains another.

    ```python-ref
    "python" in name          # True
    ```

- **`.find()`** returns the index where a substring first appears, or `-1` if it's not found.

    ```python-ref
    name.find("python")       # 8
    ```

- **`.count()`** counts how many times a substring appears.

    ```python-ref
    name.count("p")           # 1
    ```

#### Validate

- **`.startswith()`, `.endswith()`** check the beginning or end of a string specifically — faster to read than slicing and comparing manually.

    ```python-ref
    name.startswith("burmese")   # True
    name.endswith(".py")         # False
    ```

- **`.isdigit()`, `.isalpha()`** check whether every character is a digit, or a letter. Useful for validating input before converting it — `input()` always returns a string, even when the person typed a number.

    ```python-ref
    age = input("How old are you? ")   # always a string, even if they type "8"
    age.isdigit()                      # True if it's safe to pass to int()

    species = "ball"
    species.isalpha()                  # True — every character is a letter
    ```

#### Convert

- **`str()`** converts almost any value into its text representation. Handy any time you need to combine a number with text, since `+` can't join a string and a number directly.

    ```python-ref
    str(5)      # "5"
    str(4.5)    # "4.5"
    str(True)   # "True"
    ```

- **`.split()`** converts a string into a list, breaking it apart wherever the separator appears. Uses whitespace as the separator by default.

    ```python-ref
    name.split()                          # ["burmese", "python"]
    ```

### Boolean expressions

- **Truthy:** any non-empty string — even one that's just whitespace

- **Falsy:** the empty string `""`

```python-ref
if name:                # runs — name isn't empty
    print("has a name")
```

??? run "Practice with strings"

    ```python
    name = "burmese python"

    print(len(name))

    print(name[0])
    print(name[-1])
    print(name[0:7])
    print(name[8:])

    print(name[::2])
    print(name[::-1])

    species = "ball"
    name = species + " " + "python"
    print(name)

    print(species * 3)

    name = "ball"
    name += " python"
    print(name)

    species = "ball"
    length = 5
    sentence = f"the {species} python is about {length} feet long"
    print(sentence)

    print(f"{length:6}")
    print(f"{length:<6}")
    print(f"{length:>6}")
    print(f"{length:^6}")

    print(f"{1234567.5:,}")

    length_ft = 4.5
    print(f"{length_ft:.2f}")
    print(f"{length_ft:f}")
    print(f"{length_ft:.2f} ft")

    print(f"{length:d}")
    print(f"{0.25:.1%}")
    print(f"{1234.5:,.2f}")

    species = "ball"
    length_ft = 4.5

    print(species, length_ft)                    # comma — fine for a quick printout

    name = species + " " + str(length_ft)         # + — needs str() to include a number
    print(name)

    print(f"{species} is {length_ft} ft")         # f-string — no manual conversion needed

    name = "burmese python"

    print(name.upper())
    print(name.lower())
    print(name.title())
    print(name.capitalize())

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

    print(name.startswith("burmese"))
    print(name.endswith(".py"))

    age = "8"
    print(age.isdigit())

    species = "ball"
    print(species.isalpha())

    print(str(5))
    print(str(4.5))
    print(str(True))

    name = "burmese python"
    if name:
        print("has a name")
    ```

## Booleans

A boolean (`bool`) holds one of exactly two values, **`True`** or **`False`** — often used to represent yes/no, on/off, or the result of a comparison.

```python-ref
venomous = False
venomous    # False
```

### Boolean operations

#### Creating a boolean

Several kinds of operators hand back a `bool`, each answering a different question:

- **`>`, `<`, `>=`, `<=`, `==`, `!=`** compare two values — is one bigger, smaller, or equal to the other?

    ```python-ref
    length = 5
    length > 3     # True — is length bigger than 3?
    length == 5    # True — is length equal to 5?
    ```

- **`is`, `is not`** check whether two names point to the *exact same object*, not just an equal-looking value.

    ```python-ref
    venomous is None    # False — venomous is False, not None
    ```

- **`in`, `not in`** check whether a value shows up inside a string, list, or other collection.

    ```python-ref
    "python" in name    # True
    ```

- **`not`** flips a boolean to its opposite.

    ```python-ref
    not venomous    # True — venomous is False, so not flips it
    ```

#### Logical operators

`not`, `and`, `or` combine booleans to create more complex meanings.


| `A` (boolean) | `B` (boolean) | `not A` — flips to the opposite | `A and B` — `True` only if both are `True` | `A or B` — `True` if either is `True` |
|---|---|---|---|---|
| <span class="pt-bool-true">True</span>    | <span class="pt-bool-true">True</span>    | <span class="pt-bool-false">False</span> | <span class="pt-bool-true">True</span>    | <span class="pt-bool-true">True</span>    |
| <span class="pt-bool-true">True</span>    | <span class="pt-bool-false">False</span>  | <span class="pt-bool-false">False</span> | <span class="pt-bool-false">False</span>  | <span class="pt-bool-true">True</span>    |
| <span class="pt-bool-false">False</span>  | <span class="pt-bool-true">True</span>    | <span class="pt-bool-true">True</span>   | <span class="pt-bool-false">False</span>  | <span class="pt-bool-true">True</span>    |
| <span class="pt-bool-false">False</span>  | <span class="pt-bool-false">False</span>  | <span class="pt-bool-true">True</span>   | <span class="pt-bool-false">False</span>  | <span class="pt-bool-false">False</span>  |

- **`not` [boolean]** flips a boolean to its opposite.

    ```python-ref
    not venomous    # not False → True
    ```

- **[boolean] `and` [boolean]** is `True` only if **both** sides are `True`.

    ```python-ref
    length > 10 and venomous    # True and False → False
    ```

- **[boolean] `or` [boolean]** is `True` if **either** side is `True`.

    ```python-ref
    length > 10 or venomous    # True or False → True
    ```

- **Order of operations:** When several logical operators appear together, Python evaluates them in the below order. Keeping this in mind, you can use parentheses to help construct your expressions. 

    1. `not`

    2. `and`

    3. `or`


??? note "Bool is a subclass of int"
    `True` behaves like `1` and `False` behaves like `0` in arithmetic.

    ```python-ref
    isinstance(True, int)    # True
    True + True               # 2
    ```

??? run "Practice with booleans"

    ```python
    length = 5

    print(length > 3)
    print(length == 5)
    print(length != 5)

    venomous = False
    print(venomous is None)

    name = "burmese python"
    print("python" in name)

    is_python = True
    is_venomous = False

    print(is_python and is_venomous)
    print(is_python or is_venomous)
    print(not is_venomous)

    if is_venomous:
        print("be careful")
    else:
        print("should be safe")

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

- **`is`, `is not`** compare against `None` — always use these, not `==`/`!=`. `is` checks that it's the *exact same object*, which is what you want for a singleton value like `None`.

    ```python-ref
    venomous is None        # True
    venomous is not None    # False
    ```

### Boolean expressions

`None` is always falsy — there's no "sometimes truthy" case, since it's the one value that only ever means "nothing here."

- **boolean expression:**

    - Truthy: never — `None` has no truthy case

    - Falsy: `None` (its only value)

    ```python-ref
    if venomous:              # skipped — venomous is None
        print("found something")
    else:
        print("nothing found")
    ```

??? run "Practice with None"

    ```python
    venomous = None

    print(venomous is None)
    print(venomous is not None)

    if venomous:
        print("found something")
    else:
        print("nothing found")
    ```
