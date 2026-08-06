# :material-repeat:{ .lg .middle } Loops

A **loop** repeats a block of code some number of times. 

All loop definitions end with a colon `:`, and the **block** is the lines indented underneath it that is treated as a single unit. 

**There are two types of loops:**

<div class="pt-jump-table" markdown="block">

| Loop | Syntax | Use it for |
|------|--------|------------|
| [`for`](#for-loops) | `for item in sequence:` | When you know (or can generate) what you're looping over ahead of time:<ul><li>A `range()` — loop a fixed number of times</li><li>A `list` — an ordered, changeable collection of items</li><li>A `tuple` — an ordered collection that can't be changed</li><li>A `dict` — looping gives you the keys (or use `.items()` for key-value pairs)</li><li>A `str` — loops over the string one character at a time</li></ul> |
| [`while`](#while-loops) | `while condition:` | <ul><li>Repeating until something changes — not tied to a fixed collection</li><li>When you don't know in advance how many passes you'll need</li></ul> |

</div>

## For loops

A `for` loop steps through a sequence — a [list](collections.md), tuple, string, or other iterable — running its body once per item, in order.

```python-ref
for i in range(5):
    print(i)
```

### Loop a fixed number of times

`range()` generates a sequence of numbers to loop over. One argument counts up from `0` to (but not including) that number; a second sets a custom `start`; a third sets a `step` size other than `1`. It's the standard way to loop by index instead of by value — or to just repeat something a fixed number of times, using `_` instead of a real variable name when you don't need the number itself.

```python-ref
range(5)          # range(0, 5) — produces 0, 1, 2, 3, 4
range(2, 6)       # start=2, stop=6      — 2, 3, 4, 5
range(2, 10, 3)   # start=2, stop=10, step=3 — 2, 5, 8
```

### Loop over a list

Each pass hands you the item itself, not its position. This is what sets a Python `for` loop apart from the index-counting loops in some other languages. A list is the most common thing to loop over, since it's Python's all-purpose ordered collection.

```python-ref
for s in species: 
    print(s)    # burmese  rock  ball  blood
```

??? tip "Counting matches with a loop"
    Combine `if` with a loop and a counter to count how many items meet a condition. `count` starts at `0`, and the `if` condition is checked once per item — every time it's `True`, `count += 1` adds one. By the end of the loop, `count` holds the total number of matches.

    ```python-ref
    count = 0
    for s in species:
        if s == "ball":
            count += 1
    print(count)   # runs — counts every "ball" in the list
    ```

### Loop over a tuple

Works exactly like looping over a list — a tuple just can't be changed once it's created. Anything you'd loop through in a list, you can loop through the same way in a tuple.

```python-ref
for s in constrictors: 
    print(s)    # ball  burmese  boa
```

### Loop over a dictionary

Looping directly over a dict gives you its keys, one at a time. Use `.values()` to get just the values instead, or `.items()` to get the key and value together — usually the most useful of the three.

```python-ref
for key, value in snake.items(): 
    print(key, value)          # species ball  length_ft 5  venomous False
for key in snake: 
    print(key)                 # species  length_ft  venomous
for value in snake.values(): 
    print(value)               # ball  5  False
```

### Loop over a string

Hands you each character in turn, in order — including spaces. A string is just a sequence of characters, so a `for` loop treats it the same way it treats a list or tuple.

```python-ref
for letter in name: print(letter)    # b  u  r  m  e  s  e     p  y  t  h  o  n
```

### Loop with index and value

`enumerate()` hands you both the index and the value on every pass. It's the usual alternative to looping over `range(len(species))` when you need the position but still want direct access to each item.

```python-ref
for i, s in enumerate(species): print(i, s)    # 0 burmese  1 rock  2 ball  3 blood
```

??? tip "Nested loops"
    A loop can contain another loop — useful for combinations, grids, or nested collections. The inner loop runs all the way through for every single pass of the outer one.

    ```python-ref
    for s in species:
        for letter in s[:2]:
            print(s, letter)
    # burmese b  burmese u  rock r  rock o  ball b  ball a  blood b  blood l
    ```

??? tip "List comprehensions: a for loop in one line"
    A list comprehension builds a new list by running an expression once per item — the same result as a `for` loop that appends to an empty list, written on a single line.

    ```python-ref
    lengths = []
    for s in species:
        lengths.append(len(s))
    lengths                                # [7, 4, 4, 5]

    lengths = [len(s) for s in species]    # same result, one line
    ```

    Add an `if` at the end to only keep items that match a condition:

    ```python-ref
    [s for s in species if s == "ball"]    # ["ball"]
    ```

    Readable for a short, simple transformation — once the logic doesn't fit comfortably on one line, a regular `for` loop is usually clearer. More on that trade-off on the [Style](style.md#comprehensions-vs-loops) page.

??? run "Run a for loop example"
    All the examples above, combined into one script:

    ```python
    for i in range(5):
        print(i)

    for i in range(5):
        print(i)

    # start and stop
    for i in range(2, 6):
        print(i)

    # start, stop, and step
    for i in range(2, 10, 3):
        print(i)

    # just repeat 3 times — the value itself isn't needed, so use _
    for _ in range(3):
        print("hiss")

    species = ["burmese", "rock", "ball", "blood"]

    for s in species:
        print(s)

    species = ["ball", "burmese", "ball", "boa", "ball"]

    count = 0
    for s in species:
        if s == "ball":
            count += 1

    print(count)

    constrictors = ("ball", "burmese", "boa")

    for s in constrictors:
        print(s)

    snake = {"species": "ball", "length_ft": 5, "venomous": False}

    # 1. Loop through both keys and values (recommended)
    for key, value in snake.items():
        print(f"{key}: {value}")

    # 2. Loop through keys only
    for key in snake:
        print(key)

    # 3. Loop through values only
    for value in snake.values():
        print(value)

    name = "burmese python"

    for letter in name:
        print(letter)

    species = ["burmese", "rock", "ball", "blood"]

    for i, s in enumerate(species):
        print(i, s)

    species = ["ball", "burmese"]

    for s in species:
        for letter in s[:2]:
            print(s, letter)
    ```

## While loops

A `while` loop repeats its body for as long as a condition stays `True` — checked again before every pass — so it's the right choice when you don't know ahead of time how many times you'll need to loop.

```python-ref
count = 0

while count < 3:
    print(count)
    count += 1
```

??? warning "Avoiding infinite loops"
    A `while` loop repeats forever unless something inside it moves the condition toward `False`. Nothing stops it automatically, and it freezes whatever's running it — always make sure something inside the loop body moves it toward ending, like incrementing a counter or updating the value being checked.

    ```python-ref
    count = 0
    while count < 3:
        print(count)
        count += 1    # forgetting this line means count < 3 is always True
    ```

??? run "Run a while loop example"
    All the examples above, combined into one script:

    ```python
    count = 0

    while count < 3:
        print(count)
        count += 1

    count = 0
    while count < 3:
        print(count)
        count += 1
    ```

## Loop control

A `for` loop and a `while` loop can both be redirected mid-run — cut short, skipped ahead by one pass, or wrapped up with a bit of code that only runs if nothing interrupted them. These keywords work identically in either loop type.

```python-ref
species = ["burmese", "rock", "ball", "blood"]

for s in species:
    if s == "ball":
        break
    print(s)
```

### Break

Exits the loop immediately, skipping everything left in it. Nothing after it runs, and anything left in the sequence (or any remaining passes of the condition) is skipped entirely.

```python-ref
for s in species:
    if s == "ball":
        break
    print(s)                     # burmese  rock

count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1                   # 0  1  2
```

### Continue

Skips just the current pass, then keeps looping. The rest of the loop body doesn't run for that item, but the loop itself keeps going from the next item or the next check of the condition.

```python-ref
for s in species:
    if s == "ball":
        continue
    print(s)                     # burmese  rock  blood

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)                 # 1  2  4  5
```

??? note "The else clause"
    Runs once the loop finishes on its own — skipped entirely if `break` cut it short. Both `for` and `while` can end with an `else` block.

    ```python-ref
    for s in species:
        print(s)
    else:
        print("done")                # burmese  rock  ball  blood  done

    count = 0
    while count < 3:
        print(count)
        count += 1
    else:
        print("done")                # 0  1  2  done
    ```

??? tip "The pass statement"
    A no-op placeholder for an empty loop body, which Python doesn't otherwise allow. It's not just for loops — the same trick works while you're still deciding what an `if`, function, etc. should do.

    ```python-ref
    for s in species:
        pass    # does nothing, but keeps the loop syntactically valid
    ```

??? run "Run a loop control example"
    All the examples above, combined into one script:

    ```python
    species = ["burmese", "rock", "ball", "blood"]

    for s in species:
        if s == "ball":
            break
        print(s)

    species = ["burmese", "rock", "ball", "blood"]

    for s in species:
        if s == "ball":
            break
        print(s)

    count = 0
    while count < 5:
        if count == 3:
            break
        print(count)
        count += 1

    species = ["burmese", "rock", "ball", "blood"]

    for s in species:
        if s == "ball":
            continue
        print(s)

    count = 0
    while count < 5:
        count += 1
        if count == 3:
            continue
        print(count)

    species = ["burmese", "rock", "ball", "blood"]

    for s in species:
        print(s)
    else:
        print("done")

    count = 0
    while count < 3:
        print(count)
        count += 1
    else:
        print("done")

    species = ["burmese", "rock", "ball", "blood"]

    for s in species:
        pass

    print("loop finished without doing anything each pass")
    ```
