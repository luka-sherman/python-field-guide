---
description: >-
  Specialized container types beyond list/dict/tuple/set in Python's collections module:
  Counter, defaultdict, namedtuple, deque, OrderedDict, ChainMap, and the User* wrapper
  classes, with runnable examples.
---

# :material-format-list-group:{ .lg .middle } collections library

[Official documentation :material-open-in-new:](https://docs.python.org/3/library/collections.html){ target="_blank" }

!!! note "Not the same as the Collections page"
    This page covers the **`collections` module** — extra container types imported with
    `from collections import ...`. For the built-in `list`, `dict`, `tuple`, and `set` types
    themselves, see [Collections](../collections.md).

The **`collections`** module adds specialized containers with added functionaility on top of the
built-in [`str`](../types.md#strings) [`list`](../collections.md#lists) [`dict`](../collections.md#dictionaries) [`tuple`](../collections.md#tuples) and [`set`](../collections.md#sets).

<div class="pt-jump-table" markdown="block">

| Class | Works with | Example | Use it for |
|-------|------------|---------|------------|
| <a href="#counter">**`Counter`**</a> | `list`, `str`, `tuple`, `dict`, `set`, `range` | <pre><code class="language-python-ref">Counter(species)</code></pre> | Counting how many times each item appears |
| <a href="#defaultdict">**`defaultdict`**</a> | `dict` | <pre><code class="language-python-ref">defaultdict(list)</code></pre> | Grouping items under keys that aren't known ahead of time |
| <a href="#namedtuple">**`namedtuple`**</a> | `tuple`, `list` | <pre><code class="language-python-ref">Snake("ball", 5)</code></pre> | A tuple whose positions have names instead of a mental lookup table |
| <a href="#deque">**`deque`**</a> | `list`, `str`, `tuple`, `dict`, `set`, `range` | <pre><code class="language-python-ref">deque(species)</code></pre> | A queue that's fast to add to or remove from at either end |
| <a href="#ordereddict">**`OrderedDict`**</a> | `dict` | <pre><code class="language-python-ref">OrderedDict(snake)</code></pre> | A dict where order itself matters for `==` comparisons |
| <a href="#chainmap">**`ChainMap`**</a> | `dict` | <pre><code class="language-python-ref">ChainMap(overrides,&#10;  defaults)</code></pre> | Layering overrides on top of defaults without merging them |
| <a href="#user-wrapper-classes">**`UserDict`**</a> | `dict` | <pre><code class="language-python-ref">class C(UserDict): ...</code></pre> | Subclassing dict when overriding a method directly doesn't work |
| <a href="#user-wrapper-classes">**`UserList`**</a> | `list` | <pre><code class="language-python-ref">class C(UserList): ...</code></pre> | Subclassing list when overriding a method directly doesn't work |
| <a href="#user-wrapper-classes">**`UserString`**</a> | `str` | <pre><code class="language-python-ref">class C(UserString): ...</code></pre> | Subclassing str when overriding a method directly doesn't work |

</div>

<div class="pfg-section" markdown="block">

## Install

`collections` ships with Python's standard library — nothing to install.

</div>

<div class="pfg-section" markdown="block">

## Import

Each class is imported individually by name, rather than through a `collections.` prefix —
so the import line differs per class, shown under its own "Import" heading below.

</div>

<div class="pfg-section" markdown="block">

## Counter

`Counter` takes any iterable — a list, string, tuple, dict (its keys), set, or range — of
hashable items (strings, numbers, booleans, other tuples) and returns a dict-like object
mapping each distinct item to how many times it appears.

```python-ref
species = ["ball", "burmese", "ball", "boa", "ball", "burmese"]
counts = Counter(species)
print(counts)  # Counter({'ball': 3, 'burmese': 2, 'boa': 1})
```

### Import

```python-ref
from collections import Counter
```

### Counter operations

#### Count

- **`counts[item]`** looks up an item's count. Missing items return `0` instead of raising
  `KeyError`, unlike indexing a plain dict.

    ```python-ref
    counts["ball"]         # 3
    counts["reticulated"]  # 0
    ```

- **`most_common(n)`** returns the `n` highest-count items as `(item, count)` tuples, sorted
  from most to least frequent. Leave out `n` to get all of them.

    ```python-ref
    counts.most_common(2)  # [('ball', 3), ('burmese', 2)]
    ```

- **`total()`** adds up every count into a single number — the same result as
  `sum(counts.values())`.

    ```python-ref
    counts.total()  # 6
    ```

#### Inspect

- **`elements()`** does the reverse of counting — expands a `Counter` back out into an
  iterator that repeats each item by its count.

    ```python-ref
    list(counts.elements())  # ['ball', 'ball', 'ball', 'burmese', 'burmese', 'boa']
    ```

#### Update

- **`update()`** adds more items to an existing `Counter`, incrementing counts instead of
  replacing them — the counting equivalent of a list's `.extend()`. Passing another `Counter`
  (or a plain dict of `item: count`) adds its counts in directly.

    ```python-ref
    counts.update(["ball", "boa"])  # Counter({'ball': 4, 'burmese': 2, 'boa': 2})
    ```

- **`subtract()`** is `update()`'s counting-down counterpart — decrements in place instead of
  returning a new `Counter`, and allows counts to go negative.

    ```python-ref
    counts.subtract({"ball": 1, "cobra": 1})  # ball: 3, cobra: -1
    ```

#### Combine

- **`+` / `-` / `&` / `|`** combine two `Counter` objects item by item, returning a new one:
  add counts, subtract counts (dropping anything that would go negative), take the minimum of
  each count, or the maximum.

    ```python-ref
    more_counts = Counter({"ball": 1, "boa": 3})
    counts + more_counts  # Counter({'boa': 3, 'ball': 3, 'burmese': 1})
    counts - more_counts  # Counter({'ball': 1}) — burmese/boa dropped, not negative
    ```

??? run "Practice with Counter"
    Each box below is fully editable — write your answer, then click Run.

    **1. Count items.** Build a `Counter` from `species`, then print how many times `"cobra"` appears.

    ```python
    from collections import Counter

    species = ["cobra", "viper", "cobra", "mamba", "cobra"]

    # your code here
    ```

    **2. Most common.** Print the single most common item, as a `(item, count)` tuple.

    ```python
    from collections import Counter

    species = ["cobra", "viper", "cobra", "mamba", "cobra"]
    counts = Counter(species)

    # your code here
    ```

    **3. Update and total.** Add `["viper", "viper"]` into `counts`, then print the total number of items counted.

    ```python
    from collections import Counter

    species = ["cobra", "viper", "cobra", "mamba", "cobra"]
    counts = Counter(species)

    # your code here
    ```

    ??? note "Show solutions"
        ```python
        # 1. Count items
        from collections import Counter

        species = ["cobra", "viper", "cobra", "mamba", "cobra"]
        counts = Counter(species)
        print(counts["cobra"])
        ```
        ```python
        # 2. Most common
        from collections import Counter

        species = ["cobra", "viper", "cobra", "mamba", "cobra"]
        counts = Counter(species)
        print(counts.most_common(1))
        ```
        ```python
        # 3. Update and total
        from collections import Counter

        species = ["cobra", "viper", "cobra", "mamba", "cobra"]
        counts = Counter(species)
        counts.update(["viper", "viper"])
        print(counts.total())
        ```

</div>

<div class="pfg-section" markdown="block">

## defaultdict

A plain `dict` raises `KeyError` when indexing a missing key. `defaultdict` instead takes
a **`default_factory`** — a type like `list`/`int`/`set`, or any other zero-argument callable
— and calls it to create a value the first time a new key is used.

```python-ref
by_venomous = defaultdict(list)

snakes = [
    {"species": "ball", "venomous": False},
    {"species": "cobra", "venomous": True},
    {"species": "burmese"},    # no "venomous" key — data wasn't recorded
]

for snake in snakes:
    venomous = snake.get("venomous", "unknown")
    by_venomous[venomous].append(snake["species"])

print(by_venomous)
# defaultdict(<class 'list'>, {False: ['ball'], True: ['cobra'], 'unknown': ['burmese']})
```

### Import

```python-ref
from collections import defaultdict
```

### Reading vs. writing

- **`snake.get("venomous", "unknown")`** only *reads* — it falls back to `"unknown"` for the
  burmese python's missing key instead of raising `KeyError`, the way `snake["venomous"]`
  would. It doesn't touch `by_venomous` at all.

    ```python-ref
    snake.get("venomous", "unknown")  # "unknown"
    ```

- **`by_venomous[venomous]`** is a *write*: appending to a list that has to exist first. A
  plain dict's `.get()` can't help there — `by_venomous.get(venomous, []).append(...)` would
  append to a throwaway list that's never stored back in `by_venomous`, silently losing the
  item. `defaultdict` makes that write safe: indexing a key it hasn't seen before both creates
  the empty list *and* stores it, so `.append()` actually sticks — no
  `if venomous not in by_venomous: by_venomous[venomous] = []` check needed first.

- **`defaultdict(lambda: "unknown")`** shows the factory doesn't have to be a container type
  — any zero-argument callable works, so a `lambda` covers a scalar default too.

    ```python-ref
    by_species = defaultdict(lambda: "unknown")
    by_species["cobra"]  # "unknown" — created on first access, not a KeyError
    ```

??? run "Practice with defaultdict"
    Each box below is fully editable — write your answer, then click Run.

    **1. Group by key.** Group `snakes` into a `defaultdict(list)` keyed by `"family"`, then print the whole result.

    ```python
    from collections import defaultdict

    snakes = [
        {"species": "cobra", "family": "elapid"},
        {"species": "viper", "family": "viperid"},
        {"species": "mamba", "family": "elapid"},
    ]

    # your code here
    ```

    **2. Count with a factory.** Build a `defaultdict(int)` counting how many snakes are in each family — increment `by_family[family] += 1` inside the loop.

    ```python
    from collections import defaultdict

    snakes = [
        {"species": "cobra", "family": "elapid"},
        {"species": "viper", "family": "viperid"},
        {"species": "mamba", "family": "elapid"},
    ]

    # your code here
    ```

    ??? note "Show solutions"
        ```python
        # 1. Group by key
        from collections import defaultdict

        snakes = [
            {"species": "cobra", "family": "elapid"},
            {"species": "viper", "family": "viperid"},
            {"species": "mamba", "family": "elapid"},
        ]

        by_family = defaultdict(list)
        for snake in snakes:
            by_family[snake["family"]].append(snake["species"])
        print(by_family)
        ```
        ```python
        # 2. Count with a factory
        from collections import defaultdict

        snakes = [
            {"species": "cobra", "family": "elapid"},
            {"species": "viper", "family": "viperid"},
            {"species": "mamba", "family": "elapid"},
        ]

        by_family = defaultdict(int)
        for snake in snakes:
            by_family[snake["family"]] += 1
        print(by_family)
        ```

</div>

<div class="pfg-section" markdown="block">

## namedtuple

Builds a tuple subclass whose fields can be accessed by name (`snake.species`) as well as
by position (`snake[0]`) — a lightweight alternative to a full class when all it needs to
hold is a fixed group of fields.

```python-ref
Snake = namedtuple("Snake", ["species", "length_ft"])
snake = Snake("ball", 5)

print(snake.species)    # "ball"
print(snake.length_ft)  # 5
print(snake[0])          # "ball" — still works by position too
```

Like a plain tuple, a `namedtuple` instance is immutable — there's no `snake.length_ft = 6`.

### Import

```python-ref
from collections import namedtuple
```

### namedtuple operations

#### Create

- **`namedtuple(name, fields)`** — `fields` can be a list of strings, or one
  space/comma-separated string (`"species length_ft"`).

    ```python-ref
    Snake = namedtuple("Snake", ["species", "length_ft", "venomous"])
    ```

- **`defaults=`** gives fields a default value, applied to the rightmost fields first — the
  same rule as default arguments on a regular function.

    ```python-ref
    Snake = namedtuple("Snake", ["species", "length_ft", "venomous"], defaults=[False])
    snake = Snake("ball", 5)  # venomous defaults to False
    ```

- **`_make(iterable)`** is the classmethod equivalent of `Snake(*iterable)` — builds an
  instance from an existing list or tuple of values, handy when the values are already
  sitting in a sequence (e.g. a CSV row).

    ```python-ref
    row = ["burmese", 12]
    Snake._make(row)  # Snake(species='burmese', length_ft=12, venomous=False)
    ```

#### Convert

- **`_asdict()`** converts an instance to a regular dict.

    ```python-ref
    snake._asdict()  # {'species': 'ball', 'length_ft': 5, 'venomous': False}
    ```

- **`_replace()`** returns a new instance with some fields changed, since the original can't
  be mutated.

    ```python-ref
    snake._replace(length_ft=6)  # Snake(species='ball', length_ft=6, venomous=False)
    ```

#### Inspect

- **`_fields`** lists the field names; **`_field_defaults`** reports the defaults as a dict,
  the same information `defaults=` set, mapped back to field names.

    ```python-ref
    Snake._fields          # ('species', 'length_ft', 'venomous')
    Snake._field_defaults  # {'venomous': False}
    ```

??? run "Practice with namedtuple"
    Each box below is fully editable — write your answer, then click Run.

    **1. Create and access.** Build a `Snake` namedtuple with fields `species` and `length_ft`, make one for `"boa"` at `8` feet, then print `.species`.

    ```python
    from collections import namedtuple

    # your code here
    ```

    **2. Replace a field.** Using the `snake` from above, create a new instance with `length_ft` changed to `9`, then print it.

    ```python
    from collections import namedtuple

    Snake = namedtuple("Snake", ["species", "length_ft"])
    snake = Snake("boa", 8)

    # your code here
    ```

    **3. Convert to a dict.** Print `snake` as a regular dict.

    ```python
    from collections import namedtuple

    Snake = namedtuple("Snake", ["species", "length_ft"])
    snake = Snake("boa", 8)

    # your code here
    ```

    ??? note "Show solutions"
        ```python
        # 1. Create and access
        from collections import namedtuple

        Snake = namedtuple("Snake", ["species", "length_ft"])
        snake = Snake("boa", 8)
        print(snake.species)
        ```
        ```python
        # 2. Replace a field
        from collections import namedtuple

        Snake = namedtuple("Snake", ["species", "length_ft"])
        snake = Snake("boa", 8)
        updated = snake._replace(length_ft=9)
        print(updated)
        ```
        ```python
        # 3. Convert to a dict
        from collections import namedtuple

        Snake = namedtuple("Snake", ["species", "length_ft"])
        snake = Snake("boa", 8)
        print(snake._asdict())
        ```

</div>

<div class="pfg-section" markdown="block">

## deque

Pronounced "deck" — short for "double-ended queue." A `deque` works like a list, but adding or removing items
from the front (`appendleft()`, `popleft()`) is fast, where doing the same on a plain list
requires shifting every other item over. It's built from any iterable — a list, string,
tuple, dict (its keys), set, or range — the same as calling `list()` on one.

```python-ref
queue = deque(["ball", "burmese", "boa"])

queue.append("cobra")      # add to the right end
queue.appendleft("blood")  # add to the left end

print(queue)  # deque(['blood', 'ball', 'burmese', 'boa', 'cobra'])
```

### Import

```python-ref
from collections import deque
```

### deque operations

#### Add

- **`append()` / `appendleft()`** add one item to the right or left end.

    ```python-ref
    queue.append("viper")
    queue.appendleft("krait")
    ```

- **`extend()` / `extendleft()`** add several items at once. `extendleft()` reverses the
  order it's given, since each item is pushed to the front one at a time.

    ```python-ref
    queue.extend(["cobra", "viper"])       # add several to the right
    queue.extendleft(["ball", "blood"])    # add several to the left, one at a time
    ```

- **`insert()`** adds one item at a specific index, exactly like a list's `insert()`.

    ```python-ref
    queue.insert(1, "viper")
    ```

#### Remove

- **`pop()` / `popleft()`** remove and return the item from the right or left end.

    ```python-ref
    queue.pop()       # removes and returns the last item
    queue.popleft()   # removes and returns the first item
    ```

- **`remove()` / `clear()`** work exactly like their list equivalents: delete the first
  matching value, or empty the deque out entirely.

    ```python-ref
    queue.remove("boa")
    queue.clear()
    ```

#### Inspect

- **`count()` / `index()`** count occurrences of a value, or find its first position — same
  as on a list.

    ```python-ref
    queue.count("ball")
    queue.index("cobra")
    ```

- **`copy()`** makes an independent copy — same as on a list.

    ```python-ref
    backup = queue.copy()
    ```

#### Reorder

- **`rotate(n)`** shifts every item `n` places to the right (or left, with a negative `n`),
  wrapping the ones that fall off the end back around to the other side.

    ```python-ref
    queue.rotate(1)
    ```

- **`reverse()`** flips the order in place — same as on a list.

    ```python-ref
    queue.reverse()
    ```

- **`maxlen=`**, passed when creating the deque, caps it at a fixed size. If the starting
  iterable already has more than `maxlen` items, only the last `maxlen` of them are kept —
  the earlier ones are cut from the front, as if they'd already scrolled off.

    ```python-ref
    recent = deque(["ball", "burmese", "boa", "cobra"], maxlen=3)
    print(recent)  # deque(['burmese', 'boa', 'cobra'], maxlen=3) — "ball" was cut
    ```

  Once full, adding to either end drops one item off the *other* end to make room, which
  makes it a ready-made "last `n` seen" tracker. Which side gets dropped depends on which
  side you add to:

    ```python-ref
    recent = deque(["ball", "burmese", "boa"], maxlen=3)

    recent.append("cobra")      # adds to the right — drops from the left
    print(recent)  # deque(['burmese', 'boa', 'cobra'], maxlen=3) — "ball" dropped

    recent.appendleft("krait")  # adds to the left — drops from the right
    print(recent)  # deque(['krait', 'burmese', 'boa'], maxlen=3) — "cobra" dropped
    ```

??? run "Practice with deque"
    Each box below is fully editable — write your answer, then click Run.

    **1. Add to both ends.** Build a `deque` from `["burmese", "boa"]`, append `"cobra"` to the right, and `"ball"` to the left. Print the result.

    ```python
    from collections import deque

    # your code here
    ```

    **2. Pop from both ends.** Using the deque above, pop one item from the right and one from the left, then print both.

    ```python
    from collections import deque

    queue = deque(["ball", "burmese", "boa", "cobra"])

    # your code here
    ```

    **3. Bounded queue.** Build a `deque` with `maxlen=2`, append `"ball"`, `"burmese"`, and `"boa"` one at a time, then print the final result.

    ```python
    from collections import deque

    # your code here
    ```

    ??? note "Show solutions"
        ```python
        # 1. Add to both ends
        from collections import deque

        queue = deque(["burmese", "boa"])
        queue.append("cobra")
        queue.appendleft("ball")
        print(queue)
        ```
        ```python
        # 2. Pop from both ends
        from collections import deque

        queue = deque(["ball", "burmese", "boa", "cobra"])
        right = queue.pop()
        left = queue.popleft()
        print(right, left)
        ```
        ```python
        # 3. Bounded queue
        from collections import deque

        recent = deque(maxlen=2)
        for species in ["ball", "burmese", "boa"]:
            recent.append(species)
        print(recent)
        ```

</div>

<div class="pfg-section" markdown="block">

## OrderedDict

Until Python 3.7 (released in 2018), a plain `dict` didn't guarantee it would remember insertion order — `OrderedDict` existed specifically to add that guarantee. Now it's mostly seen in legacy code written before 3.7, and in code that specifically needs its reordering functionality.

```python-ref
snake = OrderedDict([("species", "ball"), ("length_ft", 5), ("venomous", False)])
```

### Import

```python-ref
from collections import OrderedDict
```

### OrderedDict operations

#### Reorder

- **`move_to_end(key, last=True)`** relocates an existing key to the back (or, with
  `last=False`, to the front).

    ```python-ref
    snake.move_to_end("species")
    # OrderedDict([('length_ft', 5), ('venomous', False), ('species', 'ball')])
    ```

- **`popitem(last=True)`** removes and returns the last (or first, with `last=False`)
  key-value pair — a plain dict's `popitem()` can only ever take the last one.

    ```python-ref
    snake.popitem(last=False)  # ('species', 'ball')
    ```

#### Compare

- **`==`** checks order as well as contents — two plain dicts with the same items in a
  different order are still equal, but two `OrderedDict` objects aren't.

    ```python-ref
    OrderedDict([("a", 1), ("b", 2)]) == OrderedDict([("b", 2), ("a", 1)])  # False
    ```

</div>

<div class="pfg-section" markdown="block">

## ChainMap

Searches several dicts as if they were one, without copying or merging their contents.
Looking up a key checks each dict in order and returns the first match — useful for layering
a set of overrides on top of a set of defaults, where the underlying dicts might still change
later and should stay separate.

```python-ref
defaults = {"venomous": False, "docile": True}
overrides = {"venomous": True}  # this particular snake is an exception

snake = ChainMap(overrides, defaults)

print(snake["venomous"])  # True — found in overrides, checked first
print(snake["docile"])    # True — not in overrides, falls back to defaults
```

Writing to a `ChainMap` (`snake["docile"] = False`) only ever changes the first dict in the
chain — the rest are left untouched, read-only from the `ChainMap`'s point of view.

### Import

```python-ref
from collections import ChainMap
```

### ChainMap operations

#### Extend

- **`new_child(m)`** returns a new `ChainMap` with `m` (an empty dict by default) added to
  the front — useful for pushing a fresh, temporary layer of overrides on top without
  touching the original.

    ```python-ref
    scoped = snake.new_child({"venomous": None})
    scoped["venomous"]  # None — the new front dict wins
    ```

#### Inspect

- **`.maps`** is the underlying list of dicts, in search order, so it can be inspected or
  edited directly.

    ```python-ref
    snake.maps  # [{'venomous': True}, {'venomous': False, 'docile': True}]
    ```

- **`.parents`** is the reverse of `new_child()`: a new `ChainMap` with the *first* dict
  dropped.

    ```python-ref
    scoped.parents["venomous"]  # True — back to what snake itself would return
    ```

</div>

<div class="pfg-section" markdown="block">

## User\* wrapper classes

`UserDict`, `UserList`, and `UserString` wrap a plain `dict`, `list`, or `str` for
subclassing[^subclassing]. Subclassing `dict`/`list`/`str` directly is possible, but several of their
built-in methods internally bypass any method you've overridden — so an override doesn't
reliably run. The `User*` classes store the real data on a `.data` attribute instead, which
sidesteps that problem, at the cost of being another import.

```python-ref
class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)

snake = CaseInsensitiveDict()
snake["SPECIES"] = "ball"
print(snake)  # {'species': 'ball'} — key was lowercased on the way in
```

### Import

```python-ref
from collections import UserDict, UserList, UserString
```

This is a niche tool — reach for it only when subclassing `dict`, `list`, or `str` directly
turns out not to work, not as a first choice for everyday container code.

[^subclassing]: Defining a new class that inherits from another class, reusing (and
    optionally overriding) its attributes and methods.

</div>

