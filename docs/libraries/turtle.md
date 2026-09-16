---
description: >-
  Building small movement-based games in Python with the turtle module: window setup,
  positions and motion, drawing shapes, the animation loop, keyboard and mouse input, and
  collision detection.
---

# :material-turtle:{ .lg .middle } Turtle library

[Official documentation :material-open-in-new:](https://docs.python.org/3/library/turtle.html){ target="_blank" }

<div class="pfg-section" markdown="block">

## Concepts

**turtle** draws with a single virtual pen — called a turtle — that sits on a window with a **position** (x,y coordinate) and a **heading** (the direction it's currently facing). `forward()` moves it in that direction, `left()`/`right()` change the heading, and if the pen is down, moving it traces a line behind it. 

The window also reacts to keyboard and mouse input, which makes turtle a natural fit for small, no-install games. A game needs a real window and display to run in, so the examples below aren't runnable in the browser — copy them into a local `.py` file to see them in action.

The origins of this library predate ordinary people owning computers: it comes from Logo, a language built in 1967 for teaching programming, whose original "turtle" was an actual robot that dragged a pen across a sheet of paper on the floor.

</div>

<div class="pfg-section" markdown="block">

## Setup { data-card-link="skip" }

`turtle` ships with the standard library — nothing to install.

```python-ref
from turtle import *
```

`*` imports everything at once; if you want to explicitly specify of what you're using, import the precise function names instead (`from turtle import forward, left, done`). 

</div>

<div class="pfg-section" markdown="block">

## The screen

Everything gets drawn inside one window — the screen.

### Screen setup

Start by creating a window..

```python-ref
setup(500, 500)   # width, height
title('My Game')  # optional
```

### Background

A solid color or a full image, set once on the window itself — not something that needs redrawing every frame.

```python-ref
bgcolor('skyblue')        # a solid color
bgpic('landscape.gif')    # or a full image, stretched to fit the window
```

Anything more custom than a flat color or a single picture — a gradient, a tiled pattern, a drawn horizon — is drawn by hand instead, using the same shapes from Drawing shapes below. Unlike `bgcolor()`/`bgpic()`, a hand-drawn background has to be part of the loop, since `clear()` erases it along with everything else each frame.

```python-ref
clear()
rectangle(Vec2D(-200, -200), 400, 400, 'skyblue')   # backdrop, drawn first
# ... draw everything else on top ...
update()
```

??? tip "The Tkinter Canvas underneath"
    turtle's window is a [Tkinter](tkinter.md) `Canvas` widget underneath — `getcanvas()` returns it directly, for mixing in real Tkinter widgets or features once turtle's own tools stop being enough.

### Clear screen

`clear()` erases drawings, leaving everything else — position, shape, color, event bindings — untouched, which is why it's the one used every frame. 

`clearscreen()` is a full reset instead: drawings gone, every turtle removed, background and bindings back to their defaults, tracer back on. More like starting the whole script over than clearing one frame — useful for a "play again" restart, not for the frame loop itself.


### Colors

Anywhere a color is expected — `color()`, `bgcolor()`, `dot()`'s color argument — turtle accepts three formats, all borrowed from Tk rather than defined by Python itself.

| Format | Example |
|---|---|
| A named color string | `'skyblue'` |
| A hex string | `'#33cc8c'` |
| An RGB tuple | `(0.2, 0.8, 0.5)` — each value `0.0`–`1.0` by default |

There's no small fixed list of named colors — turtle draws from the same [X11 color names](https://en.wikipedia.org/wiki/X11_color_names) Tk uses, a few hundred names in all. `colormode(255)` switches RGB tuples to the more familiar `0`–`255` range instead of `0.0`–`1.0`.


### Closing the window

`done()` (covered under The game loop) keeps the window open until it's closed by hand. `exitonclick()` is a common alternative for a finished game: keep the window open, then close it on the next click instead of waiting on the window's own close button. `bye()` closes it immediately, from code, without waiting for a click at all.

```python-ref
exitonclick()   # instead of done() — click anywhere to quit
```


</div>

<div class="pfg-section" markdown="block">

## The turtle cursor

The turtle is the only thing directly controllable at any moment. Other moveable parts are plain data (Positions and motion) instead of as turtles of their own. (The class-based `Turtle()` interface can create more than one, each independently controllable, but that's a different, more advanced style than the one covered here.)

Everything about the turtle itself otherwise falls into four groups: what it looks like, what it draws with (if anything), what shapes it traces, and where it is.

### Shape

#### Show or hide

The turtle — the small controllable arrow shown by default — is separate from anything it draws. Hiding it doesn't erase existing lines or shapes, and drawing continues normally either way; only the cursor itself disappears.

```python-ref
hideturtle()     # ht() — hide it
showturtle()     # st() — show it again
isvisible()      # True or False
```

#### Shape, color, size

`shape(shape_name)` switches between every built-in shapes.

| Shape name | Looks like |
|---|---|
| `'classic'` | A small, thin-tailed arrow — the default. |
| `'arrow'` | A plain triangular arrowhead, larger than `'classic'`. |
| `'turtle'` | A small turtle outline. |
| `'circle'` | A filled circle. |
| `'square'` | A filled square. |
| `'triangle'` | A filled triangle. |
| `'blank'` | Nothing at all — another way to hide the turtle, besides calling `hideturtle()`. |


`color()` sets its outline and fill, and can be any color format as described in the above [colors section](#colors).

```python-ref
shape('turtle')
shapesize(2)                    # scale it up 2x
color('darkgreen', 'green')     # outline, fill
```

#### Custom images

`register_shape()` installs an image file or a custom polygon as a shape, usable anywhere `shape()` is — a way to swap the cursor for a small custom picture. A limitation is that the custom image won't rotate. The built in shapes above turn to face the turtle's heading as it moves. An image shape always faces the same direction.

```python-ref
register_shape('snake.gif')
```

#### In a game

Many games hide the turtle and draws its own shapes instead — the right call once there's a trail, or several independent pieces, that no single turtle could represent alone. A game with just one clearly visible player, though, doesn't need any of that: give the turtle a shape and a color, then move it directly with `goto()`.

```python-ref
shape('turtle')
color('green')

def move():
    global player
    player = player + aim
    goto(player)      # the turtle itself is what moves on screen
    ontimer(move, 100)
```

That suits something like a maze runner or a chase game — one visible character the player steers, with everything else (walls, an enemy) drawn separately around it.

Being a visible, real turtle also means it can be clicked directly: `onclick(function)` fires only when the click lands on the turtle's own shape — unlike `onscreenclick()` (Input), which fires no matter where on the window the click happens.

```python-ref
def on_hit(x, y):
    print('hit!')

onclick(on_hit)
```

### Trace movement

#### With tracer

The Tracer is whether or not you can see the animation of the turtle moving. 

By default, turtle animates its own movement — `forward()`, `goto()`, etc. are drawn bit by bit, animated as if it is moving across the screen. This is called the `tracer` and by default it is True.

If you don't want that, the alternative is turning the `tracer()` off. Every move then happens instantly, with nothing new appearing on screen until you call `update()`. `tracer()` can be switched on or off again at any point in a script, though turning it off before the first `update()` avoids a first frame flashing briefly.

```python-ref
tracer(False)

update()      # if tracer is off, then rely on update() to redraw things
```

A related but separate setting — `speed(n)` controls how fast each individual `forward()`/`goto()` animates, from `1` (slowest) to `10` (fastest), or `0` for no animation delay at all. It only matters while `tracer()` is left on; with `tracer(False)`, nothing animates regardless of speed.

??? tip "Partial animation"
    `tracer()` also accepts two numbers, `tracer(n, delay)` — show only every `n`-th update, with `delay` milliseconds between them, instead of turning animation off completely. Useful for speeding up something slow and complex without losing the animation altogether.

??? tip "no_animation() block"
    A context manager wrapping the same idea as `tracer(False)`/`tracer(True)` — animation is off for whatever runs inside the block, then back on (and shown) once it exits. The same `with` pattern as [opening a file](../files.md#opening-a-file), applied to animation instead of a file handle.

    ```python-ref
    with no_animation():
        circle(50)   # drawn instantly, all at once
    ```

#### Without tracer

```python-ref
setup(420, 420, 370, 0)
tracer(False)
```

With `tracer(False)`, nothing new appears on screen until `update()` is called — normally once per frame, after everything for that frame has been drawn, so a whole frame gets drawn and shown at once instead of stroke-by-stroke. `clear()` wipes the previous frame's drawing first, so shapes don't pile up on top of each other.

```python-ref
clear()
# ... draw everything for this frame ...
update()
```

### Ink

The "pen" is really the ink behind it:

- **Down** means the tip is touching the paper, so ink comes out as the turtle moves.

- **Up** means it's lifted, so moving it leaves no line behind. 

| Function | What it does |
|---|---|
| `up()` / `down()` | Lift or lower the pen — move without drawing, or draw a line while moving. |
| `isdown()` | Return whether the pen is currently down. |
| `pensize(width)` | Set the line's thickness. |
| `color(outline_color, fill_color)` | Set colors for outline and fill. |
| `pencolor(outline_color)` | Set outline color. |
| `fillcolor(fill_color)` | Set fill color. |

```python-ref
color('black', 'yellow')  # set outline and fill at once 
down()
pensize(3)
forward(50)      # draws a 3px-thick line
up()
isdown()         # False
goto(0, 0)       # moves back without drawing
```

### Drawing shapes

Shapes are drawn by moving the pen with `up()`/`down()` (pen up means move without drawing a line), `goto()`, `forward()`, and `left()`, then filling the outline with `begin_fill()`/`end_fill()`.

| Function | What it does |
|---|---|
| `clear()` | Erase the previous frame's drawing. |
| `up()` / `down()` | Lift or lower the pen — move without drawing, or draw a line while moving. |
| `goto(x, y)` | Move the pen to an absolute position (also accepts a single `Vec2D`). |
| `forward(distance)` | Move the pen forward in its current heading, drawing a line if the pen is down. |
| `left(angle)` | Turn the pen's heading, in degrees. |
| `color(fill_color)` | Set the pen's fill/outline color. |
| `begin_fill()` / `end_fill()` | Start/stop filling the shape traced in between. |
| `pensize(width)` | Set the outline's thickness. |
| `update()` | Show everything drawn since the last `update()`. |

`clear()` always comes first and `update()` always comes last in a frame — everything in between is whatever needs drawing that frame. Within that: `up()` before moving somewhere without a line trailing behind, `down()` before tracing an outline; `begin_fill()` right before that outline, `end_fill()` right after it, with nothing in between that isn't part of the shape.

```python-ref
def square(point, size, fill_color):
    """Draw a filled square centered on point."""
    x, y = point
    up()
    goto(x - size / 2, y - size / 2)
    down()
    color(fill_color)
    begin_fill()
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()
```

#### Dot

A filled circle, built into turtle directly — no custom function needed. `dot(diameter, color)` draws it centered on wherever the pen currently is.

```python-ref
up()
goto(0, 0)
dot(20, 'green')
```

#### Circle

`circle(radius)` traces an actual curved path instead of stamping an instant dot — the center ends up `radius` units to the turtle's left, and the pen itself ends up back on the circle once it's done.

```python-ref
circle(50)
```

An `extent` (an angle) draws only part of the circle — an arc, or a pie-slice shape once combined with `begin_fill()`/`end_fill()` — instead of the whole thing.

```python-ref
begin_fill()
circle(50, 90)   # a quarter-circle arc
end_fill()
```

`steps` swaps the smooth curve for a regular polygon with that many sides instead — the same `forward()`/`left()` loop `square()` uses by hand, done automatically.

```python-ref
circle(50, steps=6)   # a hexagon
```

#### Rectangle

Same idea as `square()`, with independent width and height, drawn from a corner instead of the center — the shape a paddle or panel-style element would use.

```python-ref
def rectangle(point, width, height, fill_color):
    """Draw a filled rectangle with point as its bottom-left corner."""
    x, y = point
    up()
    goto(x, y)
    down()
    color(fill_color)
    begin_fill()
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()
```

#### Stamping

When the built-in `shape()` already looks right, `stamp()` leaves a copy of it at the pen's current position — a shortcut over writing a custom drawing function like `square()` or `rectangle()`. It returns an id, so a specific stamp can be erased later with `clearstamp(stamp_id)`.

```python-ref
shape('circle')
goto(food)
stamp_id = stamp()
```

#### Text

`write(text)` draws a string at the pen's current position — the way a score or a message gets shown, since none of the shapes above are built for it.

```python-ref
up()
goto(0, 180)
write('Score: 3', align='center', font=('Arial', 16, 'normal'))
```

`align` positions the text relative to that point (`'left'`, `'center'`, or `'right'`) instead of always starting from it. Like everything else on screen, a score needs to be redrawn as part of the frame — `clear()` erases it too, so `write()` has to run again every time the score changes.

### Positions and motion

A position is two numbers, x and y. turtle represents one with **`Vec2D`**, a tuple that also supports vector arithmetic — unlike a plain tuple, adding two `Vec2D`s adds their coordinates instead of concatenating them.

```python-ref
from turtle import Vec2D

ball = Vec2D(0, 0)
aim = Vec2D(3, 5)
ball = ball + aim     # Vec2D(3, 5) — moved by aim
x, y = ball            # unpack like any other tuple — 3, 5
```

??? note "Vec2D is immutable"
    `Vec2D` has no `.x`/`.y` attributes to assign to — like any tuple, it can't be changed in place. Moving something means reassigning the variable to a brand-new `Vec2D`, not editing the old one.

    ```python-ref
    aim = Vec2D(0, -10)
    aim = Vec2D(10, 0)     # a new Vec2D — not aim.x = 10
    ```

??? tip "Reassigning from inside a function"
    Reassigning a global variable's name from inside a function needs `global`, covered on [Functions](../functions.md#local-vs-global-variables) — a game typically has at least one small function whose only job is reassigning a position or direction this way. *Mutating* something in place instead (`trail.append(...)`, `paddles[1] = paddles[1] + Vec2D(0, 20)`, both from "Many positions at once" below) doesn't need `global`, since the name itself is never reassigned — only reassignment does.

    ```python-ref
    aim = Vec2D(0, -10)

    def change(x, y):
        global aim
        aim = Vec2D(x, y)
    ```

#### The turtle's own position

The turtle itself always knows where it is — `pos()` returns its current location as a `Vec2D`, the same type used everywhere else on this page, so a separate variable isn't strictly needed if the pen itself is what's moving.

```python-ref
goto(50, 30)
here = pos()   # Vec2D(50, 30)
```

`towards(point)` returns the angle from the turtle's current position toward another point, for aiming one thing at another instead of moving toward it directly. `setheading(angle)` then turns the pen to face that angle, in degrees, before `forward()` moves it.

```python-ref
setheading(towards(ball))
forward(5)
```

#### Many positions at once

A game's state is rarely just one lone position — a trail that grows over time, or several independent entities tracked at once. Both build on the same list/dict operations covered on [Collections](../collections.md).

```python-ref
trail = [Vec2D(10, 0)]
trail.append(trail[-1] + aim)   # grow by one at the end
trail.pop(0)                    # shrink by one at the start
```

```python-ref
paddles = {1: Vec2D(-200, 0), 2: Vec2D(190, 0)}
paddles[1] = paddles[1] + Vec2D(0, 20)   # move just one of them
```

</div>

<div class="pfg-section" markdown="block">

## The game loop

`ontimer(function, ms)` calls a function once, after a delay. Having that function schedule *itself* again as its last line turns a single call into a repeating loop — the heartbeat of any turtle game: move, redraw, schedule the next frame.

| Function | What it does |
|---|---|
| `ontimer(function, ms)` | Run a function once, after a delay — the basis of the game loop. |
| `done()` | Keep the window open, listening for scheduled calls. |

Call the loop function once, by hand, to draw the first frame — after that, it reschedules itself with `ontimer()` every time it runs.

```python-ref
def move():
    # ... update positions, redraw the screen ...
    ontimer(move, 100)   # call move() again in 100ms

move()   # kick off the first frame
done()   # keeps the window open, listening for the scheduled calls
```

??? tip "Spawning and removing things over time"
    A loop can also grow or shrink a list of its own entities as it runs — occasionally adding a new one, and dropping ones that have drifted off-screen or otherwise stopped mattering, using the same list operations as Positions and motion's "Many positions at once". `randrange()` is from the [random](random.md) module, not turtle.

    ```python-ref
    from random import randrange

    if randrange(10) == 0:
        entities.append(new_entity())

    while entities and not inside(entities[0]):
        entities.pop(0)
    ```

### done()

A Python script normally runs top to bottom and exits once it reaches the last line. `done()` is always that last line — but instead of letting the script exit, it **blocks**: it hands control to the window and just sits there, waiting.

While it waits, it watches for the scheduled calls and input registered earlier — `ontimer()`, keyboard clicks, mouse clicks — and fires them as they come in. Those registering functions don't wait around themselves; each one just notes down a function to run later and immediately moves on. Without a final `done()` (or `mainloop()`, an alias for the same thing) to block and keep the window alive, the script would reach its own end and exit before any of that registered work got a chance to run.

- **Before `done()`:** window setup, turtle setup, the function definitions, and the one manual call that kicks off the first frame.
- **`done()` itself:** called exactly once, by itself, as the very last line.
- **After `done()`:** nothing. That line never finishes, so anything placed below it never runs.

</div>

<div class="pfg-section" markdown="block">

## Input

Every kind of input turtle supports works the same way: register a function once, and it gets called automatically whenever the matching event happens — nothing actually listens for anything until `done()` starts the event loop at the end of the script, so registration itself can happen in any order.

### Keyboard

`listen()` puts the window in a state where it's paying attention to keyboard events; `onkey(function, key)` then binds one key to a function, called with no arguments every time that key is pressed.

| Function | What it does |
|---|---|
| `listen()` | Start paying attention to keyboard events. |
| `onkey(function, key)` | Run a function, with no arguments, whenever a key is pressed. |

```python-ref
def change(x, y):
    global aim
    aim = Vec2D(x, y)

listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
```

??? tip "Press vs release"
    `onkey()` is really an alias for `onkeypress()` — a key firing the moment it's pressed down. `onkeyrelease(function, key)` is the counterpart, firing when the key comes back up instead.

### Mouse

`onscreenclick(function)` calls a function every time the window is clicked, passing the click's x and y coordinates as arguments.

| Function | What it does |
|---|---|
| `onscreenclick(function)` | Run a function, passed the click's x/y, whenever the window is clicked. |

```python-ref
def tap(x, y):
    global ball
    ball = ball + Vec2D(0, 30)

onscreenclick(tap)
```

??? tip "Dragging and releasing"
    `ondrag(function)` calls a function repeatedly, passed the pointer's x/y, while the mouse moves with the button held down — for something dragged around rather than tapped. `onrelease(function)` is the counterpart to `onscreenclick()`, firing when a click ends instead of when it starts.

### Dialog prompts

`textinput(title, prompt)` and `numinput(title, prompt)` pop up a small dialog box asking for a string or a number, returning what the player typed (or `None` if they cancelled). It's a separate native window, centered over the game window rather than drawn on the canvas.

Unlike everything else on this page, **a dialog pauses until it's answered.**

```python-ref
name = textinput('Player name', 'Enter your name:')
lives = numinput('Lives', 'How many lives?', default=3, minval=1, maxval=5)
```

</div>

<div class="pfg-section" markdown="block">

## Detecting collisions

Many games reduce to the same question: is this position touching that one?

```python-ref
def inside(point):
    """Return True if point is within the screen's boundaries."""
    x, y = point
    return -200 < x < 200 and -200 < y < 200
```

### Distance

`abs()` on a `Vec2D` returns its length — subtracting two positions first gives the distance between them, without writing out a square root by hand.

```python-ref
paddle = Vec2D(-200, 0)
close_enough = abs(ball - paddle) < 15
```

### Overlap

Checking whether a point falls within a range — a paddle's height, say — is a plain comparison, no vector math needed.

```python-ref
_, paddle_y = paddle
_, ball_y = ball

low = paddle_y
high = paddle_y + 50
touching = low <= ball_y <= high
```

### Membership

A position can also collide with itself — checking whether it already appears somewhere in a list of positions, the same `in` used for any other membership check.

```python-ref
head = trail[-1] + aim
crashed = head in trail
```

</div>

<div class="pfg-section" markdown="block">

## Common patterns

Every block above is a small, general-purpose piece. Combined, a few recurring shapes cover most simple games — each sketched below as pseudocode, the shape to fill in with real building blocks from the sections above.

**A single controlled object** — one position (Positions and motion), moved by keyboard or mouse input (Input), redrawn every frame (The game loop).

```python-ref
position = starting point
direction = nothing, to start

def on_key(new_direction):
    change direction to new_direction

def move():
    position = position + direction
    redraw the object at its new position
    schedule the next frame
```

**A trail that grows** — a list of positions instead of one (Many positions at once), growing at one end and shrinking at the other as the controlled object moves, checked against its own history for a collision (Membership).

```python-ref
trail = [starting position]
direction = starting direction

def move():
    new_head = trail[-1] + direction

    if new_head is out of bounds or new_head in trail:
        stop — game over

    trail.append(new_head)
    if new_head did NOT reach a target:
        trail.pop(0)   # shrink back down to the same length
    # otherwise leave the tail alone — the trail grows by one

    redraw every position in trail
    schedule the next frame
```

**Several independent entities** — more than one position tracked at once: a dict keyed by name or number for entities that stick around the whole game (Many positions at once), or a list that grows and shrinks as entities come and go over time (The game loop's "Spawning and removing things over time").

```python-ref
entities = []   # or {}, for ones with names rather than a changing count

def move():
    for each entity in entities:
        move it

    occasionally, append a new entity
    remove any entity that's drifted off-screen or otherwise stopped mattering

    redraw every entity
    schedule the next frame
```

**Reacting to a collision** — once two positions are found to be touching (Distance, Overlap, Membership, or the boundary check that opens Detecting collisions), something specific has to change as a result — the collision check on its own doesn't do anything.

```python-ref
def move():
    # ... update positions ...

    if touching(a, b):
        one of:
            stop entirely, without scheduling another frame   # a game-ending collision
            change direction                                  # a bouncing collision
            update score, or remove one of the two             # a scoring collision

    redraw everything
    schedule the next frame
```

**Bouncing off a boundary** — a special case of reacting to a collision, common enough on its own: hitting an edge flips the *component* of direction pointing into it, and leaves the other one alone, so the bounce looks like a reflection instead of a stop or a reversal.

```python-ref
def move():
    position = position + direction
    x, y = position
    dx, dy = direction

    if x is past the left or right edge:
        direction = Vec2D(-dx, dy)   # only the x part flips
    if y is past the top or bottom edge:
        direction = Vec2D(dx, -dy)   # only the y part flips

    redraw everything
    schedule the next frame
```

**Multiple players** — more than one controlled object (Several independent entities), each moved by its own subset of key bindings instead of one shared direction.

```python-ref
players = {1: starting position, 2: another starting position}

def move_player(which, change):
    players[which] = players[which] + change

on_key(lambda: move_player(1, up), key_for_player_1_up)
on_key(lambda: move_player(2, up), key_for_player_2_up)
# ... one binding per player, per direction ...
```

**A permanent trail instead of redrawing** — leaving the pen down the whole time (Ink as the game itself) instead of lifting it to reposition, so movement itself draws something that's never erased, rather than a shape cleared and redrawn every frame.

```python-ref
def move():
    position = position + direction
    goto(position)   # pen stays down — this itself draws the trail

    if position in trail:
        stop entirely   # crossed its own ink

    trail.append(position)
    schedule the next frame
```

Mixing and matching these — a controlled object *and* a growing trail, say, or several players *and* a score — is how a specific game takes shape from these general pieces.

</div>

<div class="pfg-section" markdown="block">

## More advanced games { data-card-link="skip" }

turtle's window and shapes are enough for something like snake, flappy, or pong, but not for much more — no sprites, no sound, no real physics. For anything more advanced, [pygame](https://www.pygame.org/docs/) and [arcade](https://api.arcade.academy/) are the two most common next steps; both have their own official documentation, linked above.

</div>
