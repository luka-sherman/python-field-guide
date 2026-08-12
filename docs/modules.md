# :material-import:{ .lg .middle } Modules & Imports

A **module** is just a Python file — any `.py` file can be imported into another one, the same way `import random` pulls in code someone else already wrote. As a project grows past a single script, splitting related functions and classes into their own files, then importing between them, keeps any one file from becoming unmanageable.

## Importing libraries

`import` makes a module's code available under its own name, so you call things through it with a `.` — `random.randint(...)`, not just `randint(...)`.

```python-ref
import random

print(random.randint(1, 10))
```

Imports go at the very top of the file, grouped in order: Python's own standard library first, then third-party packages, then your own local files — with a blank line between each group.

```python-ref
import random                    # standard library

import requests                  # third-party — installed separately

import snake_data                # your own file
```

??? tip "Avoid `from module import *`"
    Pulls in every name from that module without saying which ones, so it's unclear later where a given name actually came from — `randint` on its own gives no hint it came from `random` rather than somewhere else in the file.

    ```python-ref
    from random import *
    randint(1, 10)    # works, but where did randint come from?
    ```

??? run "Run an import example"
    All the examples above, combined into one script:

    ```python
    import random

    print(random.randint(1, 10))
    ```

## Creating your own module

Importing from your own file works exactly like importing a library: use the filename, without `.py`, as the module name.

```python-ref
# snake_helpers.py

def describe(species):
    return f"a {species} python"
```

```python-ref
# main.py

from snake_helpers import describe

print(describe("ball"))
```

The imported file has to sit in the same folder as the one importing it (or be installed like a real package). This is also why avoiding a library's name for your own file matters — covered in the [naming rules](foundations.md#naming-variables) on the Foundations page: a file named `random.py` shadows Python's own `random` module for anything else in that project.

## The main guard

`if __name__ == "__main__":` controls what runs only when a file is executed directly — not when it's imported into another file.

```python-ref
def describe(species):
    return f"a {species} python"

if __name__ == "__main__":
    print(describe("ball"))
```

`__name__` is a variable Python sets automatically: `"__main__"` when the file is run directly, or the file's own module name when it's imported elsewhere instead. Wrapping your "do the actual work" code in this check means another file can `import` yours — to reuse a function, say — without that code running as a side effect. Covered again, as one piece of a whole file's conventional layout, on the [Style](style.md#order) page.

??? run "Run a main guard example"
    All the examples above, combined into one script:

    ```python
    def describe(species):
        return f"a {species} python"

    if __name__ == "__main__":
        print(describe("ball"))
    ```
