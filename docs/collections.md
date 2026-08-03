# Collections of data

A **collection** is a single object that groups multiple values together, so a whole set of data can be stored in one variable, passed around, and looped over as a unit — instead of juggling a separate variable per value, like you would with the [basic types](types.md). Python's built-in collections mainly differ along two lines: whether items are **ordered** by position or looked up by **key**, and whether the collection is **mutable** (changeable after creation) or not.

| Type | Example | Access values by | Mutable (changeable after creation) | Duplicates allowed | Use it for |
|------|---------|:-----------------:|:-------:|:-------:|------------|
| `list` | `["ball", "burmese"]` | Index | Yes | Yes | <ul><li>Ordered sequence</li><li>Looking up by value (`in`) scans item by item</li></ul> |
| `tuple` | `("ball", "burmese")` | Index | No | Yes | <ul><li>Fixed sequence that shouldn't change — records, dict keys</li></ul> |
| `dict` | `{"species": "ball", ...}` | Key | Yes | No (keys must be unique) | <ul><li>Key → value lookups, records with named fields</li><li>No positional access — only by key</li></ul> |

??? tip "Check type"
    `type()` reports the exact collection type, even one holding mixed data types inside. Works the same way for any collection on this page — and each has its own constructor (`list()`, `tuple()`, `dict()`) if you'd rather build one that way than with literal brackets, parens, or braces.

    ```python-ref
    type(["burmese", "rock"])            # <class 'list'>
    list(("burmese", "rock", "ball"))    # ["burmese", "rock", "ball"]
    ```

## Lists

A list stores multiple items, in order, inside a single variable.

Lists have three defining traits:

- **Ordered** — items keep the position you put them in, unless you explicitly reorder them.
- **Changeable (mutable)** — you can add, remove, or change items after the list is created.
- **Allow duplicates** — since items are accessed by position, not by value, the same value can appear more than once.

```python-ref
species = ["burmese", "rock", "ball", "blood"]
species    # ["burmese", "rock", "ball", "blood"]
```

### Length

`len()` returns how many items are in a list. The count updates automatically as you add or remove items.

```python-ref
len(species)    # 4
```

### Accessing items

Items are accessed by index, starting at `0` for the first item. Negative indexes count down from the end, starting at `-1` for the last item. A slice `list[start:end]` returns a new list containing items from `start` up to (but not including) `end`.

```python-ref
species[0]      # "burmese"
species[-1]     # "blood"
species[1:3]    # ["rock", "ball"]
```

### Check if item in list

`in` checks whether a value exists in a list at all. `index()` finds the position of the first match; `count()` counts how many times a value appears.

```python-ref
"burmese" in species          # True
species.index("burmese")      # 0
species.count("ball")         # 1
```

### Change list items

Assign to an index to change a single item. Assign to a slice to change a whole range at once — the replacement doesn't need to be the same length. `insert()` adds an item at a specific index without overwriting what's already there.

```python-ref
species[1] = "carpet"        # ["burmese", "carpet", "ball", "blood"]
species[1:3] = ["carpet"]    # ["burmese", "carpet", "blood"]
species.insert(1, "carpet")  # ["burmese", "carpet", "rock", "ball", "blood"]
```

### Add list items

`append()` adds one item to the end of the list. `insert()` adds one item at a chosen position. `extend()` adds every item from another iterable, one at a time — not the iterable itself.

```python-ref
species.append("carpet")                             # ["burmese", "rock", "ball", "blood", "carpet"]
species.insert(0, "carpet")                          # ["carpet", "burmese", "rock", "ball", "blood"]
species.extend(["carpet", "central african rock"])   # ["burmese", "rock", "ball", "blood", "carpet", "central african rock"]
```

### Remove list items

`remove()` deletes the first item that matches a given value. `pop()` deletes an item by index and returns it — with no index, it removes the last item. `del` removes an item by index, or can delete the entire list. `clear()` empties the list but keeps the (now empty) list around.

```python-ref
species.remove("rock")    # ["burmese", "ball", "blood"]
species.pop()             # "blood" (removed and returned)
del species[0]            # ["rock", "ball", "blood"]
species.clear()           # []
```

### Loop lists

The most common way to loop is directly over the items. `enumerate()` gives you the index and the value together, which is handy when you need both. A `while` loop works too, if you'd rather manage the index yourself.

