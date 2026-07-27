# Conditionals

A **conditional** lets a program make decisions by running a block of code only when a condition is `True`. 

The condition ends with a colon `:`, and every line meant to run as part of that block must be indented underneath it.

| Statement              | Example                                                                                                                                                                       | When to use                                                          |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `if` / `elif` / `else` | <pre><code class="language-python-ref">if length_ft &gt; 15:&#10;    print("giant")&#10;elif length_ft &gt; 8:&#10;    print("large")&#10;else:&#10;    print("small")</code></pre> | The general-purpose default — works for any condition, so use this unless `match` is clearly a better fit |
| `match` / `case`       | <pre><code class="language-python-ref">match species:&#10;    case "ball":&#10;        print("small")&#10;    case _:&#10;        print("other")</code></pre> | Comparing one value against several specific, known possibilities     |

## If / Elif / Else

A chain of `if`, `elif`, and `else` checks a series of conditions in order, running the indented block under the first one that's `True`.

```python
length_ft = 12

if length_ft > 10:
    print("that's a big snake")
elif length_ft > 4:
    print("that's a medium snake")
else:
    print("that's a small snake")
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Boolean Expressions

```python-ref
length_ft > 10    # True — a boolean expression
```

</summary>

A **boolean expression** is just a boolean value (`True` or `False`) or anything that produces one — like a comparison (`>`, `<`, `==`, and so on). This is what `if` checks: not the raw numbers or text themselves, but the `True`/`False` result of comparing them. Every `if` follows this same shape:

```
if [boolean expression/value]:
    [indented block]
```

```python
length_ft = 12

length_ft > 10       # True
length_ft == 12      # True
length_ft < 5         # False
```

</details>

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

`elif` ("else if") is checked only if every condition above it was `False`. Python runs the first branch whose condition is `True` and skips the rest, no matter how many `elif`s follow.

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

An `if` can contain another `if`, checked only once the outer condition is already `True` — Each level of nesting adds another decision. If both conditions are simple, combining them with [`and`](#local-operators-and-or-not) is usually clearer than nesting.

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

### Shorthand `if` & `if`-`else`

```python-ref
if venomous: print("careful")    # single-line if — the colon is still required
"careful" if venomous else "safe"    # "careful" — a compact if/else that evaluates to a value
```

</summary>

For a single statement, the body can go right on the same line as the condition. Save this for short, simple conditions — a normal multi-line `if` reads more clearly for anything more involved.

The `if`-`else` version is a single expression, not a statement — it evaluates to one value or the other, so it's most useful for a quick assignment or a function argument, not as a stand-in for a full `if` block. `value_if_true if condition else value_if_false` reads almost like the English sentence it describes.

```python
venomous = True
if venomous: print("careful")

status = "careful" if venomous else "safe"
print(status)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Logical Operators `not` `and` `or`

```python-ref
not venomous                  # not False → True

length_ft > 10 and venomous   # True and False → False

length_ft > 10 or venomous    # True or False → True
```

</summary>

The same comparisons that produce a [boolean](basic_types.md#booleans) (`>`, `<`, `==`, and so on) can be combined with `and`, `or`, and `not`, so a single `if`/`elif` statement can make more complex decisions.

`not` reverses a condition, turning `True` into `False` and `False` into `True`.

`and` is only `True` when both sides are `True`.

`or` is `True` when either side is `True`.


When several logical operators appear together, Python evaluates `not` first, then `and`, then `or`. Even when parentheses aren't required, they often make the condition much easier to read.

```python
length_ft = 12
venomous = False

if length_ft > 10 and venomous:
    print("big and dangerous")
if length_ft > 10 or venomous:
    print("worth a closer look")
if not venomous:
    print("safe to handle")

if (length_ft > 10 and not venomous) or length_ft > 20:
    print("worth a closer look")
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

Python doesn't allow an empty block after a colon. `pass` does nothing, but acts as a placeholder until you're ready to add code.

```python
venomous = True

if venomous:
    pass

print("checked venomous status, no action taken yet")
```

</details>

## Match / Case

A `match` statement compares one value against several `case` options and runs the code for the first matching `case`.

Both examples below do the same thing, but `match` is often easier to read than a long `if/elif` sequence when checking one value against many possibilities.

```python
species = "ball"

# if/elif chain
if species == "ball":
    print("small constrictor")
elif species == "burmese":
    print("large constrictor")
else:
    print("unknown species")

# the same logic as a match statement
match species:
    case "ball":
        print("small constrictor")
    case "burmese":
        print("large constrictor")
    case _:
        print("unknown species")
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Matching Multiple Values with `|`

```python-ref
match species:
    case "ball" | "corn":
        print("small species")     # runs — species is "ball"
    case _:
        print("other")
```

</summary>

`|` lets one `case` match several possible values, so you don't need a separate `case` for each one.

```python
species = "ball"

match species:
    case "ball" | "corn":
        print("small species")
    case _:
        print("other")
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### The Wildcard `_`

```python-ref
match species:
    case "anaconda":
        print("giant")
    case _:
        print("not an anaconda")   # runs — no other case matched
```

</summary>

`_` matches anything, so it's usually placed last to catch every value that wasn't matched earlier. It works much like `else` in an `if` statement. Without it, a value matching no `case` would run nothing.

```python
species = "ball"

match species:
    case "anaconda":
        print("giant")
    case _:
        print("not an anaconda")
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Adding an `if` to a `case`

```python-ref
length_ft = 12
match length_ft:
    case n if n > 10:
        print("big")              # runs — 12 > 10
    case n:
        print("small")
```

</summary>

A `case` can store the matched value in a variable (here `n`) and add an `if` condition. That branch only runs if both the value matches and the `if` condition is `True`.

```python
length_ft = 12

match length_ft:
    case n if n > 10:
        print("big")
    case n:
        print("small")
```

</details>
