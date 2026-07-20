# Data Types

## Lists

A list stores multiple items, in order, inside a single variable.

Lists have three defining traits:

- **Ordered** — items keep the position you put them in, unless you explicitly reorder them.
- **Changeable (mutable)** — you can add, remove, or change items after the list is created.
- **Allow duplicates** — since items are accessed by position, not by value, the same value can appear more than once.

```python
species = ["burmese", "rock", "ball", "blood"]

print(species)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Length

```python-ref
len(species)    # 4
```

</summary>

`len()` returns how many items are in a list, and the count updates automatically as you add or remove items.

```python
species = ["burmese", "rock", "ball"]
print(len(species))
species.append("indian")
print(len(species))
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Accessing Items

```python-ref
species[0]      # "burmese"
species[-1]     # "blood"
species[1:3]    # ["rock", "ball"]
```

</summary>

Items are accessed by index, starting at `0` for the first item.

Negative indexes count down from the end, starting at `-1` for the last item.

A slice `list[start:end]` returns a new list containing items from `start` up to (but not including) `end`.

```python
species = ["indian", "rock", "ball", "burmese", "short tailed", "bornean", "angolan", "blood"]

print(species[0])
print(species[2])

print(species[-1])

print(species[1:3])
print(species[:2])
print(species[3:])
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Check if Item in List

```python-ref
"burmese" in species          # True
species.index("burmese")      # 0
species.count("ball")         # 1
```

</summary>

Use `in` to check whether a value exists in a list at all.

`index()` finds the position of the first match; `count()` counts how many times a value appears.

```python
species = ["indian", "rock", "ball", "burmese", "short tailed", "bornean", "angolan", "blood"]

print("burmese" in species)
print("cobra" in species)

print(species.index("burmese"))
print(species.count("ball"))
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Change List Items

```python-ref
species[1] = "carpet"        # ["burmese", "carpet", "ball", "blood"]
species[1:3] = ["carpet"]    # ["burmese", "carpet", "blood"]
species.insert(1, "carpet")  # ["burmese", "carpet", "rock", "ball", "blood"]
```

</summary>

Assign to an index to change a single item.

Assign to a slice to change a whole range at once — the replacement doesn't need to be the same length.

`insert()` adds an item at a specific index without overwriting what's already there.

```python
species = ["ball", "burmese", "blood"]
species[1] = "bornean"
print(species)

species = ["ball", "burmese", "blood", "angolan"]
species[1:3] = ["bornean"]
print(species)

species = ["ball", "burmese", "blood"]
species.insert(1, "bornean")
print(species)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Add List Items

```python-ref
species.append("carpet")                            # ["burmese", "rock", "ball", "blood", "carpet"]
species.insert(0, "carpet")                          # ["carpet", "burmese", "rock", "ball", "blood"]
species.extend(["carpet", "central african rock"])   # ["burmese", "rock", "ball", "blood", "carpet", "central african rock"]
```

</summary>

`append()` adds one item to the end of the list.

`insert()` adds one item at a chosen position.

`extend()` adds every item from another iterable, one at a time — not the iterable itself.

```python
species = ["ball", "blood"]
species.append("burmese")
print(species)

species = ["ball", "blood"]
species.insert(0, "burmese")
print(species)

species = ["ball", "blood"]
more_species = ["bornean", "angolan"]
species.extend(more_species)
print(species)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Remove List Items

```python-ref
species.remove("rock")   # ["burmese", "ball", "blood"]
species.pop()             # "blood" (removed and returned)
del species[0]            # ["rock", "ball", "blood"]
species.clear()           # []
```

</summary>

`remove()` deletes the first item that matches a given value.

`pop()` deletes an item by index and returns it — with no index, it removes the last item.

`del` removes an item by index, or can delete the entire list.

`clear()` empties the list but keeps the (now empty) list around.

```python
species = ["ball", "bornean", "burmese"]
species.remove("bornean")
print(species)

species = ["ball", "bornean", "burmese"]
last = species.pop()
print(last)
print(species)

species = ["ball", "bornean", "burmese"]
del species[0]
print(species)

species = ["ball", "bornean", "burmese"]
species.clear()
print(species)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop Lists

```python-ref
for s in species: print(s)                        # burmese  rock  ball  blood
for i, s in enumerate(species): print(i, s)        # 0 burmese  1 rock  2 ball  3 blood
i = 0
while i < len(species): print(species[i]); i += 1  # same output as the for loop
```

</summary>

The most common way to loop is directly over the items.

`enumerate()` gives you the index and the value together, which is handy when you need both.

A `while` loop works too, if you'd rather manage the index yourself.

```python
species = ["ball", "bornean", "burmese"]

