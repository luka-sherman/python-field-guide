# Loops

A **loop** repeats a block of code some number of times. 

All loop definitions end with a colon `:`, and the **block** is the lines indented underneath it that is treated as a single unit. 

**There are two types of loops:**


| Loop | Syntax | Use it for |
|------|--------|------------|
| `for` | `for item in sequence:` | When you know (or can generate) what you're looping over ahead of time:<ul><li>A `range()` — loop a fixed number of times</li><li>A `list` — an ordered, changeable collection of items</li><li>A `tuple` — an ordered collection that can't be changed</li><li>A `dict` — looping gives you the keys (or use `.items()` for key-value pairs)</li><li>A `str` — loops over the string one character at a time</li></ul> |
| `while` | `while condition:` | <ul><li>Repeating until something changes — not tied to a fixed collection</li><li>When you don't know in advance how many passes you'll need</li></ul> |

## For loops

A `for` loop steps through a sequence — a [list](collections.md), tuple, string, or other iterable — running its body once per item, in order.

```python
for i in range(5):
    print(i)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop a fixed number of times

`range()` generates a sequence of numbers to loop over.
{: .pt-subheading }

```python-ref
range(5)          # range(0, 5) — produces 0, 1, 2, 3, 4
range(2, 6)       # start=2, stop=6      — 2, 3, 4, 5
range(2, 10, 3)   # start=2, stop=10, step=3 — 2, 5, 8
```

</summary>

One argument counts up from `0` to (but not including) that number; a second sets a custom `start`; a third sets a `step` size other than `1`. It's the standard way to loop by index instead of by value — or to just repeat something a fixed number of times, using `_` instead of a real variable name when you don't need the number itself.

```python
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
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop over a list

Each pass hands you the item itself, not its position.
{: .pt-subheading }

```python-ref
for s in species: 
    print(s)    # burmese  rock  ball  blood
```

</summary>

This is what sets a Python `for` loop apart from the index-counting loops in some other languages. A list is the most common thing to loop over, since it's Python's all-purpose ordered collection.

```python
species = ["burmese", "rock", "ball", "blood"]

for s in species:
    print(s)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Counting matches with a loop

Combine `if` with a loop and a counter to count how many items meet a condition.
{: .pt-subheading }

```python-ref
count = 0
for s in species:
    if s == "ball":
        count += 1
print(count)   # runs — counts every "ball" in the list
```

</summary>

`count` starts at `0`, and the `if` condition is checked once per item — every time it's `True`, `count += 1` adds one. By the end of the loop, `count` holds the total number of matches.

```python
species = ["ball", "burmese", "ball", "boa", "ball"]

count = 0
for s in species:
    if s == "ball":
        count += 1

print(count)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop over a tuple

Works exactly like looping over a list — a tuple just can't be changed once it's created.
{: .pt-subheading }

```python-ref
for s in constrictors: 
    print(s)    # ball  burmese  boa
```

</summary>

Anything you'd loop through in a list, you can loop through the same way in a tuple.

```python
constrictors = ("ball", "burmese", "boa")

for s in constrictors:
    print(s)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop over a dictionary

Looping directly over a dict gives you its keys, one at a time.
{: .pt-subheading }

```python-ref
for key, value in snake.items(): 
    print(key, value)          # species ball  length_ft 5  venomous False
for key in snake: 
    print(key)                 # species  length_ft  venomous
for value in snake.values(): 
    print(value)               # ball  5  False
```

</summary>

Use `.values()` to get just the values instead, or `.items()` to get the key and value together — usually the most useful of the three.

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

### Loop over a string

Hands you each character in turn, in order — including spaces.
{: .pt-subheading }

```python-ref
for letter in name: print(letter)    # b  u  r  m  e  s  e     p  y  t  h  o  n
```

</summary>

A string is just a sequence of characters, so a `for` loop treats it the same way it treats a list or tuple.

```python
name = "burmese python"

for letter in name:
    print(letter)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Loop with index and value

`enumerate()` hands you both the index and the value on every pass.
{: .pt-subheading }

```python-ref
for i, s in enumerate(species): print(i, s)    # 0 burmese  1 rock  2 ball  3 blood
```

</summary>

It's the usual alternative to looping over `range(len(species))` when you need the position but still want direct access to each item.

```python
species = ["burmese", "rock", "ball", "blood"]

for i, s in enumerate(species):
    print(i, s)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Nested loops

A loop can contain another loop — useful for combinations, grids, or nested collections.
{: .pt-subheading }

```python-ref
for s in species:
    for letter in s[:2]:
        print(s, letter)
# burmese b  burmese u  rock r  rock o  ball b  ball a  blood b  blood l
```

</summary>

The inner loop runs all the way through for every single pass of the outer one.

```python
species = ["ball", "burmese"]

for s in species:
    for letter in s[:2]:
        print(s, letter)
```

</details>

## While loops

A `while` loop repeats its body for as long as a condition stays `True` — checked again before every pass — so it's the right choice when you don't know ahead of time how many times you'll need to loop.

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Avoiding infinite loops

A `while` loop repeats forever unless something inside it moves the condition toward `False`.
{: .pt-subheading }

```python-ref
count = 0
while count < 3:
    print(count)
    count += 1    # forgetting this line means count < 3 is always True
```

</summary>

Nothing stops it automatically, and it freezes whatever's running it — always make sure something inside the loop body moves it toward ending, like incrementing a counter or updating the value being checked.

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

</details>

## Loop control

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

Exits the loop immediately, skipping everything left in it.
{: .pt-subheading }

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

Nothing after it runs, and anything left in the sequence (or any remaining passes of the condition) is skipped entirely.

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

Skips just the current pass, then keeps looping.
{: .pt-subheading }

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

The rest of the loop body doesn't run for that item, but the loop itself keeps going from the next item or the next check of the condition.

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

### The else clause

Runs once the loop finishes on its own — skipped entirely if `break` cut it short.
{: .pt-subheading }

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

Both `for` and `while` can end with an `else` block.

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

### The pass statement

A no-op placeholder for an empty loop body, which Python doesn't otherwise allow.
{: .pt-subheading }

```python-ref
for s in species:
    pass    # does nothing, but keeps the loop syntactically valid
```

</summary>

It's not just for loops — the same trick works while you're still deciding what an `if`, function, etc. should do.

```python
species = ["burmese", "rock", "ball", "blood"]

for s in species:
    pass

print("loop finished without doing anything each pass")
```

</details>
