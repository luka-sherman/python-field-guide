---
description: >-
  Python's basic data types explained with runnable examples: integers, floats,
  strings, booleans, and None, plus the operations each one supports.
---

# :material-shape-outline:{ .lg .middle } Basic data types

Every value in Python has a **type**, which determines what operations it supports and how it behaves. 

A basic ("scalar") data type holds a single value, as opposed to a [collection](collections.md) data type, which groups multiple values together.

<div class="pt-jump-table" markdown="block">

| Basic Type | Example | Use it for |
|------|---------|------------|
| <a href="#integers">**`integer "int"`**</a> | <pre><code class="language-python-ref">5</code></pre> | <ul><li>Counts — how many of something there are, like items in a list</li><li>Indexes — the position of an item in a sequence, like `species[2]`</li><li>IDs — a unique whole-number identifier, like a user or record ID</li></ul> |
| <a href="#floats">**`float`**</a> | <pre><code class="language-python-ref">4.5</code></pre> | <ul><li>Measurements, ratios — anything with a decimal</li></ul> |
| <a href="#strings">**`string "str"`**</a> | <pre><code class="language-python-ref">"ball python"</code></pre> | <ul><li>Text — names, labels, messages</li><li>Ordered and indexable like a list, but immutable — `.upper()`, `.replace()`, etc. return a *new* string</li></ul> |
| <a href="#booleans">**`boolean "bool"`**</a> | <pre><code class="language-python-ref">`True`</code></pre> | <ul><li>Flags, yes/no switches, comparison results (`length > 3`)</li><li>Secretly a subclass of `int` — `True + True == 2`</li></ul> |
| <a href="#none">**`None`**</a> | <pre><code class="language-python-ref">None</code></pre> | <ul><li>Marking "no value yet" — a default placeholder, or what a function returns if it falls through without a `return`</li><li>Compare with `is None`, not `== None`</li><li>`not thing` also catches `None`, but it's true for any falsy value (`0`, `""`, `[]`) too — use `is None` when you mean *specifically* "no value"</li></ul> |

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

An integer a.k.a. "`int`" is a whole number — positive, negative, or zero — with no decimal point.

```python-ref
length = 5
```

### Integer operations { data-card-link="skip" }

#### Arithmetic

If both sides are `int` the result will be `int`, except for division.

- **`+` addition**, **`-` subtraction**

    ```python-ref
    length + 3   # 8
    length - 2   # 3
    ```

