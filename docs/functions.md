# :material-function-variant:{ .lg .middle } Functions

A **function** packages a block of code under a name, so it can be run again — with different inputs — instead of copying and pasting the same lines every time you need them. Python already has some built in (`print()`, `len()`), but `def` lets you write your own.

| Concept | Example | What it is |
|---------|---------|------------|
| Parameter | `def describe(species):` | A name a function expects to receive a value for, listed in its definition |
| Argument | `describe("ball")` | The actual value passed in when the function is called |
| Return value | `return f"a {species} python"` | The value a function sends back to whatever called it |
| Default value | `def describe(species="ball"):` | A fallback used when the caller doesn't supply that argument |

## Defining a function

`def` names a function and lists the parameters it expects; the indented block underneath is what runs each time it's called.

```python-ref
def describe(species):
    print(f"a {species} python")

describe("ball")
describe("burmese")
```

??? tip "Indenting a block"
    Select a line (or several), then indent or unindent it in one keystroke instead of retyping spaces. These are the defaults in VS Code, PyCharm, Thonny, and IDLE. Selecting multiple lines first — click and drag, or hold ++shift++ while using the arrow keys — indents or unindents all of them together, which matters here since every line inside a function body needs the same indentation.

    | Action | Shortcut |
    |--------|------------------|
    | Indent selected lines | ++tab++ |
    | Unindent selected lines | ++shift+tab++ |

### Docstrings

A triple-quoted string as a function's first line documents what it does — most editors show it automatically when you use the function elsewhere. A **docstring** is the same triple-quoted-string trick covered on the [Foundations](foundations.md#multi-line-comments-with) page, but placed as the very first line inside a function specifically to document it. Unlike a regular comment, Python actually stores a docstring (as the function's `__doc__` attribute) rather than discarding it — which is how editors are able to show it in a tooltip when you call the function elsewhere, without you needing to go find the definition.

Short, single-line docstrings are common for simple functions:

```python-ref
def describe(species):
    """Return a short description of the given snake species."""
    return f"a {species} python"
```

For a function where you want to document its parameters or return values, you can spell them out using this standard format. You list all parameters/arguments and their name, type, and description, the return type and description, and the one-line summary:

```python-ref
def is_too_long(species, length_ft):
    """
    Check whether a snake is unusually long for its species.

    Args:
        species (str): the snake's species name.
        length_ft (float): the snake's measured length, in feet.

    Returns:
        bool: True if length_ft is unusually long for species.
    """
    return length_ft > 5
```

### Return values

