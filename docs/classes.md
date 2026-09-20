---
description: >-
  Python classes and object-oriented programming explained with runnable examples:
  attributes, methods, property/staticmethod/classmethod, and inheritance.
---

# :material-package-variant:{ .lg .middle } Classes

A **class** bundles related data together with the behavior (methods) that acts on it, instead of keeping them separate. A [dictionary](collections.md#dictionaries) can already hold a snake's data as key-value pairs — a class goes one step further, pairing that data with the functions that work on it. Structuring code this way is called **object-oriented programming (OOP)**.

| Concept | Example | What it is |
|---------|---------|------------|
| Class | `class Snake:` | The blueprint — defines what data and behavior every object built from it will have |
| Object (instance) | `ball = Snake("ball", 5)` | One specific thing built from the blueprint, with its own independent copy of the data |
| Attribute | `self.species` | A piece of data that belongs to an object |
| Method | `def describe(self):` | A function that belongs to a class and acts on a specific object |
| Inheritance | `class Boa(Snake):` | A new class that reuses — and can extend or override — another class's attributes and methods |

<div class="pfg-section" markdown="block">

## Defining a class

A class is a blueprint for creating objects — it defines what attributes and methods every object built from it will have. An object is one specific instance built from that blueprint, with its own copy of the attributes.

The class definition line contains **`class`**, a **class name** (capitalized in PascalCase, unlike variables' `snake_case`), and a **colon**. Under it is an indented **body** — usually starting with `__init__`, the method that sets up a new object's starting attributes.

```python-ref
class ClassName:
    def __init__(self, parameter):
        self.attribute = parameter
```

Create an object by calling the class like a function: `ClassName(argument)`.

```python-ref
class Snake:
    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

ball = Snake("ball", 5)

print(ball.species)
print(ball.length_ft)
```

What `ball = Snake("ball", 5)` does:

0. Creates a new, empty object.
1. Calls `__init__` automatically, passing that object in as `self`, plus the arguments given — `"ball"` and `5`, matching `species` and `length_ft`.
2. `self.species = species` and `self.length_ft = length_ft` store those as **attributes** — data belonging to this one object, not to the `Snake` class as a whole.
3. Stores the finished object in `ball`.

`burmese = Snake("burmese", 16)` builds a separate object the same way — `burmese.species` and `ball.species` don't share data, same as two function calls (previous page) don't share local variables.

### The `__init__()` method

Runs automatically every time a new object is created — step 1 above. It's where an object's starting attributes get set up. Python calls this a **constructor**. You never call `__init__()` directly — `Snake("ball", 5)` is what triggers Python to call it.

```python-ref
ball = Snake("ball", 5)    # __init__ runs automatically, setting ball.species and ball.length_ft
```

??? warning "Avoid mutable default arguments"
    A default argument's value is created once, when the method is defined — not fresh for every object. For a mutable default like a list or dict, every object that doesn't pass its own value ends up sharing that exact same one.

    ```python-ref
    class Snake:
        def __init__(self, species, tags=[]):    # tags=[] is created once, not per-object
            self.species = species
            self.tags = tags

    ball = Snake("ball")
    ball.tags.append("captive-bred")

    burmese = Snake("burmese")
    print(burmese.tags)    # ["captive-bred"] — leaked from ball, since both share the same list
    ```

    Use `None` as the default instead, and build a fresh list inside `__init__` only if nothing was passed:

    ```python-ref
    class Snake:
        def __init__(self, species, tags=None):
            self.species = species
            self.tags = tags if tags is not None else []    # a new list every time
    ```

### The self parameter

Refers to the specific object a method was called on. One `Snake` class, but many `Snake` objects (`ball`, `burmese`, ...) sharing its method code — `self` is how a method written once still knows which object to act on.

`self` is always a method's first parameter, filled in automatically by Python — you never supply it yourself (`ball.describe()`, not `ball.describe(ball)`). Writing `ball.describe()` is what passes `ball` in as `self`.

```python-ref
self.species    # inside a method, refers to *this* object's own species — "ball" for ball, "burmese" for burmese
```

Same method, different object, different `self`:

```python-ref
ball.describe()      # self is ball    → "a 5 ft ball python"
burmese.describe()   # self is burmese → "a 16 ft burmese python"
```

### Object methods

A method is a function defined inside a class — parameters, `return`, and defaults all work the same as on the [Functions](functions.md) page. The one addition is `self`, which lets it read or change that specific object's own attributes.

```python-ref
ball.describe()    # "a 5 ft ball python"
```

### Instance attributes

An instance attribute is set with `self.x = value`, usually inside `__init__`. This is the default way a class stores data — each object gets its own independent copy, separate from every other object's.

```python-ref
class Snake:
    def __init__(self, species, length_ft):
        self.species = species      # instance attribute
        self.length_ft = length_ft

ball = Snake("ball", 5)
burmese = Snake("burmese", 16)

print(ball.species)       # "ball"
print(burmese.species)    # "burmese" — a separate copy, not shared
```

For a value every object should share instead of holding its own copy, see [class attributes](#class-attributes) below.

<div data-advanced="true" markdown="block">

??? efficiency "For efficiency, use __slots__ when creating many instances"
    | | Time | Space (n instances) |
    |---|---|---|
    | Plain instance | — | <span class="pt-bigo pt-bigo--ok">O(n)</span> |
    | `__slots__` | — | <span class="pt-bigo pt-bigo--ok">O(n)</span> (same class, smaller constant) |

    Each instance normally keeps its attributes in a per-object `__dict__`, which costs some [memory](style.md#time-and-space) on top of the attribute values themselves — usually not worth worrying about, but it adds up when a program holds thousands or millions of instances at once. `__slots__` trades that flexibility for a fixed, lighter attribute layout:

    ```python-ref
    class Snake:
        __slots__ = ("species", "length_ft")   # only these attributes are allowed, no __dict__

        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft
    ```

    An instance built from this class can no longer get a new attribute added after creation — `ball.venomous = False` raises `AttributeError`, since there's no `__dict__` left for it to go into.

    See [Efficiency](style.md#efficiency) for why this distinction matters.

</div>

### Class attributes

A class attribute is set directly in the class body, outside `__init__` — shared by every object built from that class, unlike an [instance attribute](#instance-attributes), which is a separate copy per object. Assigning to `object.attribute` always creates (or updates) an instance attribute, even if a class attribute of the same name exists — it doesn't change the shared value, just shadows it for that one object.

```python-ref
class Snake:
    kingdom = "Animalia"    # class attribute — shared by every Snake object

    def __init__(self, species, length_ft):
        self.species = species        # instance attribute — its own copy per object
        self.length_ft = length_ft

ball = Snake("ball", 5)
burmese = Snake("burmese", 16)

print(ball.kingdom)       # "Animalia"
print(burmese.kingdom)    # "Animalia" — same value, shared

ball.kingdom = "Reptilia"    # creates an instance attribute — doesn't touch the class attribute
print(ball.kingdom)          # "Reptilia" — this object's own copy now
print(burmese.kingdom)       # "Animalia" — unaffected
```

| | Instance attribute | Class attribute |
|---|---|---|
| Set with | `self.x = value`, usually in `__init__` | `x = value` directly in the class body |
| Copies | One per object | One, shared by every object |
| Changing it on one object | Only that object sees the change | Reassigning through the class changes it for every object that hasn't shadowed it |
| Use it for | Data that's different for each object — `species`, `length_ft` | A value every object of the class shares — a constant, a shared default, a running count |

### Going further { data-card-link="skip" }

??? tip "The `__str__()` method"
    Controls what `print()` shows for an object, instead of its memory address. By default, `print()`-ing an object just shows its memory address, which isn't very useful.

    ```python-ref
    print(ball)    # without __str__: <__main__.Snake object at 0x...>
                   # with __str__:    "ball python, 5 ft"
    ```

??? tip "The `__repr__()` method"
    Controls what `repr()` returns for an object — used when Python needs a representation and there's no `__str__()` to fall back on, like printing an object *inside* a list.

    ```python-ref
    print([ball])    # without __repr__: [<__main__.Snake object at 0x...>]
                      # with __repr__:    [Snake('ball', 5)]
    ```

    Convention is to make it look like the code that would recreate the object — unlike `__str__()`'s more casual, human-readable description.

    ```python-ref
    def __repr__(self):
        return f"Snake({self.species!r}, {self.length_ft})"
    ```

??? tip "Modify & delete attributes"
    Assign to `object.attribute` to change it after creation — an object is **mutable**, so this changes it in place, the same as [updating an item in a list](collections.md#access-and-update-items). That also means a second variable pointing at the same object sees the change too: `twin = ball` doesn't copy `ball`, it just gives the same object a second name.

    `del object.attribute` removes a single attribute; `del object` removes the object itself.

    ```python-ref
    ball.length_ft = 6        # change an attribute directly, like any variable

    twin = ball                # twin and ball are the same object, not a copy
    twin.length_ft = 7         # mutates that shared object
    print(ball.length_ft)      # 7 — the change shows up through ball too

    del ball.length_ft         # remove just that attribute
    del ball                   # remove the whole object
    ```

??? tip "pass placeholder"
    A placeholder for a class you haven't filled in yet. Same as in a loop or function — an empty class body is a syntax error on its own.

    ```python-ref
    class Snake:
        pass    # an empty class body — valid syntax, nothing defined yet
    ```

??? run "Run a classes and objects example"
    All the examples above, combined into one script:

    ```python
    class Snake:
        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft

    ball = Snake("ball", 5)

    print(ball.species)
    print(ball.length_ft)

    burmese = Snake("burmese", 16)
    print(burmese.species)
    print(burmese.length_ft)


    class Snake:
        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft

    ball = Snake("ball", 5)
    burmese = Snake("burmese", 16)

    print(ball.species)
    print(burmese.species)


    class Snake:
        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft

        def describe(self):
            return f"a {self.length_ft} ft {self.species} python"

    ball = Snake("ball", 5)
    print(ball.describe())


    class Snake:
        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft

        def __str__(self):
            return f"{self.species} python, {self.length_ft} ft"

    ball = Snake("ball", 5)
    print(ball)


    class Snake:
        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft

    ball = Snake("ball", 5)
    ball.length_ft = 6
    print(ball.length_ft)

    del ball.length_ft
    print(ball.species)

    del ball
    print("ball object deleted")


    class Snake:
        pass

    s = Snake()
    print(s)
    ```

</div>

<div class="pfg-section" markdown="block">

## Method decorators { data-advanced="true" }

Python provides 3 built-in [decorators](functions.md#decorators) for methods that change how the method is called and add functionality:

```python-ref
class Snake:
    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

    @property                                   # a computed attribute
    def length_cm(self):                        # will be called like an attribute, not a method
        return self.length_ft * 30.48

    @staticmethod                               # a class-level utility
    def is_valid_length(length_ft):             # no self — doesn't need an object
        return length_ft > 0

    @classmethod                                # an alternate constructor to __init__
    def from_cm(cls, species, length_cm):       # receives cls (the class) instead of self
        return cls(species, length_cm / 30.48)

ball = Snake("ball", 5)
ball.length_cm                           # 152.4 — called like an attribute, no parentheses
Snake.is_valid_length(5)                 # True — called on the class, no object needed
Snake.from_cm("ball", 152.4).length_ft   # 5.0 — builds a new object instead of modifying one
```

### @property

Call it like a plain attribute, no parentheses. Turns a method into a value computed fresh every time it's read, instead of stored and going stale — `length_cm` below always reflects the current `length_ft`, even if it changes later. 

Use it for a value that's cheap to derive from existing attributes and should look like a plain attribute to the rest of the code; skip it if the computation is expensive to redo on every access, or needs its own arguments beyond `self`.

??? tip "Property setters"
    A property is read-only by default — assigning to it raises an error unless you also define a setter with `@x.setter`, named the same as the property.

    ```python-ref
    class Snake:
        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft

        @property
        def length_cm(self):
            return self.length_ft * 30.48

        @length_cm.setter
        def length_cm(self, value):
            self.length_ft = value / 30.48

    ball = Snake("ball", 5)
    ball.length_cm = 304.8    # runs the setter, which updates length_ft
    ball.length_ft            # 10.0
    ```

### @staticmethod

Call it without needing an object at all, directly on the class. Removes the automatic `self`, so the method can't read or change any object's data — it's really just a plain function, grouped under the class because it's conceptually related. 

Use it for logic tied to the class's purpose but not to any one object's state, like a validation check; if it needs `self`, it should be a regular method instead.

### @classmethod

Call it as an alternative way to build an object. Receives the class itself (conventionally named `cls`) instead of an object, so it can construct and return a new instance. 

Use it when there's more than one sensible way to build an object — `Snake.from_cm(...)` alongside the usual `Snake(...)` — as a second, clearly-named constructor; skip it if there's only one way to build the object, since `__init__()` would be complete.

</div>

<div class="pfg-section" markdown="block">

## Inheritance

A child class reuses — and can extend or override — everything defined in a parent class, instead of rewriting it from scratch. The parent is also called the **base class**; the child is the **derived class**.

```python-ref
class Snake:
    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

    def describe(self):
        return f"a {self.length_ft} ft {self.species} python"


class Boa(Snake):
    pass

boa = Boa("boa constrictor", 10)
print(boa.describe())
```

### Overriding `__init__()`

Adding `__init__()` to a child class replaces the parent's version entirely. Call `Parent.__init__(self, ...)` explicitly inside it if you still want the parent's setup to run too.

```python-ref
class Boa(Snake):
    def __init__(self, species, length_ft, region):
        Snake.__init__(self, species, length_ft)
        self.region = region
```

### Using super()

Calls the parent's version of a method without naming the parent class directly. The usual, cleaner way to do what the previous example did by hand.

```python-ref
super().__init__(species, length_ft)    # same as Snake.__init__(self, species, length_ft), without naming the parent
```

### Adding attributes and methods

A child class isn't limited to what its parent has. It can define brand-new attributes and methods of its own, on top of everything it inherits.

```python-ref
boa.region       # "south america" — new attribute, parent Snake has no such thing
boa.habitat()    # new method, only Boa has it
```

### Overriding methods

Defining a method in the child class with the exact same name as one in the parent replaces the parent's version for that child. This is the foundation of polymorphism, covered next.

```python-ref
snake.describe()    # "a 5 ft ball python"        — Snake's own version
boa.describe()      # "a heavy-bodied constrictor" — Boa's version replaces it
```

### Multiple inheritance { data-advanced="true" }

A class can list more than one parent, comma-separated — it inherits the combined attributes and methods of all of them. When two parents define the same method, Python searches left to right through the parents listed and uses the first match — this search order is called the **MRO** (method resolution order).

```python-ref
class Venomous:
    def warning(self):
        return "handle with extreme caution"

class Constrictor:
    def warning(self):
        return "handle with care, can constrict"

class Cobra(Venomous, Constrictor):
    pass

cobra = Cobra()
print(cobra.warning())    # "handle with extreme caution" — Venomous is listed first
```

`Cobra.__mro__` shows the actual search order Python used, in case more than two parents makes it unclear.

### Going further { data-card-link="skip" }

??? run "Run an inheritance example"
    All the examples above, combined into one script:

    ```python
    class Snake:
        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft

        def describe(self):
            return f"a {self.length_ft} ft {self.species} python"


    class Boa(Snake):
        pass

    boa = Boa("boa constrictor", 10)
    print(boa.describe())


    class Snake:
        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft


    class Boa(Snake):
        def __init__(self, species, length_ft, region):
            Snake.__init__(self, species, length_ft)
            self.region = region

    boa = Boa("boa constrictor", 10, "south america")
    print(boa.species)
    print(boa.region)


    class Snake:
        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft


    class Boa(Snake):
        def __init__(self, species, length_ft, region):
            super().__init__(species, length_ft)
            self.region = region

    boa = Boa("boa constrictor", 10, "south america")
    print(boa.species)
    print(boa.region)


    class Snake:
        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft


    class Boa(Snake):
        def __init__(self, species, length_ft, region):
            super().__init__(species, length_ft)
            self.region = region

        def habitat(self):
            return f"found in {self.region}"

    boa = Boa("boa constrictor", 10, "south america")
    print(boa.region)
    print(boa.habitat())


    class Snake:
        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft

        def describe(self):
            return f"a {self.length_ft} ft {self.species} python"


    class Boa(Snake):
        def describe(self):
            return "a heavy-bodied constrictor"

    snake = Snake("ball", 5)
    boa = Boa("boa constrictor", 10)

    print(snake.describe())
    print(boa.describe())
    ```

</div>

<div class="pfg-section" markdown="block">

## Polymorphism { data-advanced="true" }

**Polymorphism** ("many forms") means the same method or function name behaves differently depending on which object it's called on — so you can call `.describe()` on any snake-like object without needing to know exactly which one it is.

```python-ref
print(len("burmese python"))
print(len(["ball", "burmese", "boa"]))
print(len({"species": "ball", "length_ft": 5}))
```

### Duplicate method names

Classes don't need to be related by inheritance to share a method name. As long as each one defines its own `.move()`, calling it works the same way no matter which object it's called on.

```python-ref
ball.move()     # "slither"
gecko.move()    # "climb"
```

### Polymorphism via inheritance

Looping over a mix of parent and child objects and calling the same method name runs each object's own version automatically. This is the more common case — a child class overrides a parent's method, as in the previous section.

```python-ref
for s in (snake, boa): print(s.describe())
# a 5 ft ball python
# a heavy-bodied constrictor
```

### Going further { data-card-link="skip" }

??? run "Run a polymorphism example"
    All the examples above, combined into one script:

    ```python
    print(len("burmese python"))
    print(len(["ball", "burmese", "boa"]))
    print(len({"species": "ball", "length_ft": 5}))


    class Snake:
        def move(self):
            print("slither")


    class Gecko:
        def move(self):
            print("climb")

    ball = Snake()
    gecko = Gecko()

    for animal in (ball, gecko):
        animal.move()


    class Snake:
        def __init__(self, species, length_ft):
            self.species = species
            self.length_ft = length_ft

        def describe(self):
            return f"a {self.length_ft} ft {self.species} python"


    class Boa(Snake):
        def describe(self):
            return "a heavy-bodied constrictor"

    snake = Snake("ball", 5)
    boa = Boa("boa constrictor", 10)

    for s in (snake, boa):
        print(s.describe())
    ```

</div>

<div class="pfg-section" markdown="block">

## Encapsulation { data-advanced="true" }

**Encapsulation** restricts direct access to an object's data, so it can only be read or changed through the class's own methods. Python doesn't enforce this the way some other languages do — it's a naming convention the caller is trusted to respect, not a hard restriction.

### Single underscore

A leading underscore (`_species`) signals "internal — not part of the class's public interface." Python doesn't actually stop outside code from reading or changing it; it's a convention, not a lock.

```python-ref
class Snake:
    def __init__(self, species, length_ft):
        self._species = species    # leading underscore — treat as internal

ball = Snake("ball", 5)
ball._species    # "ball" — still accessible, just a signal not to
```

### Double underscore

A leading double underscore (`__species`) triggers **name mangling** — Python renames the attribute internally to `_ClassName__species`, making it awkward (though still not impossible) to reach from outside the class.

```python-ref
class Snake:
    def __init__(self, species, length_ft):
        self.__species = species    # name-mangled

ball = Snake("ball", 5)
ball.__species          # AttributeError — not found under this name
ball._Snake__species    # "ball" — the actual mangled name
```

### Controlled access with @property

Pair an underscore-prefixed attribute with [`@property`](#property) to actually enforce something — like validation — instead of only signaling intent.

```python-ref
class Snake:
    def __init__(self, species, length_ft):
        self._length_ft = length_ft

    @property
    def length_ft(self):
        return self._length_ft

    @length_ft.setter
    def length_ft(self, value):
        if value <= 0:
            raise ValueError("length_ft must be positive")
        self._length_ft = value

ball = Snake("ball", 5)
ball.length_ft = -1    # ValueError — blocked by the setter
```

</div>

<div class="pfg-section" markdown="block">

## Operator overloading { data-advanced="true" }

Defining a dunder method lets a built-in operator (`==`, `<`, `+`, ...) work on your own objects — the same mechanism as [`__str__()`](#defining-a-class) and [`__repr__()`](#defining-a-class), just for operators instead of printing.

```python-ref
ball = Snake("ball", 5)
ball == Snake("ball", 5)    # False — without __eq__, Python compares by identity, not by data
```

### Comparing with `__eq__` and `__lt__`

`__eq__` defines what `==` does; `__lt__` defines what `<` does. Without them, `==` falls back to comparing identity (is this the exact same object?) rather than the data inside.

```python-ref
class Snake:
    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

    def __eq__(self, other):
        return self.length_ft == other.length_ft

    def __lt__(self, other):
        return self.length_ft < other.length_ft

ball = Snake("ball", 5)
burmese = Snake("burmese", 16)

print(ball == Snake("ball", 5))    # True — same length_ft
print(ball < burmese)              # True — 5 < 16
```

### Arithmetic with `__add__`

`__add__` defines what `+` does between two objects — whatever combining them should mean for this class.

```python-ref
class Snake:
    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

    def __add__(self, other):
        return self.length_ft + other.length_ft

ball = Snake("ball", 5)
burmese = Snake("burmese", 16)

print(ball + burmese)    # 21 — combined length
```

</div>

<div class="pfg-section" markdown="block">

## Dataclasses { data-advanced="true" }

`@dataclass` generates `__init__()` and `__repr__()` automatically from a list of typed attributes, instead of writing them by hand.

```python-ref
from dataclasses import dataclass

@dataclass
class Snake:
    species: str
    length_ft: float

ball = Snake("ball", 5)
print(ball)    # Snake(species='ball', length_ft=5) — __repr__ generated automatically
```

Equivalent to writing the same class by hand:

```python-ref
class Snake:
    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

    def __repr__(self):
        return f"Snake(species={self.species!r}, length_ft={self.length_ft!r})"
```

Use it for a class that's mostly just holding data, with little or no custom behavior; skip it once a class needs real logic beyond storing and reporting its attributes.

</div>

<div class="pfg-section" markdown="block">

## Abstract base classes { data-advanced="true" }

An **abstract base class** defines methods that every subclass must implement, using `abc.ABC` and `@abstractmethod`. Trying to create an object from a class that hasn't implemented all of them raises a `TypeError` immediately, instead of failing later when the missing method actually gets called.

```python-ref
from abc import ABC, abstractmethod

class Snake(ABC):
    @abstractmethod
    def move(self):
        ...

class Boa(Snake):
    def move(self):
        return "slither"

boa = Boa()      # works — Boa implements move()
snake = Snake()  # TypeError — can't instantiate abstract class with abstract method 'move'
```

Use it when a base class should only ever be a template — never instantiated directly — and every subclass must supply certain methods; skip it for ordinary inheritance where the base class already works fine on its own, as with `Snake` and `Boa` [earlier on this page](#inheritance).

</div>

