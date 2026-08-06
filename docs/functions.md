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

??? tip "Docstrings"
    A triple-quoted string as a function's first line documents what it does — most editors show it automatically when you use the function elsewhere. A **docstring** is the same triple-quoted-string trick covered on the [Foundations](foundations.md#multiline-comments-with) page, but placed as the very first line inside a function specifically to document it. Unlike a regular comment, Python actually stores a docstring (as the function's `__doc__` attribute) rather than discarding it — which is how editors are able to show it in a tooltip when you call the function elsewhere, without you needing to go find the definition. Short, single-line docstrings like this one are common for simple functions; longer functions often use a multi-line docstring describing each parameter and what's returned.

    ```python-ref
    def describe(species):
        """Return a short description of the given snake species."""
        return f"a {species} python"
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

??? run "Run a function example"
    All the examples above, combined into one script:
TODO: add titles to code blocks
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