`return` sends a value back to the caller, instead of just printing it. Without a `return`, a function hands back `None` automatically — covered on the [Types](types.md#functions-return-none-by-default) page. `return` also exits the function immediately, skipping any code written after it.

```python-ref
def describe(species):
    return f"a {species} python"

message = describe("ball")    # "a ball python" — stored, not printed
```

### Default parameter values

A parameter can fall back to a default value if the caller doesn't supply one. Parameters with a default must come after every parameter without one — Python reads arguments left to right, so a required parameter can't follow an optional one.

```python-ref
def describe(species, length_ft=5):
    return f"a {length_ft} ft {species} python"

describe("ball")            # "a 5 ft ball python" — uses the default
describe("burmese", 12)     # "a 12 ft burmese python" — overrides it
```

### Keyword arguments

Passing `name=value` lets you specify arguments out of order, or skip earlier defaults. Arguments passed by position (like `describe("ball")`) must still come first; keyword arguments can follow in any order, and are matched by name instead of position.

```python-ref
def describe(species, length_ft=5, venomous=False):
    return f"{species}, {length_ft} ft, venomous: {venomous}"

describe(species="ball", venomous=True)    # length_ft still uses its default
```

??? tip "pass placeholder"
    Temporarily fill an empty function body when you're not ready to write the inside code yet. Python doesn't allow an empty block after a colon. `pass` does nothing, but acts as a placeholder until you're ready to add code so that the empty block won't cause a syntax error in the meantime. Covered in more detail on the [Conditionals](conditionals.md#if-elif-else) page.

    ```python-ref
    def describe(species):
        pass    # placeholder — does nothing, but prevents a syntax error
    ```

??? run "Run a function example"
    All the examples above, combined into one script:

    ```python
    def describe(species):
        print(f"a {species} python")

    describe("ball")
    describe("burmese")


    def describe(species):
        """Return a short description of the given snake species."""
        return f"a {species} python"

    print(describe("ball"))
    print(describe.__doc__)


    def describe(species):
        return f"a {species} python"

    message = describe("ball")
    print(message)


    def check_length(length_ft):
        if length_ft > 10:
            return "long snake"
        return "short snake"    # only reached if the if above didn't return

    print(check_length(12))
    print(check_length(4))


    def describe(species, length_ft=5):
        return f"a {length_ft} ft {species} python"

    print(describe("ball"))
    print(describe("burmese", 12))


    def describe(species, length_ft=5, venomous=False):
        return f"{species}, {length_ft} ft, venomous: {venomous}"

    print(describe("ball", venomous=True))
    print(describe(species="burmese", length_ft=12))
    ```

## Flexible arguments

`*args` and `**kwargs` let a function accept an unpredictable number of arguments, instead of a fixed list of parameters.

```python-ref
def total_length(*lengths):
    return sum(lengths)

print(total_length(5, 12, 8))
```

### `*args`

Collects any number of positional arguments into a tuple. `*lengths` gathers however many positional arguments were passed into a single tuple named `lengths` — the function works the same whether it's called with one length or ten. `*args` is the conventional name, but any name after `*` works.

```python-ref
def total_length(*lengths):
    return sum(lengths)    # lengths is (5, 12, 8) inside the function

total_length(5, 12, 8)    # 25
```

### `**kwargs`

Collects any number of keyword arguments into a dict. `**details` gathers every `name=value` keyword argument into a dict named `details`, keyed by argument name. `**kwargs` is the conventional name, but like `*args`, any name after `**` works.

```python-ref
def describe(**details):
    return details    # {"species": "ball", "length_ft": 5}

describe(species="ball", length_ft=5)
```

??? run "Run a flexible arguments example"
    All the examples above, combined into one script:

    ```python
    def total_length(*lengths):
        return sum(lengths)

    print(total_length(5, 12, 8))


    def total_length(*lengths):
        print(lengths)
        return sum(lengths)

    print(total_length(5, 12, 8))
    print(total_length(4.5))


    def describe(**details):
        for key, value in details.items():
            print(key, value)

    describe(species="ball", length_ft=5, venomous=False)
    ```

## Scope

A variable created inside a function is **local** — it only exists while that function is running, and isn't visible outside it.

```python-ref
def set_species():
    species = "ball"    # local to this function
    print(species)

set_species()
```

### Local vs global variables

A variable defined at the top level of a file is **global** — readable from inside any function. A function can *read* a global variable freely, but assigning to that name inside a function creates a brand-new local variable instead of changing the global one — the next section covers how to actually change a global from inside a function.

```python-ref
species = "ball"    # global

def show_species():
    print(species)    # reads the global — no error
```

??? tip "Modifying a global variable"
    `global` tells Python that an assignment inside a function should change the global variable, not create a local one. Without `global`, `count += 1` here would raise an error — Python sees the assignment and treats `count` as local for the whole function, then finds no local `count` to add to. `global` is needed occasionally, but reaching for it often is usually a sign the code would read more clearly passing values in and returning them instead.

    ```python-ref
    count = 0

    def record_sighting():
        global count
        count += 1    # changes the global count, not a local copy
    ```

??? run "Run a scope example"
    All the examples above, combined into one script:

    ```python
    def set_species():
        species = "ball"    # local to this function
        print(species)

    set_species()

    species = "ball"


    def show_species():
        print(species)

    show_species()
    print(species)

    count = 0


    def record_sighting():
        global count
        count += 1

    record_sighting()
    record_sighting()
    print(count)
    ```

## Recursion

A function can call itself — this is called **recursion**, an alternative to a loop for problems that break down into smaller versions of themselves.

```python-ref
def countdown(n):
    if n == 0:              # base case — stops the recursion
        print("liftoff")
        return
    print(n)
    countdown(n - 1)        # recursive case — calls itself with a smaller input

countdown(3)                 # 3  2  1  liftoff
```

Every recursive function needs two parts:

- **Base case** — the condition that stops the recursion. Without one, the function calls itself forever.
- **Recursive case** — where the function calls itself again, with an input that's closer to the base case than before.

??? warning "Infinite recursion"
    Forgetting the base case (or writing one that's never reached) makes a function call itself forever, the same way a `while` loop with no way to become `False` never stops. Python enforces a limit before endless recursion could freeze the whole program — hitting it raises a `RecursionError` instead.

    ```python-ref
    def countdown(n):
        print(n)
        countdown(n - 1)    # never stops — no base case

    countdown(3)              # RecursionError: maximum recursion depth exceeded
    ```

??? tip "Recursion vs. a loop"
    Anything recursion can do, a loop can do too — recursion is rarely the only option, just sometimes the more natural fit. It reads most naturally for problems already defined in terms of themselves, like a [nested dictionary](collections.md#dictionaries) of arbitrary depth, where the number of levels isn't known ahead of time. For a simple countdown like the one above, a `while` loop is just as clear and doesn't risk a `RecursionError`.

    ```python-ref
    n = 3
    while n > 0:
        print(n)
        n -= 1
    print("liftoff")
    ```

??? run "Run a recursion example"
    All the examples above, combined into one script:

    ```python
    def countdown(n):
        if n == 0:
            print("liftoff")
            return
        print(n)
        countdown(n - 1)

    countdown(3)

    n = 3
    while n > 0:
        print(n)
        n -= 1
    print("liftoff")
    ```
