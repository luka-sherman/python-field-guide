# :material-dice-multiple:{ .lg .middle } random library

The **`random`** module generates pseudo-random numbers and makes random selections — rolling a dice, shuffling a deck, or picking a specimen to feature at random.

## Install

`random` ships with Python's standard library — nothing to install.

## Import

The whole module is used through the `random.` prefix, so a plain import is all you need.

```python-ref
import random
```

| Function | Returns | Example |
|----------|---------|---------|
| `random()` | A random float between `0.0` and `1.0` | `0.37454` |
| `randint(a, b)` | A random integer, `a` and `b` both included | `randint(1, 6)` → `4` |
| `choice(seq)` | One random item from a sequence | `choice(species)` |
| `shuffle(seq)` | Reorders a list in place, returns `None` | `shuffle(species)` |
| `sample(seq, k)` | `k` unique random items, as a new list | `sample(species, 2)` |

## Random numbers

`random()` and `randint()` are the two basic building blocks — a random fraction, or a random whole number within a range.

```python-ref
import random

print(random.random())
print(random.randint(1, 6))
```

??? tip "Setting a seed"
    Locks the sequence of "random" numbers that follow it, so the same seed always produces the same results. Useful for a reproducible example or a test, where genuine randomness would make output impossible to predict or verify.

    ```python-ref
    random.seed(0)
    random.randint(1, 6)    # always 4, whenever the seed is 0
    ```

??? run "Run a random numbers example"
    All the examples above, combined into one script:

    ```python
    import random

    print(random.random())
    print(random.randint(1, 6))

    import random

    random.seed(0)
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    ```

## Random selections

`choice()` picks one item at random from an existing sequence — no need to generate a number and index into the list by hand.

```python-ref
import random

species = ["ball", "burmese", "boa", "blood"]

print(random.choice(species))
```

### Shuffling a list

Reorders a list randomly, in place. `shuffle()` returns `None`, so the point is the side effect on `species` itself, not a return value to assign.

```python-ref
species = ["ball", "burmese", "boa", "blood"]
random.shuffle(species)
species    # e.g. ["boa", "ball", "blood", "burmese"] — order is randomized
```

### Sampling without replacement

Picks several items at once, all guaranteed distinct. Unlike calling `choice()` in a loop, which could return the same item twice. The original list is left unchanged; `sample()` returns a new list.

```python-ref
species = ["ball", "burmese", "boa", "blood"]
random.sample(species, 2)    # e.g. ["burmese", "blood"] — 2 distinct items
```

??? run "Run a random selections example"
    All the examples above, combined into one script:

    ```python
    import random

    species = ["ball", "burmese", "boa", "blood"]

    print(random.choice(species))

    import random

    species = ["ball", "burmese", "boa", "blood"]
    random.shuffle(species)
    print(species)

    import random

    species = ["ball", "burmese", "boa", "blood"]
    print(random.sample(species, 2))
    ```
