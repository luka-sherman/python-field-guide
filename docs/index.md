---
description: >-
  A free Python reference with runnable code examples covering data types, collections,
  loops, functions, classes, error handling, and popular libraries.
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

    Write Python on your computer.

    [**`install`**](workspace.md#step-0-install-python): 
    [`download`](workspace.md#step-0-install-python) 
    [`version`](workspace.md#step-0-install-python) 

    [**`code editors`**](workspace.md#step-1-pick-an-application-to-write-code-in): 
    [`IDLE`](workspace.md#step-1-pick-an-application-to-write-code-in) 
    [`Pycharm`](workspace.md#step-1-pick-an-application-to-write-code-in) 
    [`Thonny`](workspace.md#step-1-pick-an-application-to-write-code-in) 
    [`VS Code`](workspace.md#step-1-pick-an-application-to-write-code-in) 

    [**`how to write and run .py file`**](workspace.md#step-2-write-and-run-a-python-file): 
    [`file naming`](workspace.md#step-2-write-and-run-a-python-file) 

    [**`Terminal`**](workspace.md#using-the-terminal-optional): 
    [`cd`](workspace.md#using-the-terminal-optional) 
    [`ls`](workspace.md#using-the-terminal-optional) 
    [`pwd`](workspace.md#using-the-terminal-optional) 
    [`shortcuts`](workspace.md#using-the-terminal-optional) 

    [**`virtual environments`**](workspace.md#virtual-environments-optional): 
    [`activate`](workspace.md#virtual-environments-optional) 
    [`pip`](workspace.md#virtual-environments-optional) 
    [`requirements.txt`](workspace.md#virtual-environments-optional) 
    [`venv`](workspace.md#virtual-environments-optional) 

-   :material-cube-outline:{ .lg .middle } [__Foundations__](foundations.md)

    Storing, displaying, and inputting values.

    [**`variables`**](foundations.md#variables): 
    [`naming`](foundations.md#naming-variables) 
    [`printing`](foundations.md#printing-variables) 
    [`reassigning`](foundations.md#reassigning-a-variable) 
    [`types`](foundations.md#variables-and-types) 

    [**`print`**](foundations.md#print-function): 
    [`escape sequences`](foundations.md#escape-sequences) 

    [**`input`**](foundations.md#input-function)

    [**`comments`**](foundations.md#comments): 
    [`"""`](foundations.md#multi-line-comments-with) 
    [`#`](foundations.md#single-line-comments-with) 
    [`FIXME`](foundations.md#single-line-comments-with) 
    [`TODO`](foundations.md#single-line-comments-with) 

    [**`tips for getting started`**](foundations.md#tips-for-getting-started)

</div>
</div>

<div class="pt-category" markdown="block">
#### Data types { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-shape-outline:{ .lg .middle } [__Basics__](types.md)

    Kinds of values, and what you can do with them.

    [`isinstance`](types.md) 
    [`type`](types.md) 

    [**`integers`**](types.md#integers): 
    [`+ - * / **`](types.md#arithmetic) 
    [`+= -= *= /= //= %= **=`](types.md#apply-arithmetic-to-a-variable) 
    [`// % divmod`](types.md#floor-division-modulo) 
    [`abs`](types.md#absolute-value) 
    [`boolean expressions`](types.md#boolean-expressions) 
    [`int`](types.md#convert) 

    [**`floats`**](types.md#floats): 
    [`+ - * / **`](types.md#arithmetic_1) 
    [`+= -= *= /= //= %= **=`](types.md#apply-arithmetic-to-a-variable_1) 
    [`// % divmod`](types.md#floor-division-modulo_1) 
    [`abs`](types.md#adjust) 
    [`boolean expressions`](types.md#boolean-expressions_1) 
    [`float`](types.md#convert_1) 
    [`round`](types.md#adjust) 

    [**`strings`**](types.md#strings): 
    [`+ * += *=`](types.md#combine) 
    [`boolean expressions`](types.md#boolean-expressions_2) 
    [`capitalize`](types.md#modify) 
    [`combine`](types.md#combine) 
    [`count`](types.md#search) 
    [`endswith`](types.md#validate) 
    [`f-string`](types.md#f-strings) 
    [`find`](types.md#search) 
    [`format`](types.md#f-strings) 
    [`in`](types.md#search) 
    [`index`](types.md#access-characters) 
    [`isalpha`](types.md#validate) 
    [`isdigit`](types.md#validate) 
    [`join`](types.md#combine) 
    [`len`](types.md#inspect) 
    [`lower`](types.md#modify) 
    [`replace`](types.md#modify) 
    [`slice`](types.md#access-characters) 
    [`split`](types.md#convert_2) 
    [`startswith`](types.md#validate) 
    [`step`](types.md#access-characters) 
    [`str`](types.md#convert_2) 
    [`strip`](types.md#modify) 
    [`title`](types.md#modify) 
    [`upper`](types.md#modify) 

    [**`booleans`**](types.md#booleans): 
    [`== != > < >= <=`](types.md#boolean-expressions_3) 
    [`and`](types.md#logical-operators) 
    [`in`](types.md#boolean-expressions_3) 
    [`is`](types.md#boolean-expressions_3) 
    [`not`](types.md#logical-operators) 
    [`or`](types.md#logical-operators) 

    [**`None`**](types.md#none): 
    [`boolean expressions`](types.md#boolean-expressions_4) 
    [`is`](types.md#check-for-none) 
    [`is not`](types.md#check-for-none) 

-   :material-basket-outline:{ .lg .middle } [__Collections__](collections.md)

    Multiple related values grouped into one container.

    [`isinstance`](collections.md) 
    [`type`](collections.md) 

    [**`lists`**](collections.md#lists): 
    [`+`](collections.md#create) 
    [`append`](collections.md#add-item) 
    [`boolean expressions`](collections.md#boolean-expressions) 
    [`clear`](collections.md#remove-item) 
    [`comprehension`](collections.md#list-comprehension) 
    [`copy`](collections.md#create) 
    [`count`](collections.md#inspect) 
    [`create`](collections.md#create-a-list) 
    [`del`](collections.md#remove-item) 
    [`extend`](collections.md#add-item) 
    [`in`](collections.md#boolean-expressions) 
    [`index`](collections.md#create-a-list) 
    [`insert`](collections.md#add-item) 
    [`item`](collections.md#lists) 
    [`len`](collections.md#inspect) 
    [`list`](collections.md#create) 
    [`loop`](collections.md#loop-through-a-list) 
    [`max`](collections.md#arithmetic) 
    [`min`](collections.md#arithmetic) 
    [`pop`](collections.md#remove-item) 
    [`remove`](collections.md#remove-item) 
    [`reverse`](collections.md#sort) 
    [`slice`](collections.md#access-and-update-items) 
    [`sort`](collections.md#sort) 
    [`sorted`](collections.md#sort) 
    [`step`](collections.md#access-and-update-items) 
    [`sum`](collections.md#arithmetic) 

    [**`dictionaries`**](collections.md#dictionaries): 
    [`access a value`](collections.md#access-a-value) 
    [`boolean expressions`](collections.md#boolean-expressions_1) 
    [`clear`](collections.md#remove_1) 
    [`copy`](collections.md#create_1) 
    [`del`](collections.md#remove_1) 
    [`dict`](collections.md#create_1) 
    [`get`](collections.md#dictionary-operations) 
    [`items`](collections.md#loop-through-a-dictionary) 
    [`key`](collections.md#dictionaries) 
    [`len`](collections.md#inspect_1) 
    [`loop`](collections.md#loop-through-a-dictionary) 
    [`pop`](collections.md#remove_1) 
    [`popitem`](collections.md#remove_1) 
    [`update`](collections.md#update_1) 
    [`value`](collections.md#dictionaries) 
    [`values`](collections.md#loop-through-a-dictionary) 

    [**`tuples`**](collections.md#tuples): 
    [`access items`](collections.md#access-items) 
    [`boolean expressions`](collections.md#boolean-expressions_2) 
    [`count`](collections.md#inspect_2) 
    [`immmutable`](collections.md#tuples) 
    [`index`](collections.md#tuples) 
    [`index`](collections.md#inspect_2) 
    [`len`](collections.md#inspect_2) 
    [`loop`](collections.md#loop-through-a-tuple) 
    [`max`](collections.md#arithmetic_1) 
    [`min`](collections.md#arithmetic_1) 
    [`packing`](collections.md#packing-and-unpacking) 
    [`sum`](collections.md#arithmetic_1) 
    [`tuple`](collections.md#create_2) 
    [`unpacking`](collections.md#packing-and-unpacking) 

    [**`sets`**](collections.md#sets): 
    [`add`](collections.md#update_1) 
    [`boolean expressions`](collections.md#boolean-expressions_3) 
    [`clear`](collections.md#remove_1) 
    [`copy`](collections.md#create_3) 
    [`discard`](collections.md#remove_1) 
    [`isdisjoint`](collections.md#compare) 
    [`issubset`](collections.md#compare) 
    [`issuperset`](collections.md#compare) 
    [`len`](collections.md#inspect_3) 
    [`loop`](collections.md#loop-through-a-set) 
    [`max`](collections.md#arithmetic_2) 
    [`min`](collections.md#arithmetic_2) 
    [`pop`](collections.md#remove_1) 
    [`remove`](collections.md#remove_1) 
    [`set`](collections.md#create_3) 
    [`sum`](collections.md#arithmetic_2) 
    [`update`](collections.md#update_1) 
    [`| & - ^`](collections.md#combine) 

</div>
</div>

<div class="pt-category" markdown="block">
#### Control flow { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-source-branch:{ .lg .middle } [__Conditionals__](conditionals.md)

    Decision points that run code only if a condition is met.

    [**`if, elif, else`**](conditionals.md#if-elif-else): 
    [`and, or, not`](conditionals.md#logical-operators) 
    [`boolean expressions`](conditionals.md#boolean-expressions) 

    [**`match, case`**](conditionals.md#match-case): 
    [`_ wildcard`](conditionals.md#default-value-_) 
    [`case + if`](conditionals.md#case-if) 
    [`match with |`](conditionals.md#match-multiple-values-with) 
    [`unpacking`](conditionals.md#unpacking-a-tuple) 

    [**`control flow`**](conditionals.md#control-flow-statements): 
    [`break`](conditionals.md#break) 
    [`continue`](conditionals.md#continue) 
    [`pass`](conditionals.md#going-further_2) 

-   :material-repeat:{ .lg .middle } [__Loops__](loops.md)

    Repeat a block of code multiple times.

    [**`for`**](loops.md#for-loops): 
    [`enumerate`](loops.md#loop-with-index-and-value) 
    [`loop a set number of times`](loops.md#loop-a-certain-number-of-times) 
    [`loop through a collection`](loops.md#loop-through-a-collection) 
    [`range`](loops.md#iterable-range) 
    [`reversed`](loops.md#loop-in-reverse) 
    [`zip`](loops.md#loop-with-index-and-value) 

    [**`while`**](loops.md#while-loops): 
    [`and`](loops.md#logical-operators) 
    [`boolean expressions`](loops.md#boolean-expressions) 
    [`counter and flag names`](loops.md#counter-and-flag-names) 
    [`flag`](loops.md#using-a-flag) 
    [`not`](loops.md#logical-operators) 
    [`or`](loops.md#logical-operators) 
    [`sentinel`](loops.md#sentinel) 

    [**`common patterns`**](loops.md#common-patterns): 
    [`accumulator`](loops.md#accumulator) 
    [`counter`](loops.md#counter) 
    [`nested loops`](loops.md#nested-loops) 

    [**`control flow`**](loops.md#control-flow-statements): 
    [`break`](loops.md#break) 
    [`continue`](loops.md#continue) 
    [`else`](loops.md#else) 
    [`pass`](loops.md#going-further_2) 


</div>
</div>

<div class="pt-category" markdown="block">
#### Code organization { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-function-variant:{ .lg .middle } [__Functions__](functions.md)

    Package a named block of code to run it at any time.

    [**`def`**](functions.md#defining-a-function): 
    [`default parameter values`](functions.md#default-parameter-values) 
    [`docstrings`](functions.md#docstrings) 
    [`keep functions focused`](functions.md#keep-functions-focused) 
    [`keyword arguments`](functions.md#keyword-arguments) 
    [`return`](functions.md#return-values) 
    [`type hints`](functions.md#type-hints) 

    [**`flexible arguments`**](functions.md#flexible-arguments): 
    [`**kwargs`](functions.md#kwargs) 
    [`*args`](functions.md#args) 

    [**`scope`**](functions.md#scope): 
    [`local vs global`](functions.md#local-vs-global-variables) 

    [**`recursion`**](functions.md#recursion)

    [**`decorators`**](functions.md#decorators): 
    [`accepting any arguments`](functions.md#accepting-any-arguments) 
    [`applying a decorator manually`](functions.md#applying-a-decorator-manually) 
    [`decorators with arguments`](functions.md#decorators-with-arguments) 
    [`preserving identity`](functions.md#preserving-identity) 
    [`stacking decorators`](functions.md#stacking-decorators) 
    [`wrapping the call`](functions.md#wrapping-the-call) 

-   :material-package-variant:{ .lg .middle } [__Classes__](oop.md)

    Bundle related values and functions to a reusable blueprint for similar objects.

    [**`class`**](oop.md#classes-and-objects): 
    [`__init__()`](oop.md#the-__init__-method) 
    [`object methods`](oop.md#object-methods) 
    [`self`](oop.md#the-self-parameter) 

    [**`method decorators`**](oop.md#method-decorators): 
    [`@classmethod`](oop.md#classmethod) 
    [`@property`](oop.md#property) 
    [`@staticmethod`](oop.md#staticmethod) 

    [**`inheritance`**](oop.md#inheritance): 
    [`adding attributes and methods`](oop.md#adding-attributes-and-methods) 
    [`overriding __init__()`](oop.md#overriding-__init__) 
    [`overriding methods`](oop.md#overriding-methods) 
    [`super()`](oop.md#using-super) 

    [**`polymorphism`**](oop.md#polymorphism): 
    [`polymorphism via inheritance`](oop.md#polymorphism-via-inheritance) 
    [`same method name, unrelated classes`](oop.md#same-method-name-unrelated-classes) 

</div>
</div>

<div class="pt-category" markdown="block">
#### External files and resources { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-import:{ .lg .middle } [__Modules & Imports__](modules.md)

    Splitting code across files, and using someone else's code.

    [**`import`**](modules.md#importing-modules): 
    [`as`](modules.md#as) 
    [`from`](modules.md#from) 
    [`import`](modules.md#import) 
    [`import order`](modules.md#order-of-multiple-imports) 
    [`nested paths`](modules.md#nested-paths) 
    [`packages`](modules.md#packages) 

    [**`your own module`**](modules.md#creating-your-own-module): 
    [`main guard`](modules.md#the-main-guard) 

    [**`module, package, library`**](modules.md#modules-vs-packages-vs-libraries)

-   :material-file-document-outline:{ .lg .middle } [__Reading & Writing Files__](files.md)

    Read and write text files on your computer.

    [**`open()`**](files.md#opening-a-file)

    [**`read()`**](files.md#reading-a-file)

    [**`write()`**](files.md#writing-multiple-lines)

    [**`append`**](files.md#appending-vs-overwriting)

</div>
</div>

<div class="pt-category" markdown="block">
#### Robust programming practices { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-palette-outline:{ .lg .middle } [__Style__](style.md)

    Conventions for standardized and readable Python.

    [**`PEP 8`**](style.md#pep-8-style-guide): 
    [`blank lines`](style.md#blank-lines) 
    [`comments`](style.md#comments) 
    [`constants`](style.md#constants) 
    [`docstrings`](style.md#docstrings) 
    [`indentation`](style.md#indentation) 
    [`naming`](style.md#naming) 
    [`order`](style.md#file-order) 
    [`quote style`](style.md#quote-style) 
    [`whitespace`](style.md#whitespace) 

    [**`Pythonic patterns`**](style.md#pythonic-patterns): 
    [`common patterns`](style.md#common-patterns) 

    [**`best practices`**](style.md#additional-best-practices)

    [**`linter`**](style.md#linter-tool)

    [**`checklist`**](style.md#checklist)

-   :material-bug-outline:{ .lg .middle } [__Errors__](errors.md)

    How to understand, fix, and handle errors.

    [**`kinds`**](errors.md#kinds-of-errors): 
    [`bugs`](errors.md) 
    [`exceptions`](errors.md) 
    [`logic errors`](errors.md#logic-errors) 
    [`runtime errors`](errors.md#runtime-errors) 
    [`syntax errors`](errors.md#syntax-errors) 

    [**`fixing`**](errors.md#fixing-errors): 
    [`debugger tool`](errors.md#debugger-tool) 
    [`debugging strategies`](errors.md#debugging-strategies) 
    [`isolate problems`](errors.md#isolate-the-problem) 
    [`print debugging`](errors.md#print-debugging) 
    [`rubber duck debugging`](errors.md#read-it-out-loud) 
    [`syntax error message`](errors.md#reading-a-syntax-error-message) 
    [`testing`](errors.md#detect-errors-with-testing) 
    [`TODO / FIXME`](errors.md#flag-as-todofixme) 
    [`tracebacks`](errors.md#reading-a-traceback) 

    [**`handling`**](errors.md#handling-errors): 
    [`assert`](errors.md#assert-a-condition) 
    [`else`](errors.md#finally) 
    [`finally`](errors.md#finally) 
    [`raise`](errors.md#raise-an-exception) 
    [`try/except`](errors.md#catch-with-tryexcept) 

</div>
</div>

# Add-On Libraries

<div class="pt-category pt-category--wide pt-lib--1" markdown="block">
#### Testing { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-test-tube:{ .lg .middle } [__pytest__](libraries/pytest.md) 
[:material-download-outline:](libraries/pytest.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Writing and running tests: assertions, fixtures, and parametrizing.

    [**`writing and running a test`**](libraries/pytest.md#writing-and-running-a-test): 
    [`from the command line`](libraries/pytest.md#from-the-command-line) 

    [**`reading a failure`**](libraries/pytest.md#reading-a-failure)

    [**`fixtures`**](libraries/pytest.md#fixtures)

    [**`parametrizing tests`**](libraries/pytest.md#parametrizing-tests)

    [**`testing for exceptions`**](libraries/pytest.md#testing-for-exceptions)

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--3" markdown="block">
#### Utilities { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-format-list-group:{ .lg .middle } [__collections__](libraries/collections.md) 
[:material-language-python:](libraries/collections.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Specialized containers with advanced functionality.

    [**`Counter`**](libraries/collections.md#counter): 
    [`+ - & |`](libraries/collections.md#combine) 
    [`counts[item]`](libraries/collections.md#count) 
    [`elements`](libraries/collections.md#inspect) 
    [`most_common`](libraries/collections.md#count) 
    [`subtract`](libraries/collections.md#update) 
    [`total`](libraries/collections.md#count) 
    [`update`](libraries/collections.md#update) 

    [**`defaultdict`**](libraries/collections.md#defaultdict): 
    [`default_factory`](libraries/collections.md#defaultdict) 
    [`get`](libraries/collections.md#reading-vs-writing) 

    [**`namedtuple`**](libraries/collections.md#namedtuple): 
    [`_asdict`](libraries/collections.md#convert) 
    [`_field_defaults`](libraries/collections.md#inspect_1) 
    [`_fields`](libraries/collections.md#inspect_1) 
    [`_make`](libraries/collections.md#create) 
    [`_replace`](libraries/collections.md#convert) 
    [`defaults=`](libraries/collections.md#create) 

    [**`deque`**](libraries/collections.md#deque): 
    [`append`](libraries/collections.md#add) 
    [`appendleft`](libraries/collections.md#add) 
    [`clear`](libraries/collections.md#remove) 
    [`copy`](libraries/collections.md#inspect_2) 
    [`count`](libraries/collections.md#inspect_2) 
    [`extend`](libraries/collections.md#add) 
    [`extendleft`](libraries/collections.md#add) 
    [`index`](libraries/collections.md#inspect_2) 
    [`insert`](libraries/collections.md#add) 
    [`maxlen=`](libraries/collections.md#reorder) 
    [`pop`](libraries/collections.md#remove) 
    [`popleft`](libraries/collections.md#remove) 
    [`remove`](libraries/collections.md#remove) 
    [`reverse`](libraries/collections.md#reorder) 
    [`rotate`](libraries/collections.md#reorder) 

    [**`OrderedDict`**](libraries/collections.md#ordereddict): 
    [`==`](libraries/collections.md#compare) 
    [`move_to_end`](libraries/collections.md#reorder_1) 
    [`popitem`](libraries/collections.md#reorder_1) 

    [**`ChainMap`**](libraries/collections.md#chainmap): 
    [`maps`](libraries/collections.md#inspect_3) 
    [`new_child`](libraries/collections.md#extend) 
    [`parents`](libraries/collections.md#inspect_3) 

    [**`User* wrapper`**](libraries/collections.md#user-wrapper-classes): 
    [`UserDict`](libraries/collections.md#user-wrapper-classes) 
    [`UserList`](libraries/collections.md#user-wrapper-classes) 
    [`UserString`](libraries/collections.md#user-wrapper-classes) 

-   :material-calendar-clock:{ .lg .middle } [__datetime__](libraries/datetime.md) 
[:material-language-python:](libraries/datetime.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Calculating and formatting dates and times.

    [`creating a specific date`](libraries/datetime.md#creating-a-specific-date) 
    [`date`](libraries/datetime.md#creating-dates-and-times) 
    [`strftime`](libraries/datetime.md#formatting-with-strftime) 

    [`difference between two dates`](libraries/datetime.md#difference-between-two-dates) 
    [`strptime`](libraries/datetime.md#parsing-a-string-with-strptime) 
    [`timedelta`](libraries/datetime.md#date-arithmetic) 

-   :material-dice-multiple:{ .lg .middle } [__random__](libraries/random.md) 
[:material-language-python:](libraries/random.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Random numbers, random picks, shuffled order.

    [**`randint`**](libraries/random.md#random-numbers)

    [**`choice`**](libraries/random.md#random-selections): 
    [`sample`](libraries/random.md#sampling-without-replacement) 
    [`shuffle`](libraries/random.md#shuffling-a-list) 

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--4" markdown="block">
#### Data analysis { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-file-delimited-outline:{ .lg .middle } [__csv__](libraries/csv.md) 
[:material-language-python:](libraries/csv.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Reading and writing spreadsheets.

    [`writer`](libraries/csv.md#writing-csv-files)

    [`DictReader`](libraries/csv.md#reading-rows-as-dictionaries) 
    [`reader`](libraries/csv.md#reading-csv-files) 

-   :material-chart-line:{ .lg .middle } [__matplotlib__](libraries/matplotlib.md) 
[:material-download-outline:](libraries/matplotlib.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Charts and plots: line, bar, and scatter, built directly from plain Python data.

    [**`line plots`**](libraries/matplotlib.md#line-plots): 
    [`labels and title`](libraries/matplotlib.md#labels-and-title) 
    [`multiple lines and a legend`](libraries/matplotlib.md#multiple-lines-and-a-legend) 

    [**`bar charts`**](libraries/matplotlib.md#bar-charts)

    [**`scatter plots`**](libraries/matplotlib.md#scatter-plots)

    [**`subplots`**](libraries/matplotlib.md#subplots)

    [**`saving a figure`**](libraries/matplotlib.md#saving-a-figure)

-   :material-matrix:{ .lg .middle } [__NumPy__](libraries/numpy.md) 
[:material-download-outline:](libraries/numpy.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Fast numeric arrays, with math applied to a whole array at once instead of item by item.

    [**`array operations`**](libraries/numpy.md#array-operations): 
    [`boolean mask`](libraries/numpy.md#filtering-with-a-boolean-mask) 
    [`mean`](libraries/numpy.md#aggregating-an-array) 

    [`arange`](libraries/numpy.md#building-arrays-without-a-list) 
    [`ndarray`](libraries/numpy.md#creating-arrays) 

-   :material-table:{ .lg .middle } [__pandas__](libraries/pandas.md) 
[:material-download-outline:](libraries/pandas.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Tabular data: rows and columns, like a spreadsheet, built on top of NumPy.

    [**`DataFrame`**](libraries/pandas.md#building-a-dataframe)

    [**`working with a DataFrame`**](libraries/pandas.md#working-with-a-dataframe): 
    [`mean`](libraries/pandas.md#summarizing-a-column) 
    [`sort_values`](libraries/pandas.md#sorting-rows) 

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--2" markdown="block">
#### APIs { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-code-json:{ .lg .middle } [__json__](libraries/json.md) 
[:material-language-python:](libraries/json.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Reading and writing JSON data: nested dicts and lists, saved to a file or a string.

    [`dump`](libraries/json.md#writing-json-files)

    [`load`](libraries/json.md#reading-json-files) 
    [`nested data`](libraries/json.md#nested-data) 

    [`loads`](libraries/json.md#working-with-strings-instead-of-files)

-   :material-webhook:{ .lg .middle } [__requests__](libraries/requests.md) 
[:material-download-outline:](libraries/requests.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Fetching data over the internet, like asking a website or API for information.

    [**`get`**](libraries/requests.md#making-a-request): 
    [`json`](libraries/requests.md#parsing-json) 
    [`params`](libraries/requests.md#query-parameters) 
    [`status_code`](libraries/requests.md#checking-the-status-code) 

    [**`error handling`**](libraries/requests.md#handling-request-errors)

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block">
#### Image editing { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-image-outline:{ .lg .middle } [__Pillow__](libraries/pillow.md) 
[:material-download-outline:](libraries/pillow.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Opening, editing, and saving images, built around one Image object.

    [**`why Pillow?`**](libraries/pillow.md#why-pillow)

    [**`Image`**](libraries/pillow.md#the-image): 
    [`basic operations`](libraries/pillow.md#basic-operations) 
    [`crop`](libraries/pillow.md#crop) 
    [`image modes`](libraries/pillow.md#image-modes) 
    [`opening and saving images`](libraries/pillow.md#opening-and-saving-images) 
    [`resize`](libraries/pillow.md#resize) 
    [`rotate and flip`](libraries/pillow.md#rotate-and-flip) 

    [**`ImageOps`**](libraries/pillow.md#imageops-module): 
    [`common ImageOps functions`](libraries/pillow.md#common-imageops-functions) 

    [**`ImageDraw`**](libraries/pillow.md#imagedraw-module): 
    [`shapes and lines`](libraries/pillow.md#shapes-and-lines) 

    [**`ImageFont`**](libraries/pillow.md#imagefont-module): 
    [`loading a font`](libraries/pillow.md#loading-a-font) 

    [**`ImageColor`**](libraries/pillow.md#imagecolor-module): 
    [`converting color names`](libraries/pillow.md#converting-color-names) 

    [**`ImageFilter`**](libraries/pillow.md#imagefilter-module): 
    [`applying a filter`](libraries/pillow.md#applying-a-filter) 

    [**`ImageEnhance`**](libraries/pillow.md#imageenhance-module): 
    [`enhancing an image`](libraries/pillow.md#enhancing-an-image) 

    [**`ImageChops`**](libraries/pillow.md#imagechops-module): 
    [`comparing and combining images`](libraries/pillow.md#comparing-and-combining-images) 

    [**`convert`**](libraries/pillow.md#format-conversion): 
    [`converting between formats`](libraries/pillow.md#converting-between-formats) 

    [**`ImageSequence`**](libraries/pillow.md#imagesequence-module): 
    [`looping over GIF frames`](libraries/pillow.md#looping-over-gif-frames) 

    [**`putting it together`**](libraries/pillow.md#putting-it-together): 
    [`an interactive filter tool`](libraries/pillow.md#an-interactive-filter-tool) 

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block">
#### Desktop UIs { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-application-outline:{ .lg .middle } [__Tkinter__](libraries/tkinter.md) 
[:material-language-python:](libraries/tkinter.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Creating desktop applications: text, buttons, dropdowns, forms, output, etc.

    [**`Tk`**](libraries/tkinter.md#creating-a-window)

    [**`Button`**](libraries/tkinter.md#widgets): 
    [`Button`](libraries/tkinter.md#button) 
    [`Entry`](libraries/tkinter.md#entry) 
    [`Label`](libraries/tkinter.md#label) 

    [**`pack`**](libraries/tkinter.md#layout-managers): 
    [`grid`](libraries/tkinter.md#grid) 
    [`pack`](libraries/tkinter.md#pack) 

    [**`configure`**](libraries/tkinter.md#configuring-widgets): 
    [`reading and changing options`](libraries/tkinter.md#reading-and-changing-options) 

    [**`command`**](libraries/tkinter.md#handling-events): 
    [`binding events`](libraries/tkinter.md#binding-events) 
    [`command callbacks`](libraries/tkinter.md#command-callbacks) 

    [**`Style`**](libraries/tkinter.md#styling-with-ttk): 
    [`customizing a style`](libraries/tkinter.md#customizing-a-style) 

    [**`messagebox`**](libraries/tkinter.md#dialogs): 
    [`file dialogs`](libraries/tkinter.md#file-dialogs) 
    [`message boxes`](libraries/tkinter.md#message-boxes) 

    [**`winfo_width`**](libraries/tkinter.md#introspecting-widgets): 
    [`winfo methods`](libraries/tkinter.md#winfo-methods) 

    [**`putting it together`**](libraries/tkinter.md#putting-it-together): 
    [`a simple form`](libraries/tkinter.md#a-simple-form) 

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block">
#### Computer vision { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-face-recognition:{ .lg .middle } [__OpenCV__](libraries/opencv.md) 
[:material-download-outline:](libraries/opencv.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Real-time image and video analysis, built directly on NumPy arrays: color spaces, edge detection, face detection.

    [**`reading, displaying, saving images`**](libraries/opencv.md#reading-displaying-and-saving-images): 
    [`displaying a window`](libraries/opencv.md#displaying-a-window) 
    [`imread`](libraries/opencv.md#reading-a-file) 
    [`saving a file`](libraries/opencv.md#saving-a-file) 

    [**`drawing`**](libraries/opencv.md#drawing-shapes-and-text): 
    [`shapes and lines`](libraries/opencv.md#shapes-and-lines) 
    [`text`](libraries/opencv.md#text) 

    [**`color spaces`**](libraries/opencv.md#color-spaces): 
    [`cvtColor`](libraries/opencv.md#converting-color-spaces) 

    [**`CascadeClassifier`**](libraries/opencv.md#face-detection-with-cascade-classifiers): 
    [`detecting and labeling faces`](libraries/opencv.md#detecting-and-labeling-faces) 

    [**`VideoCapture`**](libraries/opencv.md#working-with-video): 
    [`reading frames`](libraries/opencv.md#reading-frames) 

    [**`basic operations`**](libraries/opencv.md#basic-operations): 
    [`cropping`](libraries/opencv.md#cropping) 
    [`resize`](libraries/opencv.md#resize) 
    [`rotating`](libraries/opencv.md#rotating) 

    [**`thresholding, edge detection`**](libraries/opencv.md#thresholding-and-edge-detection): 
    [`Canny`](libraries/opencv.md#edge-detection) 
    [`threshold`](libraries/opencv.md#threshold) 

    [**`blurring`**](libraries/opencv.md#blurring): 
    [`gaussian blur`](libraries/opencv.md#gaussian-blur) 

    [**`contours`**](libraries/opencv.md#contours): 
    [`finding and drawing contours`](libraries/opencv.md#finding-and-drawing-contours) 

</div>
</div>

</div>

### FAQ

??? ai "Why learn to code yourself, if AI can do it for you?"

    <div class="pt-compare">

    |  | Learn to do it yourself | Have AI do it for you |
    |---|---|---|
    | **Writing & struggling with code** | :material-check:{ .pt-icon-success } **Productive struggle** is what builds understanding<ul><li>You can solve the problem again on your own</li><li>Adapt the answer, and catch when it's wrong</li></ul> | :material-close:{ .pt-icon-fail } Being handed the answer skips [the friction that builds understanding](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf)<ul><li>If you skip that struggle, you *won't develop the knowledge* to solve the problem again, adapt the answer, or recognize when it's wrong.</li></ul> |
    | **Reading & verifying code** | :material-check:{ .pt-icon-success } Understanding programming fundamentals makes AI more useful — you can read code you didn't write, and check it before you trust it<ul><li>Spot mistakes</li><li>Understand *why* a solution works</li><li>Communicate your problem to AI more effectively</li></ul> | :material-close:{ .pt-icon-fail } Inefficient communication with AI if you don't fully understand what's going on, and AI code can look correct while being **wrong and insecure**<ul><li>You can't tell *why* a solution works</li><li>Researchers are already documenting this skill gap in [students who rely on AI code generation](https://dl.acm.org/doi/10.1145/3617367) before they've [built their own foundation](https://dl.acm.org/doi/10.1145/3624720)</li><li>One [Stanford study](https://dl.acm.org/doi/10.1145/3576915.3623157) found developers using AI wrote *less* secure code — but were *more* confident it was secure</li></ul> |
    | **On the job** | :material-check:{ .pt-icon-success } Employers are still hiring for understanding, not prompting<ul><li>Code review, debugging, and interviews all test whether you can reason about code</li><li>And judge whether it's correct</li><li>Learning to program on your own turns AI into a tool you can direct and verify, instead of one you're assuming got it right</li></ul> | :material-close:{ .pt-icon-fail } AI will likely be available at work too — but it isn't what's being tested |

    </div>

??? ai "How to use AI to support your learning"

    ```mermaid
    swimlane-beta TB
        accTitle: Using AI to learn
        accDescr: AI walks you through setup before you start. You attempt each problem yourself with autocomplete off, then check whether you can explain why it works and whether it actually holds up — if either check fails, you describe what you tried rather than handing over your code, so AI explains the concept instead of fixing it, and you try again. Passing both checks means you understand it well enough for a practice problem, or for the code review, debugging, and interviews that are what your job actually tests.

        subgraph You
            you_help_setup(Need help setting up your computer to start programming?)
            you_have_project(Do you have a project to work on?)
            you_attempt(Attempt it yourself, autocomplete off so you understand everything that's there, utilize debug strategies)
            you_writeup(Stuck? Write out your problem: what you expect to happen, what you're observing, what you've tried already, see if this helps you process or rethink your strategy)
            you_finish("Learning to program means making mistakes, getting stuck, and eventually figuring things out and forming a mental model. That's the process that builds skills you can rely on to continue solving problems and detecting issues — ready for code review, debugging, and interviews, where AI won't be tested, your reasoning will. ")
        end

        subgraph AI
            ai_help_setup(AI can help guide you through setup on your exact device — which could make getting started more accessible for beginners)
            ai_suggest_problem(Suggests a problem based on your skill level, interests, and what you're trying to improve)
            explain(With that context AI can provide more targeted, efficient help. Don't just paste the code/error, ask AI to explain what a line does, or what an error means — an explanation to help you understand concepts, be clear you do NOT want it to write code, just explain)
        end

       
        ai_help_setup ~~~ you_help_setup
        ai_suggest_problem ~~~ you_have_project
        you_help_setup -->|Yes| ai_help_setup
        you_help_setup -->|No| you_have_project
        ai_help_setup --> you_have_project
        
        you_have_project -->|No| ai_suggest_problem
        
        you_have_project -->|Yes| you_attempt
        
        ai_suggest_problem --> you_attempt
        you_attempt <--> you_writeup
        you_attempt -->|Done!| you_finish
        you_writeup --> |still stuck?| explain
        explain --> you_attempt
        explain ~~~ you_finish

        %% Edge label text colored red if it leads into the AI lane, green
        %% if it leads into the You lane, matching the lane colors. This is
        %% linkStyle's "color" property (not background) — the one styling
        %% mechanism mermaid applies from inside its own closed shadow
        %% root, so it's the only thing that actually reaches the label.
        linkStyle 0 color:#a33f3f
        linkStyle 1 color:#3f6b52
        linkStyle 3 color:#3f6b52
        linkStyle 4 color:#a33f3f
        linkStyle 7 color:#3f6b52
        linkStyle 8 color:#a33f3f

        classDef you fill:#3f6b521f,stroke:#3f6b52,stroke-width:2px,color:#3f6b52
        classDef ai fill:#a33f3f1a,stroke:#a33f3f,stroke-width:2px,color:#a33f3f
        class you_writeup,you_help_setup,you_have_project,you_attempt,you_finish you
        class explain,ai_help_setup,ai_suggest_problem ai
        style You fill:#3f6b521f,stroke:#3f6b52,color:#3f6b52
        style AI fill:#a33f3f1a,stroke:#a33f3f,color:#a33f3f
    ```

    <p class="pfg-diagram-caption">FIG: when to use AI while learning to program</p>

??? info "What is Python, and what is this guide?"

    **Readable, and quick to write.** *Python* is a general-purpose language built for code that's easy to read back later — even by someone who didn't write it. No compiling: write a `.py` file, run it directly.

    - **Shows up everywhere** — web backends, data analysis and machine learning, automating repetitive tasks, scientific computing, quick glue scripts. Several of these are covered on this site's [Libraries](#utilities) pages.
    - **The skills transfer.** Variables, conditionals, loops, functions, classes — the fundamentals every language shares — read closer to plain English here, so you spend your effort learning to *think* like a programmer instead of fighting a stricter syntax. Once solid, those fundamentals carry over to whatever language you pick up next.
    - **Often the fastest language to write *correct* code in** — even though it's not the fastest to *run* — which is why it's such a common first choice for a new project.

    **This guide.** *Python Field Guide* is a free, in-browser reference — most code blocks are editable and runnable directly on the page.

    - **For learners** — self-taught, students in an intro course, or anyone who wants one combined reference to work through start to finish, instead of a scattered pile of search results.
