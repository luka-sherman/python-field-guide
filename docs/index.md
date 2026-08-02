---
hide:
  - navigation
  - toc
---

# Python Field Guide

*Quick field notes for learning Python, with code you can run in place.*

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Why should I learn how to code, if AI can do it for me?

</summary>

Anyone can instantly generate working code with an AI prompt, which raises a fair question.

**Learning happens through productive struggle.** The friction of working something out yourself—instead of being handed the answer—is what builds understanding, sometimes called a ["desirable difficulty"](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf). Skip that struggle, and you don't develop the knowledge to solve the problem again, apply what you learned to a new situation, or recognize when the answer is wrong.

**These programming fundamentals make AI more useful.** Variables, loops, conditionals, functions, etc. are the small, reusable concepts that every program is built from. Once you can recognize a loop or trace what a conditional does, you can read code you didn't write, spot mistakes an AI tool made, and break larger problems into manageable pieces. Understanding these concepts also helps you communicate with AI more effectively—the better you can describe a problem, the more useful the generated code tends to be.

**You need to be able to read what AI writes.** If you can't read the code an AI generated, you can't tell whether it's correct, secure, or doing what you actually asked. Researchers are already documenting this skill gap in [students who rely on AI code generation](https://dl.acm.org/doi/10.1145/3617367) before they've [built their own foundation](https://dl.acm.org/doi/10.1145/3624720).

**Your job shifts from writing every line to verifying every line.** This matters even more as AI-generated code gets better. An AI can write code that looks confident and correct while being subtly wrong, and the best defense is someone who can trace through it and verify that it does what it's supposed to do. One [Stanford study](https://dl.acm.org/doi/10.1145/3576915.3623157) found that developers using an AI coding assistant wrote *less* secure code than those without AI—while being *more* confident that their code was secure. The skill that matters most going forward may not be writing code from scratch so much as reading and verifying it—and you can't verify what you don't understand at a basic level.

Learning to program first turns AI into a tool you can direct and verify, instead of one you're assuming got it right.

</details>

## Getting started

The building blocks every other page assumes you already know.

<div class="grid cards" markdown="block">

- **[Running Python](running_python.md)**

    Every example here runs in the browser — but on your own computer, you'll run a `.py` file from the terminal or an IDE instead.

    [installing Python](running_python.md#step-0-install-python) · [code editors](running_python.md#step-1-pick-a-code-editor) · [terminal](running_python.md#using-the-terminal-optional)

</div>

## Data types

Programs store information in variables — these are the kinds of values variables can hold.

<div class="grid cards" markdown="block">

- **[Basic Types](basic_types.md)**

    A single value on its own — a number, some text, or true/false. Every value in Python has one of these, and it determines what you can do with it.

    [`int`](basic_types.md#integers) · [`float`](basic_types.md#floats) · [`string`](basic_types.md#strings) · [`bool`](basic_types.md#booleans) · [`None`](basic_types.md#none)

- **[Collections](collections.md)**

    Multiple basic values that are related and grouped into one container, so you can work with them together.

    [`list`](collections.md#lists) · [`tuple`](collections.md#tuples) · [`dict`](collections.md#dictionaries)

</div>

## Control flow

This is how Python decides which lines of code to execute and when, instead of just running each line top to bottom.

<div class="grid cards" markdown="block">

- **[Conditionals](conditionals.md)**

    Checks whether something is true, then runs different code depending on the answer.

    [`if`/`elif`/`else`](conditionals.md#if-elif-else) · [`match`/`case`](conditionals.md#match-case) · [`and`/`or`/`not`](conditionals.md#logical-operators)

- **[Loops](loops.md)**

    Repeats a block of code a certain number of times, over each item in a collection, or until a condition changes.

    [`for`](loops.md#for-loops) · [`while`](loops.md#while-loops) · [`break`](loops.md#loop-control)

</div>

## Code organization and reuse

Package code into reusable units, then bundle that logic with the data it acts on.

<div class="grid cards" markdown="block">

- **[Functions](functions.md)**

    Packages a block of code under a name, so it can be run again with different inputs instead of rewriting it each time.

    [`def`](functions.md#defining-a-function) · [`return`](functions.md#return-values) · [`*args`/`**kwargs`](functions.md#flexible-arguments) · [scope](functions.md#scope)

- **[Classes](oop.md)**

    Bundles related data and functions into a reusable blueprint, so a program can create many similar objects without duplicating code.

    [`class`](oop.md#classes-and-objects) · [`super()`](oop.md#inheritance)

</div>

## Standard libraries

Python is already preloaded with these, and puts the above fundamentals to use on real tasks.

<div class="grid cards" markdown="block">

- **[datetime](datetime.md)**

    Python's built-in toolkit for formatting and calculating dates and times.

    [`date`](datetime.md#creating-dates-and-times) · [`strftime()`](datetime.md#formatting-with-strftime) · [`timedelta`](datetime.md#date-arithmetic) · [`strptime()`](datetime.md#parsing-a-string-with-strptime)

- **[random](random.md)**

    Python's built-in toolkit for randomness — random numbers, random picks, shuffled order.

    [`randint()`](random.md#random-numbers) · [`choice()`](random.md#random-selections) · [`shuffle()`](random.md#shuffling-a-list) · [`sample()`](random.md#sampling-without-replacement)

- **[csv](csv.md)**

    Python's built-in toolkit for reading and writing spreadsheets.

    [`csv.writer`](csv.md#writing-csv-files) · [`csv.reader`](csv.md#reading-csv-files) · [`DictReader`](csv.md#reading-rows-as-dictionaries)

- **[Tkinter](tkinter.md)**

    Python's built-in toolkit for creating desktop applications: text, buttons, dropdowns, forms, output, etc.

    [`Tk()`](tkinter.md#creating-a-window) · [`Button`](tkinter.md#widgets) · [`pack()`](tkinter.md#layout-managers) · [`configure()`](tkinter.md#configuring-widgets) · [`command`](tkinter.md#handling-events) · [`ttk.Style`](tkinter.md#styling-with-ttk) · [`messagebox`](tkinter.md#dialogs) · [`winfo_width()`](tkinter.md#introspecting-widgets)

</div>

## Third-party libraries

These additional Python libraries can be installed on your computer for free.

<div class="grid cards" markdown="block">

- **[NumPy](numpy.md)**

    A third-party toolkit for fast numeric arrays — math applied to a whole array at once, instead of item by item.

    [`ndarray`](numpy.md#creating-arrays) · [`arange()`](numpy.md#building-arrays-without-a-list) · [`mean()`](numpy.md#aggregating-an-array) · [`boolean mask`](numpy.md#filtering-with-a-boolean-mask)

- **[pandas](pandas.md)**

    A third-party toolkit for tabular data — rows and columns, like a spreadsheet, built on top of NumPy.

    [`DataFrame`](pandas.md#building-a-dataframe) · [`sort_values()`](pandas.md#sorting-rows) · [`mean()`](pandas.md#summarizing-a-column)

- **[Pillow](pillow.md)**

    A third-party toolkit for opening, editing, and saving images, built around one `Image` object — useful anytime a program needs to touch actual image files.

    [`Image`](pillow.md#the-image) · [`ImageOps`](pillow.md#imageops-module) · [`ImageDraw`](pillow.md#imagedraw-module) · [`ImageFont`](pillow.md#imagefont-module) · [`ImageColor`](pillow.md#imagecolor-module) · [`ImageFilter`](pillow.md#imagefilter-module) · [`ImageEnhance`](pillow.md#imageenhance-module) · [`ImageChops`](pillow.md#imagechops-module) · [`convert()`](pillow.md#format-conversion) · [`ImageSequence`](pillow.md#imagesequence-module)

</div>

# Try it now

The specimen below is alive: edit it, run it, see what it does.

```python
# Field Journal — Entry #1
date = "2026-07-23"
species = "ball python"
length_ft = 4.5
venomous = False

print(f"Date: {date}")
print(f"Species: {species}")
print(f"Length: {length_ft} ft")
print(f"Venomous: {venomous}")
print("Notes: found coiled beneath a rock, unbothered by observation.")
```
