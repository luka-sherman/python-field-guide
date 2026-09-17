---
description: >-
  Python functions explained with runnable examples: defining, calling, arguments,
  *args/**kwargs, scope, recursion, and decorators.
---

# :material-function-variant:{ .lg .middle } Functions

A **function** packages a block of code under a name, so it can be run again — with different inputs — instead of copying and pasting the same lines every time you need them. 

Python already has some built in (`print()`, `len()`, `input()`), but `def` lets you write your own.

```python-ref
def describe(species):            # function definition: "describe" is function name, "species" is a parameter
    return f"a {species} python"  # indented block of code that is run inside of function

describe("ball")                  # function call: "ball" is an argument — the value passed in for species
message = describe("ball")        # "a ball python" is the return value, so now "message" becomes equal to it
```

??? run "Run a function example"
    All the examples above, combined into one script:

    ```python
    def describe(species):
        print(f"a {species} python")

    describe("ball")
    describe("burmese")


    def describe(species, length_ft):
        print(f"a {length_ft} ft {species} python")

    describe("ball", 5)
    describe(5, "ball")


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


    def describe(species: str, length_ft: float):
        return f"a {length_ft} ft {species} python"

    print(describe("ball python", "4.5"))


    def is_unusually_long(species: str, length_ft: float) -> bool:
        return length_ft > 5

    print(is_unusually_long("ball python", 6))
    ```

<div class="pfg-section" markdown="block">

## Defining a function

A function is first defined. After it's defined, you can [call the function](#calling-a-function) whenever you need to run it. 

The function definition line contains **`def`**, a **function name** (follows the same [naming rules as variables](foundations.md#naming-variables)), **parentheses** holding zero or more **parameters**, and a **colon**. 

Under it is an indented **body**: the block of code that runs when the function is [called](#calling-a-function).

```python-ref
def function_name(optional_parameter, optional_parameter):
    [indented block of code, run whenever the function is called]

```

??? tip "Shortcut for indenting multiple lines"
    Select several lines, then indent or unindent them in one keystroke. Selecting multiple lines first — click and drag, or hold ++shift++ while using the arrow keys — indents or unindents all of them together, which matters here since every line inside a function body needs the same indentation.

    | Action | Shortcut |
    |--------|------------------|
    | Indent selected lines | ++tab++ |
    | Unindent selected lines | ++shift+tab++ |

### Parameters

A **parameter** is the placeholder name listed in a function's own definition — as opposed to an **argument**, the actual value a caller passes in for it.

A function can list zero, one, or multiple parameters separated by commas. Arguments are matched to parameters by position — the first argument fills the first parameter, the second fills the second, and so on.

Calling with too few or too many arguments raises a `TypeError` — Python doesn't know which value goes where. Arguments can also be matched by name instead of position — see [keyword arguments](#keyword-arguments) under calling a function.

```python-ref
def describe(species, length_ft):
    print(f"a {length_ft} ft {species} python")

describe("ball", 5)    # a 5 ft ball python
describe(5, "ball")    # a ball ft 5 python — wrong order, but still runs
```

#### Default values

A parameter can fall back to a default value if the call doesn't specify one. Parameters with a default must come **after** all of the parameters without one.

```python-ref
def describe(species, length_ft=5):              # default length_ft is 5, if not given then called. 
    return f"a {length_ft} ft {species} python"

describe("burmese", 12)   # length_ft is 12
describe("ball")          # second parameter is not given, so length_ft is the default 5
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

#### *args tuple

`*args` collects any number of positional arguments into a single [tuple](collections.md#tuples), so a function can accept as many as the caller passes instead of a fixed list of parameters. `*args` is the conventional name, but any name after `*` works.

```python-ref
def total_length(*args):
    return sum(args)    # args is (5, 12, 8) inside the function

total_length(5, 12, 8)    # 25
```

#### **kwargs dict

`**kwargs` collects any number of keyword arguments into a single [dict](collections.md#dictionaries), so a function can accept as many `name=value` pairs as the caller passes instead of a fixed list of parameters. `**kwargs` is the conventional name, but any name after `**` works.

```python-ref
def describe(**details):
    return details    # {"species": "ball", "length_ft": 5}

describe(species="ball", length_ft=5)
```

#### Type hints { data-advanced="true" }

A type hint on a parameter like `species: str` annotates the type of value it's expected to receive. Python doesn't enforce it, but it can be helpful for you to keep track of it and a separate type checker (like `mypy`) can check for you.

```python-ref
def describe(species: str, length_ft: float):
    return f"a {length_ft} ft {species} python"
```

#### Combining regular, \*args, and \*\*kwargs { data-advanced="true" }  { data-card-link="skip" }

A single signature can mix regular parameters, `*args`, keyword-only parameters, and `**kwargs`, but Python requires that fixed order: positional parameters first, then `*args`, then any keyword-only parameters, then `**kwargs` last.

`venomous` sits after `*lengths`, which makes it keyword-only automatically — anything named after `*args` can only be passed by name, even without a separate bare `*`.

```python-ref
def describe(species, *lengths, venomous=False, **details):
    return species, lengths, venomous, details

describe("ball", 5, 6, venomous=True, habitat="captive")
# species = "ball", lengths = (5, 6), venomous = True, details = {"habitat": "captive"}
```

#### Positional-only { data-advanced="true" }

A `/` in the parameter list marks every parameter before it **positional-only** — it can only be passed by position, never by name. Most parameters don't need this restriction. It mainly shows up in library code, where locking a parameter to positional-only lets the author rename it later without breaking callers who passed it by keyword.

```python-ref
def describe(species, /, length_ft):
    return f"{species}, {length_ft} ft"

describe("ball", 5)                     # by position — works
describe(species="ball", length_ft=5)   # TypeError — species is positional-only
```

#### Keyword-only { data-advanced="true" }

A `*` in the parameter list marks every parameter after it **keyword-only** — it can only be passed by name, never by position. Keyword-only parameters suit options that would be unclear as a bare positional value — `venomous=True` reads clearly at the call site, `True` alone wouldn't.

```python-ref
def describe(species, *, venomous):
    return f"{species}, venomous: {venomous}"

describe("ball", venomous=True)    # by name — works
describe("ball", True)             # TypeError — venomous is keyword-only
```

### Return values

`return` sends a value back to whatever called the function, instead of just printing it. `return` also exits the function immediately, skipping any code written after it.

`message = describe("ball")`: `describe` runs with `species` set to `"ball"`, builds the string, then `return` hands it back to the `=` that called it — `message` now holds `"a ball python"`, nothing gets printed.

That's the difference from `print()`: `print()` shows a value and discards it; `return` hands the value back to be stored, passed along, or used in another expression.

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

#### Multiple values  { data-card-link="skip" } 

`return` followed by several values separated by commas [packs](collections.md#packing-and-unpacking) them into a tuple as a single return value. The caller unpacks that tuple to use the values separately — see [multiple values](#multiple-values_1) under calling a function.

```python-ref
def describe(species, length_ft):
    return species, length_ft    # packs ("ball", 5) into one tuple, once called

species, length = describe("ball", 5)    # name = "ball", length = 5
```

### Keep functions focused  { data-card-link="skip" }

A function should do one thing. If you find yourself describing it with "and" — "loads the species *and* saves it *and* prints a summary" — it's probably three functions.

Repeating the same few lines in multiple places is a sign to pull them into their own function instead — commonly called **DRY** ("don't repeat yourself"). It also means a fix only has to happen in one place, instead of every place the lines were copied to.

```python-ref
def load_and_describe(species):    # doing too much
    ...

def load_species(species):         # one job each
    ...

def describe(species):
    ...
```

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

### pass placeholder

`pass` temporarily fills an empty function block so it doesn't raise a syntax error while you're not ready to write the real code yet.

```python-ref
def describe(species):
    pass    # placeholder — does nothing, but prevents a syntax error
```


### Docstrings

A triple-quoted string as a function's first line documents what it does — most editors show it automatically when you use the function elsewhere. A **docstring** is the same triple-quoted-string trick covered on the [Foundations](foundations.md#multi-line-comments-with) page, but placed as the very first line inside a function specifically to document it. Unlike a regular comment, Python actually stores a docstring (as the function's `__doc__` attribute) rather than discarding it — which is how editors are able to show it in a tooltip when you call the function elsewhere, without you needing to go find the definition.

Short, single-line docstrings are common for simple functions:

```python-ref
def describe(species):
    """Return a short description of the given snake species."""
    return f"a {species} python"
```

For a function where you want to document its parameters or return values, you can spell them out using this conventional format. In addition to the summary, you also list all parameters/arguments and their name, type, and description, the return type and description:

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

</div>

<div class="pfg-section" markdown="block">

## Calling a function

`describe("ball")` is the call — the name, followed by parentheses, is what runs the body. `"ball"` fills in `species` for that one run. Same body, run twice — only the value in `species` changes between calls.

```python-ref
describe("ball")       # a ball python
describe("burmese")    # a burmese python
```

??? run "Run a calling a function example"
    All the examples above, combined into one script:

    ```python
    def describe(species):
        print(f"a {species} python")

    describe("ball")
    describe("burmese")
    ```

### Arguments

An **argument** is the actual value a caller passes in for a parameter — as opposed to a **parameter**, the placeholder name listed in a function's own definition.

#### Required

By default, a call needs an argument for every parameter that doesn't have one already, supplied in the same order the parameters were listed — unless passed [by keyword](#by-keyword) instead. Leaving one out, or supplying too many, raises a `TypeError`.

```python-ref
def describe(species, length_ft):
    return f"{species}, {length_ft} ft"

describe("ball", 5)    # both required arguments supplied, by position
describe("ball")       # TypeError — missing required argument: 'length_ft'
```

#### By keyword

Passing `name=value` lets you specify arguments out of order, or skip earlier defaults. Arguments passed by position (like `describe("ball")`) must still come first; keyword arguments can follow in any order, and are matched by name instead of position. A function can also catch any number of these in one parameter — see the [`**kwargs` dict](#kwargs-dict) under defining a function.

```python-ref
def describe(species, length_ft=5, venomous=False):
    return f"{species}, {length_ft} ft, venomous: {venomous}"

describe(species="ball", venomous=True)    # length_ft still uses its default
```

#### Unpacking

`*` and `**` also work in a function call, where they do the reverse of `*args`/`**kwargs`: instead of gathering separate arguments into one tuple or dict, they spread an existing list or dict back out into separate arguments. `*` unpacks a list or tuple into positional arguments; `**` unpacks a dict into keyword arguments. This is the call-site mirror of the [`*args` tuple](#args-tuple) and [`**kwargs` dict](#kwargs-dict) under defining a function — those gather a variable number of arguments into a tuple or dict at definition time; unpacking spreads a list, tuple, or dict back into individual arguments at the call site.

```python-ref
values = ["ball", 5]
describe(*values)             # same as describe("ball", 5)

details = {"species": "ball", "length_ft": 5}
describe(**details)           # same as describe(species="ball", length_ft=5)
```

### Saving the return value

Assign the call to a variable to keep the value `return` sent back, instead of it being discarded. `message = describe("ball")` runs `describe` with `species` set to `"ball"`, and `return` hands the built string back to the `=` that called it — `message` now holds `"a ball python"`. That's the difference from `print()`: `print()` shows a value and discards it; `return` hands the value back to be stored, passed along, or used in another expression.

```python-ref
def describe(species):
    return f"a {species} python"

message = describe("ball")    # "a ball python" — stored, not printed
```

#### Multiple values { data-card-link="skip" }

A function that [returns multiple values packed into a tuple](#multiple-values) can have them unpacked straight into multiple variables in one line at the call site. `name, length = describe(...)` unpacks the returned tuple, matching each variable to the tuple's items by position — the same as [unpacking any other tuple](collections.md#packing-and-unpacking). The number of variables on the left has to match the number of values returned.

```python-ref
def describe(species, length_ft):
    return species, length_ft

name, length = describe("ball", 5)    # name = "ball", length = 5
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

## Recursion { data-advanced="true" }

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

## Decorators { data-advanced="true" }

**`@decorator`** lets you add behavior to a function without editing the function's own code — write the behavior once, then apply it to as many functions as you want. It's written as `@decorator_name`, placed directly above a `def`, and takes one function in, returning a function out[^callable].

### Wrapping the call

A decorator can run its own code around a function call by returning a different function instead of the original — a **wrapper** that does something, calls the original, then returns. This is the shape behind most decorators you'll actually use — logging, timing, or checking permissions before letting a call through.

`@decorator_name` reassigns `describe` to `wrapper.` Calling `describe()` now actually runs `wrapper()`, which calls the original through `func`. `wrapper` and `decorator_name` are just names, not special syntax — any valid identifier works for either one.

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

### Returning the original function

Not every decorator needs a wrapper — the only actual requirement is returning *some* function. `catalog` below doesn't define a new one at all, it just hands back `func` itself, unchanged, so its surrounding prints only run once, the moment `describe` is defined — never again on any later call to `describe()`.

`@catalog` reassigns `describe` to whatever `catalog` returns. `return func()` would call it and hand back its result instead of the function itself — `None` here — breaking `describe` as something you can call again.

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

[^callable]: Technically a decorator just needs to return something *callable* — every decorator on this page returns a function specifically, but not all decorators do. [Classes](classes.md#method-decorators)' built-in `@property`, `@staticmethod`, and `@classmethod` return other kinds of callable object instead.

</div>

<div class="pfg-section" markdown="block">

## Generators { data-advanced="true" }

A **generator** is a function that pauses and resumes instead of running start to finish and returning once. Calling it doesn't run the body — it returns a **generator object** that produces values one at a time, only as they're asked for.

```python-ref
def species_generator():
    yield "ball"
    yield "burmese"
    yield "boa"

for species in species_generator():
    print(species)
```

### Generator vs. a regular function  { data-card-link="skip" }

A regular function does all its work up front and returns one complete result; a generator pauses after each `yield` and resumes on request.

```python-ref
def species_list():                      # regular function
    return ["ball", "burmese", "boa"]    # builds the whole list before returning

def species_generator():                 # generator — has a yield in its body
    yield "ball"        # produces one value, pauses, resumes on the next request
    yield "burmese"
    yield "boa"
```

```python-ref
values = species_list()    # values is a list
values[0]       # "ball" — a list supports indexing
len(values)     # 3 — and len()

gen = species_generator()    # gen is a generator object, not a list
gen[0]          # TypeError — a generator supports neither
len(gen)        # TypeError
```

| | Function returning a list | Generator |
|---|---|---|
| Hands back | The whole `list`, all at once, via `return` | A `generator` object, one value at a time, via `yield` |
| That result supports | Indexing, `len()`, looping more than once | Stepping forward once with `next()` or a `for` loop |
| Choose it when | The caller needs the whole result — to index into it, check its length, or reuse it more than once | Values are only ever read once, start to finish, or the full sequence is too large — or too open-ended — to hold in memory all at once |

### yield vs return

`return` exits a function and hands back one value, all at once. `yield` hands back one value but pauses the function in place, keeping its local variables intact — the next call resumes right after that `yield` instead of starting over.

`next()` steps a generator forward one `yield` at a time. A `for` loop does this automatically, and stops cleanly on `StopIteration` instead of letting it raise.

```python-ref
def species_generator():
    yield "ball"
    yield "burmese"

gen = species_generator()
next(gen)    # "ball"
next(gen)    # "burmese"
next(gen)    # StopIteration — no values left
```

### Memory efficiency

A generator produces values on demand instead of building the whole result up front, so it can represent a sequence too large to fit in memory — or one with no fixed end at all.

`count_up()` never finishes and never stores more than the current `n` — a list built the same way (`[1, 2, 3, ...]`) would have to stop somewhere or run out of memory trying not to.

```python-ref
def count_up():
    n = 1
    while True:
        yield n
        n += 1

counter = count_up()
next(counter)    # 1
next(counter)    # 2
```

### Generator expressions

Parentheses instead of brackets turn a [list comprehension](collections.md#list-comprehension) into a generator expression — same filtering and transforming syntax, but values are produced lazily instead of built into a list all at once.

`doubled_list` below is an actual `list` — `[10, 24, 16]`, every value already computed — so it supports indexing, `len()`, and looping over more than once. `doubled_gen` is a `generator` — nothing has been computed yet, and it only supports stepping forward once with `next()` or a `for` loop, the same [list vs. generator](#generator-vs-a-regular-function) tradeoff covered above.

Use a list comprehension when the result needs indexing, `len()`, or more than one pass. Use a generator expression when it's only read once, or building the whole list would hold more in memory than necessary.

```python-ref
doubled_list = [length * 2 for length in [5, 12, 8]]    # builds the whole list right away
doubled_gen = (length * 2 for length in [5, 12, 8])     # computes each value only when asked
```

```python-ref
doubled_list[0]      # 10
len(doubled_list)    # 3

next(doubled_gen)    # 10 — computed on demand
doubled_gen[0]       # TypeError — a generator doesn't support indexing
```

??? tip "Stopping early"
    A generator expression can stop before producing every value — useful for finding just the first match without computing the rest.

    ```python-ref
    first_long = next(s for s in ["ball", "burmese", "boa"] if len(s) > 5)  # "burmese" — "boa" is never checked
    ```

    The equivalent list comprehension would build and check every item first, even though only the first one ends up used.

</div>