for snake in species:
    print(snake)

for index, snake in enumerate(species):
    print(index, snake)

i = 0
while i < len(species):
    print(species[i])
    i += 1
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### List Comprehension

```python-ref
[s for s in species if len(s) > 4]    # ["burmese", "blood"]
[s.title() for s in species]          # ["Burmese", "Rock", "Ball", "Blood"]
```

</summary>

List comprehension builds a new list from an existing iterable in a single line.

The expression part can transform each item, not just filter it.

```python
species = ["indian", "rock", "ball", "burmese", "short tailed", "bornean", "angolan", "blood"]
long_names = [s for s in species if len(s) > 10]
print(long_names)

species = ["ball", "burmese", "blood"]
titled = [s.title() for s in species]
print(titled)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Sort Lists

```python-ref
species.sort()               # ["ball", "blood", "burmese", "rock"]
species.sort(reverse=True)   # ["rock", "burmese", "blood", "ball"]
sorted(species)               # same as sort() above, but returns a new list
species.sort(key=len)        # ["rock", "ball", "blood", "burmese"]
species.reverse()            # ["blood", "ball", "rock", "burmese"]
```

</summary>

`sort()` sorts a list in place, alphabetically (or ascending, for numbers) by default.

Pass `reverse=True` to sort in the opposite order.

`sorted()` does the same job but returns a new list, leaving the original untouched.

A `key` function controls what each item is sorted by — here, by name length instead of alphabetically.

`reverse()` is different from `sort(reverse=True)` — it just flips the current order in place, without sorting.

```python
species = ["ball", "burmese", "blood", "angolan"]
species.sort()
print(species)

species = ["ball", "burmese", "blood", "angolan"]
species.sort(reverse=True)
print(species)

species = ["ball", "burmese", "blood", "angolan"]
result = sorted(species)
print(result)
print(species)

species = ["ball", "burmese", "blood", "angolan"]
species.sort(key=len)
print(species)

species = ["ball", "burmese", "blood", "angolan"]
species.reverse()
print(species)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Copy Lists

```python-ref
same_list = species          # same_list and species are the same list — mutating one mutates both
backup = species.copy()      # backup is a separate, independent list
```

</summary>

Writing `new_list = old_list` does **not** copy the list — both names point to the same list, so a change through either name shows up in both.

`copy()` (or `list()`, or a full slice `[:]`) makes a real, independent copy.

```python
species = ["ball", "blood"]
same_list = species
same_list.append("burmese")
print(species)

species = ["ball", "blood"]
backup = species.copy()
backup.append("burmese")
print(species)
print(backup)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Join Lists

```python-ref
constrictors + short_tailed        # ["ball", "burmese", "sumatran short tailed", "myanmar short tailed"]
constrictors.extend(short_tailed)  # constrictors now holds all 4, in place
```

</summary>

The `+` operator concatenates two lists into a new one.

`extend()` does the same thing in place, adding onto the first list instead of creating a new one.

```python
constrictors = ["ball", "burmese"]
short_tailed = ["sumatran short tailed", "myanmar short tailed"]
combined = constrictors + short_tailed
print(combined)

constrictors = ["ball", "burmese"]
short_tailed = ["sumatran short tailed", "myanmar short tailed"]
constrictors.extend(short_tailed)
print(constrictors)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Check Type

```python-ref
type(species)                        # <class 'list'>
list(("burmese", "rock", "ball"))    # ["burmese", "rock", "ball"]
```

</summary>

A list can hold mixed data types — `type()` still reports it as one `list` object.

You can also build a list with the `list()` constructor instead of square brackets.

```python
python_info = ["ball", 3, True]  # name, average length in feet, beginner-friendly
print(python_info)
print(type(python_info))

species = list(("ball", "burmese", "blood"))
print(species)
```

</details>

### List Exercises