```python-ref
for s in species: print(s)                         # burmese  rock  ball  blood
for i, s in enumerate(species): print(i, s)        # 0 burmese  1 rock  2 ball  3 blood
i = 0
while i < len(species): print(species[i]); i += 1  # same output as the for loop
```

??? tip "List comprehension"
    Builds a new list from an existing iterable in a single line. The expression part can transform each item, not just filter it.

    ```python-ref
    [s for s in species if len(s) > 4]    # ["burmese", "blood"]
    [s.title() for s in species]          # ["Burmese", "Rock", "Ball", "Blood"]
    ```

??? tip "Sort lists"
    `sort()` sorts a list in place, alphabetically (or ascending, for numbers) by default. Pass `reverse=True` to sort in the opposite order. `sorted()` does the same job but returns a new list, leaving the original untouched. A `key` function controls what each item is sorted by — here, by name length instead of alphabetically. `reverse()` is different from `sort(reverse=True)` — it just flips the current order in place, without sorting.

    ```python-ref
    species.sort()               # ["ball", "blood", "burmese", "rock"]
    species.sort(reverse=True)   # ["rock", "burmese", "blood", "ball"]
    sorted(species)              # same as sort() above, but returns a new list
    species.sort(key=len)        # ["rock", "ball", "blood", "burmese"]
    species.reverse()            # ["blood", "ball", "rock", "burmese"]
    ```

??? warning "Copy lists"
    Writing `new_list = old_list` does **not** copy the list — both names point to the same list. A change through either name shows up in both. `copy()` (or `list()`, or a full slice `[:]`) makes a real, independent copy.

    ```python-ref
    same_list = species          # same_list and species are the same list — mutating one mutates both
    backup = species.copy()      # backup is a separate, independent list
    ```

### Join lists

The `+` operator concatenates two lists into a new one. `extend()` does the same thing in place, adding onto the first list instead of creating a new one.

```python-ref
constrictors + short_tailed        # ["ball", "burmese", "sumatran short tailed", "myanmar short tailed"]
constrictors.extend(short_tailed)  # constrictors now holds all 4, in place
```

??? run "Run a list example"
    Each box below is fully editable — write your answer, then click Run.

    **1. Access & check membership.** Print the second item in the list (index `1`), then check whether `"rock"` is in it.

    ```python
    species = ["indian", "carpet", "rock", "angolan", "blood"]

    # your code here
    ```

    **2. Change & add.** Change the first item to `"burmese"`, then add `"bornean"` to the end.

    ```python
    species = ["indian", "carpet", "rock", "angolan", "blood"]

    # your code here

    print(species)
    ```

    **3. Remove.** Remove `"carpet"` from the list, then pop the last item and print what was removed.

    ```python
    species = ["indian", "carpet", "rock", "angolan", "blood"]

    # your code here
    ```

    **4. List comprehension.** Build a list of just the names with more than 5 letters.

    ```python
    species = ["indian", "carpet", "rock", "angolan", "blood"]

    # your code here

    print(long_names)
    ```

    **5. Sort.** Sort the list in reverse alphabetical order.

    ```python
    species = ["indian", "carpet", "rock", "angolan", "blood"]

    # your code here

    print(species)
    ```

    ??? note "Show solutions"
        ```python
        # 1. Access & check membership
        species = ["indian", "carpet", "rock", "angolan", "blood"]
        print(species[1])
        print("rock" in species)
        ```
        ```python
        # 2. Change & add
        species = ["indian", "carpet", "rock", "angolan", "blood"]
        species[0] = "burmese"
        species.append("bornean")
        print(species)
        ```
        ```python
        # 3. Remove
        species = ["indian", "carpet", "rock", "angolan", "blood"]
        species.remove("carpet")
        last = species.pop()
        print(last)
        ```
        ```python
        # 4. List comprehension
        species = ["indian", "carpet", "rock", "angolan", "blood"]
        long_names = [s for s in species if len(s) > 5]
        print(long_names)
        ```
        ```python
        # 5. Sort
        species = ["indian", "carpet", "rock", "angolan", "blood"]
        species.sort(reverse=True)
        print(species)
        ```

## Tuples

A tuple stores multiple items, in order, inside a single variable — written with parentheses instead of square brackets.