- **`*` multiplication**, **`/` division** (division always returns a [`float decimal`](#floats), even when the numbers divide evenly)

    ```python-ref
    length * 2   # 10
    length / 2   # 2.5  (division always returns a float)
    ```

- **`**` exponent** a^b^ = `a**b`

    ```python-ref
    length ** 2  # 25   (length squared)
    ```

#### Floor division & modulo

- **`//` floor division** divides two numbers and keeps only the whole-number part, dropping anything after the decimal — like asking "how many whole groups of 2 fit into 7?" 

    ```python-ref
    7 // 2  # 3 (7 split into groups of 2 makes 3 full groups)
    ```

- **`%` modulo** returns the remainder after that floor division — the part `//` throws away. `//` and `%` are a pair: one tells you how many whole groups fit, the other tells you what's left afterward.

    ```python-ref
    7 % 2  # 1 (7 split into groups of 2 leaves 1 behind)
    ```

- **`divmod()`** does both at once, returning `(quotient, remainder)` as a tuple — the same two values `//` and `%` give you separately, in one call.

    ```python-ref
    divmod(7, 2) # (3, 1) — same as (7 // 2, 7 % 2)
    ```

#### Apply arithmetic to a variable

- **Combine** any of these arithmetic operations with `=` for an augmented assignment — it does that calculation on the variable, and updates the value of the variable, doing two things with one operation. Examples:  **`+=`  `-=`  `*=`  `/=`  `//=`  `%=`  `**=`**.

    ```python-ref
    length = length + 1  # this way works, it's just longer
    
    length += 1          # same thing, written more concisely 
    ```

#### Absolute value

- **`abs()`** returns a number with its sign dropped — negative becomes positive, positive stays unchanged.

    ```python-ref
    abs(-5)    # 5
    abs(5)     # 5
    abs(-4.5)  # 4.5
    ```

#### Convert

- **`int()`** converts a string of digits, or truncates a float toward zero. It cuts off the decimal — it does not round.

    ```python-ref
    int("5")   # 5
    int(5.9)   # 5   (cuts off decimal, doesn't round)
    int(True)  # 1
    ```

### Boolean expressions

- **`==` `!=` `>` `<` `>=` `<=`** compare two numbers — see [comparisons by type](#booleans) for the full rundown.

    ```python-ref
    length == 5   # True, equal to
    length != 4   # True, not equal to
    length > 3    # True, greater than
    length < 10   # True, less than
    length >= 5   # True, greater than or equal to
    length <= 5   # True, less than or equal to
    ```

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
```

### Float operations { data-card-link="skip" }

#### Arithmetic

If either side of arithmetic is `float` the result will be `float`, except for division.

- **`+` addition**, **`-` subtraction**

    ```python-ref
    weight + 3   # 7.5
    weight - 2   # 2.5
    ```

- **`*` multiplication**, **`/` division**

    ```python-ref
    weight * 2   # 9.0
    weight / 2   # 2.25
    ```

- **`**` exponent** a^b^ = `a**b`

    ```python-ref
    weight ** 2  # 20.25   (weight squared)
    ```


#### Floor division & modulo

- **floor division `//`** divides two numbers and keeps only the whole-number part, dropping anything after the decimal — like asking "how many whole groups of 2 fit into 7?" 

    ```python-ref
    7.0 // 2  # 3.0 (7.0 split into groups of 2 makes 3 full groups)
    ```

- **modulo `%`** returns the remainder after that floor division — the part `//` throws away. `//` and `%` are a pair: one tells you how many whole groups fit, the other tells you what's left afterward.

    ```python-ref
    7.0 % 2  # 1.0 (7.0 split into groups of 2 leaves 1 behind)
    ```

- **`divmod()`** does both at once, returning `(quotient, remainder)` as a tuple — the same two values `//` and `%` give you separately, in one call.

    ```python-ref
    divmod(7.0, 2.0)  # (3.0, 1.0) — same as (7.0 // 2.0, 7.0 % 2.0)
    ```

#### Apply arithmetic to a variable

- **Combine** any of these arithmetic operations with `=` for an augmented assignment — it does that calculation on the variable, and updates the value of the variable, doing two things with one operation. Examples:  **`+=`  `-=`  `*=`  `/=`  `//=`  `%=`  `**=`**.

    ```python-ref
    length = length + 1  # this way works, it's just longer
    
    length += 1          # same thing, written more concisely 
    ```

#### Adjust

- **`abs()`** works the same way it does on an `int` — drops the sign, negative becomes positive.

    ```python-ref
    abs(-4.5)  # 4.5
    ```

- **`round()`** rounds to the nearest whole number, or to a given number of decimal places. With no second argument it rounds to the nearest whole number — but Python uses "round half to even" (banker's rounding), so `round(4.5)` is `4`, not `5`. Pass a second argument to round to that many decimal places instead.

    ```python-ref
    round(weight)    # 4  (Python rounds .5 to the nearest *even* number)
    round(4.567, 2)  # 4.57
    ```

#### Convert

- **`float()`** converts an integer or a numeric string into a float.

    ```python-ref
    float(5)      # 5.0
    float("4.5")  # 4.5
    ```

### Boolean expressions

- **`==` `!=` `>` `<` `>=` `<=`** compare two numbers — see [comparisons by type](#booleans) for the full rundown.

    ```python-ref
    weight == 4.5   # True, equal to
    weight != 5.0   # True, not equal to
    weight > 3.0    # True, greater than
    weight < 10.0   # True, less than
    weight >= 4.5   # True, greater than or equal to
    weight <= 4.5   # True, less than or equal to
    ```

- **Truthy:** any nonzero float

- **Falsy:** `0.0`

```python-ref
if weight:                 # runs — weight isn't 0.0
    print("has a weight")
```

??? warning "Floating-point precision"
    Tiny rounding errors creep in, since most decimal fractions can't be stored exactly in binary.

    ```python-ref
    0.1 + 0.2  # 0.30000000000000004
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
```

### String operations { data-card-link="skip" }

#### Access characters

Strings use the same index and slice syntax as lists. `0` is the first character, negative indexes count from the end, and `start:end` slices out a substring.

- Index with `name[index]`.

    ```python-ref
    name[0]   # "b"
    name[-1]  # "n"
    ```

- A **slice** `name[start:end]` returns a substring from `start` up to (but not including) `end`.

    ```python-ref
    name[0:7]  # "burmese"
    ```

- A **step** `name[start:end:step]` skips characters instead of taking every one — leave `start`/`end` off to apply it to the whole string. A step of `-1` walks backward, which is the standard trick for reversing a string.

    ```python-ref
    name[::2]   # "breepto"  — every 2nd character
    name[::-1]  # "nohtyp esemrub"  — reversed
    ```

#### Inspect

- **`len()`** returns how many characters are in a string.

    ```python-ref
    len(name)  # 15
    ```

#### Combine

- **`+` joins** strings end to end, building a real string you can store — but every piece must already be text, so joining a string with a number raises a `TypeError` unless you convert the number with `str()` first.

    ```python-ref
    "ball" + " " + "python"  # "ball python"
    ```

    - **combine \+=** for an augmented assignment — join something to a string then update the variable with the new value, doing two things with one operation.

        ```python-ref
        name = name + "python"  # long way
        name += "python"        # short way
        ```

- **`*` repeats** a string a given number of times.

    ```python-ref
    "ball" * 3  # "ballballball"
    ```

    - **combine \*=** for an augmented assignment — repeat the string a given number of times then update the variable with the value, doing two things with one operation.

        ```python-ref
        name = name * 3  # long way
        name *= 3        # short way
        ```

- **`.join()`** glues a list of strings back together, using the string it's called on as the separator between each item.

    ```python-ref
    "-".join(["burmese", "python"])  # "burmese-python"
    ```

#### f-strings

- An **f-string** lets you embed variables directly inside `{}` and is a good choice once a string has multiple variables in it. Put a variable's name inside the `{}` and the variable's value will be inserted inside. 

    ```python-ref
    species = "ball"
    length = 5

    print(f"{species} is {length} feet")  # "ball is 5 feet"
    ```

- **`.format()`** is the older way to build a string with embedded values — `{}` placeholders in the string are filled in with the arguments passed to `.format()`, in order, instead of reading variable names directly.

    ```python-ref
    "{} {}".format(species, length)  # "ball 5"
    ```

- A **format spec** is an optional add-on *inside* one `{}` placeholder — it goes after the `value:` and controls how that value is displayed. It's built from **one or more optional** pieces, stacked together in this order: 

    `{ value : [align] [sign] [width] [thousand separator ,] [.precision] [type] }`

    - **align** — `<` left, `>` right, or `^` center, aligns *within* the width, so it requires a specificed width too.

        ```python-ref
        f"{length:<6}"  # "5     " — left-aligned in 6 characters
        f"{length:>6}"  # "     5" — right-aligned in 6 characters
        f"{length:^6}"  # "  5   " — centered in 6 characters
        ```

    - **sign** — `-` is the default where only negative numbers get a sign, `+` forces a sign on every number, `=` forces the sign to the very front, before any zero-padding.

        ```python-ref
        f"{5:+}"     # "+5" — always shows a sign
        f"{-5:+}"    # "-5"
        f"{5:=+06}"  # "+00005" — sign forced to the front, before the zero-padding
        ```

    - **width** — a plain number `width` pads the result to at least that many characters.

        ```python-ref
        f"{length:6}"  # "     5" — padded to 6 characters wide
        ```

    - **thousands separator** - a `,` adds a comma to group every 3 digits.

        ```python-ref
        f"{1234567.5:,}"  # "1,234,567.5"
        ```

    - **precision** — a `.` followed by a number `.digits` sets how many digits appear after the decimal point in a `f` and `%` type (detailed below), without a precision they default to 6 decimal places.

        ```python-ref
        f"{length_ft:.2f}"  # "4.50" — 2 digits after the decimal
        ```

    - **type** — a letter at the very end — tells Python how to display the value: `d` for an integer, `f` for fixed-point notation (displayed with decimal places), `%` for a percentage.

        ```python-ref
        f"{length:d}"       # "5" — treated as an integer
        f"{length_ft:.2f}"  # "4.50" — fixed-point notation, 2 decimal places
        f"{length_ft:f}"    # "4.500000" — no precision given, defaults to 6 digits
        f"{0.25:.1%}"       # "25.0%" — treated as a percentage
        ```

#### Modify

Since strings are immutable, these all return a **new** string rather than changing the original.

- **`.upper()`, `.lower()`, `.title()`, `.capitalize()`** change letter case. `.upper()`/`.lower()` change every character; `.title()` capitalizes every word; `.capitalize()` capitalizes only the first character and lowercases the rest.

    ```python-ref
    name.upper()       # "BURMESE PYTHON"
    name.lower()       # "burmese python"
    name.title()       # "Burmese Python"
    name.capitalize()  # "Burmese python"
    ```

- **`.strip()`** removes leading and trailing whitespace.

    ```python-ref
    "  ball  ".strip()  # "ball"
    ```

- **`.replace()`** swaps every occurrence of one substring for another.

    ```python-ref
    name.replace("burmese", "ball")  # "ball python"
    ```

#### Search

- **`in`** checks whether one string contains another.

    ```python-ref
    "python" in name  # True
    ```

- **`.find()`** returns the index where a substring first appears, or `-1` if it's not found.

    ```python-ref
    name.find("python")  # 8
    ```

- **`.count()`** counts how many times a substring appears.

    ```python-ref
    name.count("p")  # 1
    ```

#### Validate

- **`.startswith()`, `.endswith()`** check the beginning or end of a string specifically — faster to read than slicing and comparing manually.

    ```python-ref
    name.startswith("burmese")  # True
    name.endswith(".py")        # False
    ```

- **`.isdigit()`, `.isalpha()`** check whether every character is a digit, or a letter. Useful for validating input before converting it — `input()` always returns a string, even when the person typed a number.

    ```python-ref
    age = input("How old are you? ")  # always a string, even if they type "8"
    age.isdigit()                     # True if it's safe to pass to int()

    species = "ball"
    species.isalpha()                 # True — every character is a letter
    ```

#### Convert

- **`str()`** converts almost any value into its text representation. Handy any time you need to combine a number with text, since `+` can't join a string and a number directly.

    ```python-ref
    str(5)     # "5"
    str(4.5)   # "4.5"
    str(True)  # "True"
    ```

- **`.split()`** converts a string into a list, breaking it apart wherever the separator appears. Uses whitespace as the separator by default.

    ```python-ref
    name.split()  # ["burmese", "python"]
    ```

### Boolean expressions

- **`==` `!=`** check whether two strings are equal.

    ```python-ref
    name == "burmese python"  # True, equal to
    name != "ball python"     # True, not equal to
    ```

- **`in` `not in`** check whether one string is a substring of another.

    ```python-ref
    "python" in name       # True, is a substring
    "anaconda" not in name # True, is not a substring
    ```

- **`>` `<`** compare strings alphabetically — see [comparisons by type](#booleans) for the full rundown.

    ```python-ref
    name > "ball python"  # True, comes after alphabetically
    name < "ball python"  # False, doesn't come before alphabetically
    ```

- **Truthy:** any non-empty string — even one that's just whitespace

- **Falsy:** the empty string `""`

```python-ref
if name:                 # runs — name isn't empty
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

A boolean (`bool`) holds one of exactly two values, **`True`** or **`False`** — often used to represent yes/no, on/off, or the result of a comparison. They are used in [if statements](conditionals.md#if--elif--else) and [while loops](loops.md#while-loops).

```python-ref
venomous = False
```

### Boolean expressions

- A **boolean expression** is a boolean value (`True` or `False`) or anything that produces one, and is treated as the **condition** that must be `True` in order to run a block of code.

- A comparison looks different depending on the type of value being checked, as shown below. All of these comparisons result in a `True` or `False` boolean expression. 

    !!! example "Comparisons by type"

        === "int, float"

            | Operator | Meaning |
            |---|---|
            | `==` | equal to |
            | `!=` | not equal to |
            | `>` | greater than |
            | `<` | less than |
            | `>=` | greater than or equal to |
            | `<=` | less than or equal to |

            ```python-ref
            length = 12

            if length == 12:             # equal to
                print("exactly 12 ft")

            if length != 4:              # not equal
                print("not 4 ft")

            if length > 10:              # greater than
                print("long snake")

            if length < 20:              # less than
                print("under 20 ft")

            if length >= 12:             # greater than or equal to
                print("at least 12 ft")

            if length <= 12.5:           # less than or equal to
                print("12.5 ft or shorter")
            ```

        === "str"

            | Operator | Meaning |
            |---|---|
            | `==` | equal to |
            | `!=` | not equal to |
            | `in` | is a substring |
            | `not in` | is not a substring |
            | `>` | comes after alphabetically |
            | `<` | comes before alphabetically |

            ```python-ref
            name = "burmese python"

            if name == "burmese python":   # equal to
                print("it's a burmese")

            if name != "ball python":      # not equal
                print("not a ball python")

            if "python" in name:           # is it a substring
                print("name contains 'python'")

            if "anaconda" not in name:     # is it not a substring
                print("name doesn't mention anaconda")

            if name > "ball python":       # alphabetical comparison
                print("comes after 'ball python' alphabetically")
            ```

        === "bool"

            | Check | Meaning |
            |---|---|
            | `[bool]` | is the bool True |
            | `not [bool]` | is the bool False |

            Don't compare booleans with `== True` or `is True` — a boolean is already the condition, so just use the value directly (or `not` the value).

            ```python-ref
            venomous = False

            if venomous:                   # is it True — don't write venomous == True
                print("handle with care")

            if not venomous:               # is it False — don't write venomous == False
                print("safe to handle")
            ```

        === "None"

            | Operator | Meaning |
            |---|---|
            | `is` | is None |
            | `is not` | is not None |

            ```python-ref
            age = None

            if age is None:                # is it None
                print("age not recorded")

            if age is not None:            # is it anything else
                print("age was recorded")
            ```

        === "list"

            | Operator | Meaning |
            |---|---|
            | `in` | value exists in the list |
            | `not in` | value is missing from the list |
            | `==` | same contents, in the same order |
            | `!=` | different contents |

            Or compare a specific item directly, like `species[0] == "ball"`.

            ```python-ref
            species = ["ball", "burmese", "boa"]
            other_species = ["ball", "burmese", "boa"]

            if "ball" in species:          # is the value in the list
                print("ball python is in the list")

            if "anaconda" not in species:  # is the value missing from the list
                print("anaconda isn't in the list")

            if species == other_species:   # is it the same contents, in the same order
                print("both lists match")

            if "ball" == species[0]:       # compare a specific item
                print("ball python is the first item")
            ```

            | Operator | Meaning |
            |---|---|
            | `==` | same contents, even if it's a different object |
            | `is` | the exact same object, not just an equal one |

            ```python-ref
            snake = ["ball", "burmese"]
            other_snake = ["ball", "burmese"]   # separate list, but equal contents

            if snake == other_snake:      # do they contain the same items?
                print("equal contents")

            if snake != ["ball"]:         # different contents
                print("not equal to a single-item list")

            same_snake = snake                  # another name for `snake`
            if snake is same_snake:             # same_snake and snake point to the exact same list
                print("this really is the same list")

            if snake is not other_snake:        # it's a different list, even though contents match
                print("but not the same list")
            ```

        === "tuple"

            | Operator | Meaning |
            |---|---|
            | `in` | value exists in the tuple |
            | `not in` | value is missing from the tuple |
            | `==` | same contents, in the same order |
            | `!=` | different contents |

            Or compare a specific item directly, like `snake[0] == "ball"`.

            ```python-ref
            snake = ("ball", "5ft", "not venomous")
            other_snake = ("ball", "5ft", "not venomous")

            if "ball" in snake:
                print("species ball is in the tuple")

            if snake == other_snake:
                print("tuples match")

            if "ball" == snake[0]:
                print("ball python is the first item")
            ```

            | Operator | Meaning |
            |---|---|
            | `==` | same contents, even if it's a different object |
            | `is` | the exact same object, not just an equal one |

            ```python-ref
            snake = ("ball", "burmese")
            other_snake = ("ball", "burmese")   # separate tuple, but equal contents

            if snake == other_snake:      # do they contain the same items?
                print("equal contents")

            same_snake = snake                  # another name for `snake`
            if snake is same_snake:             # same_snake and snake point to the exact same tuple
                print("this really is the same tuple")

            if snake is not other_snake:        # it's a different tuple, even though contents match
                print("but not the same tuple")
            ```

        === "dict"

            | Operator | Meaning |
            |---|---|
            | `in` | key exists |
            | `not in` | key is missing |

            Or compare a specific value directly, like `snake["length"] > 2`.

            ```python-ref
            snake = {"species": "ball", "length": 3, "venomous": False}

            if "venomous" in snake:        # is it a key
                print("snake dict tracks venomous status")

            if "habitat" not in snake:     # is it not a key
                print("snake dict has no habitat key")

            if snake["length"] > 2:        # compare a specific value
                print("snake in dict is over 2 ft")
            ```

            | Operator | Meaning |
            |---|---|
            | `==` | same keys and values, even if it's a different object |
            | `is` | the exact same object, not just an equal one |

            ```python-ref
            snake = {"species": "ball", "length": 3}
            other_snake = {"species": "ball", "length": 3}   # separate dict, but equal contents

            if snake == other_snake:      # do they contain the same keys and values?
                print("equal contents")

            same_snake = snake                  # another name for `snake`
            if snake is same_snake:             # same_snake and snake point to the exact same dict
                print("this really is the same dict")

            if snake is not other_snake:        # it's a different dict, even though contents match
                print("but not the same dict")
            ```

        === "set"

            | Operator | Meaning |
            |---|---|
            | `in` | value exists in the set |
            | `not in` | value is missing from the set |
            | `==` | same contents, regardless of order |
            | `!=` | different contents |

            ```python-ref
            species = {"ball", "burmese", "boa"}
            other_species = {"ball", "burmese", "boa"}

            if "ball" in species:          # is the value in the set
                print("ball python is in the set")

            if "anaconda" not in species:  # is the value missing from the set
                print("anaconda isn't in the set")

            if species == other_species:   # same contents, regardless of order
                print("both sets match")
            ```

            | Operator | Meaning |
            |---|---|
            | `is` | the exact same object, not just an equal one |

            ```python-ref
            same_species = species              # another name for `species`
            if species is same_species:         # same_species and species point to the exact same set
                print("this really is the same set")

            if species is not other_species:    # it's a different set, even though contents match
                print("but not the same set")
            ```

            | Operator | Meaning |
            |---|---|
            | `issubset()` | every item in this set is also in another set |
            | `issuperset()` | this set contains every item in another set |
            | `isdisjoint()` | the two sets share no items at all |

            ```python-ref
            constrictors = {"ball", "burmese", "boa"}

            {"ball", "burmese"}.issubset(constrictors)   # True
            constrictors.issuperset({"ball"})            # True
            constrictors.isdisjoint({"cobra", "viper"})  # True
            ```

### Logical operators

`not`, `and`, `or` combine booleans (or boolean expressions) to create more complex meanings.


| `A` (boolean) | `B` (boolean) | `not A` — flips to the opposite | `A and B` — `True` only if both are `True` | `A or B` — `True` if either is `True` |
|---|---|---|---|---|
| <span class="pt-bool-true">True</span>    | <span class="pt-bool-true">True</span>    | <span class="pt-bool-false">False</span> | <span class="pt-bool-true">True</span>    | <span class="pt-bool-true">True</span>    |
| <span class="pt-bool-true">True</span>    | <span class="pt-bool-false">False</span>  | <span class="pt-bool-false">False</span> | <span class="pt-bool-false">False</span>  | <span class="pt-bool-true">True</span>    |
| <span class="pt-bool-false">False</span>  | <span class="pt-bool-true">True</span>    | <span class="pt-bool-true">True</span>   | <span class="pt-bool-false">False</span>  | <span class="pt-bool-true">True</span>    |
| <span class="pt-bool-false">False</span>  | <span class="pt-bool-false">False</span>  | <span class="pt-bool-true">True</span>   | <span class="pt-bool-false">False</span>  | <span class="pt-bool-false">False</span>  |

- **`not` [boolean]** flips a boolean to its opposite.

    ```python-ref
    not venomous  # not False → True
    ```

- **[boolean] `and` [boolean]** is `True` only if **both** sides are `True`.

    ```python-ref
    length > 10 and venomous  # True and False → False
    ```

- **[boolean] `or` [boolean]** is `True` if **either** side is `True`.

    ```python-ref
    length > 10 or venomous  # True or False → True
    ```

- **Order of operations:** When several logical operators appear together, Python evaluates them in the below order. Keeping this in mind, you can use parentheses to help construct your expressions. 

    1. `not`

    2. `and`

    3. `or`


??? note "Bool is a subclass of int"
    `True` behaves like `1` and `False` behaves like `0` in arithmetic.

    ```python-ref
    isinstance(True, int)  # True
    True + True            # 2
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
```

### Check for None

- **`is`, `is not`** compare against `None` — always use these, not `==`/`!=`. `is` checks that it's the *exact same object*, which is what you want for a singleton value like `None`.

    ```python-ref
    venomous is None      # True
    venomous is not None  # False
    ```

### Boolean expressions

`None` is always falsy — there's no "sometimes truthy" case, since it's the one value that only ever means "nothing here."

- **boolean expression:**

    - Truthy: never — `None` has no truthy case

    - Falsy: `None` (its only value)

    ```python-ref
    if venomous:                  # skipped — venomous is None
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
