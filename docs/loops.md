# Loops

A **loop** repeats a block of code, so you don't have to write out the same steps by hand for every item or every pass. Python has two: a **for loop**, which runs once per item in a sequence, and a **while loop**, which keeps running for as long as a condition stays `True`.

| Loop | Syntax | Use it for |
|------|--------|------------|
| `for` | `for item in sequence:` | When you know (or can generate) what you're looping over ahead of time:<ul><li>A `range()` — loop a fixed number of times</li><li>A `list` — an ordered, changeable collection of items</li><li>A `tuple` — an ordered collection that can't be changed</li><li>A `dict` — looping gives you the keys (or use `.items()` for key-value pairs)</li><li>A `str` — loops over the string one character at a time</li></ul> |
| `while` | `while condition:` | <ul><li>Repeating until something changes — not tied to a fixed collection</li><li>When you don't know in advance how many passes you'll need</li></ul> |

## For Loops

A `for` loop steps through a sequence — a [list](collections.md), tuple, string, or other iterable — running its body once per item, in order.

```python
species = ["burmese", "rock", "ball", "blood"]

for snake in species:
    print(snake)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop a Fixed Number of Times

```python-ref
range(5)          # range(0, 5) — produces 0, 1, 2, 3, 4
range(2, 6)       # 2, 3, 4, 5
range(2, 10, 3)   # 2, 5, 8  (step of 3)
```

</summary>

`range()` generates a sequence of numbers without building a whole list in memory. One argument counts up from `0` to (but not including) that number; a second sets a custom start; a third sets a step size other than `1`. It's the standard way to loop a fixed number of times, or to loop by index instead of by value.

```python
for i in range(5):
    print(i)

for i in range(2, 6):
    print(i)

for i in range(2, 10, 3):
    print(i)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop Over a List

```python-ref
for s in species: 
    print(s)    # burmese  rock  ball  blood
```

</summary>

Each pass hands you the item itself, not its position — this is what sets a Python `for` loop apart from the index-counting loops in some other languages. A list is the most common thing to loop over, since it's Python's all-purpose ordered collection.

```python
species = ["burmese", "rock", "ball", "blood"]

for s in species:
    print(s)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop Over a Tuple

```python-ref
for s in constrictors: 
    print(s)    # ball  burmese  boa
```

</summary>

Looping over a tuple works exactly like looping over a list — the only difference is that a tuple can't be changed once it's created.

```python
constrictors = ("ball", "burmese", "boa")

for s in constrictors:
    print(s)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop Over a Dictionary

```python-ref
for key, value in snake.items(): 
    print(key, value)          # species ball  length_ft 5  venomous False
for key in snake: 
    print(key)                 # species  length_ft  venomous
for value in snake.values(): 
    print(value)               # ball  5  False
```

</summary>

Looping directly over a dictionary gives you its keys, one at a time. Use `.values()` to get just the values instead, or `.items()` to get the key and value together — usually the most useful of the three.

```python
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
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop Over a String

```python-ref
for letter in name: print(letter)    # b  u  r  m  e  s  e     p  y  t  h  o  n
```

</summary>

A string is just a sequence of characters, so looping over one hands you each character in turn, in order — including spaces.

```python
name = "burmese python"

for letter in name:
    print(letter)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop With Index and Value

```python-ref
for i, s in enumerate(species): print(i, s)    # 0 burmese  1 rock  2 ball  3 blood
```

</summary>

`enumerate()` hands you both the index and the value on every pass — the usual alternative to looping over `range(len(species))` when you need the position but still want direct access to each item.

```python
species = ["burmese", "rock", "ball", "blood"]

for i, s in enumerate(species):
    print(i, s)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Nested Loops

```python-ref
for s in species:
    for letter in s[:2]:
        print(s, letter)
# burmese b  burmese u  rock r  rock o  ball b  ball a  blood b  blood l
```

</summary>

A loop can contain another loop — the inner loop runs all the way through for every single pass of the outer one. Useful for combinations, grids, or looping over a collection nested inside another collection.

```python
species = ["ball", "burmese"]

for s in species:
    for letter in s[:2]:
        print(s, letter)
```

</details>

## While Loops

A `while` loop repeats its body for as long as a condition stays `True` — checked again before every pass — so it's the right choice when you don't know ahead of time how many times you'll need to loop.

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Avoiding Infinite Loops

```python-ref
count = 0
while count < 3:
    print(count)
    count += 1    # forgetting this line means count < 3 is always True
```

</summary>

Nothing stops a `while` loop automatically — if its condition never becomes `False`, it repeats forever and freezes whatever's running it. Always make sure something inside the loop body moves it toward ending, like incrementing a counter or updating the value being checked.

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

</details>

## Loop Control

A `for` loop and a `while` loop can both be redirected mid-run — cut short, skipped ahead by one pass, or wrapped up with a bit of code that only runs if nothing interrupted them. These keywords work identically in either loop type.

```python
species = ["burmese", "rock", "ball", "blood"]

for s in species:
    if s == "ball":
        break
    print(s)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Break

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

</summary>

`break` exits the loop immediately — nothing after it runs, and anything left in the sequence (or any remaining passes of the condition) is skipped entirely.

```python
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
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Continue

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

</summary>

`continue` skips just the current pass — the rest of the loop body doesn't run for that item — but the loop itself keeps going from the next item or the next check of the condition.

```python
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
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### The Else Clause

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

</summary>

Both loop types can end with an `else` block, which runs once the loop finishes all its passes on its own — it's skipped entirely if the loop was cut short with `break`.

```python
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
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### The pass Statement

```python-ref
for s in species:
    pass    # does nothing, but keeps the loop syntactically valid
```

</summary>

An empty loop body is a syntax error — `pass` is a no-op you can use as a placeholder while you're still deciding what a loop (or `if`, function, etc.) should do.

```python
species = ["burmese", "rock", "ball", "blood"]

for s in species:
    pass

print("loop finished without doing anything each pass")
```

</details>