??? note "Details & examples"
    Each box below is fully editable — write your answer, then click Run.

    **1. Add an item.** Add `"blood"` to the end of the list.

    ```python
    species = ["ball", "burmese", "bornean"]

    # your code here

    print(species)
    ```

    **2. Remove an item.** Remove `"bornean"` from the list.

    ```python
    species = ["ball", "bornean", "burmese"]

    # your code here

    print(species)
    ```

    **3. Sort descending.** Sort the list from Z to A.

    ```python
    species = ["ball", "burmese", "blood", "angolan", "bornean"]

    # your code here

    print(species)
    ```

    **4. List comprehension.** Build a list of just the names longer than 10 characters.

    ```python
    species = ["indian", "central african rock", "ball", "south african rock", "blood"]

    # your code here

    print(long_names)
    ```

    ??? note "Show solutions"
        ```python
        # 1. Add an item
        species = ["ball", "burmese", "bornean"]
        species.append("blood")
        print(species)
        ```
        ```python
        # 2. Remove an item
        species = ["ball", "bornean", "burmese"]
        species.remove("bornean")
        print(species)
        ```
        ```python
        # 3. Sort descending
        species = ["ball", "burmese", "blood", "angolan", "bornean"]
        species.sort(reverse=True)
        print(species)
        ```
        ```python
        # 4. List comprehension
        species = ["indian", "central african rock", "ball", "south african rock", "blood"]
        long_names = [s for s in species if len(s) > 10]
        print(long_names)
        ```

# Dictionaries

A dictionary stores data as key-value pairs, inside a single variable.

Dictionaries have three defining traits:

- **Ordered** — items keep the order they were inserted in.
- **Changeable (mutable)** — you can add, remove, or change items after the dictionary is created.
- **No duplicate keys** — a key can only appear once; assigning to an existing key overwrites its value.

```python
snake = {
    "species": "ball", 
    "length_ft": 5, 
    "venomous": False
}

print(snake)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Access Items

```python-ref
snake["species"]            # "ball"
snake.get("venomous")       # False
snake.keys()                # dict_keys(['species', 'length_ft', 'venomous'])
"species" in snake          # True
```

</summary>

Values are accessed by key, in square brackets — unlike a list, there's no numeric position to use.

`get()` does the same thing, but returns `None` (or a default you choose) instead of raising an error if the key is missing.

`keys()`, `values()`, and `items()` return view objects over the dictionary's keys, values, or key-value pairs.

Use `in` to check whether a key exists at all.

```python
snake = {"species": "ball", "length_ft": 5, "venomous": False}

print(snake["species"])
print(snake.get("venomous"))

print(snake.keys())
print(snake.values())
print(snake.items())

print("species" in snake)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Change Items

```python-ref
snake["length_ft"] = 6                              # {'species': 'ball', 'length_ft': 6, 'venomous': False}
snake.update({"venomous": False, "docile": True})   # {'species': 'ball', 'length_ft': 5, 'venomous': False, 'docile': True}
```

</summary>

Assign to an existing key to change its value.

`update()` changes one or more keys at once — any key it doesn't recognize gets added instead.

```python
snake = {"species": "ball", "length_ft": 5, "venomous": False}
snake["length_ft"] = 6
print(snake)

snake = {"species": "ball", "length_ft": 5, "venomous": False}
snake.update({"venomous": False, "docile": True})
print(snake)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Add Items

```python-ref
snake["origin"] = "west africa"    # {'species': 'ball', 'length_ft': 5, 'venomous': False, 'origin': 'west africa'}
snake.update({"legless": True})    # {'species': 'ball', 'length_ft': 5, 'venomous': False, 'legless': True}
```

</summary>

Assigning to a key that doesn't exist yet adds it.

`update()` adds a key too, if it isn't already there — the same method covers both adding and changing.

```python
snake = {"species": "ball", "length_ft": 5, "venomous": False}
snake["origin"] = "west africa"
print(snake)

snake = {"species": "ball", "length_ft": 5, "venomous": False}
snake.update({"legless": True})
print(snake)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Remove Items

```python-ref
snake.pop("venomous")   # False (removed and returned)
snake.popitem()         # ('venomous', False) — removes the last inserted pair
del snake["species"]    # {'length_ft': 5, 'venomous': False}
snake.clear()           # {}
```

</summary>

`pop()` removes a key and returns its value.

`popitem()` removes and returns the last inserted key-value pair, as a tuple.

`del` removes a key-value pair by key.

`clear()` empties the dictionary but keeps the (now empty) dictionary around.

