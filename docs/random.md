# random

The **`random`** module generates pseudo-random numbers and makes random selections — rolling a dice, shuffling a deck, or picking a specimen to feature at random. It ships with Python, so no install is needed.

| Function | Returns | Example |
|----------|---------|---------|
| `random()` | A random float between `0.0` and `1.0` | `0.37454` |
| `randint(a, b)` | A random integer, `a` and `b` both included | `randint(1, 6)` → `4` |
| `choice(seq)` | One random item from a sequence | `choice(species)` |
| `shuffle(seq)` | Reorders a list in place, returns `None` | `shuffle(species)` |
| `sample(seq, k)` | `k` unique random items, as a new list | `sample(species, 2)` |

## Random Numbers

`random()` and `randint()` are the two basic building blocks — a random fraction, or a random whole number within a range.

```python
import random

print(random.random())
print(random.randint(1, 6))
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Setting a Seed

```python-ref
random.seed(0)
random.randint(1, 6)    # always 4, whenever the seed is 0
```

</summary>

`random.seed(value)` locks the sequence of "random" numbers that follow it, so the same seed always produces the same results — useful for a reproducible example or a test, where genuine randomness would make output impossible to predict or verify.

```python
import random

random.seed(0)
print(random.randint(1, 6))
print(random.randint(1, 6))
```

</details>

## Random Selections

`choice()` picks one item at random from an existing sequence — no need to generate a number and index into the list by hand.

```python
import random

species = ["ball", "burmese", "boa", "blood"]

print(random.choice(species))
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Shuffling a List

```python-ref
species = ["ball", "burmese", "boa", "blood"]
random.shuffle(species)
species    # e.g. ["boa", "ball", "blood", "burmese"] — order is randomized
```

</summary>

`shuffle()` reorders a list randomly, in place — it returns `None`, so the point is the side effect on `species` itself, not a return value to assign.

```python
import random

species = ["ball", "burmese", "boa", "blood"]
random.shuffle(species)
print(species)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Sampling Without Replacement

```python-ref
species = ["ball", "burmese", "boa", "blood"]
random.sample(species, 2)    # e.g. ["burmese", "blood"] — 2 distinct items
```

</summary>

`sample()` picks several items at once, all guaranteed distinct — unlike calling `choice()` in a loop, which could return the same item twice. The original list is left unchanged; `sample()` returns a new list.

```python
import random

species = ["ball", "burmese", "boa", "blood"]
print(random.sample(species, 2))
```

</details>
