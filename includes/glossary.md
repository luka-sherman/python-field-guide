*[exception]: Python's formal term for the type of error that was raised, like KeyError or ValueError
*[Exception]: Python's formal term for the type of error that was raised, like KeyError or ValueError
*[expensive]: Takes a relatively long time or a lot of memory to run — not about money
*[Expensive]: Takes a relatively long time or a lot of memory to run — not about money
*[constructor]: The method that runs automatically to set up a new object's starting values
*[Constructor]: The method that runs automatically to set up a new object's starting values
*[object]: A specific thing built from a class, with its own independent copy of that class's data
*[Object]: A specific thing built from a class, with its own independent copy of that class's data
*[instance]: Another word for an object — a specific thing built from a class, with its own independent copy of that class's data
*[Instance]: Another word for an object — a specific thing built from a class, with its own independent copy of that class's data
*[boolean mask]: A same-size array of True/False values, used to filter another array or column down to just the matching rows
*[Boolean mask]: A same-size array of True/False values, used to filter another array or column down to just the matching rows
*[iterable]: Anything that can hand back its items one at a time — a list, string, range, dict, and more — whether you're looping over it, converting it, or unpacking it
*[Iterable]: Anything that can hand back its items one at a time — a list, string, range, dict, and more — whether you're looping over it, converting it, or unpacking it
*[traceback]: The error report Python prints when your code crashes, showing where and why
*[Traceback]: The error report Python prints when your code crashes, showing where and why
*[docstring]: A triple-quoted string as the first line of a function or class, documenting what it does
*[Docstring]: A triple-quoted string as the first line of a function or class, documenting what it does
*[subclass]: A class that inherits from another class, reusing (and optionally overriding) its attributes and methods
*[Subclass]: A class that inherits from another class, reusing (and optionally overriding) its attributes and methods
*[mutable]: Can be changed in place after creation, without needing to build a new one
*[Mutable]: Can be changed in place after creation, without needing to build a new one
*[immutable]: Cannot be changed after creation — any "change" actually builds a brand new value
*[Immutable]: Cannot be changed after creation — any "change" actually builds a brand new value
*[block]: A group of indented lines under a colon that Python runs together as one unit — the body of an if, loop, function, or class
*[Block]: A group of indented lines under a colon that Python runs together as one unit — the body of an if, loop, function, or class
*[convention]: An agreed-upon way of doing something that Python doesn't enforce, followed anyway so code stays predictable to other readers
*[Convention]: An agreed-upon way of doing something that Python doesn't enforce, followed anyway so code stays predictable to other readers
*[conventionally]: By convention — an agreed-upon way of doing something that Python doesn't enforce, followed anyway so code stays predictable to other readers
*[Conventionally]: By convention — an agreed-upon way of doing something that Python doesn't enforce, followed anyway so code stays predictable to other readers
*[truthy]: Counts as True when used somewhere a bool is expected, even though the value itself isn't actually True — every value is either truthy or falsy
*[Truthy]: Counts as True when used somewhere a bool is expected, even though the value itself isn't actually True — every value is either truthy or falsy
*[falsy]: Counts as False when used somewhere a bool is expected, even though the value itself isn't actually False — every value is either truthy or falsy
*[Falsy]: Counts as False when used somewhere a bool is expected, even though the value itself isn't actually False — every value is either truthy or falsy
*[Pythonic]: Using Python's own built-in features and idioms, instead of a hand-rolled equivalent that reads like it was translated from another language
*[buffer]: A temporary holding area in memory where written data sits before it's actually flushed to the file on disk
*[Buffer]: A temporary holding area in memory where written data sits before it's actually flushed to the file on disk
*[view object]: A window onto a dictionary's keys, values, or items — loop over it as is or wrap it in list() if you need to work with it
*[View object]: A window onto a dictionary's keys, values, or items — loop over it as is or wrap it in list() if you need to work with it
*[packing]: Writing several values separated by commas, which implicitly builds a tuple — what's actually happening whenever you write a tuple literal
*[Packing]: Writing several values separated by commas, which implicitly builds a tuple — what's actually happening whenever you write a tuple literal
*[unpacking]: Assigning each item in a tuple (or other iterable) to its own variable in one line, one name per item
*[Unpacking]: Assigning each item in a tuple (or other iterable) to its own variable in one line, one name per item
*[augmented assignment]: Combines an operation with reassignment in one step — count += 1 is shorthand for count = count + 1
*[Augmented assignment]: Combines an operation with reassignment in one step — count += 1 is shorthand for count = count + 1
*[compile]: Translate source code into machine instructions ahead of time, as a separate step before the program runs — Python doesn't need this because it instead reads and runs code directly, line by line
*[Compile]: Translate source code into machine instructions ahead of time, as a separate step before the program runs — Python doesn't need this because it instead reads and runs code directly, line by line
*[compiling]: Translating source code into machine instructions ahead of time, as a separate step before the program runs — Python doesn't need this because it instead reads and runs code directly, line by line
*[Compiling]: Translating source code into machine instructions ahead of time, as a separate step before the program runs — Python doesn't need this because it instead reads and runs code directly, line by line
*[truthiness]: Whether a value counts as True or False when used somewhere a bool is expected, even if it isn't a bool itself
*[Truthiness]: Whether a value counts as True or False when used somewhere a bool is expected, even if it isn't a bool itself
*[hashable]: Can be used as a dict key or set member because it never changes after creation — most immutable types qualify, like int, float, str, bool, None, and tuple
*[Hashable]: Can be used as a dict key or set member because it never changes after creation — most immutable types qualify, like int, float, str, bool, None, and tuple
*[queue]: A line of items processed in the order they arrive — the first one added is the first one handled
*[Queue]: A line of items processed in the order they arrive — the first one added is the first one handled
*[bug]: A mistake in your code that makes it do the wrong thing, whether or not Python actually notices and raises an error
*[Bug]: A mistake in your code that makes it do the wrong thing, whether or not Python actually notices and raises an error
*[syntax]: The grammatical rules for what counts as validly structured code, checked before any of it runs — independent of whether the logic is actually correct
*[Syntax]: The grammatical rules for what counts as validly structured code, checked before any of it runs — independent of whether the logic is actually correct
*[callable]: Can be called with parentheses to run it, the way a function can — includes functions, classes, and any object with a __call__ method
*[Callable]: Can be called with parentheses to run it, the way a function can — includes functions, classes, and any object with a __call__ method
*[graceful]: Handling a failure without crashing or losing data — continuing on, showing a clear message, or falling back to a default instead of stopping abruptly
*[Graceful]: Handling a failure without crashing or losing data — continuing on, showing a clear message, or falling back to a default instead of stopping abruptly
*[gracefully]: In a way that handles a failure without crashing or losing data — continuing on, showing a clear message, or falling back to a default instead of stopping abruptly
*[Gracefully]: In a way that handles a failure without crashing or losing data — continuing on, showing a clear message, or falling back to a default instead of stopping abruptly
*[lazy]: Computing or producing a value only at the moment it's actually needed, instead of all at once ahead of time
*[Lazy]: Computing or producing a value only at the moment it's actually needed, instead of all at once ahead of time
*[lazily]: In a way that computes or produces a value only at the moment it's actually needed, instead of all at once ahead of time
*[Lazily]: In a way that computes or produces a value only at the moment it's actually needed, instead of all at once ahead of time
*[PascalCase]: Capitalizing each word with no separators (e.g. Snake, BallPython) — the naming convention for classes, unlike variables' snake_case
*[UTF-8]: The encoding used to save a Python file by default — the scheme that turns each Unicode character into the actual bytes a computer stores and reads, and it can represent every character Unicode defines
