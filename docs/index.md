---
description: >-
  A free Python reference with runnable code examples covering data types, collections,
  loops, functions, classes, error handling, and popular libraries.
hide:
  - navigation
  - toc
---

# Python Field Guide { .pt-visually-hidden }

??? ai "Using AI while learning to code"

    === "Why still learn to code yourself?"

        <div class="pt-compare">

        |  | Learn to do it yourself | Have AI do it for you |
        |---|---|---|
        | **Writing & struggling with code** | :material-check:{ .pt-icon-success } Productive struggle is what **builds understanding**<ul><li>You can solve the problem **again** on your own</li><li>**Adapt** the answer, and **catch** when it's wrong</li></ul> | :material-close:{ .pt-icon-fail } Being handed the answer skips [the friction that builds understanding](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf)<ul><li>If you skip that struggle, you **won't develop the knowledge** to solve the problem again, adapt the answer, or recognize when it's wrong.</li></ul> |
        | **Reading & verifying code** | :material-check:{ .pt-icon-success } **Understanding programming fundamentals** makes AI more useful — you can read and evaluate code you didn't write<ul><li>Spot mistakes</li><li>Understand **why** a solution works</li><li>Communicate your problem to AI more effectively</li></ul> | :material-close:{ .pt-icon-fail } Inefficient communication with AI **if you don't fully understand **what's going on, and AI code can look correct while being wrong or insecure<ul><li>You can't tell **why** a solution works</li><li>Researchers are already documenting this skill gap in [students who rely on AI code generation](https://dl.acm.org/doi/10.1145/3617367) before they've [built their own foundation](https://dl.acm.org/doi/10.1145/3624720)</li><li>One [Stanford study](https://dl.acm.org/doi/10.1145/3576915.3623157) found developers using AI wrote **less** secure code — but were **more** confident it was secure</li></ul> |
        | **On the job** | :material-check:{ .pt-icon-success } Programming work still requires understanding:<ul><li>Code review, debugging, system design, and interviews all test whether you can reason about code and judge whether it's correct</li><li>Learning to program on your own turns AI into a **tool you can direct and verify**, instead of one you're assuming got it right</li></ul> | :material-close:{ .pt-icon-fail } AI will likely be available at work too — but it isn't what will get you hired |

        </div>

    === "How to use AI to support your learning?"

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

    [**`Terminal`**](workspace.md#using-the-terminal): 
    [`cd`](workspace.md#using-the-terminal) 
    [`ls`](workspace.md#using-the-terminal) 
    [`pwd`](workspace.md#using-the-terminal) 
    [`shortcuts`](workspace.md#using-the-terminal) 
    {: data-advanced="true" }

    [**`virtual environments`**](workspace.md#virtual-environments): 
    [`activate`](workspace.md#virtual-environments) 
    [`pip`](workspace.md#virtual-environments) 
    [`requirements.txt`](workspace.md#virtual-environments) 
    [`venv`](workspace.md#virtual-environments) 
    {: data-advanced="true" }

-   :material-cube-outline:{ .lg .middle } [__Foundations__](foundations.md)

    Storing, displaying, and inputting values.

    [**`variables`**](foundations.md#variables): 
    [`naming`](foundations.md#naming-variables) 
    [`printing`](foundations.md#printing-variables) 
    [`reassigning`](foundations.md#reassigning-a-variable) 
    [`types`](foundations.md#variables-and-types) 

    [**`expressions and statements`**](foundations.md#expressions-and-statements)

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
    [`f-string`](types.md#building-strings) 
    [`find`](types.md#search) 
    [`format`](types.md#building-strings) 
    [`format spec`](types.md#building-strings) 
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
    {: data-advanced="true" }

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
    {: data-advanced="true" }

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
    [`**kwargs`](functions.md#kwargs-dict) 
    [`*args`](functions.md#args-tuple) 
    [`defaults`](functions.md#default-values) 
    [`docstrings`](functions.md#docstrings) 
    [`parameters`](functions.md#parameters) 
    [`pass`](functions.md#pass-placeholder) 
    [`return`](functions.md#return-values) 

    [`combining argument types`](functions.md#combining-categories) 
    [`keyword-only`](functions.md#keyword-only) 
    [`positional-only`](functions.md#positional-only) 
    [`type hints`](functions.md#type-hints) 
    {: data-advanced="true" }

    [**`calling a function`**](functions.md#calling-a-function): 
    [`arguments`](functions.md#arguments) 
    [`keyword`](functions.md#by-keyword) 
    [`required`](functions.md#required) 
    [`return value`](functions.md#saving-the-return-value) 
    [`unpacking`](functions.md#unpacking) 

    [**`scope`**](functions.md#scope): 
    [`local vs global`](functions.md#local-vs-global-variables) 

    [**`recursion`**](functions.md#recursion)
    {: data-advanced="true" }

    [**`decorators`**](functions.md#decorators): 
    [`arguments`](functions.md#accepting-arguments) 
    [`identity`](functions.md#advanced-uses) 
    [`original function`](functions.md#returning-the-original-function) 
    [`stacking`](functions.md#advanced-uses) 
    [`wrapping`](functions.md#wrapping-the-call)
    {: data-advanced="true" }

    [**`generators`**](functions.md#generators): 
    [`generator expressions`](functions.md#generator-expressions)
    [`memory`](functions.md#memory-efficiency) 
    [`yield`](functions.md#yield-vs-return) 
    {: data-advanced="true" }

-   :material-package-variant:{ .lg .middle } [__Classes__](classes.md)

    Bundle related values and functions to a reusable blueprint for similar objects.

    [**`class`**](classes.md#defining-a-class): 
    [`__init__()`](classes.md#the-__init__-method) 
    [`class attributes`](classes.md#class-attributes) 
    [`instance attributes`](classes.md#instance-attributes) 
    [`methods`](classes.md#object-methods) 
    [`self`](classes.md#the-self-parameter) 

    [**`method decorators`**](classes.md#method-decorators): 
    [`@classmethod`](classes.md#classmethod) 
    [`@property`](classes.md#property) 
    [`@staticmethod`](classes.md#staticmethod) 
    {: data-advanced="true" }

    [**`inheritance`**](classes.md#inheritance): 
    [`adding attributes and methods`](classes.md#adding-attributes-and-methods) 
    [`__init__()`](classes.md#overriding-__init__) 
    [`overriding`](classes.md#overriding-methods) 
    [`super()`](classes.md#using-super) 

    [`multiple inheritance`](classes.md#multiple-inheritance) 
    {: data-advanced="true" }

    [**`polymorphism`**](classes.md#polymorphism): 
    [`inheritance`](classes.md#polymorphism-via-inheritance) 
    [`duplicate method names`](classes.md#duplicate-method-names) 
    {: data-advanced="true" }

    [**`encapsulation`**](classes.md#encapsulation): 
    [`@property`](classes.md#controlled-access-with-property) 
    [`double underscore`](classes.md#double-underscore) 
    [`single underscore`](classes.md#single-underscore) 
    {: data-advanced="true" }

    [**`operator overloading`**](classes.md#operator-overloading): 
    [`__add__`](classes.md#arithmetic-with-__add__) 
    [`__eq__ and __lt__`](classes.md#comparing-with-__eq__-and-__lt__) 
    {: data-advanced="true" }

    [**`dataclasses`**](classes.md#dataclasses)
    {: data-advanced="true" }

    [**`abstract base classes`**](classes.md#abstract-base-classes)
    {: data-advanced="true" }

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

    [**`open`**](files.md#opening-and-closing-files): 
    [`modes`](files.md#modes-options) 
    [`paths`](files.md#file-paths) 
    [`with`](files.md#with)

    [**`read()`**](files.md#read): 
    [`existing`](files.md#r-read-existing) 
    [`functions`](files.md#functions) 
    [`modes`](files.md#modes) 
    [`read()`](files.md#whole-file) 
    [`readline()`](files.md#by-line) 
    [`readlines()`](files.md#by-line) 
    [`seek()`](files.md#seek-and-tell) 
    [`tell()`](files.md#seek-and-tell)

    [**`write()`**](files.md#write): 
    [`append`](files.md#a-append) 
    [`create`](files.md#x-create) 
    [`functions`](files.md#functions_1) 
    [`modes`](files.md#modes_1) 
    [`overwrite`](files.md#w-overwrite) 
    [`write()`](files.md#single-string) 
    [`writelines()`](files.md#multiple-strings)

    [**`related libraries`**](files.md#related-libraries)

</div>
</div>

<div class="pt-category" markdown="block">
#### Robust programming practices { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-palette-outline:{ .lg .middle } [__Style__](style.md)

    Readable Python code, and polished UI.

    [**`PEP 8`**](style.md#pep-8-style-guide): 
    [`blank lines`](style.md#blank-lines) 
    [`docstrings`](style.md#docstrings) 
    [`naming`](style.md#naming) 
    [`whitespace`](style.md#whitespace) 

    [`comments`](style.md#comments) 
    [`constants`](style.md#constants) 
    [`indentation`](style.md#indentation) 
    [`order`](style.md#file-order) 
    [`quote style`](style.md#quote-style) 
    {: data-advanced="true" }

    [**`Linters, formatters`**](style.md#linters-and-formatters)

    [**`Pythonic patterns`**](style.md#pythonic-patterns): 
    [`mutable defaults`](style.md#mutable-default-arguments)
    [`is None`](style.md#is-none-instead-of-none)

    [`truthy checks`](style.md#truthy-checks) 
    [`enumerate()`](style.md#enumerate-instead-of-range) 
    {: data-advanced="true" }

    [**`Efficiency`**](style.md#efficiency)
    [`big O`](style.md#big-o-notation)
    [`common optimizations`](style.md#common-optimizations)
    [`time`](style.md#time-and-space) 
    [`space`](style.md#time-and-space)
    {: data-advanced="true" }

    [**`Polished UX`**](style.md#polished-ux): 
    [`input validation`](style.md#input-validation) 
    [`menus`](style.md#menus) 
    [`randomize`](style.md#randomize-messages)

    [**`Polished UI`**](style.md#polished-ui): 
    [`background`](style.md#color-styling) 
    [`bold`](style.md#color-styling) 
    [`escape sequences`](style.md#escape-sequences) 
    [`color`](style.md#color-styling) 
    [`highlighting`](style.md#color-styling) 
    [`multi-line strings`](style.md#multi-line-strings) 
    [`formatting variables`](style.md#formatting-variables) 
    [`underline`](style.md#color-styling) 
    [`unicode symbols`](style.md#unicode-symbols) 
    [`dividers`](style.md#dividers) 
    [`boxes`](style.md#boxes) 
    [`progress bars`](style.md#progress-bars)

-   :material-bug-outline:{ .lg .middle } [__Errors__](errors.md)

    Resolve bugs, read and utilize exceptions.

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

<div class="pt-category pt-category--wide pt-lib--5" markdown="block">
#### Utilities { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-format-list-group:{ .lg .middle } [__collections__](libraries/collections.md) 
[:material-language-python:](libraries/collections.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 
    {: data-advanced="card" }

    Specialized containers with advanced functionality.

-   :material-calendar-clock:{ .lg .middle } [__datetime__](libraries/datetime.md) 
[:material-language-python:](libraries/datetime.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Calculating and formatting dates and times.

-   :material-square-root-box:{ .lg .middle } [__math__](libraries/math.md) 
[:material-language-python:](libraries/math.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Rounding, roots, constants, and logarithms.

-   :material-dice-multiple:{ .lg .middle } [__random__](libraries/random.md) 
[:material-language-python:](libraries/random.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Random numbers, random picks, shuffled order.

-   :material-text-search:{ .lg .middle } [__re__](libraries/re.md) 
[:material-language-python:](libraries/re.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Regular expressions: searching, extracting, and replacing text by pattern.

-   :material-clock-outline:{ .lg .middle } [__time__](libraries/time.md) 
[:material-language-python:](libraries/time.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Reading the system clock, pausing execution, and measuring elapsed time.

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--4" markdown="block">
#### Data analysis { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-file-delimited-outline:{ .lg .middle } [__csv__](libraries/csv.md) 
[:material-language-python:](libraries/csv.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Reading and writing spreadsheets.

-   :material-chart-line:{ .lg .middle } [__matplotlib__](libraries/matplotlib.md) 
[:material-download-outline:](libraries/matplotlib.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Charts and plots: line, bar, and scatter, built directly from plain Python data.

-   :material-matrix:{ .lg .middle } [__NumPy__](libraries/numpy.md) 
[:material-download-outline:](libraries/numpy.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 
    {: data-advanced="card" }

    Fast numeric arrays, with math applied to a whole array at once instead of item by item.

-   :material-table:{ .lg .middle } [__pandas__](libraries/pandas.md) 
[:material-download-outline:](libraries/pandas.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 
    {: data-advanced="card" }

    Tabular data: rows and columns, like a spreadsheet, built on top of NumPy.

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--2" markdown="block">
#### APIs { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-code-json:{ .lg .middle } [__json__](libraries/json.md) 
[:material-language-python:](libraries/json.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Reading and writing JSON data: nested dicts and lists, saved to a file or a string.

-   :material-webhook:{ .lg .middle } [__requests__](libraries/requests.md) 
[:material-download-outline:](libraries/requests.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Fetching data over the internet, like asking a website or API for information.

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block">
#### Web scraping { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-pot-steam-outline:{ .lg .middle } [__BeautifulSoup__](libraries/beautifulsoup.md) 
[:material-download-outline:](libraries/beautifulsoup.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Parsing HTML: finding tags, reading attributes and text, and turning a page into structured data.

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block">
#### Image editing { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-image-outline:{ .lg .middle } [__Pillow__](libraries/pillow.md) 
[:material-download-outline:](libraries/pillow.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Opening, editing, and saving images, built around one Image object.

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block">
#### Desktop UIs { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-application-outline:{ .lg .middle } [__Tkinter__](libraries/tkinter.md) 
[:material-language-python:](libraries/tkinter.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Creating desktop applications: text, buttons, dropdowns, forms, output, etc.

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block">
#### Games { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-turtle:{ .lg .middle } [__turtle__](libraries/turtle.md) 
[:material-language-python:](libraries/turtle.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Build small movement-based games with a pen cursor.

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block" data-advanced="true">
#### Testing { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-test-tube:{ .lg .middle } [__pytest__](libraries/pytest.md) 
[:material-download-outline:](libraries/pytest.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Writing and running tests: assertions, fixtures, and parametrizing.

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block" data-advanced="true">
#### Computer vision { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-face-recognition:{ .lg .middle } [__OpenCV__](libraries/opencv.md) 
[:material-download-outline:](libraries/opencv.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 
    {: data-advanced="card" }

    Real-time image and video analysis, built directly on NumPy arrays: color spaces, edge detection, face detection.

</div>
</div>

</div>
