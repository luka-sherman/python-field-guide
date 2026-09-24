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

-   :material-monitor:{ .lg .middle } [__Workspace Setup__](start/workspace.md)

    Write Python on your computer.

    [**`install`**](start/workspace.md#step-0-install-python): 
    [`download`](start/workspace.md#step-0-install-python) 
    [`version`](start/workspace.md#step-0-install-python) 

    [**`code editors`**](start/workspace.md#step-1-pick-an-application-to-write-code-in): 
    [`IDLE`](start/workspace.md#step-1-pick-an-application-to-write-code-in) 
    [`Pycharm`](start/workspace.md#step-1-pick-an-application-to-write-code-in) 
    [`Thonny`](start/workspace.md#step-1-pick-an-application-to-write-code-in) 
    [`VS Code`](start/workspace.md#step-1-pick-an-application-to-write-code-in) 

    [**`how to write and run .py file`**](start/workspace.md#step-2-write-and-run-a-python-file): 
    [`file naming`](start/workspace.md#step-2-write-and-run-a-python-file) 

    [**`Terminal`**](start/workspace.md#using-the-terminal): 
    [`cd`](start/workspace.md#using-the-terminal) 
    [`ls`](start/workspace.md#using-the-terminal) 
    [`pwd`](start/workspace.md#using-the-terminal) 
    [`shortcuts`](start/workspace.md#using-the-terminal) 
    {: data-advanced="true" }

    [**`virtual environments`**](start/workspace.md#virtual-environments): 
    [`activate`](start/workspace.md#virtual-environments) 
    [`pip`](start/workspace.md#virtual-environments) 
    [`requirements.txt`](start/workspace.md#virtual-environments) 
    [`venv`](start/workspace.md#virtual-environments) 
    {: data-advanced="true" }

-   :material-cube-outline:{ .lg .middle } [__Foundations__](start/foundations.md)

    Storing, displaying, and inputting values.

    [**`variables`**](start/foundations.md#variables): 
    [`naming`](start/foundations.md#naming-variables) 
    [`printing`](start/foundations.md#printing-variables) 
    [`reassigning`](start/foundations.md#reassigning-a-variable) 
    [`types`](start/foundations.md#variables-and-types) 

    [**`expressions and statements`**](start/foundations.md#expressions-and-statements)

    [**`print`**](start/foundations.md#print-function): 
    [`escape sequences`](start/foundations.md#escape-sequences) 

    [**`input`**](start/foundations.md#input-function)

    [**`comments`**](start/foundations.md#comments): 
    [`"""`](start/foundations.md#multi-line-comments-with) 
    [`#`](start/foundations.md#single-line-comments-with) 
    [`FIXME`](start/foundations.md#single-line-comments-with) 
    [`TODO`](start/foundations.md#single-line-comments-with) 

    [**`tips for getting started`**](start/foundations.md#tips-for-getting-started)

</div>
</div>

<div class="pt-category" markdown="block">
#### Data types { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-shape-outline:{ .lg .middle } [__Basics__](types/basics.md)

    Kinds of values, and what you can do with them.

    [`isinstance`](types/basics.md) 
    [`type`](types/basics.md) 

    [**`integers`**](types/basics.md#integers): 
    [`+ - * / **`](types/basics.md#arithmetic) 
    [`+= -= *= /= //= %= **=`](types/basics.md#apply-arithmetic-to-a-variable) 
    [`// % divmod`](types/basics.md#floor-division-modulo) 
    [`abs`](types/basics.md#absolute-value) 
    [`boolean expressions`](types/basics.md#boolean-expressions) 
    [`int`](types/basics.md#convert) 

    [**`floats`**](types/basics.md#floats): 
    [`+ - * / **`](types/basics.md#arithmetic_1) 
    [`+= -= *= /= //= %= **=`](types/basics.md#apply-arithmetic-to-a-variable_1) 
    [`// % divmod`](types/basics.md#floor-division-modulo_1) 
    [`abs`](types/basics.md#adjust) 
    [`boolean expressions`](types/basics.md#boolean-expressions_1) 
    [`float`](types/basics.md#convert_1) 
    [`round`](types/basics.md#adjust) 

    [**`strings`**](types/basics.md#strings): 
    [`+ * += *=`](types/basics.md#combine) 
    [`boolean expressions`](types/basics.md#boolean-expressions_2) 
    [`capitalize`](types/basics.md#modify) 
    [`combine`](types/basics.md#combine) 
    [`count`](types/basics.md#search) 
    [`endswith`](types/basics.md#validate) 
    [`f-string`](types/basics.md#building-strings) 
    [`find`](types/basics.md#search) 
    [`format`](types/basics.md#building-strings) 
    [`format spec`](types/basics.md#building-strings) 
    [`in`](types/basics.md#search) 
    [`index`](types/basics.md#access-characters) 
    [`isalpha`](types/basics.md#validate) 
    [`isdigit`](types/basics.md#validate) 
    [`join`](types/basics.md#combine) 
    [`len`](types/basics.md#inspect) 
    [`lower`](types/basics.md#modify) 
    [`replace`](types/basics.md#modify) 
    [`slice`](types/basics.md#access-characters) 
    [`split`](types/basics.md#convert_2) 
    [`startswith`](types/basics.md#validate) 
    [`step`](types/basics.md#access-characters) 
    [`str`](types/basics.md#convert_2) 
    [`strip`](types/basics.md#modify) 
    [`title`](types/basics.md#modify) 
    [`upper`](types/basics.md#modify) 

    [**`booleans`**](types/basics.md#booleans): 
    [`== != > < >= <=`](types/basics.md#boolean-expressions_3) 
    [`and`](types/basics.md#logical-operators) 
    [`in`](types/basics.md#boolean-expressions_3) 
    [`is`](types/basics.md#boolean-expressions_3) 
    [`not`](types/basics.md#logical-operators) 
    [`or`](types/basics.md#logical-operators) 

    [**`None`**](types/basics.md#none): 
    [`boolean expressions`](types/basics.md#boolean-expressions_4) 
    [`is`](types/basics.md#check-for-none) 
    [`is not`](types/basics.md#check-for-none) 

-   :material-basket-outline:{ .lg .middle } [__Collections__](types/collections.md)

    Multiple related values grouped into one container.

    [`isinstance`](types/collections.md) 
    [`type`](types/collections.md) 

    [**`lists`**](types/collections.md#lists): 
    [`+`](types/collections.md#create) 
    [`append`](types/collections.md#add-item) 
    [`boolean expressions`](types/collections.md#boolean-expressions) 
    [`clear`](types/collections.md#remove-item) 
    [`comprehension`](types/collections.md#list-comprehension) 
    [`copy`](types/collections.md#create) 
    [`count`](types/collections.md#inspect) 
    [`create`](types/collections.md#create-a-list) 
    [`del`](types/collections.md#remove-item) 
    [`extend`](types/collections.md#add-item) 
    [`in`](types/collections.md#boolean-expressions) 
    [`index`](types/collections.md#create-a-list) 
    [`insert`](types/collections.md#add-item) 
    [`item`](types/collections.md#lists) 
    [`len`](types/collections.md#inspect) 
    [`list`](types/collections.md#create) 
    [`loop`](types/collections.md#loop-through-a-list) 
    [`max`](types/collections.md#arithmetic) 
    [`min`](types/collections.md#arithmetic) 
    [`pop`](types/collections.md#remove-item) 
    [`remove`](types/collections.md#remove-item) 
    [`reverse`](types/collections.md#sort) 
    [`slice`](types/collections.md#access-and-update-items) 
    [`sort`](types/collections.md#sort) 
    [`sorted`](types/collections.md#sort) 
    [`step`](types/collections.md#access-and-update-items) 
    [`sum`](types/collections.md#arithmetic) 

    [**`dictionaries`**](types/collections.md#dictionaries): 
    [`access a value`](types/collections.md#access-a-value) 
    [`boolean expressions`](types/collections.md#boolean-expressions_1) 
    [`clear`](types/collections.md#remove_1) 
    [`copy`](types/collections.md#create_1) 
    [`del`](types/collections.md#remove_1) 
    [`dict`](types/collections.md#create_1) 
    [`get`](types/collections.md#dictionary-operations) 
    [`items`](types/collections.md#loop-through-a-dictionary) 
    [`key`](types/collections.md#dictionaries) 
    [`len`](types/collections.md#inspect_1) 
    [`loop`](types/collections.md#loop-through-a-dictionary) 
    [`pop`](types/collections.md#remove_1) 
    [`popitem`](types/collections.md#remove_1) 
    [`update`](types/collections.md#update_1) 
    [`value`](types/collections.md#dictionaries) 
    [`values`](types/collections.md#loop-through-a-dictionary) 

    [**`tuples`**](types/collections.md#tuples): 
    [`access items`](types/collections.md#access-items) 
    [`boolean expressions`](types/collections.md#boolean-expressions_2) 
    [`count`](types/collections.md#inspect_2) 
    [`immmutable`](types/collections.md#tuples) 
    [`index`](types/collections.md#tuples) 
    [`index`](types/collections.md#inspect_2) 
    [`len`](types/collections.md#inspect_2) 
    [`loop`](types/collections.md#loop-through-a-tuple) 
    [`max`](types/collections.md#arithmetic_1) 
    [`min`](types/collections.md#arithmetic_1) 
    [`packing`](types/collections.md#packing-and-unpacking) 
    [`sum`](types/collections.md#arithmetic_1) 
    [`tuple`](types/collections.md#create_2) 
    [`unpacking`](types/collections.md#packing-and-unpacking) 
    {: data-advanced="true" }

    [**`sets`**](types/collections.md#sets): 
    [`add`](types/collections.md#update_1) 
    [`boolean expressions`](types/collections.md#boolean-expressions_3) 
    [`clear`](types/collections.md#remove_1) 
    [`copy`](types/collections.md#create_3) 
    [`discard`](types/collections.md#remove_1) 
    [`isdisjoint`](types/collections.md#compare) 
    [`issubset`](types/collections.md#compare) 
    [`issuperset`](types/collections.md#compare) 
    [`len`](types/collections.md#inspect_3) 
    [`loop`](types/collections.md#loop-through-a-set) 
    [`max`](types/collections.md#arithmetic_2) 
    [`min`](types/collections.md#arithmetic_2) 
    [`pop`](types/collections.md#remove_1) 
    [`remove`](types/collections.md#remove_1) 
    [`set`](types/collections.md#create_3) 
    [`sum`](types/collections.md#arithmetic_2) 
    [`update`](types/collections.md#update_1) 
    [`| & - ^`](types/collections.md#combine) 
    {: data-advanced="true" }

</div>
</div>

<div class="pt-category" markdown="block">
#### Control flow { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-source-branch:{ .lg .middle } [__Conditionals__](flow/conditionals.md)

    Decision points that run code only if a condition is met.

    [**`if, elif, else`**](flow/conditionals.md#if-elif-else): 
    [`and, or, not`](flow/conditionals.md#logical-operators) 
    [`boolean expressions`](flow/conditionals.md#boolean-expressions) 

    [**`match, case`**](flow/conditionals.md#match-case): 
    [`_ wildcard`](flow/conditionals.md#default-value-_) 
    [`case + if`](flow/conditionals.md#case-if) 
    [`match with |`](flow/conditionals.md#match-multiple-values-with) 
    [`unpacking`](flow/conditionals.md#unpacking-a-tuple) 

    [**`control flow`**](flow/conditionals.md#control-flow-statements): 
    [`break`](flow/conditionals.md#break) 
    [`continue`](flow/conditionals.md#continue) 
    [`pass`](flow/conditionals.md#going-further_2) 

-   :material-repeat:{ .lg .middle } [__Loops__](flow/loops.md)

    Repeat a block of code multiple times.

    [**`for`**](flow/loops.md#for-loops): 
    [`enumerate`](flow/loops.md#loop-with-index-and-value) 
    [`loop a set number of times`](flow/loops.md#loop-a-certain-number-of-times) 
    [`loop through a collection`](flow/loops.md#loop-through-a-collection) 
    [`range`](flow/loops.md#iterable-range) 
    [`reversed`](flow/loops.md#loop-in-reverse) 
    [`zip`](flow/loops.md#loop-with-index-and-value) 

    [**`while`**](flow/loops.md#while-loops): 
    [`and`](flow/loops.md#logical-operators) 
    [`boolean expressions`](flow/loops.md#boolean-expressions) 
    [`counter and flag names`](flow/loops.md#counter-and-flag-names) 
    [`flag`](flow/loops.md#using-a-flag) 
    [`not`](flow/loops.md#logical-operators) 
    [`or`](flow/loops.md#logical-operators) 
    [`sentinel`](flow/loops.md#sentinel) 

    [**`common patterns`**](flow/loops.md#common-patterns): 
    [`accumulator`](flow/loops.md#accumulator) 
    [`counter`](flow/loops.md#counter) 
    [`nested loops`](flow/loops.md#nested-loops) 

    [**`control flow`**](flow/loops.md#control-flow-statements): 
    [`break`](flow/loops.md#break) 
    [`continue`](flow/loops.md#continue) 
    [`else`](flow/loops.md#else) 
    [`pass`](flow/loops.md#going-further_2) 


</div>
</div>

<div class="pt-category" markdown="block">
#### Organization { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-function-variant:{ .lg .middle } [__Functions__](organization/functions.md)

    Package a named block of code to run it at any time.

    [**`def`**](organization/functions.md#defining-a-function): 
    [`**kwargs`](organization/functions.md#kwargs-dict) 
    [`*args`](organization/functions.md#args-tuple) 
    [`defaults`](organization/functions.md#default-values) 
    [`docstrings`](organization/functions.md#docstrings) 
    [`parameters`](organization/functions.md#parameters) 
    [`pass`](organization/functions.md#pass-placeholder) 
    [`return`](organization/functions.md#return-values) 

    [`combining argument types`](organization/functions.md#combining-categories) 
    [`keyword-only`](organization/functions.md#keyword-only) 
    [`positional-only`](organization/functions.md#positional-only) 
    [`type hints`](organization/functions.md#type-hints) 
    {: data-advanced="true" }

    [**`calling a function`**](organization/functions.md#calling-a-function): 
    [`arguments`](organization/functions.md#arguments) 
    [`keyword`](organization/functions.md#by-keyword) 
    [`required`](organization/functions.md#required) 
    [`return value`](organization/functions.md#saving-the-return-value) 
    [`unpacking`](organization/functions.md#unpacking) 

    [**`scope`**](organization/functions.md#scope): 
    [`local vs global`](organization/functions.md#local-vs-global-variables) 

    [**`recursion`**](organization/functions.md#recursion)
    {: data-advanced="true" }

    [**`decorators`**](organization/functions.md#decorators): 
    [`arguments`](organization/functions.md#accepting-arguments) 
    [`identity`](organization/functions.md#advanced-uses) 
    [`original function`](organization/functions.md#returning-the-original-function) 
    [`stacking`](organization/functions.md#advanced-uses) 
    [`wrapping`](organization/functions.md#wrapping-the-call)
    {: data-advanced="true" }

    [**`generators`**](organization/functions.md#generators): 
    [`generator expressions`](organization/functions.md#generator-expressions)
    [`memory`](organization/functions.md#memory-efficiency) 
    [`yield`](organization/functions.md#yield-vs-return) 
    {: data-advanced="true" }

-   :material-package-variant:{ .lg .middle } [__Classes__](organization/classes.md)

    Bundle related values and functions to a reusable blueprint for similar objects.

    [**`class`**](organization/classes.md#defining-a-class): 
    [`__init__()`](organization/classes.md#the-__init__-method) 
    [`class attributes`](organization/classes.md#class-attributes) 
    [`instance attributes`](organization/classes.md#instance-attributes) 
    [`methods`](organization/classes.md#object-methods) 
    [`self`](organization/classes.md#the-self-parameter) 

    [**`method decorators`**](organization/classes.md#method-decorators): 
    [`@classmethod`](organization/classes.md#classmethod) 
    [`@property`](organization/classes.md#property) 
    [`@staticmethod`](organization/classes.md#staticmethod) 
    {: data-advanced="true" }

    [**`inheritance`**](organization/classes.md#inheritance): 
    [`adding attributes and methods`](organization/classes.md#adding-attributes-and-methods) 
    [`__init__()`](organization/classes.md#overriding-__init__) 
    [`overriding`](organization/classes.md#overriding-methods) 
    [`super()`](organization/classes.md#using-super) 

    [`multiple inheritance`](organization/classes.md#multiple-inheritance) 
    {: data-advanced="true" }

    [**`polymorphism`**](organization/classes.md#polymorphism): 
    [`inheritance`](organization/classes.md#polymorphism-via-inheritance) 
    [`duplicate method names`](organization/classes.md#duplicate-method-names) 
    {: data-advanced="true" }

    [**`encapsulation`**](organization/classes.md#encapsulation): 
    [`@property`](organization/classes.md#controlled-access-with-property) 
    [`double underscore`](organization/classes.md#double-underscore) 
    [`single underscore`](organization/classes.md#single-underscore) 
    {: data-advanced="true" }

    [**`operator overloading`**](organization/classes.md#operator-overloading): 
    [`__add__`](organization/classes.md#arithmetic-with-__add__) 
    [`__eq__ and __lt__`](organization/classes.md#comparing-with-__eq__-and-__lt__) 
    {: data-advanced="true" }

    [**`dataclasses`**](organization/classes.md#dataclasses)
    {: data-advanced="true" }

    [**`abstract base classes`**](organization/classes.md#abstract-base-classes)
    {: data-advanced="true" }

</div>
</div>

<div class="pt-category" markdown="block">
#### External files and resources { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-import:{ .lg .middle } [__Modules & Imports__](resources/modules.md)

    Splitting code across files, and using someone else's code.

    [**`import`**](resources/modules.md#importing-modules): 
    [`as`](resources/modules.md#as) 
    [`from`](resources/modules.md#from) 
    [`import`](resources/modules.md#import) 
    [`import order`](resources/modules.md#order-of-multiple-imports) 
    [`nested paths`](resources/modules.md#nested-paths) 
    [`packages`](resources/modules.md#packages) 

    [**`your own module`**](resources/modules.md#creating-your-own-module): 
    [`main guard`](resources/modules.md#the-main-guard) 

    [**`module, package, library`**](resources/modules.md#modules-vs-packages-vs-libraries)

-   :material-file-document-outline:{ .lg .middle } [__Reading & Writing Files__](resources/files.md)

    Read and write text files on your computer.

    [**`open`**](resources/files.md#opening-and-closing-files): 
    [`modes`](resources/files.md#modes-options) 
    [`paths`](resources/files.md#file-paths) 
    [`with`](resources/files.md#with)

    [**`read()`**](resources/files.md#read): 
    [`existing`](resources/files.md#r-read-existing) 
    [`functions`](resources/files.md#functions) 
    [`modes`](resources/files.md#modes) 
    [`read()`](resources/files.md#whole-file) 
    [`readline()`](resources/files.md#by-line) 
    [`readlines()`](resources/files.md#by-line) 
    [`seek()`](resources/files.md#seek-and-tell) 
    [`tell()`](resources/files.md#seek-and-tell)

    [**`write()`**](resources/files.md#write): 
    [`append`](resources/files.md#a-append) 
    [`create`](resources/files.md#x-create) 
    [`functions`](resources/files.md#functions_1) 
    [`modes`](resources/files.md#modes_1) 
    [`overwrite`](resources/files.md#w-overwrite) 
    [`write()`](resources/files.md#single-string) 
    [`writelines()`](resources/files.md#multiple-strings)

    [**`related libraries`**](resources/files.md#related-libraries)

</div>
</div>

<div class="pt-category" markdown="block">
#### Robust programming practices { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-palette-outline:{ .lg .middle } [__Style__](practices/style.md)

    Readable Python code, and polished UI.

    [**`PEP 8`**](practices/style.md#pep-8-style-guide): 
    [`blank lines`](practices/style.md#blank-lines) 
    [`docstrings`](practices/style.md#docstrings) 
    [`naming`](practices/style.md#naming) 
    [`whitespace`](practices/style.md#whitespace) 

    [`comments`](practices/style.md#comments) 
    [`constants`](practices/style.md#constants) 
    [`indentation`](practices/style.md#indentation) 
    [`order`](practices/style.md#file-order) 
    [`quote style`](practices/style.md#quote-style) 
    {: data-advanced="true" }

    [**`Linters, formatters`**](practices/style.md#linters-and-formatters)

    [**`Pythonic patterns`**](practices/style.md#pythonic-patterns): 
    [`mutable defaults`](practices/style.md#mutable-default-arguments)
    [`is None`](practices/style.md#is-none-instead-of-none)

    [`truthy checks`](practices/style.md#truthy-checks) 
    [`enumerate()`](practices/style.md#enumerate-instead-of-range) 
    {: data-advanced="true" }

    [**`Efficiency`**](practices/style.md#efficiency)
    [`big O`](practices/style.md#big-o-notation)
    [`common optimizations`](practices/style.md#common-optimizations)
    [`time`](practices/style.md#time-and-space) 
    [`space`](practices/style.md#time-and-space)
    {: data-advanced="true" }

    [**`Polished UX`**](practices/style.md#polished-ux): 
    [`input validation`](practices/style.md#input-validation) 
    [`menus`](practices/style.md#menus) 
    [`randomize`](practices/style.md#randomize-messages)

    [**`Polished UI`**](practices/style.md#polished-ui): 
    [`background`](practices/style.md#color-styling) 
    [`bold`](practices/style.md#color-styling) 
    [`escape sequences`](practices/style.md#escape-sequences) 
    [`color`](practices/style.md#color-styling) 
    [`highlighting`](practices/style.md#color-styling) 
    [`multi-line strings`](practices/style.md#multi-line-strings) 
    [`formatting variables`](practices/style.md#formatting-variables) 
    [`underline`](practices/style.md#color-styling) 
    [`unicode symbols`](practices/style.md#unicode-symbols) 
    [`dividers`](practices/style.md#dividers) 
    [`boxes`](practices/style.md#boxes) 
    [`progress bars`](practices/style.md#progress-bars)

-   :material-bug-outline:{ .lg .middle } [__Errors__](practices/errors.md)

    Resolve bugs, read and utilize exceptions.

    [**`kinds`**](practices/errors.md#kinds-of-errors): 
    [`bugs`](practices/errors.md) 
    [`exceptions`](practices/errors.md) 
    [`logic errors`](practices/errors.md#logic-errors) 
    [`runtime errors`](practices/errors.md#runtime-errors) 
    [`syntax errors`](practices/errors.md#syntax-errors) 

    [**`fixing`**](practices/errors.md#fixing-errors): 
    [`debugger tool`](practices/errors.md#debugger-tool) 
    [`debugging strategies`](practices/errors.md#debugging-strategies) 
    [`isolate problems`](practices/errors.md#isolate-the-problem) 
    [`print debugging`](practices/errors.md#print-debugging) 
    [`rubber duck debugging`](practices/errors.md#read-it-out-loud) 
    [`syntax error message`](practices/errors.md#reading-a-syntax-error-message) 
    [`testing`](practices/errors.md#detect-errors-with-testing) 
    [`TODO / FIXME`](practices/errors.md#flag-as-todofixme) 
    [`tracebacks`](practices/errors.md#reading-a-traceback) 

    [**`handling`**](practices/errors.md#handling-errors): 
    [`assert`](practices/errors.md#assert-a-condition) 
    [`else`](practices/errors.md#finally) 
    [`finally`](practices/errors.md#finally) 
    [`raise`](practices/errors.md#raise-an-exception) 
    [`try/except`](practices/errors.md#catch-with-tryexcept) 

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
