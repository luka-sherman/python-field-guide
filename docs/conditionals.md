# Conditionals

A **conditional** runs a block of code only when some condition is `True` — the same comparisons that produce a [boolean](basic_data_types.md#booleans) (`>`, `<`, `==`, and so on) are exactly what an `if` statement checks.

| Keyword | Example | What it does |
|---------|---------|---------------|
| `if` | `if length_ft > 10:` | Runs its block only when the condition is `True` |
| `elif` | `elif length_ft > 4:` | Checked only if every condition above it was `False` — runs the first one that's `True` |
| `else` | `else:` | Catches everything not caught above — always comes last, with no condition of its own |

## If, Elif & Else

An `if` statement runs its indented block only when its condition is `True` — otherwise Python skips straight past it.

```python
length_ft = 12

if length_ft > 10:
    print("that's a big snake")
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Chaining Conditions With `elif`

```python-ref
length_ft = 12
if length_ft > 15:
    print("giant")
elif length_ft > 8:
    print("large")     # runs — 12 > 8, and nothing below it gets checked
elif length_ft > 4:
    print("medium")
else:
    print("small")
```

</summary>

`elif` ("else if") is checked only if every condition above it was `False`. Python runs the first branch that matches and skips the rest, no matter how many `elif`s follow.

```python
length_ft = 12
if length_ft > 15:
    print("giant")
elif length_ft > 8:
    print("large")
elif length_ft > 4:
    print("medium")
else:
    print("small")

length_ft = 3
if length_ft > 15:
    print("giant")
elif length_ft > 8:
    print("large")
elif length_ft > 4:
    print("medium")
else:
    print("small")
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### The `else` Clause

```python-ref
venomous = False
if venomous:
    print("handle with care")
else:
    print("safe to handle")    # runs — venomous is False
```

</summary>

`else` is the catch-all — it runs when nothing above it matched. It always comes last and never has a condition of its own. A conditional chain can have `elif` without `else`, but `else` (if present) must always be the final branch.

```python
venomous = False

if venomous:
    print("handle with care")
else:
    print("safe to handle")
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Nested `if` Statements

```python-ref
length_ft = 12
venomous = False
if length_ft > 10:
    if venomous:
        print("big and dangerous")
    else:
        print("big but harmless")    # runs
```

</summary>

An `if` can contain another `if`, checked only once the outer condition is already `True` — each level of nesting adds another layer of decision-making. If both conditions are simple, combining them with `and` (see below) is usually clearer than nesting.

```python
length_ft = 12
venomous = False

if length_ft > 10:
    if venomous:
        print("big and dangerous")
    else:
        print("big but harmless")
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Shorthand `if`

```python-ref
if venomous: print("careful")    # single-line if — the colon is still required
```

</summary>

For a single statement, the body can go right on the same line as the condition. Save this for short, simple conditions — a normal multi-line `if` reads more clearly for anything more involved.

```python
venomous = True
if venomous: print("careful")
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Shorthand `if`-`else` (Ternary)

```python-ref
"careful" if venomous else "safe"    # "careful" — a compact if/else that evaluates to a value
```

</summary>

This is a single expression, not a statement — it evaluates to one value or the other, so it's most useful for a quick assignment or a function argument, not as a stand-in for a full `if` block. `value_if_true if condition else value_if_false` reads almost like the English sentence it describes.

```python
venomous = True
status = "careful" if venomous else "safe"
print(status)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### The `pass` Statement

```python-ref
if venomous:
    pass    # placeholder — does nothing, but keeps the block syntactically valid
```

</summary>

An empty block is a syntax error — `pass` is a no-op you can use as a placeholder while you're still deciding what a branch should do.

```python
venomous = True

if venomous:
    pass

print("checked venomous status, no action taken yet")
```

</details>

## Logical Operators

`and`, `or`, and `not` combine or invert conditions, so a single `if` can check more than one thing at once.

```python
length_ft = 12
venomous = False

if length_ft > 10 and not venomous:
    print("big but safe to observe")
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### `and`

```python-ref
length_ft > 10 and venomous    # True and False → False
```

</summary>

`and` needs both sides to be `True` for the whole condition to pass — if either side is `False`, the block is skipped.

```python
length_ft = 12
venomous = False

if length_ft > 10 and venomous:
    print("big and dangerous")
else:
    print("not both conditions were true")
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### `or`

```python-ref
length_ft > 10 or venomous    # True or False → True
```

</summary>

`or` only needs one side to be `True` — the block runs even if the other side is `False`.

```python
length_ft = 12
venomous = False

if length_ft > 10 or venomous:
    print("worth a closer look")
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### `not`

```python-ref
not venomous    # not False → True
```

</summary>

`not` flips a condition's result — useful for checking that something *isn't* the case, without rewriting the condition itself.

```python
venomous = False

if not venomous:
    print("safe to handle")
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Operator Precedence

```python-ref
length_ft > 10 and not venomous or length_ft > 20   # not, then and, then or
```

</summary>

When mixing operators, Python evaluates `not` first, then `and`, then `or`. Parentheses aren't required, but they make the intended order obvious at a glance — `(length_ft > 10 and not venomous) or length_ft > 20` means the same thing as the line above, with no guessing.

```python
length_ft = 12
venomous = False

if (length_ft > 10 and not venomous) or length_ft > 20:
    print("worth a closer look")
```

</details>
