# :material-source-branch:{ .lg .middle } Conditionals

A **conditional** lets a program make decisions by running a **block** of code only when a [condition](#boolean-expressions) is `True`. 

The condition ends with a colon `:`, and the block is the lines indented underneath it, treated as a single unit. 

**There are two types of conditional statements:**

<div class="pt-jump-table" markdown="block">

| Statement              | Example                                                                                                                                                                       | When to use                                                          |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <a href="#if-elif-else">**`if` / `elif` / `else`**</a> | <pre><code class="language-python-ref">if length &gt; 15:&#10;    print("giant")&#10;elif length &gt; 8:&#10;    print("large")&#10;else:&#10;    print("small")</code></pre> | The general-purpose default — ranges, comparisons, or checking unrelated things, so use this unless `match` is clearly a better fit |
| <a href="#match-case">**`match` / `case`**</a>       | <pre><code class="language-python-ref">species = "ball"&#10;match species:&#10;    case "ball":&#10;        print("ball python")&#10    case "burmese":&#10;        print("burmese python")&#10;    case _:&#10;        print("other")</code></pre> | Comparing one value against exact, known possibilities — or splitting a tuple into named pieces while checking its values |

</div>

## If / elif / else

A chain of `if`, `elif`, and `else`: 

1. Checks a series of [conditions](#boolean-expressions) in order
2. Runs the indented block under the first one that's `True`
3. Then exits the whole chain without checking any conditions below it. 

**if:**

This always comes first, and has a condition. If the condition is `True`, it runs the block of code indented under it, then exits the chain.

**elif:**

Short for "else if." Any number of `elif`s can follow the `if` (or none) — each has its own condition, but is only checked if every condition above it was `False`. Python runs the block under the first one that's `True`, then exits the chain, skipping the rest no matter how many `elif`s follow.

**else:**

Optional, and always comes last if present. It has no condition of its own — it's the catch-all that runs only when none of the `if`/`elif` conditions above it were `True`.



```python-ref
length = 12

if length > 10:                    # always starts with the if 
    print("that's a big snake")
elif length > 7:                   # then any number (or none) of elifs
    print("that's a medium snake")
elif length > 4:
    print("that's a small snake")
else:                              # lastly comes one optional else 
    print("that's a tiny snake")
```

??? tip "See the decision path this code follows"
    ```mermaid
    flowchart TD
        A{"`if length > 10:`"} -->|True| B["`print('big snake')`"]
        A -->|False| C{"`elif length > 7:`"}
        C -->|True| D["`print('medium snake')`"]
        C -->|False| E{"`elif length > 4:`"}
        E -->|True| F["`print('small snake')`"]
        E -->|False| G["`else:`"]
        G --> H["`print('tiny snake')`"]

        B -.-> EXIT(["`done, exits the chain`"])
        D -.->EXIT
        F -.->EXIT
        H -.->EXIT

        linkStyle 0 stroke:#3f6b52,stroke-width:2px
        linkStyle 1 stroke:#a33f3f,stroke-width:2px
        linkStyle 2 stroke:#3f6b52,stroke-width:2px
        linkStyle 3 stroke:#a33f3f,stroke-width:2px
        linkStyle 4 stroke:#3f6b52,stroke-width:2px
        linkStyle 5 stroke:#a33f3f,stroke-width:2px
        linkStyle 6 stroke:#3f6b52,stroke-width:2px
        linkStyle 7 stroke:#3f6b52,stroke-width:2px
        linkStyle 8 stroke:#3f6b52,stroke-width:2px
        linkStyle 9 stroke:#3f6b52,stroke-width:2px
        linkStyle 10 stroke:#3f6b52,stroke-width:2px
    ```

### Boolean expressions

A boolean expression is needed for every `if`/`elif`.

```python-ref
if [boolean expression]:
    [indented code block that runs if above expression is True]
elif [boolean expression]:
    [indented code block that runs if above expression is True and others above were False]
```

A **boolean expression** is a boolean value (`True` or `False`) or anything that produces one, and is treated as the **condition** that must be `True` in order to run a block of code.

A comparison looks different depending on the type of value being checked, as shown below. All of these comparisons result in a `True` or `False` boolean expression. 

!!! example "Comparisons by type"

    === "int, float"

        | Operator | Meaning |
        |---|---|
        | `==` | equal to |
        | `!=` | not equal to |
        | `>` | greater than |
        | `<` | less than |
        | `>=` | greater than or equal to |
        | `<=` | less than or equal to |

        ```python-ref
        length = 12

        if length == 12:             # equal to
            print("exactly 12 ft")

        if length != 4:              # not equal
            print("not 4 ft")

        if length > 10:              # greater than
            print("long snake")

        if length < 20:              # less than
            print("under 20 ft")

        if length >= 12:             # greater than or equal to
            print("at least 12 ft")

        if length <= 12.5:           # less than or equal to
            print("12.5 ft or shorter")
        ```

    === "str"

        | Operator | Meaning |
        |---|---|
        | `==` | equal to |
        | `!=` | not equal to |
        | `in` | is a substring |
        | `not in` | is not a substring |
        | `>` | comes after alphabetically |
        | `<` | comes before alphabetically |

        ```python-ref
        name = "burmese python"

        if name == "burmese python":   # equal to
            print("it's a burmese")

        if name != "ball python":      # not equal
            print("not a ball python")

        if "python" in name:           # is it a substring
            print("name contains 'python'")

        if "anaconda" not in name:     # is it not a substring
            print("name doesn't mention anaconda")

        if name > "ball python":       # alphabetical comparison
            print("comes after 'ball python' alphabetically")
        ```

    === "bool"

        | Check | Meaning |
        |---|---|
        | `[bool]` | is the bool True |
        | `not [bool]` | is the bool False |

        Don't compare booleans with `== True` or `is True` — a boolean is already the condition, so just use the value directly (or `not` the value).

        ```python-ref
        venomous = False

        if venomous:                   # is it True — don't write venomous == True
            print("handle with care")

        if not venomous:               # is it False — don't write venomous == False
            print("safe to handle")
        ```

    === "None"

        | Operator | Meaning |
        |---|---|
        | `is` | is None |
        | `is not` | is not None |

        ```python-ref
        age = None

        if age is None:                # is it None
            print("age not recorded")

        if age is not None:            # is it anything else
            print("age was recorded")
        ```

    === "list"

        | Operator | Meaning |
        |---|---|
        | `in` | value exists in the list |
        | `not in` | value is missing from the list |
        | `==` | same contents, in the same order |
        | `!=` | different contents |

        Or compare a specific item directly, like `species[0] == "ball"`.

        ```python-ref
        species = ["ball", "burmese", "boa"]
        other_species = ["ball", "burmese", "boa"]

        if "ball" in species:          # is the value in the list
            print("ball python is in the list")

        if "anaconda" not in species:  # is the value missing from the list
            print("anaconda isn't in the list")

        if species == other_species:   # is it the same contents, in the same order
            print("both lists match")

        if "ball" == species[0]:       # compare a specific item
            print("ball python is the first item")
        ```

        | Operator | Meaning |
        |---|---|
        | `==` | same contents, even if it's a different object |
        | `is` | the exact same object, not just an equal one |

        ```python-ref
        snake = ["ball", "burmese"]
        other_snake = ["ball", "burmese"]   # separate list, but equal contents

        if snake == other_snake:      # do they contain the same items?
            print("equal contents")

        if snake != ["ball"]:         # different contents
            print("not equal to a single-item list")

        same_snake = snake                  # another name for `snake`
        if snake is same_snake:             # same_snake and snake point to the exact same list
            print("this really is the same list")

        if snake is not other_snake:        # it's a different list, even though contents match
            print("but not the same list")
        ```

    === "tuple"

        | Operator | Meaning |
        |---|---|
        | `in` | value exists in the tuple |
        | `not in` | value is missing from the tuple |
        | `==` | same contents, in the same order |
        | `!=` | different contents |

        Or compare a specific item directly, like `snake[0] == "ball"`.

        ```python-ref
        snake = ("ball", "5ft", "not venomous")
        other_snake = ("ball", "5ft", "not venomous")

        if "ball" in snake:
            print("species ball is in the tuple")

        if snake == other_snake:
            print("tuples match")

        if "ball" == snake[0]:
            print("ball python is the first item")
        ```

        | Operator | Meaning |
        |---|---|
        | `==` | same contents, even if it's a different object |
        | `is` | the exact same object, not just an equal one |

        ```python-ref
        snake = ("ball", "burmese")
        other_snake = ("ball", "burmese")   # separate tuple, but equal contents

        if snake == other_snake:      # do they contain the same items?
            print("equal contents")

        same_snake = snake                  # another name for `snake`
        if snake is same_snake:             # same_snake and snake point to the exact same tuple
            print("this really is the same tuple")

        if snake is not other_snake:        # it's a different tuple, even though contents match
            print("but not the same tuple")
        ```

    === "dict"

        | Operator | Meaning |
        |---|---|
        | `in` | key exists |
        | `not in` | key is missing |

        Or compare a specific value directly, like `snake["length"] > 2`.

        ```python-ref
        snake = {"species": "ball", "length": 3, "venomous": False}

        if "venomous" in snake:        # is it a key
            print("snake dict tracks venomous status")

        if "habitat" not in snake:     # is it not a key
            print("snake dict has no habitat key")

        if snake["length"] > 2:        # compare a specific value
            print("snake in dict is over 2 ft")
        ```

### Logical operators

Logical operators `not`, `and`, `or` let a single `if` combine boolean expressions to create more complex conditions.

```python-ref
not venomous               # not False → True

length > 10 and venomous   # True and False → False

length > 10 or venomous    # True or False → True
```

A and B here are [boolean expressions](#boolean-expressions).

| `A`                                       | `B`                                       | `not A` — flips to the opposite          | `A and B` — `True` only if both are `True` | `A or B` — `True` if either is `True`     |
|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|
| <span class="pt-bool-true">True</span>    | <span class="pt-bool-true">True</span>    | <span class="pt-bool-false">False</span> | <span class="pt-bool-true">True</span>    | <span class="pt-bool-true">True</span>    |
| <span class="pt-bool-true">True</span>    | <span class="pt-bool-false">False</span>  | <span class="pt-bool-false">False</span> | <span class="pt-bool-false">False</span>  | <span class="pt-bool-true">True</span>    |
| <span class="pt-bool-false">False</span>  | <span class="pt-bool-true">True</span>    | <span class="pt-bool-true">True</span>   | <span class="pt-bool-false">False</span>  | <span class="pt-bool-true">True</span>    |
| <span class="pt-bool-false">False</span>  | <span class="pt-bool-false">False</span>  | <span class="pt-bool-true">True</span>   | <span class="pt-bool-false">False</span>  | <span class="pt-bool-false">False</span>  |

**Order of operations:** When several logical operators appear together, Python evaluates `not` first, then `and`, then `or`. Even when parentheses aren't required, they often make the condition much easier to read.

??? tip "Nested if"
    Checks a second condition only after the first is `True`. An `if` can contain another `if`, checked only once the outer condition is already `True` — each level of nesting adds another decision. If both conditions are simple, combining them with [`and`](#logical-operators) is usually clearer than nesting.

    ```python-ref
    length = 12
    venomous = False
    if length > 10:
        if venomous:
            print("big and dangerous")
        else:
            print("big but harmless")    # runs
    ```

??? tip "One-line if"
    Simple checks can be written in one line. For a single statement, the body can go right on the same line as the condition. Save this for short, simple conditions — a normal multi-line `if` reads more clearly for anything more involved.

    The `if`-`else` version is a single expression, not a statement — it evaluates to one value or the other, so it's most useful for a quick assignment or a function argument, not as a stand-in for a full `if` block. `value_if_true if condition else value_if_false` reads almost like the English sentence it describes.

    ```python-ref
    if venomous: print("careful")    # single-line if — the colon is still required
    "careful" if venomous else "safe"    # "careful" — a compact if/else that evaluates to a value
    ```

??? run "Run an if/elif/else example"
    All the examples above, combined into one script:

    ```python
    length = 12

    if length > 10:
        print("that's a big snake")
    elif length > 7:
        print("that's a medium snake")
    elif length > 4:
        print("that's a small snake")
    else:
        print("that's a tiny snake")

    length = 12

    if length == 12:             # equal to
        print("exactly 12 ft")

    if length != 4:              # not equal
        print("not 4 ft")

    if length > 10:              # greater than
        print("long snake")

    if length < 20:              # less than
        print("under 20 ft")

    if length >= 12:             # greater than or equal to
        print("at least 12 ft")

    if length <= 12.5:           # less than or equal to
        print("12.5 ft or shorter")

    name = "burmese python"

    if name == "burmese python":   # equal to
        print("it's a burmese")

    if name != "ball python":      # not equal
        print("not a ball python")

    if "python" in name:           # is it a substring
        print("name contains 'python'")

    if "anaconda" not in name:     # is it not a substring
        print("name doesn't mention anaconda")

    if name > "ball python":       # alphabetical comparison
        print("comes after 'ball python' alphabetically")

    venomous = False

    if venomous:                   # is it True
        print("handle with care")

    if not venomous:               # is it False
        print("safe to handle")

    age = None

    if age is None:                # is it None
        print("age not recorded")

    if age is not None:            # is it anything else
        print("age was recorded")

    species = ["ball", "burmese", "boa"]
    other_species = ["ball", "burmese", "boa"]

    if "ball" in species:          # is the value in the list
        print("ball python is in the list")

    if "anaconda" not in species:  # is the value missing from the list
        print("anaconda isn't in the list")

    if species == other_species:   # is it the same contents, in the same order
        print("both lists match")

    if "ball" == species[0]:       # compare a specific item
        print("ball python is the first item")

    snake = ("ball", "5ft", "not venomous")   # a tuple works the same way

    if "ball" in snake:
        print("species ball is in the tuple")

    if snake == ("ball", "5ft", "not venomous"):
        print("tuples match")

    snake = {"species": "ball", "length": 3, "venomous": False}

    if "venomous" in snake:        # is it a key
        print("snake dict tracks venomous status")

    if "habitat" not in snake:     # is it not a key
        print("snake dict has no habitat key")

    if snake["length"] > 2:        # compare a specific value
        print("snake in dict is over 2 ft")

    snake = ["ball", "burmese"]
    other_snake = ["ball", "burmese"]   # separate list, but equal contents

    if snake == other_snake:      # do they contain the same items?
        print("equal contents")

    if snake != ["ball"]:         # different contents
        print("not equal to a single-item list")

    snake = ["ball", "burmese"]

    same_snake = snake                  # another name for `snake`
    if snake is same_snake:             # same_snake and snake point to the exact same list
        print("this really is the same list")

    other_snake = ["ball", "burmese"]   # separate list, but equal contents
    if snake is not other_snake:        # it's a different list, even though contents match
        print("but not the same list")

    length = 12
    if length > 15:
        print("giant")
    elif length > 8:
        print("large")
    elif length > 4:
        print("medium")
    else:
        print("small")

    length = 3
    if length > 15:
        print("giant")
    elif length > 8:
        print("large")
    elif length > 4:
        print("medium")
    else:
        print("small")

    venomous = False

    if venomous:
        print("handle with care")
    else:
        print("safe to handle")

    length = 12
    venomous = False

    if length > 10 and venomous:
        print("big and dangerous")
    if length > 10 or venomous:
        print("worth a closer look")
    if not venomous:
        print("safe to handle")

    if (length > 10 and not venomous) or length > 20:
        print("worth a closer look")

    length = 12
    venomous = False

    if length > 10:
        if venomous:
            print("big and dangerous")
        else:
            print("big but harmless")

    venomous = True
    if venomous: print("careful")

    status = "careful" if venomous else "safe"
    print(status)
    ```

## Match / case

A `match` statement compares one value against several `case` options and runs the code for the first matching `case`.

Both examples below do the same thing, but `match` is often easier to read than a long `if/elif` sequence when checking one value against many possibilities.

```python-ref
species = "ball"

# if/elif chain
if species == "ball":
    print("small constrictor")    # runs
elif species == "burmese":
    print("large constrictor")
else:
    print("unknown species")

# the same logic as a match statement
match species:
    case "ball":
        print("small constrictor")    # runs
    case "burmese":
        print("large constrictor")
    case _:
        print("unknown species")
```

??? tip "See the decision path this code follows"

    ```mermaid
    flowchart TD
        START["`match species:`"] --> A{"`case 'ball':`"}
        A -->|match| B["`print('small constrictor')`"]
        A -->|no match| C{"`case 'burmese':`"}
        C -->|match| D["`print('large constrictor')`"]
        C -->|no match| E["`case _:`"]
        E --> F["`print('unknown species')`"]

        B -.-> EXIT(["`done, exits the chain`"])
        D -.->EXIT
        F -.->EXIT

        linkStyle 1 stroke:#3f6b52,stroke-width:2px
        linkStyle 2 stroke:#a33f3f,stroke-width:2px
        linkStyle 3 stroke:#3f6b52,stroke-width:2px
        linkStyle 4 stroke:#a33f3f,stroke-width:2px
        linkStyle 5 stroke:#3f6b52,stroke-width:2px
        linkStyle 6 stroke:#3f6b52,stroke-width:2px
        linkStyle 7 stroke:#3f6b52,stroke-width:2px
        linkStyle 8 stroke:#3f6b52,stroke-width:2px
    ```

??? tip "Matching an int"
    A `case` can compare any type of value, not just strings.

    ```python-ref
    match length:
        case 3:
            print("hatchling size")
        case _:
            print("not a hatchling")
    ```

### Match multiple values with |

Lets one `case` match several possible values using `|`, so you don't need a separate `case` for each one.

```python-ref
match species:
    case "ball" | "corn":
        print("small species")     # runs — species is "ball"
    case _:
        print("other")
```

### Default value _

Runs a block of code if no `case` matched — either discarding the value with `_`, or capturing it into a variable.

```python-ref
match species:
    case "burmese":
        print("it's a burmese!")
    case _:                             # Option 1:  Unsaved default value
        print("not a burmese")          # value discarded

match species:
    case "burmese":
        print("it's a burmese")
    case n:                             # Option 2: Saved default value
        print(f"{n} is not a burmese")  # stores the value as new variable n
```

If you want the code to still run a block of code even if no specific `case` matched, there are two ways to add a default value at the end that will match anything. A default value goes last — without one, a value matching no cases would not run any block of code. **Option 1** (`_`) throws the matched value away; **Option 2** (giving it a variable name, like `n`) saves it so the block can use it.

### case + if

Only run the block of code if there's a `case` match *and* the `if` condition is also `True`. Adding `if [condition]` after a pattern turns it into a guard — the branch only runs if the pattern matches *and* the condition is `True`. If the guard is `False`, Python moves on to the next `case` even though the pattern itself matched.

```python-ref
length = 12
match length:
    case n if n > 10:
        print("big")     # runs — 12 > 10
    case n:
        print("small")
```

### Unpacking a tuple

A `case` can pull a tuple apart into named pieces *while also* checking its shape or specific values.

```python-ref
snake = (12, "ball")
match snake:
    case (length, "ball"):                      # tuple with 2 items, where second is "ball"
        print(f"a {length} ft ball python")     # in this example, this case will run
    case (length, species):                     # tuple with any 2 items
        print(f"a {length} ft {species} python")
    case (length,):                             # tuple with any 1 item
        print(f"just a length: {length}")
    case _:                                     # 0 items, or tuple with more than 2 items
        print("invalid format")
```

A `match` can pick a different `case` depending on the tuple's length or the value in a specific position, while *still* unpacking the rest into names — all in one step, as shown above. Compare with regular assignment (`length, species = snake`), which always unpacks the same way, would crash on a 1- or 3-item tuple, and can't pick a different case based on species.

??? run "Run a match/case example"
    All the examples above, combined into one script:

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

    length = 3

    match length:
        case 3:
            print("hatchling size")
        case _:
            print("not a hatchling")

    species = "ball"

    match species:
        case "ball" | "corn":
            print("small species")

    species = "ball"

    match species:
        case "anaconda":
            print("giant")
        case _:
            print("not an anaconda")

    species = "ball"

    match species:
        case "anaconda":
            print("giant")
        case n:                    # any variable name works here, not just n
            print(f"{n} is not an anaconda or burmese")

    snake = (12, "ball")

    length, species = snake   # regular assignment — see note above
    print(species, length)

    match snake:
        case (length, "ball"):                  # 2 items, second is 'ball'
            print(f"a {length} ft ball python")
        case (length, species):                 # 2 items, any other species
            print(f"a {length} ft {species}")
        case (length,):                         # 1 item — comma makes this a 1-tuple pattern
            print(f"just a length: {length}")
        case _:                                 # 0 items, or more than 2
            print("0 items, or more than 2")

    length = 12

    match length:
        case n if n > 10:
            print("big")
        case n:
            print("small")
    ```

## Control flow statements

`break` and `continue` are loop-control keywords, not conditional ones, but they almost always appear inside a conditional — checking a condition, then stopping the loop early (`break`) or skipping straight to the next pass (`continue`). They work the same way whether checked with `if`/`elif` or `match`/`case`, since neither creates its own loop scope — both just pass straight through to whatever loop contains them. Covered fully, with more examples, on the [Loops](loops.md#control-flow-statements) page.

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

for s in species:
    match s:
        case "ball":
            break                 # stops the loop, same as it would inside an if
        case _:
            print(s)
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

for s in species:
    match s:
        case "ball":
            continue              # skips just "ball", same as it would inside an if
        case _:
            print(s)
```

??? tip "pass placeholder"
    Temporarily fill an empty block when you're not ready to write the inside code yet. Python doesn't allow an empty block after a colon. `pass` does nothing, but acts as a placeholder until you're ready to add code so that the empty block won't cause a syntax error in the meantime — works the same way after `if`/`elif`/`else` and `case` alike.

    ```python-ref
    if venomous:
        pass    # placeholder — does nothing, but prevents a syntax error

    match venomous:
        case True:
            pass    # same idea, inside a case block
    ```

??? run "Run a control flow example"
    All the examples above, combined into one script:

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

    for s in species:
        match s:
            case "ball":
                break
            case _:
                print(s)

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

    for s in species:
        match s:
            case "ball":
                continue
            case _:
                print(s)

    venomous = True

    if venomous:
        pass

    match venomous:
        case True:
            pass

    print("checked venomous status, no action taken yet")
    ```
