---
hide:
  - navigation
  - toc
---

# Python Field Guide { .pt-visually-hidden }

<div class="pt-category-grid" markdown="block">

<div class="pt-category" markdown="block">
#### Get started { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-monitor:{ .lg .middle } [__Workspace Setup__](workspace.md)

    What you need to write and run Python on your own computer.

    [**`installing Python`**](workspace.md#step-0-install-python) · [**`running a file`**](workspace.md#step-2-write-and-run-a-python-file) · [**`.py`**](workspace.md#step-2-write-and-run-a-python-file) · [**`code editors`**](workspace.md#step-1-pick-an-application-to-write-code-in) · [**`using the terminal`**](workspace.md#using-the-terminal-optional)

-   :material-cube-outline:{ .lg .middle } [__Foundations__](foundations.md)

    The basic building blocks every Python program starts with: storing, displaying, and reading in values.

    [**`variables`**](foundations.md#variables) · [**`print()`**](foundations.md#print-function) · [**`input()`**](foundations.md#input-function) · [**`comments`**](foundations.md#comments) · [**`tips for getting started`**](foundations.md#tips-for-getting-started)

</div>
</div>

<div class="pt-category" markdown="block">
#### Data types { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-shape-outline:{ .lg .middle } [__Basics__](types.md)

    The kind of value something is, like a number, text, or true/false.

    [**`int`**](types.md#integers) · [**`float`**](types.md#floats) · [**`string`**](types.md#strings) · [**`bool`**](types.md#booleans) · [**`None`**](types.md#none)

    [`truthy/falsy`](types.md#boolean-expressions) · [`//, %, divmod()`](types.md#floor-division-modulo) · [`abs()`](types.md#absolute-value) · [`round()`](types.md#adjust) · [`indexing, slicing`](types.md#access-characters) · [`f-string`](types.md#f-strings) · [`.lower() .upper() .strip() .replace()`](types.md#modify) · [`.find() .count()`](types.md#search) · [`.startswith() .endswith() .isdigit() .isalpha()`](types.md#validate) · [`.split()`](types.md#convert_2) · [`is, in`](types.md#creating-a-boolean) · [`and, or, not`](types.md#logical-operators) · [`type() isinstance()`](types.md)

-   :material-basket-outline:{ .lg .middle } [__Collections__](collections.md)

    Multiple related values grouped into one container, so you can work with them together.

    [**`list`**](collections.md#lists) · [**`tuple`**](collections.md#tuples) · [**`dict`**](collections.md#dictionaries) · [**`set`**](collections.md#sets)

    [`.append()`](collections.md#list-operations) · [`len()`](collections.md#list-operations) · [`in`](collections.md#list-operations) · [`min() max() sum()`](collections.md#list-operations) · [`.pop()`](collections.md#list-operations) · [`.sort()`](collections.md#list-operations) · [`.get()`](collections.md#dictionary-operations) · [`.keys() .values() .items()`](collections.md#dictionary-operations) · [`packing, unpacking`](collections.md#packing-and-unpacking)

</div>
</div>

<div class="pt-category" markdown="block">
#### Control flow { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-source-branch:{ .lg .middle } [__Conditionals__](conditionals.md)

    Lets a program make decisions, running different code depending on whether something is true.

    [**`if, elif, else`**](conditionals.md#if-elif-else) · [**`match, case`**](conditionals.md#match-case) · [**`break, continue`**](conditionals.md#control-flow-statements)

    [`boolean expressions`](conditionals.md#boolean-expressions) · [`and, or, not`](conditionals.md#logical-operators) · [`unpacking`](conditionals.md#unpacking-a-tuple) · [`_ (wildcard)`](conditionals.md#default-value-_)

-   :material-repeat:{ .lg .middle } [__Loops__](loops.md)

    Repeats a block of code without writing it out multiple times.

    [**`for`**](loops.md#for-loops) · [**`while`**](loops.md#while-loops) · [**`break, continue`**](loops.md#control-flow-statements) · [**`common patterns`**](loops.md#common-patterns)

    [`loop through a collection`](loops.md#loop-through-a-collection) · [`accumulator`](loops.md#accumulator) · [`counter`](loops.md#counter) · [`nested loops`](loops.md#nested-loops) · [`range()`](loops.md#iterable-range) · [`enumerate()`](loops.md#loop-with-index-and-value) · [`reversed()`](loops.md#loop-in-reverse) · [`zip()`](loops.md#loop-with-index-and-value)

</div>
</div>

<div class="pt-category" markdown="block">
#### Code organization { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-function-variant:{ .lg .middle } [__Functions__](functions.md)

    Packages a block of code under a name, so it can be run again with different inputs instead of rewriting it each time.

    [**`def`**](functions.md#defining-a-function) · [**`*args, **kwargs`**](functions.md#flexible-arguments) · [**`scope`**](functions.md#scope) · [**`recursion`**](functions.md#recursion)

    [`return`](functions.md#return-values) · [`default parameter values`](functions.md#default-parameter-values) · [`keyword arguments`](functions.md#keyword-arguments) · [`docstrings`](functions.md#docstrings) · [`local vs global`](functions.md#local-vs-global-variables)

-   :material-package-variant:{ .lg .middle } [__Classes__](oop.md)

    Bundles related data and functions into a reusable blueprint, so a program can create many similar objects without duplicating code.

    [**`class`**](oop.md#classes-and-objects) · [**`inheritance`**](oop.md#inheritance) · [**`polymorphism`**](oop.md#polymorphism)

    [`__init__()`](oop.md#the-__init__-method) · [`self`](oop.md#the-self-parameter) · [`super()`](oop.md#using-super)

</div>
</div>

<div class="pt-category" markdown="block">
#### External files and resources { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-import:{ .lg .middle } [__Modules & Imports__](modules.md)

    Splitting code across files, and pulling in code someone else already wrote.

    [**`import`**](modules.md#importing-modules) · [**`your own module`**](modules.md#creating-your-own-module) · [**`module, package, library`**](modules.md#modules-vs-packages-vs-libraries)

    [`from`](modules.md#from) · [`as`](modules.md#as) · [`main`](modules.md#the-main-guard) · [`import order`](modules.md#order-of-multiple-imports) · [`packages`](modules.md#packages) · [`nested paths`](modules.md#nested-paths)

-   :material-file-document-outline:{ .lg .middle } [__Reading & Writing Files__](files.md)

    Saves data outside the program itself, so it's still there the next time it runs.

    [**`open()`**](files.md#opening-a-file) · [**`read()`**](files.md#reading-a-file) · [**`write()`**](files.md#writing-multiple-lines) · [**`append`**](files.md#appending-vs-overwriting)

</div>
</div>

<div class="pt-category" markdown="block">
#### Robust programming practices { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-palette-outline:{ .lg .middle } [__Style__](style.md)

    Conventions for writing Python that stays readable as a file grows.

    [**`PEP 8`**](style.md#pep-8-style-guide) · [**`pythonic patterns`**](style.md#pythonic-patterns) · [**`best practices`**](style.md#additional-best-practices) · [**`linter`**](style.md#linter-tool) · [**`checklist`**](style.md#checklist)

    [`naming`](style.md#naming) · [`docstrings`](style.md#docstrings) · [`type hints`](style.md#type-hints) · [`order`](style.md#file-order) · [`constants`](style.md#constants) · [`catch specific exceptions`](style.md#catch-specific-exceptions)

-   :material-bug-outline:{ .lg .middle } [__Errors__](errors.md)

    How to read error messages, handle them gracefully, and track down what went wrong.

    [**`try, except`**](errors.md#handling-errors) · [**`tracebacks`**](errors.md#reading-errors) · [**`debugger`**](errors.md#using-a-debugger) · [**`debugging strategies`**](errors.md#debugging-strategies)

    [`exception types`](errors.md#common-exception-types) · [`rubber duck debugging`](errors.md#read-it-out-loud) · [`print debugging`](errors.md#print-debugging)

</div>
</div>

<div class="pt-category pt-category--wide" markdown="block">
#### Add-on Libraries { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-file-delimited-outline:{ .lg .middle } [__csv__](libraries/csv.md) [:material-language-python:](libraries/csv.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Reading and writing spreadsheets.

    [**`install`**](libraries/csv.md#install) · [**`import`**](libraries/csv.md#import)

    [`csv.writer`](libraries/csv.md#writing-csv-files) · [`csv.reader`](libraries/csv.md#reading-csv-files) · [`DictReader`](libraries/csv.md#reading-rows-as-dictionaries)

-   :material-calendar-clock:{ .lg .middle } [__datetime__](libraries/datetime.md) [:material-language-python:](libraries/datetime.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Calculating and formatting dates and times.

    [**`install`**](libraries/datetime.md#install) · [**`import`**](libraries/datetime.md#import)

    [`date`](libraries/datetime.md#creating-dates-and-times) · [`timedelta`](libraries/datetime.md#date-arithmetic) · [`strftime()`](libraries/datetime.md#formatting-with-strftime) · [`strptime()`](libraries/datetime.md#parsing-a-string-with-strptime)

-   :material-code-json:{ .lg .middle } [__json__](libraries/json.md) [:material-language-python:](libraries/json.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Reading and writing JSON data: nested dicts and lists, saved to a file or a string.

    [**`install`**](libraries/json.md#install) · [**`import`**](libraries/json.md#import)

    [`json.dump()`](libraries/json.md#writing-json-files) · [`json.load()`](libraries/json.md#reading-json-files) · [`json.dumps()`](libraries/json.md#working-with-strings-instead-of-files) · [`json.loads()`](libraries/json.md#working-with-strings-instead-of-files)

-   :material-matrix:{ .lg .middle } [__NumPy__](libraries/numpy.md) [:material-download-outline:](libraries/numpy.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Fast numeric arrays, with math applied to a whole array at once instead of item by item.

    [**`install`**](libraries/numpy.md#install) · [**`import`**](libraries/numpy.md#import) · [**`array operations`**](libraries/numpy.md#array-operations)

    [`ndarray`](libraries/numpy.md#creating-arrays) · [`arange()`](libraries/numpy.md#building-arrays-without-a-list) · [`mean()`](libraries/numpy.md#aggregating-an-array) · [`boolean mask`](libraries/numpy.md#filtering-with-a-boolean-mask)

-   :material-face-recognition:{ .lg .middle } [__OpenCV__](libraries/opencv.md) [:material-download-outline:](libraries/opencv.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Real-time image and video analysis, built directly on NumPy arrays: color spaces, edge detection, face detection.

    [**`install`**](libraries/opencv.md#install) · [**`import`**](libraries/opencv.md#import) · [**`reading, displaying, saving images`**](libraries/opencv.md#reading-displaying-and-saving-images) · [**`drawing`**](libraries/opencv.md#drawing-shapes-and-text) · [**`color spaces`**](libraries/opencv.md#color-spaces) · [**`CascadeClassifier`**](libraries/opencv.md#face-detection-with-cascade-classifiers) · [**`VideoCapture()`**](libraries/opencv.md#working-with-video) · [**`basic operations`**](libraries/opencv.md#basic-operations) · [**`thresholding, edge detection`**](libraries/opencv.md#thresholding-and-edge-detection) · [**`blurring`**](libraries/opencv.md#blurring) · [**`contours`**](libraries/opencv.md#contours)

    [`imread()`](libraries/opencv.md#reading-a-file) · [`cvtColor()`](libraries/opencv.md#converting-color-spaces) · [`Canny()`](libraries/opencv.md#edge-detection) · [`resize()`](libraries/opencv.md#resize)

-   :material-table:{ .lg .middle } [__pandas__](libraries/pandas.md) [:material-download-outline:](libraries/pandas.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Tabular data: rows and columns, like a spreadsheet, built on top of NumPy.

    [**`install`**](libraries/pandas.md#install) · [**`import`**](libraries/pandas.md#import) · [**`DataFrame`**](libraries/pandas.md#building-a-dataframe) · [**`working with a DataFrame`**](libraries/pandas.md#working-with-a-dataframe)

    [`sort_values()`](libraries/pandas.md#sorting-rows) · [`mean()`](libraries/pandas.md#summarizing-a-column)

-   :material-image-outline:{ .lg .middle } [__Pillow__](libraries/pillow.md) [:material-download-outline:](libraries/pillow.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Opening, editing, and saving images, built around one `Image` object.

    [**`install`**](libraries/pillow.md#install) · [**`import`**](libraries/pillow.md#import) · [**`why Pillow?`**](libraries/pillow.md#why-pillow) · [**`Image`**](libraries/pillow.md#the-image) · [**`ImageOps`**](libraries/pillow.md#imageops-module) · [**`ImageDraw`**](libraries/pillow.md#imagedraw-module) · [**`ImageFont`**](libraries/pillow.md#imagefont-module) · [**`ImageColor`**](libraries/pillow.md#imagecolor-module) · [**`ImageFilter`**](libraries/pillow.md#imagefilter-module) · [**`ImageEnhance`**](libraries/pillow.md#imageenhance-module) · [**`ImageChops`**](libraries/pillow.md#imagechops-module) · [**`convert()`**](libraries/pillow.md#format-conversion) · [**`ImageSequence`**](libraries/pillow.md#imagesequence-module) · [**`putting it together`**](libraries/pillow.md#putting-it-together)

-   :material-dice-multiple:{ .lg .middle } [__random__](libraries/random.md) [:material-language-python:](libraries/random.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Random numbers, random picks, shuffled order.

    [**`install`**](libraries/random.md#install) · [**`import`**](libraries/random.md#import) · [**`randint()`**](libraries/random.md#random-numbers) · [**`choice()`**](libraries/random.md#random-selections)

    [`shuffle()`](libraries/random.md#shuffling-a-list) · [`sample()`](libraries/random.md#sampling-without-replacement)


-   :material-api:{ .lg .middle } [__requests__](libraries/requests.md) [:material-download-outline:](libraries/requests.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Fetching data over the internet, like asking a website or API for information.

    [**`install`**](libraries/requests.md#install) · [**`import`**](libraries/requests.md#import) · [**`get()`**](libraries/requests.md#making-a-request) · [**`error handling`**](libraries/requests.md#handling-request-errors)

    [`status_code`](libraries/requests.md#checking-the-status-code) · [`json()`](libraries/requests.md#parsing-json) · [`params`](libraries/requests.md#query-parameters)

-   :material-application-outline:{ .lg .middle } [__Tkinter__](libraries/tkinter.md) [:material-language-python:](libraries/tkinter.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Creating desktop applications: text, buttons, dropdowns, forms, output, etc.

    [**`install`**](libraries/tkinter.md#install) · [**`import`**](libraries/tkinter.md#import) · [**`Tk()`**](libraries/tkinter.md#creating-a-window) · [**`Button`**](libraries/tkinter.md#widgets) · [**`pack()`**](libraries/tkinter.md#layout-managers) · [**`configure()`**](libraries/tkinter.md#configuring-widgets) · [**`command`**](libraries/tkinter.md#handling-events) · [**`ttk.Style`**](libraries/tkinter.md#styling-with-ttk) · [**`messagebox`**](libraries/tkinter.md#dialogs) · [**`winfo_width()`**](libraries/tkinter.md#introspecting-widgets) · [**`putting it together`**](libraries/tkinter.md#putting-it-together)

</div>
</div>

</div>

### FAQ

=== ":material-creation: Why learn to code yourself, if AI can do it for you?"

    **Understanding programming fundamentals make AI more useful.** 
    
    Once you understand these building blocks you can read code you didn't write, spot mistakes, understand *why* a solution works, and communicate your problem to AI more effectively.

    **Learning happens through productive struggle.** 
    
    The friction of working something out yourself, instead of being handed the answer, [is what builds understanding](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf). If you skip that struggle, you *won't develop the knowledge* to solve the problem again, adapt the answer, or recognize when it's wrong.

    **You need to be able to verify AI code.** 
    
    AI can generate code that looks correct while being wrong and insecure. Researchers are already documenting this skill gap in [students who rely on AI code generation](https://dl.acm.org/doi/10.1145/3617367) before they've [built their own foundation](https://dl.acm.org/doi/10.1145/3624720), and one [Stanford study](https://dl.acm.org/doi/10.1145/3576915.3623157) found that developers using AI wrote *less* secure code—but were *more* confident that it was secure. 

    **Employers are still hiring for understanding, not prompting.** 
    
    AI will likely be available on the job too, but code review, debugging, and interviews all test whether you can reason about code and judge whether it's correct.

    **Learning to program on your own turns AI into a tool you can direct and verify, instead of one you're assuming got it right.**

=== ":material-creation: Using AI to learn"

    **Guide you through setting up your workspace** 
    
    Setting up your computer for programming can be an intimidating hurdle, especially if you haven't used your Terminal before. Having AI walk you through the setup process can make this task **safer and accessible for solo beginners**. 

    **Ask AI to explain, not solve.** 
    
    If you're stuck on your own code, ask what a line does or *why* you got a certain error. Let AI help you *understand* concepts, not write them for you.

    **Have it write you a practice problem, not just solve one.** 
    
    Tell it your experience level, what topic you want to practice, and what you're specifically trying to get better at, and ask it to write *you* a small problem to solve — not the solution. That's the same kind of exercise a textbook or course would give you, just generated on demand and matched to exactly what you need next.

    **If you're stuck, clearly communicate your problem.** 
    
    Make a strong attempt before turning to AI. Then **describe** what you've tried, what you expected to happen, and exactly where you're stuck *instead of just dumping in your code and an error message*. The process of **putting your problem into words** is a significant learning tool, and will also gives AI the context it needs to provide more targeted, efficient help.

    **Disable AI autocomplete.** 
    
    Many code editors now have an AI autocomplete enabled, which reads your code as you write and suggests ways to finish it and whole functions to add. This is not helpful for a beginner and can you leave you **not understanding what your own code does**.

    **Don't outsource the productive struggle.** 
    
    Learning to program means making mistakes, getting stuck, and eventually figuring things out and forming a mental model. That's the process that **builds skills** you can rely on.

=== ":material-information-outline: What is Python?"

    **Python** is a general-purpose programming language known for readable syntax and a huge built-in and third-party library ecosystem — designed to be quick to write and easy to read back later, even by someone who didn't write it. It doesn't need to be compiled before it runs: write a `.py` file, then run it directly.

    That readability, plus the sheer range of libraries already built for it, is why it turns up almost everywhere: web backends, data analysis and machine learning, automating repetitive tasks, scientific computing, and quick scripts gluing other tools together — several of which are covered on this site's [Libraries](#add-on-libraries) pages. Python usually isn't the fastest language for raw performance, but it's often the fastest to write *correct* code in, which is why it's such a common first choice for a new project.

    That same readability is also why Python is such a common **first language to learn programming in**. Variables, conditionals, loops, functions, classes — the same fundamentals every language shares — read closer to plain English here than in most other languages, so you spend your effort learning to *think* like a programmer instead of fighting a stricter syntax. Once those fundamentals are solid, they carry over directly to whatever language you pick up next.

=== ":material-information-outline: What is this guide?"

    **Python Field Guide** is a free, in-browser reference for learning Python from the ground up — most code blocks are editable and runnable directly on the page, if you want to experiment with how something works.

    It's built for people learning Python — self-taught learners, students in an intro course, or anyone who wants one combined reference to work through from start to finish rather than a scattered pile of search results. 
