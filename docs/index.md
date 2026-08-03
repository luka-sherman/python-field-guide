---
hide:
  - navigation
  - toc
---

# Python Field Guide { .pt-visually-hidden }

??? ai "Using AI to learn to code"
    === "Why should I learn how to code, if AI can do it for me?"

        Now that anyone can instantly generate working code with an AI prompt, it raises a fair question.

        **Learning happens through productive struggle.** 
        
        The friction of working something out yourself, instead of being handed the answer, is what builds understanding (sometimes called a ["desirable difficulty"](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf)). If you skip that struggle, you won't develop the knowledge to solve the problem again, adapt the answer, or recognize when it's wrong.

        **Programming fundamentals make AI more useful, not less.** 
        
        Variables, loops, conditionals, functions, etc. are the small, reusable concepts that every program is built from. Once you understand these building blocks, you can read code you didn't write, spot mistakes, understand *why* a solution works, and communicate your problem to AI more effectively.

        **You need to be able to verify what AI writes.** 
        
        AI can generate code that looks correct while being subtly wrong, insecure, or not actually solving the problem you asked. Researchers are already documenting this skill gap in [students who rely on AI code generation](https://dl.acm.org/doi/10.1145/3617367) before they've [built their own foundation](https://dl.acm.org/doi/10.1145/3624720), and one [Stanford study](https://dl.acm.org/doi/10.1145/3576915.3623157) found that developers using an AI coding assistant wrote *less* secure code than those without AI—while being *more* confident that it was secure. As AI gets better, the ability to evaluate its output becomes even more important.

        **Employers are still hiring for understanding, not prompting.** 
        
        AI will likely be available on the job too, but technical interviews, code review, and debugging all test whether you can reason about code and judge whether it's correct. AI can help you write code—but it can't replace understanding it.

        Learning to program first turns AI into a tool you can direct and verify, instead of one you're assuming got it right.

    === "How should I use AI while I'm learning?"

        None of this means avoiding AI altogether—but it does mean being **deliberate** about which parts of the work you hand over.

        **Use AI to remove friction, not the learning.** 
        
        Environment setup, confusing error messages, unfamiliar terminology, and other roadblocks are great things to ask about because they aren't the skill you're trying to build.

        **Ask AI to explain, not solve.** 
        
        If an explanation on this site doesn't click, ask follow-up questions. If you're stuck on your own code, ask what a line does or why you got a certain error. Let AI help you *understand* your work, not do it for you.

        **Try first, then ask.** 
        
        Make a genuine attempt before turning to AI. Once you can explain exactly where you're stuck, AI becomes much more useful—and you still get the benefit of working through the problem yourself.

        **Disable AI autocomplete.** 
        
        Many code editors now have an AI autocomplete enabled by default, which reads your code as you write and suggests ways to finish it and whole functions to add. This is not helpful for a beginner and can you leave you not understanding how your code works.

        **Don't outsource the productive struggle.** 
        
        Learning to program means making mistakes, getting stuck, and eventually figuring things out. That's the process that builds skills you can rely on long after you've forgotten the syntax.


<div class="grid cards" markdown="block">

-   :material-monitor:{ .lg .middle } [__Workspace Setup__](workspace.md)

    What you need to write and run Python: installing it, picking a code editor, running and debugging, and using the terminal.

    ---

    [`installing Python`](workspace.md#step-0-install-python) · [`code editors`](workspace.md#step-1-pick-a-code-editor) · [`running a file`](workspace.md#step-2-write-and-run-a-python-file) · [`terminal`](workspace.md#using-the-terminal-optional)

-   :material-cube-outline:{ .lg .middle } [__Foundations__](foundations.md)

    Store a value in a variable, show output with `print()`, and leave notes for yourself with comments.

    ---

    [`variables`](foundations.md#variables) · [`print()`](foundations.md#print) · [`comments`](foundations.md#comments)

-   :material-shape-outline:{ .lg .middle } [__Basic Data Types__](types.md)

    A single value on its own — a number, some text, or true/false — that every variable holds and that determines what you can do with it.

    ---

    [`int`](types.md#integers) · [`float`](types.md#floats) · [`string`](types.md#strings) · [`bool`](types.md#booleans) · [`None`](types.md#none)

-   :material-format-list-bulleted:{ .lg .middle } [__Collection Data Types__](collections.md)

    Multiple related values grouped into one container, so you can work with them together.

    ---

    [`list`](collections.md#lists) · [`tuple`](collections.md#tuples) · [`dict`](collections.md#dictionaries)


-   :material-source-branch:{ .lg .middle } [__Conditionals__](conditionals.md)

    Checks whether something is true, then runs different code based on the answer — how Python decides which lines to run instead of top to bottom.

    ---

    [`if`/`elif`/`else`](conditionals.md#if-elif-else) · [`match`/`case`](conditionals.md#match-case) · [`and`/`or`/`not`](conditionals.md#logical-operators)

-   :material-repeat:{ .lg .middle } [__Loops__](loops.md)

    Repeats a block of code a certain number of times, over each item in a collection, or until a condition changes.

    ---

    [`for`](loops.md#for-loops) · [`while`](loops.md#while-loops) · [`break`](loops.md#loop-control)


-   :material-function-variant:{ .lg .middle } [__Functions__](functions.md)

    Packages a block of code under a name, so it can be run again with different inputs instead of rewriting it each time.

    ---

    [`def`](functions.md#defining-a-function) · [`return`](functions.md#return-values) · [`*args`/`**kwargs`](functions.md#flexible-arguments) · [`scope`](functions.md#scope)

-   :material-package-variant:{ .lg .middle } [__Classes__](oop.md)

    Bundles related data and functions into a reusable blueprint, so a program can create many similar objects without duplicating code.

    ---

    [`class`](oop.md#classes-and-objects) · [`super()`](oop.md#inheritance) · [`polymorphism`](oop.md#polymorphism)

-   :material-bug-outline:{ .lg .middle } [__Bugs__](bugs.md)

    Understand an error message, handle an error instead of crashing, or debug your code line by line to find where it went wrong.

    ---

    [`tracebacks`](bugs.md#reading-errors) · [`try`/`except`](bugs.md#handling-errors) · [`debugger`](bugs.md#using-a-debugger)

</div>

### Libraries

<div class="grid cards" markdown="block">

-   :material-file-delimited-outline:{ .lg .middle } [__csv__](libraries/csv.md)

    Reading and writing spreadsheets.

    ---

    [`csv.writer`](libraries/csv.md#writing-csv-files) · [`csv.reader`](libraries/csv.md#reading-csv-files) · [`DictReader`](libraries/csv.md#reading-rows-as-dictionaries)

-   :material-calendar-clock:{ .lg .middle } [__datetime__](libraries/datetime.md)

    Calculating and formatting dates and times.

    ---

    [`date`](libraries/datetime.md#creating-dates-and-times) · [`strftime()`](libraries/datetime.md#formatting-with-strftime) · [`timedelta`](libraries/datetime.md#date-arithmetic) · [`strptime()`](libraries/datetime.md#parsing-a-string-with-strptime)

-   :material-matrix:{ .lg .middle } [__NumPy__](libraries/numpy.md)

    Fast numeric arrays — math applied to a whole array at once, instead of item by item.

    ---

    [`ndarray`](libraries/numpy.md#creating-arrays) · [`arange()`](libraries/numpy.md#building-arrays-without-a-list) · [`mean()`](libraries/numpy.md#aggregating-an-array) · [`boolean mask`](libraries/numpy.md#filtering-with-a-boolean-mask)

-   :material-face-recognition:{ .lg .middle } [__OpenCV__](libraries/opencv.md)

    Real-time image and video analysis — color spaces, edge detection, face detection, built directly on NumPy arrays.

    ---

    [`imread()`](libraries/opencv.md#reading-a-file) · [`cvtColor()`](libraries/opencv.md#converting-color-spaces) · [`drawing`](libraries/opencv.md#drawing-shapes-and-text) · [`Canny()`](libraries/opencv.md#edge-detection) · [`CascadeClassifier`](libraries/opencv.md#face-detection-with-cascade-classifiers) · [`VideoCapture()`](libraries/opencv.md#working-with-video)

-   :material-table:{ .lg .middle } [__pandas__](libraries/pandas.md)

    Tabular data — rows and columns, like a spreadsheet, built on top of NumPy.

    ---

    [`DataFrame`](libraries/pandas.md#building-a-dataframe) · [`sort_values()`](libraries/pandas.md#sorting-rows) · [`mean()`](libraries/pandas.md#summarizing-a-column)

-   :material-image-outline:{ .lg .middle } [__Pillow__](libraries/pillow.md)

    Opening, editing, and saving images, built around one `Image` object.

    ---

    [`Image`](libraries/pillow.md#the-image) · [`ImageOps`](libraries/pillow.md#imageops-module) · [`ImageDraw`](libraries/pillow.md#imagedraw-module) · [`ImageFont`](libraries/pillow.md#imagefont-module) · [`ImageColor`](libraries/pillow.md#imagecolor-module) · [`ImageFilter`](libraries/pillow.md#imagefilter-module) · [`ImageEnhance`](libraries/pillow.md#imageenhance-module) · [`ImageChops`](libraries/pillow.md#imagechops-module) · [`convert()`](libraries/pillow.md#format-conversion) · [`ImageSequence`](libraries/pillow.md#imagesequence-module)

-   :material-dice-multiple:{ .lg .middle } [__random__](libraries/random.md)

    Random numbers, random picks, shuffled order.

    ---

    [`randint()`](libraries/random.md#random-numbers) · [`choice()`](libraries/random.md#random-selections) · [`shuffle()`](libraries/random.md#shuffling-a-list) · [`sample()`](libraries/random.md#sampling-without-replacement)


-   :material-api:{ .lg .middle } [__requests__](libraries/requests.md)

    Fetching data over the internet, like asking a website or API for information.

    ---

    [`get()`](libraries/requests.md#making-a-request) · [`status_code`](libraries/requests.md#checking-the-status-code) · [`json()`](libraries/requests.md#parsing-json) · [`params`](libraries/requests.md#query-parameters) · [`error handling`](libraries/requests.md#handling-request-errors)

-   :material-application-outline:{ .lg .middle } [__Tkinter__](libraries/tkinter.md)

    Creating desktop applications: text, buttons, dropdowns, forms, output, etc.

    ---

    [`Tk()`](libraries/tkinter.md#creating-a-window) · [`Button`](libraries/tkinter.md#widgets) · [`pack()`](libraries/tkinter.md#layout-managers) · [`configure()`](libraries/tkinter.md#configuring-widgets) · [`command`](libraries/tkinter.md#handling-events) · [`ttk.Style`](libraries/tkinter.md#styling-with-ttk) · [`messagebox`](libraries/tkinter.md#dialogs) · [`winfo_width()`](libraries/tkinter.md#introspecting-widgets)

</div>
