# Basic Data Types

Every value in Python has a **type**, which determines what operations it supports and how it behaves — Python figures this out from the value itself, since you never declare a type explicitly. A basic (or "scalar") data type holds a single, indivisible value, as opposed to a [collection](collections.md), which groups many values together. The basic types are also all **immutable**: once created, the value itself can never be changed in place — only replaced with a different value.

| Type | Example | Use it for |
|------|---------|------------|
| `int` | `5` | <ul><li>Counts — how many of something there are, like items in a list</li><li>Indexes — the position of an item in a sequence, like `species[2]`</li><li>IDs — a unique whole-number identifier, like a user or record ID</li></ul> |
| `float` | `4.5` | <ul><li>Measurements, ratios — anything with a decimal</li><li>Binary rounding errors mean `0.1 + 0.2 != 0.3`</li></ul> |
| `str` | `"ball python"` | <ul><li>Text — names, labels, messages</li><li>Ordered and indexable like a list, but immutable — `.upper()`, `.replace()`, etc. return a *new* string</li></ul> |
| `bool` | `True` | <ul><li>Flags, yes/no switches, comparison results (`length > 3`)</li><li>Secretly a subclass of `int` — `True + True == 2`</li></ul> |
| `None` | `None` | <ul><li>Marking "no value yet" — a default placeholder, or what a function returns if it falls through without a `return`</li><li>Compare with `is None`, not `== None`</li><li>`not thing` also catches `None`, but it's true for any falsy value (`0`, `""`, `[]`) too — use `is None` when you mean *specifically* "no value"</li></ul> |

## Integers

An integer (`int`) is a whole number — positive, negative, or zero — with no decimal point.

```python
length = 5

print(length)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Arithmetic

```python-ref
length + 3     # 8
length - 2     # 3
length * 2     # 10
length / 2     # 2.5  (/ always returns a float)
length // 2    # 2    (floor division — drops the remainder)
length % 2     # 1    (modulo — the remainder)
length ** 2    # 25   (exponent)
```

</summary>

The standard math operators work as expected, with two that surprise beginners: `/` (true division) always returns a `float`, even when the numbers divide evenly — use `//` (floor division) if you want an `int` result.

```python
length = 5

print(length + 3)
print(length - 2)
print(length * 2)
print(length / 2)
print(length // 2)
print(length % 2)
print(length ** 2)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Check type

```python-ref
type(length)                # <class 'int'>
isinstance(length, int)     # True
```

</summary>

`type()` shows the exact type; `isinstance()` checks whether a value is that type (or a subclass of it), and is usually the better choice inside an `if`.

```python
length = 5

print(type(length))
print(isinstance(length, int))
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Convert to integer

```python-ref
int("5")      # 5
int(5.9)      # 5   (truncates, doesn't round)
int(True)     # 1
```

</summary>

`int()` converts a string of digits, or truncates a float toward zero (it cuts off the decimal — it does not round).

```python
print(int("5"))
print(int(5.9))
print(int(True))
```

</details>

## Floats

A float is a number with a decimal point — for anything that isn't a whole number.

```python
weight = 4.5

print(weight)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Arithmetic

```python-ref
weight + 1.5    # 6.0
weight / 2      # 2.25
10 / 2          # 5.0  (still a float, even though it divides evenly)
```

</summary>

Floats support the same operators as integers. Notably, `/` always returns a `float` — even `10 / 2`, which divides evenly, gives `5.0`, not `5`.

```python
weight = 4.5

print(weight + 1.5)
print(weight / 2)
print(10 / 2)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Rounding

```python-ref
round(weight)         # 4  (Python rounds .5 to the nearest *even* number)
round(4.567, 2)        # 4.57
```

</summary>

