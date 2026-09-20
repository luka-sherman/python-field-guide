---
description: >-
  A path through turtle, random, and classes for building a small game from scratch — a window,
  movement, randomness, and more than one moving thing to keep track of.
---

# :material-gamepad-variant-outline:{ .lg .middle } Make games

This expedition strings together the building blocks for a small, no-install game: a window that
responds to input, movement that isn't the same every time, and code organized well enough to
hold more than one moving thing at once.

The path: [turtle](../libraries/turtle.md) → [random](../libraries/random.md) →
[classes](../classes.md).

## turtle

[turtle](../libraries/turtle.md) is the foundation: a window, a drawing surface, and a game loop
(`ontimer`) that redraws the screen on a fixed schedule. Its [Positions and
motion](../libraries/turtle.md#positions-and-motion), [Input](../libraries/turtle.md#input), and
[Detecting collisions](../libraries/turtle.md#detecting-collisions) sections cover what a single
controlled object needs: read where it is, move it, and tell when it's touching something else.
[Common patterns](../libraries/turtle.md#common-patterns) sketches the shapes these combine into —
worth reading once as a preview of where this expedition ends up.

## random

A game with no randomness plays the same way every time. [random](../libraries/random.md)
supplies the opposite: where the next piece of food appears, which direction a new enemy enters
from, which of several outcomes a hit produces. [Random
numbers](../libraries/random.md#random-numbers) covers a random point or value; [Random
selections](../libraries/random.md#random-selections) covers a random pick from a list of
options already on hand.

## classes

One moving object is easy to track with a couple of variables. More than one — a player and
several enemies, a snake and its food — gets unwieldy fast without a shared shape to hold each
one's state. [Defining a class](../classes.md#defining-a-class) and [Instance
attributes](../classes.md#instance-attributes) give each entity its own position, direction, and
behavior, instead of parallel lists that have to stay in sync by hand.

## Build one

[Common patterns](../libraries/turtle.md#common-patterns) lays out the recurring shapes — a
single controlled object, a growing trail, several independent entities, a bouncing boundary — as
pseudocode to fill in with the pieces above. Pick one and build it out: snake needs the
growing-trail pattern plus `random` for food placement; pong needs the bouncing-boundary pattern
plus a `Paddle` class for the two players; a simple shooter needs several independent entities
plus `random` for when new ones spawn.
