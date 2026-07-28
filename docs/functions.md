# Functions

A **function** packages a block of code under a name, so it can be run again — with different inputs — instead of copying and pasting the same lines every time you need them. Python already has some built in (`print()`, `len()`), but `def` lets you write your own.

| Concept | Example | What it is |
|---------|---------|------------|
| Parameter | `def describe(species):` | A name a function expects to receive a value for, listed in its definition |
| Argument | `describe("ball")` | The actual value passed in when the function is called |
| Return value | `return f"a {species} python"` | The value a function sends back to whatever called it |
| Default value | `def describe(species="ball"):` | A fallback used when the caller doesn't supply that argument |

## Defining a Function

`def` names a function and lists the parameters it expects; the indented block underneath is what runs each time it's called.

```python
def describe(species):
    print(f"a {species} python")

describe("ball")
describe("burmese")
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Return Values

`return` sends a value back to the caller, instead of just printing it.
{: .pt-subheading }

```python-ref
def describe(species):
    return f"a {species} python"

message = describe("ball")    # "a ball python" — stored, not printed
```

</summary>

Without a `return`, a function hands back `None` automatically — covered on the [Basic Types](basic_types.md#functions-return-none-by-default) page. `return` also exits the function immediately, skipping any code written after it.

```python
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
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Default Parameter Values

A parameter can fall back to a default value if the caller doesn't supply one.
{: .pt-subheading }

```python-ref
def describe(species, length_ft=5):
    return f"a {length_ft} ft {species} python"

describe("ball")            # "a 5 ft ball python" — uses the default
describe("burmese", 12)     # "a 12 ft burmese python" — overrides it
```

</summary>

Parameters with a default must come after every parameter without one — Python reads arguments left to right, so a required parameter can't follow an optional one.

```python
def describe(species, length_ft=5):
    return f"a {length_ft} ft {species} python"

print(describe("ball"))
print(describe("burmese", 12))
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Keyword Arguments

Passing `name=value` lets you specify arguments out of order, or skip earlier defaults.
{: .pt-subheading }

```python-ref
def describe(species, length_ft=5, venomous=False):
    return f"{species}, {length_ft} ft, venomous: {venomous}"

describe(species="ball", venomous=True)    # length_ft still uses its default
```

</summary>

Arguments passed by position (like `describe("ball")`) must still come first; keyword arguments can follow in any order, and are matched by name instead of position.

```python
def describe(species, length_ft=5, venomous=False):
    return f"{species}, {length_ft} ft, venomous: {venomous}"

print(describe("ball", venomous=True))
print(describe(species="burmese", length_ft=12))
```

</details>

## Flexible Arguments

`*args` and `**kwargs` let a function accept an unpredictable number of arguments, instead of a fixed list of parameters.

```python
def total_length(*lengths):
    return sum(lengths)

print(total_length(5, 12, 8))
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### `*args`

Collects any number of positional arguments into a tuple.
{: .pt-subheading }

```python-ref
def total_length(*lengths):
    return sum(lengths)    # lengths is (5, 12, 8) inside the function

total_length(5, 12, 8)    # 25
```

</summary>

`*lengths` gathers however many positional arguments were passed into a single tuple named `lengths` — the function works the same whether it's called with one length or ten. `*args` is the conventional name, but any name after `*` works.

```python
def total_length(*lengths):
    print(lengths)
    return sum(lengths)

print(total_length(5, 12, 8))
print(total_length(4.5))
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### `**kwargs`

Collects any number of keyword arguments into a dict.
{: .pt-subheading }

```python-ref
def describe(**details):
    return details    # {"species": "ball", "length_ft": 5}

describe(species="ball", length_ft=5)
```

</summary>

`**details` gathers every `name=value` keyword argument into a dict named `details`, keyed by argument name. `**kwargs` is the conventional name, but like `*args`, any name after `**` works.

```python
def describe(**details):
    for key, value in details.items():
        print(key, value)

describe(species="ball", length_ft=5, venomous=False)
```

</details>

## Scope

A variable created inside a function is **local** — it only exists while that function is running, and isn't visible outside it.

```python
def set_species():
    species = "ball"    # local to this function
    print(species)

set_species()
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Local vs Global Variables

A variable defined at the top level of a file is **global** — readable from inside any function.
{: .pt-subheading }

```python-ref
species = "ball"    # global

def show_species():
    print(species)    # reads the global — no error
```

</summary>

A function can *read* a global variable freely, but assigning to that name inside a function creates a brand-new local variable instead of changing the global one — the next section covers how to actually change a global from inside a function.

```python
species = "ball"

def show_species():
    print(species)

show_species()
print(species)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Modifying a Global Variable

`global` tells Python that an assignment inside a function should change the global variable, not create a local one.
{: .pt-subheading }

```python-ref
count = 0

def record_sighting():
    global count
    count += 1    # changes the global count, not a local copy
```

</summary>

Without `global`, `count += 1` here would raise an error — Python sees the assignment and treats `count` as local for the whole function, then finds no local `count` to add to. `global` is needed occasionally, but reaching for it often is usually a sign the code would read more clearly passing values in and returning them instead.

```python
count = 0

def record_sighting():
    global count
    count += 1

record_sighting()
record_sighting()
print(count)
```

</details>
