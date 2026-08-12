# :material-package-variant:{ .lg .middle } Classes & Object-oriented programming (OOP)

**Object-oriented programming** groups related data and the functions that act on it into a single unit, instead of keeping them separate. A [dictionary](collections.md#dictionaries) can already hold a snake's data as key-value pairs — a **class** goes one step further, bundling that data together with the behavior (methods) that belongs to it.

| Concept | Example | What it is |
|---------|---------|------------|
| Class | `class Snake:` | The blueprint — defines what data and behavior every object built from it will have |
| Object (instance) | `ball = Snake("ball", 5)` | One specific thing built from the blueprint, with its own independent copy of the data |
| Attribute | `self.species` | A piece of data that belongs to an object |
| Method | `def describe(self):` | A function that belongs to a class and acts on a specific object |
| Inheritance | `class Boa(Snake):` | A new class that reuses — and can extend or override — another class's attributes and methods |

## Classes and objects

A class is a blueprint for creating objects — it defines what attributes and methods every object built from it will have. An object is one specific instance built from that blueprint, with its own copy of the attributes.

```python-ref
class Snake:
    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

ball = Snake("ball", 5)

print(ball.species)
print(ball.length_ft)
```

### The `__init__()` method

Runs automatically every time a new object is created. It's where you set up the object's starting attributes. Python calls this a **constructor**.

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

### The `self` parameter

Refers to the specific object a method was called on. `self` is the first parameter of every method in a class — it's how `ball.species` and `burmese.species` hold different values while sharing the same class. Python passes it in automatically; you never supply it yourself when calling a method (`ball.describe()`, not `ball.describe(ball)`).

```python-ref
self.species    # inside a method, refers to *this* object's own species — "ball" for ball, "burmese" for burmese
```

### Object methods

A method is just a function defined inside a class. Since it always receives `self`, it can read (or change) that specific object's own attributes.

```python-ref
ball.describe()    # "a 5 ft ball python"
```

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
    Assign to `object.attribute` to change it after creation. `del object.attribute` removes a single attribute; `del object` removes the object itself.

    ```python-ref
    ball.length_ft = 6      # change an attribute directly, like any variable
    del ball.length_ft      # remove just that attribute
    del ball                # remove the whole object
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

### Using `super()`

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

## Polymorphism

**Polymorphism** ("many forms") means the same method or function name behaves differently depending on which object it's called on — so you can call `.describe()` on any snake-like object without needing to know exactly which one it is.

```python-ref
print(len("burmese python"))
print(len(["ball", "burmese", "boa"]))
print(len({"species": "ball", "length_ft": 5}))
```

### Same method name, unrelated classes

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