Tuples have three defining traits:

- **Ordered** — items keep the position you put them in.
- **Immutable** — unlike a list, a tuple can't be changed, added to, or shrunk once created.
- **Allow duplicates** — the same value can appear more than once.

```python-ref
species = ("burmese", "rock", "ball", "blood")
species    # ("burmese", "rock", "ball", "blood")
```

### Access items

Tuples use the same index and slice syntax as lists. `0` for the first item, negative indexes count from the end, `start:end` slices out a sub-tuple.

```python-ref
species[0]      # "burmese"
species[-1]     # "blood"
species[1:3]    # ("rock", "ball")
```

### Check if item in tuple

`in` checks whether a value exists in the tuple. `count()` counts how many times a value appears; `index()` finds the position of the first match — a tuple has only these two methods, since it can't be changed.

```python-ref
"rock" in species          # True
species.count("burmese")   # 1
species.index("ball")      # 2
```

### Unpacking

Assigns each item in a tuple to its own variable in one line. The number of variables has to match the number of items. A [`match` statement](conditionals.md#unpacking-a-tuple) can do this same unpacking while also branching on the tuple's shape or specific values, which plain assignment can't do.

```python-ref
a, b, c, d = species    # a="burmese"  b="rock"  c="ball"  d="blood"
```

??? tip "Work around immutability"
    A tuple has no `append()` or `remove()` — but `+` builds a **new** tuple with an item added. Note the trailing comma in `("carpet",)`, needed to make it a one-item tuple rather than just parentheses around a string. For bigger changes, convert to a list with `list()`, edit it normally, then convert back with `tuple()`.

    ```python-ref
    species + ("carpet",)                          # ("burmese", "rock", "ball", "blood", "carpet")
    tuple(list(species) + ["carpet"])              # same result, via a list round-trip
    ```

### Loop tuples

Works exactly like looping over a list.

```python-ref
for s in species: print(s)    # burmese  rock  ball  blood
```

??? run "Run a tuple example"
    Each box below is fully editable — write your answer, then click Run.

    **1. Access & check membership.** Print the last item, then check whether `"carpet"` is in the tuple.

    ```python
    species = ("indian", "carpet", "rock", "blood")

    # your code here
    ```

    **2. Unpacking.** Unpack the tuple into four variables named `a`, `b`, `c`, `d`, then print them.

    ```python
    species = ("indian", "carpet", "rock", "blood")

    # your code here
    ```

    **3. Work around immutability.** Tuples can't be appended to directly — build a new tuple with `"angolan"` added to the end, using `+`.

    ```python
    species = ("indian", "carpet", "rock", "blood")

    # your code here

    print(species)
    ```

    ??? note "Show solutions"
        ```python
        # 1. Access & check membership
        species = ("indian", "carpet", "rock", "blood")
        print(species[-1])
        print("carpet" in species)
        ```
        ```python
        # 2. Unpacking
        species = ("indian", "carpet", "rock", "blood")
        a, b, c, d = species
        print(a, b, c, d)
        ```
        ```python
        # 3. Work around immutability
        species = ("indian", "carpet", "rock", "blood")
        species = species + ("angolan",)
        print(species)
        ```

## Dictionaries

A dictionary stores data as key-value pairs, inside a single variable.

Dictionaries have three defining traits:

- **Ordered** — items keep the order they were inserted in.
- **Changeable (mutable)** — you can add, remove, or change items after the dictionary is created.
- **No duplicate keys** — a key can only appear once; assigning to an existing key overwrites its value.

```python-ref
snake = {"species": "ball", "length_ft": 5, "venomous": False}
snake    # {'species': 'ball', 'length_ft': 5, 'venomous': False}
```

### Access items

Values are accessed by key, in square brackets — unlike a list, there's no numeric position to use. `get()` does the same thing, but returns `None` (or a default you choose) instead of raising an error if the key is missing. `keys()`, `values()`, and `items()` return view objects over the dictionary's keys, values, or key-value pairs. Use `in` to check whether a key exists at all.

```python-ref
snake["species"]            # "ball"
snake.get("venomous")       # False
snake.keys()                # dict_keys(['species', 'length_ft', 'venomous'])
"species" in snake          # True
```

### Change items

Assign to an existing key to change its value. `update()` changes one or more keys at once — any key it doesn't recognize gets added instead.

```python-ref
snake["length_ft"] = 6                              # {'species': 'ball', 'length_ft': 6, 'venomous': False}
snake.update({"venomous": False, "docile": True})   # {'species': 'ball', 'length_ft': 5, 'venomous': False, 'docile': True}
```

### Add items

Assigning to a key that doesn't exist yet adds it. `update()` adds a key too, if it isn't already there — the same method covers both adding and changing.

```python-ref
snake["origin"] = "west africa"    # {'species': 'ball', 'length_ft': 5, 'venomous': False, 'origin': 'west africa'}
snake.update({"legless": True})    # {'species': 'ball', 'length_ft': 5, 'venomous': False, 'legless': True}
```

### Remove items

`pop()` removes a key and returns its value. `popitem()` removes and returns the last inserted key-value pair, as a tuple. `del` removes a key-value pair by key. `clear()` empties the dictionary but keeps the (now empty) dictionary around.

```python-ref
snake.pop("venomous")   # False (removed and returned)
snake.popitem()         # ('venomous', False) — removes the last inserted pair
del snake["species"]    # {'length_ft': 5, 'venomous': False}
snake.clear()           # {}
```

### Loop dictionaries

Looping directly over a dictionary gives you its keys, one at a time. Loop over `.values()` to get just the values instead, or `.items()` to get both the key and the value together.

```python-ref
for key in snake: print(key)                        # species  length_ft  venomous
for value in snake.values(): print(value)           # ball  5  False
for key, value in snake.items(): print(key, value)  # species ball  length_ft 5  venomous False
```

??? warning "Copy dictionaries"
    Writing `new_dict = old_dict` does **not** copy the dictionary — both names point to the same dictionary. A change through either name shows up in both. `copy()` (or `dict()`) makes a real, independent copy.

    ```python-ref
    same_dict = snake          # same_dict and snake are the same dictionary — mutating one mutates both
    backup = snake.copy()      # backup is a separate, independent dictionary
    ```

??? note "Nested dictionaries"
    A dictionary's values can be other dictionaries. Useful for grouping related records under one variable, like a whole collection of snakes keyed by species. Chain square brackets to reach a value nested inside an inner dictionary.

    ```python-ref
    snakes = {"ball": snake, "burmese": {"length_ft": 16, "venomous": False}}
    snakes["burmese"]["length_ft"]    # 16
    ```

??? run "Run a dictionary example"
    Each box below is fully editable — write your answer, then click Run.

    **1. Add & change.** Add a `"docile"` key set to `True`, then change `"length_ft"` to `16`.

    ```python
    snake = {"species": "burmese", "length_ft": 12, "venomous": False}

    # your code here

    print(snake)
    ```

    **2. Remove.** Remove the `"venomous"` key from the dictionary.

    ```python
    snake = {"species": "burmese", "length_ft": 16, "venomous": False}

    # your code here

    print(snake)
    ```

    **3. Loop and collect.** Build a list of just the dictionary's values, using a loop (not `list(snake.values())`).

    ```python
    snake = {"species": "burmese", "length_ft": 16, "venomous": False}
    values = []

    # your code here

    print(values)
    ```

    **4. Nested access.** Given the dictionary below, print the ball python's length.

    ```python
    snakes = {
        "burmese": {"length_ft": 16, "venomous": False},
        "ball": {"length_ft": 5, "venomous": False},
    }

    # your code here
    ```

    ??? note "Show solutions"
        ```python
        # 1. Add & change
        snake = {"species": "burmese", "length_ft": 12, "venomous": False}
        snake["docile"] = True
        snake["length_ft"] = 16
        print(snake)
        ```
        ```python
        # 2. Remove
        snake = {"species": "burmese", "length_ft": 16, "venomous": False}
        del snake["venomous"]
        print(snake)
        ```
        ```python
        # 3. Loop and collect
        snake = {"species": "burmese", "length_ft": 16, "venomous": False}
        values = []
        for value in snake.values():
            values.append(value)
        print(values)
        ```
        ```python
        # 4. Nested access
        snakes = {
            "burmese": {"length_ft": 16, "venomous": False},
            "ball": {"length_ft": 5, "venomous": False},
        }
        print(snakes["ball"]["length_ft"])
        ```
