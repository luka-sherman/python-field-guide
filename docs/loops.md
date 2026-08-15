# :material-repeat:{ .lg .middle } Loops

A **loop** repeats a block of code multiple times. 

<div class="pt-jump-table" markdown="block">

| Loop type | Syntax | Use it for |
|------|--------|------------|
| <a href="#for-loops">**`for`**</a> | <pre><code class="language-python-ref">for loop_variable in iterable:</code></pre> | Goes through an **iterable** (something that contains multiple values) one value at a time, assigning each value to `loop_variable` as it goes.<ul><li>Runs the block of code once for each item in the iterable</li><li>Repeating something a set number of times, or counting passes — using a `range()`</li><li>Processing each item in something you already have — a list, tuple, dict, set, or string</li></ul> |
| <a href="#while-loops">**`while`**</a> | <pre><code class="language-python-ref">while condition:</code></pre> | A `while` loop repeats as long as a **condition** is `True`, checking the condition before it starts each pass.<ul><li>Use it when you don't know how many times the loop needs to run</li><li>The condition determines when the loop stops</li></ul> |

</div>

??? tip "Which loop do I need?"

    ```mermaid
    %%{init: {"themeVariables": {"edgeLabelBackground": "transparent"}}}%%
    flowchart TD
        choice{"Do you know what you're\nworking with, or how many\ntimes to repeat?"} -->|Yes| forConfirm["for loop!"]
        forConfirm --> known{"Already have a collection\nto go through? (list, tuple,\ndict, set, or string)"}
        choice -->|No, just know\nwhen to stop| whileConfirm["while loop!"]
        whileConfirm --> whileloop["condition = a boolean expression"]
        known -->|Yes| forvalue["iterable = the collection"]
        known -->|No| forcount["iterable = range()"]

        linkStyle 0 stroke:#3f6b52,stroke-width:2px
        linkStyle 2 stroke:#3f6b52,stroke-width:2px
        linkStyle 4 stroke:#3f6b52,stroke-width:2px
        linkStyle 5 stroke:#a33f3f,stroke-width:2px

        classDef decision fill:none,stroke:#8A8370,stroke-width:1px
        classDef result fill:none,stroke:#3f6b52,stroke-width:2px,color:#3f6b52
        classDef confirm fill:none,stroke:#3f6b52,stroke-width:3px,color:#3f6b52
        class known,choice decision
        class forvalue,forcount,whileloop result
        class forConfirm,whileConfirm confirm
    ```

## For loops

A `for` loop goes through an **iterable** (something that contains multiple values) one value at a time, assigning each value to `loop_variable` as it goes. They types of iterables are: 

| Iterable | Loop variable | Use it for |
|---|---|---|
| `range()` | represents the current count |Repeating a block of code a set number of times |
| a Collection: list / tuple / dict / set / string | represents the current item | Repeating a block of code for each item in a collection |

