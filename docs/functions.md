---
description: >-
  Python functions explained with runnable examples: defining, calling, arguments,
  *args/**kwargs, scope, recursion, and decorators.
---

# :material-function-variant:{ .lg .middle } Functions

A **function** packages a block of code under a name, so it can be run again — with different inputs — instead of copying and pasting the same lines every time you need them. Python already has some built in (`print()`, `len()`), but `def` lets you write your own.

| Concept | Example | What it is |
|---------|---------|------------|
| Parameter | `def describe(species):` | A name a function expects to receive a value for, listed in its definition |
| Argument | `describe("ball")` | The actual value passed in when the function is called |
| Return value | `return f"a {species} python"` | The value a function sends back to whatever called it |
| Default value | `def describe(species="ball"):` | A fallback used when the caller doesn't supply that argument |

<div class="pfg-section" markdown="block">

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

`return` sends a value back to the caller, instead of just printing it. `return` also exits the function immediately, skipping any code written after it.

```python-ref
def describe(species):
    return f"a {species} python"

message = describe("ball")    # "a ball python" — stored, not printed
```

If a function runs to the end without hitting a `return` statement, it returns `None` automatically. This is what you get back if a lookup silently "doesn't find" anything.

```python-ref
def find_species(name):
    if name == "ball":
        return "found it"
    # falls through here for anything else — implicitly returns None

result = find_species("cobra")    # None — the function fell through without a return
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

### Type hints

A **type hint** annotates a parameter or return value with the type it's expected to be — `species: str`, `length_ft: float`, `-> bool` — without Python enforcing it at runtime; it's documentation an editor or a separate type checker (like `mypy`) can check for you.

```python-ref
def is_unusually_long(species: str, length_ft: float) -> bool:
    return length_ft > 5
```

A wrong type still runs — Python doesn't stop you from calling `is_unusually_long("ball python", "4.5")` with a string instead of a `float` — the hint only helps a tool catch the mismatch before you do, and helps a reader (or their editor) see what's expected without reading the function body.

### Keep functions focused

A function should do one thing. If you find yourself describing it with "and" — "loads the species *and* saves it *and* prints a summary" — it's probably three functions.

```python-ref
def load_and_describe(species):    # doing too much
    ...

def load_species(species):         # one job each
    ...

def describe(species):
    ...
```

Repeating the same few lines in multiple places is a sign to pull them into their own function instead — commonly called **DRY** ("don't repeat yourself"). It also means a fix only has to happen in one place, instead of every place the lines were copied to.

??? tip "Guard clauses: return early instead of nesting"
    Handle the exception case first and return, rather than wrapping the rest of the function in an `else`. It keeps the normal path at the lowest indentation level, instead of nested one level deeper for every added check.

    ```python-ref
    def describe(length_ft):
        if length_ft > 0:
            return f"{length_ft} ft"
        else:
            return "unknown length"
    ```

    ```python-ref
    def describe(length_ft):
        if length_ft <= 0:
            return "unknown length"
        return f"{length_ft} ft"
    ```

    Both versions do the same thing — the second reads top to bottom without having to track which `if` branch you're inside.

### Going further { data-card-link="skip" }

??? tip "pass placeholder"
    Temporarily fill an empty function body when you're not ready to write the inside code yet. Python doesn't allow an empty block after a colon. `pass` does nothing, but acts as a placeholder until you're ready to add code so that the empty block won't cause a syntax error in the meantime. Covered in more detail on the [Conditionals](conditionals.md#if-elif-else) page.

    ```python-ref
    def describe(species):
        pass    # placeholder — does nothing, but prevents a syntax error
    ```

??? warning "Mutable default argument"
    A default value is only ever created **once**, when the function is defined — not fresh on every call. For a list or dict default, that means every call sharing that default is silently reading and writing the *same* object, so it keeps growing across calls instead of starting empty each time.

    ```python-ref
    def add_sighting(species, log=[]):    # log=[] is created once, not per call
        log.append(species)
        return log

    add_sighting("ball")       # ["ball"]
    add_sighting("burmese")    # ["ball", "burmese"] — the same list, not a fresh one
    ```

    Default to `None` instead, and create the list inside the function body:

    ```python-ref
    def add_sighting(species, log=None):
        if log is None:
            log = []
        log.append(species)
        return log
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


    def find_species(name):
        if name == "ball":
            return "found it"
        # falls through here for anything else — implicitly returns None

    result = find_species("cobra")
    print(result)


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


    def is_unusually_long(species: str, length_ft: float) -> bool:
        return length_ft > 5

    print(is_unusually_long("ball python", 6))
    ```

</div>

<div class="pfg-section" markdown="block">

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

### Going further { data-card-link="skip" }

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

</div>

<div class="pfg-section" markdown="block">

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

### Going further { data-card-link="skip" }

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

</div>

<div class="pfg-section" markdown="block">

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

</div>

<div class="pfg-section" markdown="block">

## Decorators

**`@decorator`** lets you add behavior to a function without editing the function's own code — write the behavior once, then apply it to as many functions as you want. It's written as `@decorator_name`, placed directly above a `def`, and takes one function in, returning a function out[^callable].

### Wrapping the call

A decorator can run its own code around a function call by returning a different function instead of the original — a **wrapper** that does something, calls the original, then returns. This is the shape behind most decorators you'll actually use — logging, timing, or checking permissions before letting a call through.

```python
def decorator_name(func):              # func is the function being decorated (here it's "describe()")
    def wrapper():                     # defines a new function that runs in place of func from now on
        print("looking up a snake...")
        func()                         # calls the original, still reachable through func
        print("found it")
    return wrapper                     # decorator returns the new function name

@decorator_name        # decorator_name can be any name you pick
def describe():        # here is your regular function you are decorating
    print("a python")

describe()  # every function call now prints "looking up a snake...", "a python", then "found it"
```

`@decorator_name` reassigns `describe` to `wrapper.` Calling `describe()` now actually runs `wrapper()`, which calls the original through `func`. `wrapper` and `decorator_name` are just names, not special syntax — any valid identifier works for either one.

### Returning the original function

Not every decorator needs a wrapper — the only actual requirement is returning *some* function. `catalog` below doesn't define a new one at all, it just hands back `func` itself, unchanged, so its surrounding prints only run once, the moment `describe` is defined — never again on any later call to `describe()`.

```python
def catalog(func):
    print("looking up a snake...")
    func()
    print("found it")
    return func    # func, not func() — a reference to the function, not a call to it

@catalog
def describe():
    print("a python")

describe()    # "a python" only — the surrounding prints already ran once, at decoration

@catalog
def count():
    return 5

print(count())    # 5 — return values pass through untouched too
```

`@catalog` reassigns `describe` to whatever `catalog` returns. `return func()` would call it and hand back its result instead of the function itself — `None` here — breaking `describe` as something you can call again.

### Accepting arguments

`describe` above takes no arguments, so `wrapper` didn't need to accept any either. Most functions do take arguments — `describe` normally takes a `species`, for instance — and `wrapper` has to accept whatever the decorated function needs.

`*args` and `**kwargs` let `wrapper` accept anything and print exactly what came in — useful for seeing what a function was actually called with, whatever its shape:

```python
def decorator(func):
    def wrapper(*args, **kwargs):     # accepts any parameters, instead of a fixed signature
        print(f"called with {args}")  # shows exactly what was passed in
        return func(*args, **kwargs)  # then forwards it all to func
    return wrapper

@decorator
def describe(species):
    return f"a {species} python"

print(describe("ball"))    # prints "called with ('ball',)", then "a ball python"

@decorator
def total_length(*lengths):
    return sum(lengths)

print(total_length(5, 12, 8))    # prints "called with (5, 12, 8)", then 25 — same decorator, different signature
```

### Advanced uses

??? tip "Decorators with arguments"
    A decorator that needs its own settings takes those arguments one level out — a function that *returns* a decorator, instead of being one directly. This is how a decorator like Flask's `@app.route("/users")` gets its own argument (the URL path), separate from whatever function it ends up decorating.

    ```python
    def tag(label):              # called first, with the decorator's own argument
        def decorator(func):      # this is the actual decorator tag(label) builds
            def wrapper(*args, **kwargs):
                print(f"[{label}]")
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @tag("sighting")
    def describe(species):
        return f"a {species} python"

    print(describe("ball"))
    ```

??? tip "Applying a decorator manually"
    `@decorator_name` is shorthand for calling the decorator directly and reassigning the function's name yourself — the two lines below have the exact same effect as `@decorator` above a `def describe():`.

    ```python
    def decorator(func):
        def wrapper():
            print("looking up a snake...")
            func()
            print("found it")
        return wrapper

    def describe():
        print("a python")

    describe = decorator(describe)    # same effect as @decorator, written out by hand
    describe()                         # prints "looking up a snake...", "a python", then "found it"
    ```

    Writing it out by hand is useful when a function shouldn't always be decorated — `@` applies unconditionally, every time the function is defined, while the manual form can sit behind a condition:

    ```python
    def decorator(func):
        def wrapper():
            print("looking up a snake...")
            func()
            print("found it")
        return wrapper

    debug = True

    def describe():
        print("a python")

    if debug:
        describe = decorator(describe)    # only decorated when debug is True

    describe()
    ```

??? note "Stacking decorators"
    Multiple decorators on the same function apply bottom-up — the one closest to `def` wraps first, and each one after it wraps the result of the one before. Stacking is common whenever a function needs more than one independent behavior — a web view that's both registered at a URL and requires the user to be logged in, for instance.

    ```python
    def bold(func):
        def wrapper(*args, **kwargs):
            return f"**{func(*args, **kwargs)}**"    # wraps whatever it's given in **
        return wrapper

    def shout(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs).upper()    # uppercases whatever it's given
        return wrapper

    @bold
    @shout
    def describe(species):
        return f"a {species} python"

    print(describe("ball"))    # shout wraps describe first, then bold wraps shout's result
    ```

??? tip "Preserving identity"
    Decorating a function replaces its identity with the wrapper's — `describe.__name__` becomes `"wrapper"`, not `"describe"`, since Python only sees the function `decorator` returned. `functools.wraps` copies the original function's name, docstring, and other metadata onto the wrapper so introspection tools still see the right name. This matters beyond cosmetics — some frameworks (Flask included) use a decorated function's `__name__` internally, so skipping `@wraps` can break things that have nothing to do with printing a name.

    ```python
    from functools import wraps

    def decorator(func):
        @wraps(func)                          # copies func's __name__, __doc__, etc. onto wrapper
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    @decorator
    def describe(species):
        return f"a {species} python"

    print(describe.__name__)    # "describe" — without @wraps(func), this would be "wrapper" instead
    ```

[^callable]: Technically a decorator just needs to return something *callable* — every decorator on this page returns a function specifically, but not all decorators do. [Classes](oop.md#method-decorators)' built-in `@property`, `@staticmethod`, and `@classmethod` return other kinds of callable object instead.

</div>

