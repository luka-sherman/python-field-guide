---
description: >-
  Rounding, roots, constants, and logarithms in Python with the math module, with runnable
  examples.
---

# :material-square-root-box:{ .lg .middle } math library

[Official documentation :material-open-in-new:](https://docs.python.org/3/library/math.html){ target="_blank" }

The **`math`** module extends Python's built-in arithmetic with functions it doesn't provide directly — square roots, rounding modes, constants like pi, and logarithms.

<div class="pfg-section" markdown="block">

## Setup { data-card-link="skip" }

`math` ships with Python's standard library — nothing to install. The whole module is used through the `math.` prefix, so a plain import is all you need.

```python-ref
import math
```

| Function/constant | Returns | Example |
|--------------------|---------|---------|
| `floor(x)` | Largest integer `<= x` | `floor(6.75)` → `6` |
| `ceil(x)` | Smallest integer `>= x` | `ceil(6.75)` → `7` |
| `sqrt(x)` | Square root of `x` | `sqrt(16)` → `4.0` |
| `pow(x, y)` | `x` raised to `y`, as a float | `pow(4, 2)` → `16.0` |
| `pi` | The constant π | `3.141592653589793` |
| `log(x)`, `log2(x)`, `log10(x)` | Logarithm of `x`, in the given base | `log2(64)` → `6.0` |
| `isclose(a, b)` | Whether `a` and `b` are close enough to count as equal | `isclose(0.1 + 0.2, 0.3)` → `True` |

</div>

<div class="pfg-section" markdown="block">

## Rounding

`floor()` and `ceil()` round down and up to the nearest integer. Unlike the built-in `round()`, they never round to the nearest value — `floor()` always goes down, `ceil()` always goes up.

```python-ref
import math

lengths_ft = [3.5, 12, 4.75]
avg = sum(lengths_ft) / len(lengths_ft)

print(avg)
print(math.floor(avg))
print(math.ceil(avg))
```

### trunc

Chops off the decimal part instead of rounding toward a direction — the same as `floor()` for a positive number, but different for a negative one, where it rounds toward zero instead of down.

```python-ref
math.trunc(6.75)     # 6 — same as floor here
math.trunc(-6.75)    # -6 — floor(-6.75) would be -7
```

??? run "Run a rounding example"
    All the examples above, combined into one script:

    ```python
    import math

    lengths_ft = [3.5, 12, 4.75]
    avg = sum(lengths_ft) / len(lengths_ft)

    print(avg)
    print(math.floor(avg))
    print(math.ceil(avg))

    import math

    print(math.trunc(6.75))
    print(math.trunc(-6.75))
    ```

</div>

<div class="pfg-section" markdown="block">

## Roots and powers

`sqrt()` finds a square root — useful anywhere the Pythagorean theorem shows up, like the diagonal brace of a square enclosure.

```python-ref
import math

side_ft = 4
diagonal = math.sqrt(side_ft ** 2 + side_ft ** 2)

print(diagonal)
```

### pow

Raises a number to a power, same idea as the `**` operator — but `math.pow()` always returns a `float`, even when the inputs are whole numbers, while `**` keeps an integer result an `int`.

```python-ref
side_ft ** 2         # 16 — an int
math.pow(side_ft, 2) # 16.0 — always a float
```

??? tip "Integer square roots with isqrt"
    `math.sqrt()` always returns a `float`, even for a perfect square. `math.isqrt()` works on integers only and rounds down, avoiding any floating-point rounding error.

    ```python-ref
    math.sqrt(50)     # 7.0710678118654755
    math.isqrt(50)    # 7 — rounded down, exact
    ```

??? run "Run a roots and powers example"
    All the examples above, combined into one script:

    ```python
    import math

    side_ft = 4
    diagonal = math.sqrt(side_ft ** 2 + side_ft ** 2)

    print(diagonal)
    print(side_ft ** 2)
    print(math.pow(side_ft, 2))
    ```

</div>

<div class="pfg-section" markdown="block">

## Constants

`math.pi` is the constant π, accurate to the precision of a `float` — no need to type out `3.14159...` by hand.

```python-ref
import math

radius_ft = 3
circumference = 2 * math.pi * radius_ft

print(circumference)
```

??? tip "inf and nan"
    `math.inf` is a value larger than any number, useful as a starting point when searching for a minimum. `math.nan` ("not a number") represents an undefined result, like `0 / 0` in floating-point math — check for it with `math.isnan()`, since `nan == nan` is always `False`.

    ```python-ref
    smallest = math.inf
    for length in [5, 12, 3.5]:
        if length < smallest:
            smallest = length
    smallest    # 3.5

    math.isnan(math.nan)    # True
    ```

??? run "Run a constants example"
    All the examples above, combined into one script:

    ```python
    import math

    radius_ft = 3
    circumference = 2 * math.pi * radius_ft

    print(circumference)

    import math

    smallest = math.inf
    for length in [5, 12, 3.5]:
        if length < smallest:
            smallest = length

    print(smallest)
    print(math.isnan(math.nan))
    ```

</div>

<div class="pfg-section" markdown="block">

## Logarithms

`log2()` is the inverse of doubling — how many times a starting value has to double to reach a target. A breeding program tracking how many generations it takes to go from 2 snakes to 64 is a direct fit.

```python-ref
import math

starting = 2
population = 64

generations = math.log2(population / starting)

print(generations)
```

`log()` and `log10()` work the same way in base *e* and base 10, and `exp()` reverses `log()` — raising *e* to a power.

```python-ref
math.log10(1000)    # 3.0
math.exp(1)          # 2.718281828459045 — the same as math.e
```

??? run "Run a logarithms example"
    All the examples above, combined into one script:

    ```python
    import math

    starting = 2
    population = 64

    generations = math.log2(population / starting)

    print(generations)
    print(math.log10(1000))
    print(math.exp(1))
    ```

</div>

<div class="pfg-section" markdown="block">

## Comparing floats

Floating-point math loses tiny amounts of precision, so two values that should be mathematically equal often aren't exactly equal in code. `math.isclose()` checks whether two numbers are close enough to count as equal instead of comparing them bit for bit.

```python-ref
import math

0.1 + 0.2 == 0.3            # False — a floating-point rounding artifact
math.isclose(0.1 + 0.2, 0.3) # True
```

??? warning "Never compare floats with =="
    `0.1 + 0.2` is actually `0.30000000000000004` under the hood — every float is stored as a binary approximation, and `0.1` can't be represented exactly in binary any more than `1/3` can be written exactly in decimal. `==` compares that approximation exactly, so it fails in cases that look like they should match. `math.isclose()` is the fix any time float results are compared, not just when the numbers came from a fraction like this one.

??? run "Run a comparing floats example"
    All the examples above, combined into one script:

    ```python
    import math

    print(0.1 + 0.2 == 0.3)
    print(math.isclose(0.1 + 0.2, 0.3))
    ```

</div>