`round()` with no second argument rounds to the nearest whole number — but Python uses "round half to even" (banker's rounding), so `round(4.5)` is `4`, not `5`. Pass a second argument to round to that many decimal places instead.

```python
weight = 4.5
print(round(weight))
print(round(4.567, 2))
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Convert to float

```python-ref
float(5)         # 5.0
float("4.5")      # 4.5
```

</summary>

`float()` converts an integer or a numeric string into a float.

```python
print(float(5))
print(float("4.5"))
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Floating-point precision

```python-ref
0.1 + 0.2    # 0.30000000000000004
```

</summary>

Floats are stored in binary, and most decimal fractions (like `0.1`) can't be represented exactly in binary — so tiny rounding errors creep in during arithmetic. This is a property of floating-point math in virtually every programming language, not a Python bug. If you need exact decimal arithmetic (for money, for example), use the `decimal` module instead of `float`.

```python
print(0.1 + 0.2)
print(round(0.1 + 0.2, 2))
```

</details>

## Strings

A string stores text — a sequence of characters — inside a single variable.

Strings have three defining traits:

- **Ordered** — characters keep the position they're written in.
- **Immutable** — unlike a list, a string can't be changed in place; every "modification" actually builds a new string.
- **Indexable** — since a string is a sequence, it supports the same `[]` indexing and slicing as a list.

```python
name = "burmese python"

print(name)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Access characters

```python-ref
name[0]      # "b"
name[-1]     # "n"
name[0:7]    # "burmese"
```

</summary>

Strings use the same index and slice syntax as lists — `0` for the first character, negative indexes count from the end, and `start:end` slices out a substring.

```python
name = "burmese python"

print(name[0])
print(name[-1])
print(name[0:7])
print(name[8:])
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Concatenate & repeat

```python-ref
"ball" + " " + "python"    # "ball python"
"ball" * 3                  # "ballballball"
```

</summary>

`+` joins strings end to end.

`*` repeats a string a given number of times.

```python
species = "ball"
name = species + " " + "python"
print(name)

print(species * 3)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Format strings

```python-ref
f"the {species} python is about {length} feet long"    # "the ball python is about 5 feet long"
```

</summary>

An f-string (a string literal prefixed with `f`) lets you embed variables and expressions directly inside `{}`, without manually joining pieces with `+`.

```python
species = "ball"
length = 5
sentence = f"the {species} python is about {length} feet long"
print(sentence)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Modify strings

```python-ref
name.upper()          # "BURMESE PYTHON"
name.title()          # "Burmese Python"
"  ball  ".strip()    # "ball"
name.replace("burmese", "ball")   # "ball python"
```

</summary>

`upper()`, `lower()`, and `title()` change letter case — and since strings are immutable, each returns a **new** string rather than changing the original.

`strip()` removes leading and trailing whitespace.

`replace()` swaps every occurrence of one substring for another.

```python
name = "burmese python"

print(name.upper())
print(name.title())

padded = "  ball python  "
print(padded.strip())

print(name.replace("burmese", "ball"))
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Split & join

```python-ref
name.split()                          # ["burmese", "python"]
"-".join(["burmese", "python"])       # "burmese-python"
```

</summary>

`split()` breaks a string into a list, using whitespace as the separator by default.

`join()` does the reverse — it glues a list of strings back together, using the string it's called on as the separator between each item.

```python
name = "burmese python"
parts = name.split()
print(parts)

rejoined = "-".join(parts)
print(rejoined)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Check substring

```python-ref
"python" in name          # True
name.find("python")       # 8
name.count("p")           # 1
```

</summary>

Use `in` to check whether one string contains another.

`find()` returns the index where a substring first appears, or `-1` if it's not found.

`count()` counts how many times a substring appears.

```python
name = "burmese python"

print("python" in name)
print("cobra" in name)

print(name.find("python"))
print(name.count("p"))
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Convert to string

```python-ref
str(5)      # "5"
str(4.5)    # "4.5"
str(True)   # "True"
```

</summary>

`str()` converts almost any value into its text representation — handy any time you need to combine a number with text, since `+` can't join a string and a number directly.

```python
print(str(5))
print(str(4.5))
print(str(True))
```

</details>

## Booleans

A boolean (`bool`) holds one of exactly two values, `True` or `False` — used to represent yes/no, on/off, or the result of a comparison.

```python
venomous = False

print(venomous)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Comparisons return booleans

```python-ref
length = 5
length > 3     # True
length == 5    # True
length != 5    # False
```

</summary>

Every comparison operator (`>`, `<`, `>=`, `<=`, `==`, `!=`) evaluates to a `bool` — this is what powers every `if` statement.

```python
length = 5

print(length > 3)
print(length == 5)
print(length != 5)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Combine booleans

```python-ref
is_python and is_venomous    # True and False → False
is_python or is_venomous     # True or False  → True
not is_venomous              # not False      → True
```

</summary>

`and` is `True` only if both sides are; `or` is `True` if either side is; `not` flips a boolean.

```python
is_python = True
is_venomous = False

print(is_python and is_venomous)
print(is_python or is_venomous)
print(not is_venomous)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Truthy & falsy values

```python-ref
bool(0)       # False
bool("")      # False
bool([])      # False
bool(None)    # False
bool("ball")  # True
bool(5)       # True
```

</summary>

Every value in Python is "truthy" or "falsy" when used somewhere a boolean is expected, like an `if`. Zero, empty strings, empty collections, and `None` are all falsy; almost everything else — including any non-empty string or nonzero number — is truthy.

```python
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(None))

print(bool("ball"))
print(bool(5))
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Bool is a subclass of int

```python-ref
isinstance(True, int)    # True
True + True               # 2
```

</summary>

`bool` is technically a subclass of `int` — `True` behaves like `1` and `False` behaves like `0` in arithmetic, though it's rare to rely on this on purpose.

```python
print(isinstance(True, int))
print(True + True)
```

</details>

## None

`None` represents the absence of a value — Python's way of saying "nothing here," distinct from `0`, `False`, or an empty string.

```python
venomous = None

print(venomous)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Check type

```python-ref
type(venomous)    # <class 'NoneType'>
```

</summary>

`None` is the only value of its own type, `NoneType`.

```python
venomous = None
print(type(venomous))
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Check for None

```python-ref
venomous is None        # True
venomous is not None    # False
```

</summary>

Always compare to `None` with `is` / `is not`, not `==` / `!=` — `is` checks that it's the *exact same object*, which is what you want for a singleton value like `None`, and avoids surprising results from custom `__eq__` methods.

```python
venomous = None

print(venomous is None)
print(venomous is not None)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Functions return None by default

```python-ref
result = find_species("cobra")    # None — the function fell through without a return
```

</summary>

If a function runs to the end without hitting a `return` statement, it returns `None` automatically — this is what you get back if a lookup silently "doesn't find" anything.

```python
def find_species(name):
    if name == "ball":
        return "found it"
    # falls through here for anything else — implicitly returns None

result = find_species("cobra")
print(result)
print(result is None)
```

</details>