See [common patterns](#common-patterns) for [accumulating](#accumulator) something new during a loop, or [counting](#counter), as you loop.

You can use [control flow statements](#control-flow-statements) to [break](#break) a loop early or [continue](#continue) ahead to the next iteration as needed. 

### Loop a certain number of times

#### iterable = range()

- `range()` generates a sequence of numbers to loop over.
- it will run the block of code once for each number in the sequence
- The first time it runs, the loop_variable will be equal to the first number in the range sequence, and so on until the block has run as many times are there are numbers in the range sequence

- **The 3 parts of range():**

    | range() part | Default value | Meaning |
    |---|---|---|
    | `start` | `0` | Where to start counting<ul><li>This is the first loop_variable value</li></ul> |
    | `stop` | *(required — no default)* | Where to stop (exclusive)<ul><li>**not** included in the range sequence, so the last number is the one before</li></ul> |
    | `step` | `1` | How much to count by to get to the next number<ul><li>starting with the `start` value, adds `step` to it each time to get the next number in the sequence</li></ul> |

- **How many parts you specify**

    | # of range parts given | Sets parts | Not set, so uses defaults for |
    |---|---|---|
    | 1 | `stop` | `start = 0`, `step = 1` |
    | 2 | `start`, `stop` | `step = 1`|
    | 3 | `start`, `stop`, `step` | - |

    - **range(stop)** 

        ```python
        for i in range(5):
            print(i)
        ```

        ```mermaid
        %%{init: {"themeVariables": {"edgeLabelBackground": "transparent"}}}%%
        flowchart LR
            a(("0")) -->|"+1"| b(("1")) -->|"+1"| c(("2")) -->|"+1"| d(("3")) -->|"+1"| e(("4"))
            e -.->|"+1"| f(("5"))

            classDef included fill:none,stroke:#3f6b52,stroke-width:2px,color:#3f6b52
            classDef excluded fill:none,stroke:#8A8370,stroke-width:1px,stroke-dasharray:3 3,color:#8A8370
            class a,b,c,d,e included
            class f excluded
        ```

    - **range(start, stop)**

        ```python
        for i in range(2, 6):
            print(i)
        ```

        ```mermaid
        %%{init: {"themeVariables": {"edgeLabelBackground": "transparent"}}}%%
        flowchart LR
            a(("2")) -->|"+1"| b(("3")) -->|"+1"| c(("4")) -->|"+1"| d(("5"))
            d -.->|"+1"| e(("6"))

            classDef included fill:none,stroke:#3f6b52,stroke-width:2px,color:#3f6b52
            classDef excluded fill:none,stroke:#8A8370,stroke-width:1px,stroke-dasharray:3 3,color:#8A8370
            class a,b,c,d included
            class e excluded
        ```

    - **range(start, stop, step)**

        ```python
        for i in range(2, 8, 2):
            print(i)
        ```

        ```mermaid
        %%{init: {"themeVariables": {"edgeLabelBackground": "transparent"}}}%%
        flowchart LR
            a(("2")) -->|"+2"| b(("4")) -->|"+2"| c(("6"))
            c -.->|"+2"| d(("8"))

            classDef included fill:none,stroke:#3f6b52,stroke-width:2px,color:#3f6b52
            classDef excluded fill:none,stroke:#8A8370,stroke-width:1px,stroke-dasharray:3 3,color:#8A8370
            class a,b,c included
            class d excluded
        ```

- **Counting backwards**

    If `start` is larger than `stop`, use a negative `step` to count backwards instead.

    ```python
    for i in range(5, 0, -1):
        print(i)
    ```

    ```mermaid
    %%{init: {"themeVariables": {"edgeLabelBackground": "transparent"}}}%%
    flowchart LR
        a(("5")) -->|"-1"| b(("4")) -->|"-1"| c(("3")) -->|"-1"| d(("2")) -->|"-1"| e(("1"))
        e -.->|"-1"| f(("0"))

        classDef included fill:none,stroke:#3f6b52,stroke-width:2px,color:#3f6b52
        classDef excluded fill:none,stroke:#8A8370,stroke-width:1px,stroke-dasharray:3 3,color:#8A8370
        class a,b,c,d,e included
        class f excluded
    ```

#### Loop variable = an index

Naming the variable in a `range()` loop comes down to one of three choices:

- **`i`, for a simple counter**

    Short for **index** — a naming convention borrowed from math, where `i`, `j`, and `k` are the traditional names for a counting variable. It's not a special keyword; any name works, but `i` is what most Python code uses by convention for a loop over `range()`.

    ```python
    for i in range(5):
        print(i)
    ```

- **A descriptive name, when the count means something**

    If what you're counting through actually represents something, a descriptive name reads better than `i` — says what the number *means* at a glance, instead of leaving the reader to infer it from how it's used. Same [naming](style.md#naming) rule as any other variable: `i` is fine for a short, throwaway loop, but a meaningful name is worth it once the number stands for something specific.

    ```python
    for year in range(2020, 2026):
        print(year)

    for attempt in range(3):
        print(attempt)
    ```

- **`_`, when you don't need it at all**

    Use `_` instead of a real loop variable when you just need to repeat something a fixed number of times and don't need the number itself.

    ```python
    for _ in range(3):
        print("hiss")
    ```

### Loop through a collection

#### iterable = collection

A `for` loop steps through any type of collection[^str-collection] the same way — the difference is what each pass hands you to work with.

[^str-collection]: A string isn't technically one of Python's collection types — see the [Types](types.md#strings) page — but it's structurally iterable and indexable the same way a list is, so it loops the same way too.

!!! example "How to loop each type"

    === "list"

        Each pass hands you the item itself, not its position. This is what sets a Python `for` loop apart from the index-counting loops in some other languages. A list is the most common thing to loop over, since it's Python's all-purpose ordered collection.

        ```python
        species = ["burmese", "rock", "ball", "blood"]

        for s in species:
            print(s)
        ```

    === "tuple"

        Works exactly like looping over a list — a tuple just can't be changed once it's created. Anything you'd loop through in a list, you can loop through the same way in a tuple.

        ```python
        constrictors = ("ball", "burmese", "boa")

        for s in constrictors:
            print(s)
        ```

    === "dict"

        Looping directly over a dict gives you its keys, one at a time. Use `.values()` to get just the values instead, or `.items()` to get the key and value together — usually the most useful of the three.

        ```python
        snake = {"species": "ball", "length_ft": 5, "venomous": False}

        for key, value in snake.items():
            print(key, value)
        for key in snake:
            print(key)
        for value in snake.values():
            print(value)
        ```

    === "str"

        Hands you each character in turn, in order — including spaces. A string is just a sequence of characters, so a `for` loop treats it the same way it treats a list or tuple.

        ```python
        name = "burmese python"

        for letter in name:
            print(letter)
        ```

    === "set"

        Works the same as a list, except the order isn't guaranteed — a set has no fixed position for its items, so each pass just hands you the next value in whatever order Python happens to iterate.

        ```python
        species = {"burmese", "rock", "ball", "blood"}

        for s in species:
            print(s)
        ```

#### Loop variable = singular item

Looping over a collection follows a different naming convention than counting with `range()`: name the loop variable the **singular** of the collection's plural name — `for snake in snakes:`, `for length in lengths:` — so each pass reads as "this one item from the group." Site examples on this page often abbreviate to a single letter (`s` for `species`) to keep code blocks compact, but a real singular word is clearer in actual code.

```python
snakes = ["burmese", "rock", "ball", "blood"]

for snake in snakes:
    print(snake)
```

#### Loop with index and value

`enumerate()` hands you both the index and the value on every pass. It's the usual alternative to looping over `range(len(species))` when you need the index but still want direct access to each item.

```python
species = ["burmese", "rock", "ball", "blood"]

for i, s in enumerate(species):
    print(i, s)
```

#### Loop in reverse

`reversed()` steps through a collection back to front, without needing to build a reversed copy first. Works on anything with a fixed order — list, tuple, string, `range()` — but not on a `set`, since it has no order to reverse.

```python
species = ["burmese", "rock", "ball", "blood"]

for s in reversed(species):
    print(s)     # blood  ball  rock  burmese
```

??? tip "Loop two collections at the same time with zip()"
    `zip()` pairs up items from two (or more) iterables by position — the first item from each, then the second from each, and so on — stopping as soon as the shortest one runs out. Works with any iterable, mixed types included — list, tuple, string, dict (its keys, by default), even a `range()`. Because it is based on order, using an unordered collection like `set` or plain `dict` can produce pairings in an unpredictable order.

    ```python
    species = ["burmese", "rock", "ball", "blood"]
    length_ft = [12, 4, 5, 3.5]

    for s, ft in zip(species, length_ft):
        print(s, ft)
    ```

??? tip "List comprehensions: a one-line for loop"
    A list comprehension builds a new list by running an expression once per item — the same result as a `for` loop that appends to an empty list, written on a single line.

    ```python
    species = ["burmese", "rock", "ball", "blood"]

    lengths = []
    for s in species:
        lengths.append(len(s))
    print(lengths)

    lengths = [len(s) for s in species]
    print(lengths)
    ```

    Add an `if` at the end to only keep items that match a condition:

    ```python
    species = ["burmese", "rock", "ball", "blood"]

    print([s for s in species if s == "ball"])
    ```

    Readable for a short, simple transformation — once the logic doesn't fit comfortably on one line, a regular `for` loop is usually clearer.

## While loops

A `while` loop repeats its body for as long as a condition stays `True`, checked again before every pass — the right tool when you don't know ahead of time how many passes you'll need, unlike a `for` loop's fixed number of items. That condition can be any boolean expression, watching for something to happen rather than counting toward it.

```python-ref
handled = False

while not handled:
    print("checking on the snake")
    handled = True
```

### Using a flag

A **flag** is a boolean variable, starting `True` or `False`, that gets flipped when something happens — used as the condition to end the loop based on an event rather than a pass count.

```python-ref
species = ["burmese", "rock", "ball", "blood"]

found = False
i = 0

while not found:
    if species[i] == "ball":
        found = True    # flips the flag — the next check ends the loop
    i += 1

print(found)   # True
print(i)       # 3 — stopped as soon as "ball" was found
```

### Sentinel

A **sentinel** is a specific stop-value you watch for, rather than a plain True/False flag — the loop keeps running until it sees that exact value. A common use is reading input until the user signals they're done.

```python-ref
species = ""

while species != "quit":
    species = input("Log a species (or 'quit' to stop): ")
    if species != "quit":
        print(f"logged: {species}")
```

### Counter and flag names

A `while` loop doesn't create a loop variable automatically the way `for` does — whatever's driving the condition is a variable you declare and update yourself, so naming it clearly matters just as much.

- **A counter** — named the same way as a `for` loop's: `count` works generically, but a descriptive name (`attempts`, `retries`) reads better once the number means something specific.
- **A flag** — named so `while not flag_name:` reads like plain English — `found`, `done`, `handled` — rather than something that needs mental negation to parse.

```python
handled = False

while not handled:
    handled = True
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
    handled = False

    while not handled:
        print("checking on the snake")
        handled = True

    species = ["burmese", "rock", "ball", "blood"]

    found = False
    i = 0

    while not found:
        if species[i] == "ball":
            found = True
        i += 1

    print(found)
    print(i)
    ```

### Boolean expressions

A boolean expression is needed for every `while` condition.

```python-ref
while [boolean expression]:
    [indented code block that runs, and keeps running, as long as the expression stays True]
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

Logical operators `not`, `and`, `or` let a single `while` condition combine boolean expressions to create more complex conditions.

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

## Common patterns

A few variable patterns show up across both `for` and `while` loops, tracking something as the loop runs rather than controlling it directly.

### Accumulator

An **accumulator** builds up a result across passes — summing, concatenating, or collecting values — instead of just tracking whether or how many times the loop has run. Initialize it before the loop, then update it inside the body each pass.

```python-ref
lengths_ft = [4.5, 12, 5, 3.5]

total = 0
for length in lengths_ft:
    total += length
print(total)   # 25.0

i = 0
total = 0
while i < len(lengths_ft):
    total += lengths_ft[i]
    i += 1
print(total)   # 25.0
```

??? tip "Accumulating into a list"
    Same pattern, just appending instead of adding — this is exactly what a [list comprehension](#for-loops) collapses into one line.

    ```python-ref
    species = ["burmese", "rock", "ball", "blood"]

    results = []
    for s in species:
        results.append(s.upper())
    print(results)   # ["BURMESE", "ROCK", "BALL", "BLOOD"]
    ```

### Counter

A **counter** tracks how many times a loop has run, or how many items met some condition — counting up or down, instead of accumulating a result. It follows the same three steps as an accumulator: initialize it before the loop, check or use it, and update it inside the body.

```python-ref
species = ["ball", "burmese", "ball", "boa", "ball"]

count = 0
for s in species:
    if s == "ball":
        count += 1
print(count)   # 3 — counts every "ball" in the list

attempts = 3
while attempts > 0:
    print(attempts)
    attempts -= 1
print("out of attempts")
```

### Nested loops

A loop can contain another loop — any combination of `for` and `while` works, not just two of the same kind. Useful when each item in the outer collection has its own inner collection to go through, like a list of lists. The inner loop runs all the way through for every single pass of the outer one.

```python
species_tags = {
    "ball": ["docile", "captive-bred"],
    "burmese": ["large", "escape-risk"],
}

for species, tags in species_tags.items():
    for tag in tags:
        print(species, tag)
```

??? run "Run a common patterns example"
    All the examples above, combined into one script:

    ```python
    lengths_ft = [4.5, 12, 5, 3.5]

    total = 0
    for length in lengths_ft:
        total += length
    print(total)

    i = 0
    total = 0
    while i < len(lengths_ft):
        total += lengths_ft[i]
        i += 1
    print(total)

    species = ["burmese", "rock", "ball", "blood"]

    results = []
    for s in species:
        results.append(s.upper())
    print(results)

    species = ["ball", "burmese", "ball", "boa", "ball"]

    count = 0
    for s in species:
        if s == "ball":
            count += 1
    print(count)

    attempts = 3
    while attempts > 0:
        print(attempts)
        attempts -= 1
    print("out of attempts")

    species_tags = {
        "ball": ["docile", "captive-bred"],
        "burmese": ["large", "escape-risk"],
    }

    for species, tags in species_tags.items():
        for tag in tags:
            print(species, tag)
    ```

## Control Flow Statements

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

### Else

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

??? tip "pass placeholder"
    Temporarily fill an empty loop body when you're not ready to write the inside code yet. Python doesn't allow an empty block after a colon. `pass` does nothing, but acts as a placeholder until you're ready to add code so that the empty block won't cause a syntax error in the meantime. Covered in more detail on the [Conditionals](conditionals.md#if-elif-else) page.

    ```python-ref
    for s in species:
        pass    # placeholder — does nothing, but prevents a syntax error
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