```python
snake = {"species": "ball", "length_ft": 5, "venomous": False}
popped = snake.pop("venomous")
print(popped)
print(snake)

snake = {"species": "ball", "length_ft": 5, "venomous": False}
last = snake.popitem()
print(last)
print(snake)

snake = {"species": "ball", "length_ft": 5, "venomous": False}
del snake["species"]
print(snake)

snake = {"species": "ball", "length_ft": 5, "venomous": False}
snake.clear()
print(snake)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop Dictionaries

```python-ref
for key in snake: print(key)                        # species  length_ft  venomous
for value in snake.values(): print(value)           # ball  5  False
for key, value in snake.items(): print(key, value)  # species ball  length_ft 5  venomous False
```

</summary>

Looping directly over a dictionary gives you its keys, one at a time.

Loop over `.values()` to get just the values instead.

Loop over `.items()` to get both the key and the value together.

```python
snake = {"species": "ball", "length_ft": 5, "venomous": False}

for key in snake:
    print(key)

for value in snake.values():
    print(value)

for key, value in snake.items():
    print(key, value)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Copy Dictionaries

```python-ref
same_dict = snake          # same_dict and snake are the same dictionary — mutating one mutates both
backup = snake.copy()      # backup is a separate, independent dictionary
```

</summary>

Writing `new_dict = old_dict` does **not** copy the dictionary — both speciess point to the same dictionary, so a change through either species shows up in both.

`copy()` (or `dict()`) makes a real, independent copy.

```python
snake = {"species": "ball", "length_ft": 5, "venomous": False}
same_dict = snake
same_dict["length_ft"] = 6
print(snake)

snake = {"species": "ball", "length_ft": 5, "venomous": False}
backup = snake.copy()
backup["length_ft"] = 6
print(snake)
print(backup)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Nested Dictionaries

```python-ref
snakes = {"ball": snake, "burmese": {"length_ft": 16, "venomous": False}}
snakes["burmese"]["length_ft"]    # 16
```

</summary>

A dictionary's values can be other dictionaries — useful for grouping related records under one variable, like a whole collection of snakes keyed by species.

Chain square brackets to reach a value nested inside an inner dictionary.

```python
snake = {"species": "ball", "length_ft": 5, "venomous": False}
snakes = {
    "ball": snake,
    "burmese": {"length_ft": 16, "venomous": False},
}

print(snakes["burmese"]["length_ft"])
print(snakes["ball"]["species"])
```

</details>

### Dictionary Exercises

??? note "Details & examples"
    Each box below is fully editable — write your answer, then click Run.

    **1. Add a key.** Add a `"docile"` key set to `True`.

    ```python
    snake = {"species": "ball", "length_ft": 5}

    # your code here

    print(snake)
    ```

    **2. Remove a key.** Remove `"length_ft"` from the dictionary.

    ```python
    snake = {"species": "ball", "length_ft": 5, "venomous": False}

    # your code here

    print(snake)
    ```

    **3. Loop and collect.** Build a list of just the dictionary's keys, using a loop (not `list(snake.keys())`).

    ```python
    snake = {"species": "ball", "length_ft": 5, "venomous": False}
    keys = []

    # your code here

    print(keys)
    ```

    **4. Nested access.** Given the dictionary below, print the burmese python's length.

    ```python
    snakes = {
        "ball": {"length_ft": 5, "venomous": False},
        "burmese": {"length_ft": 16, "venomous": False},
    }

    # your code here
    ```

    ??? note "Show solutions"
        ```python
        # 1. Add a key
        snake = {"species": "ball", "length_ft": 5}
        snake["docile"] = True
        print(snake)
        ```
        ```python
        # 2. Remove a key
        snake = {"species": "ball", "length_ft": 5, "venomous": False}
        del snake["length_ft"]
        print(snake)
        ```
        ```python
        # 3. Loop and collect
        snake = {"species": "ball", "length_ft": 5, "venomous": False}
        keys = []
        for key in snake:
            keys.append(key)
        print(keys)
        ```
        ```python
        # 4. Nested access
        snakes = {
            "ball": {"length_ft": 5, "venomous": False},
            "burmese": {"length_ft": 16, "venomous": False},
        }
        print(snakes["burmese"]["length_ft"])
        ```

# Strings

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

### Access Characters

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

### Concatenate & Repeat

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

### Format Strings

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

### Modify Strings

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

### Split & Join

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

### Check Substring

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

# Integers

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

### Check Type

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

### Convert to Integer

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

# Floats

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

### Convert to Float

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

### Floating-Point Precision

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
