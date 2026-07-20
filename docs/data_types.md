# Data Types

## Lists

A list stores multiple items, in order, inside a single variable.

Lists have three defining traits:

- **Ordered** — items keep the position you put them in, unless you explicitly reorder them.
- **Changeable (mutable)** — you can add, remove, or change items after the list is created.
- **Allow duplicates** — since items are accessed by position, not by value, the same value can appear more than once.

```python
species = ["burmese", "rock", "ball", "indian", "short tailed", "bornean", "angolan", "blood"]

print(species)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

#### Length

```python-ref
len(species)    # 10
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
species[1] = "bornean"
species.insert(1, "blood")
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
species.append("burmese")
species.insert(0, "burmese")
species.extend(["angolan", "rock"])
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
species.remove("bornean")
last = species.pop()
del species[0]
species.clear()
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
species = ["ball", "bornean", "burmese"]
for snake in species:
    print(snake)
# ball
# bornean
# burmese
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
species = ["indian", "rock", "ball", "burmese", "short tailed", "bornean", "angolan", "blood"]
[s for s in species if len(s) > 10]
# ["central african rock", "south african rock", "sumatran short tailed", "myanmar short tailed"]
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
species = ["ball", "burmese", "blood", "angolan"]
species.sort()
species    # ["angolan", "ball", "blood", "burmese"]
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
species = ["ball", "blood"]
backup = species.copy()
backup.append("burmese")
species    # ["ball", "blood"] — unaffected
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
constrictors = ["ball", "burmese"]
short_tailed = ["sumatran short tailed", "myanmar short tailed"]
constrictors + short_tailed
# ["ball", "burmese", "sumatran short tailed", "myanmar short tailed"]
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
type(species)    # <class 'list'>
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
