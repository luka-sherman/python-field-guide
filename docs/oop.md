# Object-Oriented Programming (OOP)

**Object-oriented programming** groups related data and the functions that act on it into a single unit, instead of keeping them separate. A [dictionary](collections.md#dictionaries) can already hold a snake's data as key-value pairs — a **class** goes one step further, bundling that data together with the behavior (methods) that belongs to it.

| Concept | Example | What it is |
|---------|---------|------------|
| Class | `class Snake:` | The blueprint — defines what data and behavior every object built from it will have |
| Object (instance) | `ball = Snake("ball", 5)` | One specific thing built from the blueprint, with its own independent copy of the data |
| Attribute | `self.species` | A piece of data that belongs to an object |
| Method | `def describe(self):` | A function that belongs to a class and acts on a specific object |
| Inheritance | `class Boa(Snake):` | A new class that reuses — and can extend or override — another class's attributes and methods |

## Classes and Objects

A class is a blueprint for creating objects — it defines what attributes and methods every object built from it will have. An object is one specific instance built from that blueprint, with its own copy of the attributes.

```python
class Snake:
    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

ball = Snake("ball", 5)

print(ball.species)
print(ball.length_ft)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### The `__init__()` Method

```python-ref
ball = Snake("ball", 5)    # __init__ runs automatically, setting ball.species and ball.length_ft
```

</summary>

`__init__()` is a special method that runs automatically every time a new object is created — it's where you set up the object's starting attributes. Python calls this a **constructor**.

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
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### The `self` Parameter

```python-ref
self.species    # inside a method, refers to *this* object's own species — "ball" for ball, "burmese" for burmese
```

</summary>

`self` is the first parameter of every method in a class, and refers to the specific object the method was called on — it's how `ball.species` and `burmese.species` hold different values while sharing the same class. Python passes it in automatically; you never supply it yourself when calling a method (`ball.describe()`, not `ball.describe(ball)`).

```python
class Snake:
    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

ball = Snake("ball", 5)
burmese = Snake("burmese", 16)

print(ball.species)
print(burmese.species)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Object Methods

```python-ref
ball.describe()    # "a 5 ft ball python"
```

</summary>

A method is just a function defined inside a class — since it always receives `self`, it can read (or change) that specific object's own attributes.

```python
class Snake:
    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

    def describe(self):
        return f"a {self.length_ft} ft {self.species} python"

ball = Snake("ball", 5)
print(ball.describe())
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### The `__str__()` Method

```python-ref
print(ball)    # without __str__: <__main__.Snake object at 0x...>
               # with __str__:    "ball python, 5 ft"
```

</summary>

By default, `print()`-ing an object just shows its memory address, which isn't very useful. Defining `__str__()` on a class controls what `print()` shows instead.

```python
class Snake:
    def __init__(self, species, length_ft):
        self.species = species
        self.length_ft = length_ft

    def __str__(self):
        return f"{self.species} python, {self.length_ft} ft"

ball = Snake("ball", 5)
print(ball)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Modify & Delete Attributes

```python-ref
ball.length_ft = 6      # change an attribute directly, like any variable
del ball.length_ft      # remove just that attribute
del ball                # remove the whole object
```

</summary>

Assign to `object.attribute` to change it after creation. `del object.attribute` removes a single attribute; `del object` removes the object itself.

```python
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
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### The `pass` Statement

```python-ref
class Snake:
    pass    # an empty class body — valid syntax, nothing defined yet
```

</summary>

Same as in a loop or function — an empty class body is a syntax error on its own. `pass` is a placeholder for a class you haven't filled in yet.

```python
class Snake:
    pass

s = Snake()
print(s)
```

</details>

## Inheritance

A child class reuses — and can extend or override — everything defined in a parent class, instead of rewriting it from scratch. The parent is also called the **base class**; the child is the **derived class**.

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
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Overriding `__init__()`

```python-ref
class Boa(Snake):
    def __init__(self, species, length_ft, region):
        Snake.__init__(self, species, length_ft)
        self.region = region
```

</summary>

Adding `__init__()` to a child class replaces the parent's version entirely — call `Parent.__init__(self, ...)` explicitly inside it if you still want the parent's setup to run too.

```python
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
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Using `super()`

```python-ref
super().__init__(species, length_ft)    # same as Snake.__init__(self, species, length_ft), without naming the parent
```

</summary>

`super()` calls the parent's version of a method without naming the parent class directly — the usual, cleaner way to do what the previous example did by hand.

```python
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
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Adding Attributes and Methods

```python-ref
boa.region       # "south america" — new attribute, parent Snake has no such thing
boa.habitat()    # new method, only Boa has it
```

</summary>

A child class isn't limited to what its parent has — it can define brand-new attributes and methods of its own, on top of everything it inherits.

```python
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
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Overriding Methods

```python-ref
snake.describe()    # "a 5 ft ball python"        — Snake's own version
boa.describe()      # "a heavy-bodied constrictor" — Boa's version replaces it
```

</summary>

Defining a method in the child class with the exact same name as one in the parent replaces the parent's version for that child — this is the foundation of polymorphism, covered next.

```python
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

</details>

## Polymorphism

**Polymorphism** ("many forms") means the same method or function name behaves differently depending on which object it's called on — so you can call `.describe()` on any snake-like object without needing to know exactly which one it is.

```python
print(len("burmese python"))
print(len(["ball", "burmese", "boa"]))
print(len({"species": "ball", "length_ft": 5}))
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Same Method Name, Unrelated Classes

```python-ref
ball.move()     # "slither"
gecko.move()    # "climb"
```

</summary>

Classes don't need to be related by inheritance to share a method name — as long as each one defines its own `.move()`, calling it works the same way no matter which object it's called on.

```python
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
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Polymorphism via Inheritance

```python-ref
for s in (snake, boa): print(s.describe())
# a 5 ft ball python
# a heavy-bodied constrictor
```

</summary>

This is the more common case — a child class overrides a parent's method (as in the previous section), so looping over a mix of parent and child objects and calling the same method name runs each object's own version automatically.

```python
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

</details>
