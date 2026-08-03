---
hide:
  - navigation
  - toc
---

# Python Field Guide

??? question "Why should I learn how to code, if AI can do it for me?"
    Now that anyone can instantly generate working code with an AI prompt, it raises a fair question.

    **Learning happens through productive struggle.** The friction of working something out yourself, instead of being handed the answer, is what builds understanding (sometimes called a ["desirable difficulty"](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf)). If you skip that struggle, you won't develop the knowledge to solve the problem again, adapt the answer, or recognize when it's wrong.

    **Programming fundamentals make AI more useful, not less.** Variables, loops, conditionals, functions, etc. are the small, reusable concepts that every program is built from. Once you understand these building blocks, you can read code you didn't write, spot mistakes, understand *why* a solution works, and communicate your problem to AI more effectively.

    **You need to be able to verify what AI writes.** AI can generate code that looks correct while being subtly wrong, insecure, or not actually solving the problem you asked. Researchers are already documenting this skill gap in [students who rely on AI code generation](https://dl.acm.org/doi/10.1145/3617367) before they've [built their own foundation](https://dl.acm.org/doi/10.1145/3624720), and one [Stanford study](https://dl.acm.org/doi/10.1145/3576915.3623157) found that developers using an AI coding assistant wrote *less* secure code than those without AI—while being *more* confident that it was secure. As AI gets better, the ability to evaluate its output becomes even more important.

    **Employers are still hiring for understanding, not prompting.** AI will likely be available on the job too, but technical interviews, code review, and debugging all test whether you can reason about code and judge whether it's correct. AI can help you write code—but it can't replace understanding it.

    Learning to program first turns AI into a tool you can direct and verify, instead of one you're assuming got it right.

??? question "How should I use AI while I'm learning?"
    None of this means avoiding AI altogether—but it does mean being **deliberate** about which parts of the work you hand over.

    **Use AI to remove friction, not the learning.** Environment setup, confusing error messages, unfamiliar terminology, and other roadblocks are great things to ask about because they aren't the skill you're trying to build.

    **Ask AI to explain, not solve.** If an explanation on this site doesn't click, ask follow-up questions. If you're stuck on your own code, ask what a line does or why you got a certain error. Let AI help you *understand* your work, not do it for you.

    **Try first, then ask.** Make a genuine attempt before turning to AI. Once you can explain exactly where you're stuck, AI becomes much more useful—and you still get the benefit of working through the problem yourself.

    **Don't outsource the productive struggle.** Learning to program means making mistakes, getting stuck, and eventually figuring things out. That's the process that builds skills you can rely on long after you've forgotten the syntax.

### Getting started

<div class="grid cards" markdown="block">

-   :material-monitor:{ .lg .middle } [__Workspace__](workspace.md)

    What you need to write and run Python: installing it, picking a code editor, running and debugging, and using the terminal.

    ---

    [`installing Python`](workspace.md#step-0-install-python) · [`code editors`](workspace.md#step-1-pick-a-code-editor) · [`running a file`](workspace.md#step-2-write-and-run-a-python-file) · [`terminal`](workspace.md#using-the-terminal-optional)

-   :material-cube-outline:{ .lg .middle } [__Foundations__](foundations.md)

    Store a value in a variable, show output with `print()`, and leave notes for yourself with comments.

    ---

    [`variables`](foundations.md#variables) · [`print()`](foundations.md#print) · [`comments`](foundations.md#comments)

</div>

### Data types

<div class="grid cards" markdown="block">

-   :material-shape-outline:{ .lg .middle } [__Types__](types.md)

    A single value on its own — a number, some text, or true/false — that every variable holds and that determines what you can do with it.

    ---

    [`int`](types.md#integers) · [`float`](types.md#floats) · [`string`](types.md#strings) · [`bool`](types.md#booleans) · [`None`](types.md#none)

-   :material-format-list-bulleted:{ .lg .middle } [__Collections__](collections.md)

    Multiple related values grouped into one container, so you can work with them together.

    ---

    [`list`](collections.md#lists) · [`tuple`](collections.md#tuples) · [`dict`](collections.md#dictionaries)

</div>

### Control flow

<div class="grid cards" markdown="block">

-   :material-source-branch:{ .lg .middle } [__Conditionals__](conditionals.md)

    Checks whether something is true, then runs different code based on the answer — how Python decides which lines to run instead of top to bottom.

    ---

    [`if`/`elif`/`else`](conditionals.md#if-elif-else) · [`match`/`case`](conditionals.md#match-case) · [`and`/`or`/`not`](conditionals.md#logical-operators)

-   :material-repeat:{ .lg .middle } [__Loops__](loops.md)

    Repeats a block of code a certain number of times, over each item in a collection, or until a condition changes.

    ---

    [`for`](loops.md#for-loops) · [`while`](loops.md#while-loops) · [`break`](loops.md#loop-control)

</div>

### Code organization and reuse

<div class="grid cards" markdown="block">

-   :material-function-variant:{ .lg .middle } [__Functions__](functions.md)

    Packages a block of code under a name, so it can be run again with different inputs instead of rewriting it each time.

    ---

    [`def`](functions.md#defining-a-function) · [`return`](functions.md#return-values) · [`*args`/`**kwargs`](functions.md#flexible-arguments) · [`scope`](functions.md#scope)

-   :material-package-variant:{ .lg .middle } [__Classes__](oop.md)

    Bundles related data and functions into a reusable blueprint, so a program can create many similar objects without duplicating code.

    ---

    [`class`](oop.md#classes-and-objects) · [`super()`](oop.md#inheritance) · [`polymorphism`](oop.md#polymorphism)

</div>

### When something goes wrong

<div class="grid cards" markdown="block">

-   :material-bug-outline:{ .lg .middle } [__Bugs__](bugs.md)

    Understand an error message, handle an error instead of crashing, or debug your code line by line to find where it went wrong.

    ---

    [`tracebacks`](bugs.md#reading-errors) · [`try`/`except`](bugs.md#handling-errors) · [`debugger`](bugs.md#using-a-debugger)

</div>

### Built-in libraries

<div class="grid cards" markdown="block">

-   :material-calendar-clock:{ .lg .middle } [__datetime__](datetime.md)

    Calculating and formatting dates and times.

    ---

    [`date`](datetime.md#creating-dates-and-times) · [`strftime()`](datetime.md#formatting-with-strftime) · [`timedelta`](datetime.md#date-arithmetic) · [`strptime()`](datetime.md#parsing-a-string-with-strptime)

-   :material-dice-multiple:{ .lg .middle } [__random__](random.md)

    Random numbers, random picks, shuffled order.

    ---

    [`randint()`](random.md#random-numbers) · [`choice()`](random.md#random-selections) · [`shuffle()`](random.md#shuffling-a-list) · [`sample()`](random.md#sampling-without-replacement)

-   :material-file-delimited-outline:{ .lg .middle } [__csv__](csv.md)

    Reading and writing spreadsheets.

    ---

    [`csv.writer`](csv.md#writing-csv-files) · [`csv.reader`](csv.md#reading-csv-files) · [`DictReader`](csv.md#reading-rows-as-dictionaries)

-   :material-application-outline:{ .lg .middle } [__Tkinter__](tkinter.md)

    Creating desktop applications: text, buttons, dropdowns, forms, output, etc.

    ---

    [`Tk()`](tkinter.md#creating-a-window) · [`Button`](tkinter.md#widgets) · [`pack()`](tkinter.md#layout-managers) · [`configure()`](tkinter.md#configuring-widgets) · [`command`](tkinter.md#handling-events) · [`ttk.Style`](tkinter.md#styling-with-ttk) · [`messagebox`](tkinter.md#dialogs) · [`winfo_width()`](tkinter.md#introspecting-widgets)

</div>

### Third-party libraries

<div class="grid cards" markdown="block">

-   :material-matrix:{ .lg .middle } [__NumPy__](numpy.md)

    Fast numeric arrays — math applied to a whole array at once, instead of item by item.

    ---

    [`ndarray`](numpy.md#creating-arrays) · [`arange()`](numpy.md#building-arrays-without-a-list) · [`mean()`](numpy.md#aggregating-an-array) · [`boolean mask`](numpy.md#filtering-with-a-boolean-mask)

-   :material-table:{ .lg .middle } [__pandas__](pandas.md)

    Tabular data — rows and columns, like a spreadsheet, built on top of NumPy.

    ---

    [`DataFrame`](pandas.md#building-a-dataframe) · [`sort_values()`](pandas.md#sorting-rows) · [`mean()`](pandas.md#summarizing-a-column)

-   :material-image-outline:{ .lg .middle } [__Pillow__](pillow.md)

    Opening, editing, and saving images, built around one `Image` object.

    ---

    [`Image`](pillow.md#the-image) · [`ImageOps`](pillow.md#imageops-module) · [`ImageDraw`](pillow.md#imagedraw-module) · [`ImageFont`](pillow.md#imagefont-module) · [`ImageColor`](pillow.md#imagecolor-module) · [`ImageFilter`](pillow.md#imagefilter-module) · [`ImageEnhance`](pillow.md#imageenhance-module) · [`ImageChops`](pillow.md#imagechops-module) · [`convert()`](pillow.md#format-conversion) · [`ImageSequence`](pillow.md#imagesequence-module)

-   :material-api:{ .lg .middle } [__requests__](requests.md)

    Fetching data over the internet, like asking a website or API for information.

    ---

    [`get()`](requests.md#making-a-request) · [`status_code`](requests.md#checking-the-status-code) · [`json()`](requests.md#parsing-json) · [`params`](requests.md#query-parameters) · [`error handling`](requests.md#handling-request-errors)

</div>
