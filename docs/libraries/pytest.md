---
description: >-
  Writing and running tests in Python with pytest: assertions, fixtures, parametrizing,
  and testing for exceptions, with runnable examples.
---

# :material-test-tube:{ .lg .middle } pytest library

<div class="pfg-section" markdown="block">

[pytest documentation :material-open-in-new:](https://docs.pytest.org/en/stable/){ .md-button target="_blank" }

pytest is an open-source project maintained by volunteer contributors.

**pytest** is Python's most widely used testing framework — it finds test functions in a project, runs each one, and reports which passed or failed. It's a third-party package, not part of the standard library, but it's largely replaced the built-in `unittest` module for new projects because a test is just a function with a plain `assert` statement, instead of a class built on a special base and assert methods like `.assertEqual()`. Every example below actually runs in your browser: Pyodide gives each page its own in-memory filesystem, so writing a test file and pointing pytest at it works the same way it would on a real computer.

</div>

<div class="pfg-section" markdown="block">

## Setup { data-card-link="skip" }

```bash
pip install pytest
```

Most of what pytest does — discovering `test_*` functions and checking plain `assert` statements — needs no import at all. A plain `import pytest` is only needed for its extra tools: fixtures, marks, and `pytest.raises`.

```python-ref
import pytest
```

| Concept | What it is |
|---------|------------|
| Test file | A file named `test_*.py` (or `*_test.py`) that pytest scans for tests |
| Test function | A function named `test_*` inside a test file — each one is a single check |
| Assertion | A plain `assert` statement — pytest reports exactly what failed, no special method needed |
| Fixture | Reusable setup code, shared across test functions with `@pytest.fixture` |
| Marker | A tag like `@pytest.mark.parametrize`, attached to a test to change how it runs |

</div>

<div class="pfg-section" markdown="block">

## Writing and running a test

A pytest test is an ordinary function, named `test_...`, that makes one or more `assert` statements about the code it's checking. No import, base class, or naming beyond the `test_` prefix is required.

```python-ref
def test_species_count():
    species = ["ball", "burmese", "boa"]
    assert len(species) == 3
```

### From the command line

Normally you run `pytest` (or `python -m pytest`) from a terminal in the project directory, and it discovers every `test_*.py` file on its own — no need to name each one. This page's sandbox has no terminal, so the examples below call `pytest.main()` directly instead, which does the same discovery-and-run programmatically.

```python-ref
import pytest

pytest.main(["-v", "test_snakes.py"])
```

??? run "Run a writing and running tests example"
    All the examples above, combined into one script:

    ```python
    import pytest

    with open("test_snakes.py", "w") as file:
        file.write(
            "def test_species_count():\n"
            "    species = [\"ball\", \"burmese\", \"boa\"]\n"
            "    assert len(species) == 3\n"
        )

    pytest.main(["-v", "test_snakes.py"])
    ```

</div>

<div class="pfg-section" markdown="block">

## Reading a failure

When an `assert` fails, pytest rewrites it behind the scenes to show the actual values it compared, not just that the statement was false — so a failure report reads like a diff, not a generic error.

```python-ref
def test_species_count():
    species = ["ball", "burmese"]
    assert len(species) == 3    # AssertionError: assert 2 == 3
```

??? note "Why plain assert is enough"
    Older frameworks like `unittest` need special methods (`.assertEqual()`, `.assertTrue()`, ...) because a bare `assert` normally only reports `AssertionError`, with no detail about *why*. pytest rewrites `assert` statements in test files at import time to capture each operand, so a plain `assert a == b` already shows both values on failure — no special method vocabulary to learn.

??? run "Run a failing test example"
    ```python
    import pytest

    with open("test_snakes.py", "w") as file:
        file.write(
            "def test_species_count():\n"
            "    species = [\"ball\", \"burmese\"]\n"
            "    assert len(species) == 3\n"
        )

    pytest.main(["-v", "test_snakes.py"])
    ```

</div>

<div class="pfg-section" markdown="block">

## Fixtures

A **fixture** is a function decorated with `@pytest.fixture` that builds some setup data once; any test function that names it as a parameter receives its return value automatically, without calling it directly.

```python-ref
@pytest.fixture
def snake():
    return {"species": "burmese python", "length_ft": 12, "venomous": False}

def test_snake_not_venomous(snake):
    assert snake["venomous"] is False
```

??? run "Run a fixtures example"
    ```python
    import pytest

    with open("test_snakes.py", "w") as file:
        file.write(
            "import pytest\n"
            "\n"
            "@pytest.fixture\n"
            "def snake():\n"
            "    return {\"species\": \"burmese python\", \"length_ft\": 12, \"venomous\": False}\n"
            "\n"
            "def test_snake_not_venomous(snake):\n"
            "    assert snake[\"venomous\"] is False\n"
        )

    pytest.main(["-v", "test_snakes.py"])
    ```

</div>

<div class="pfg-section" markdown="block">

## Parametrizing tests

`@pytest.mark.parametrize` runs the same test function once per row of arguments, instead of copy-pasting a near-identical test for every case.

```python-ref
@pytest.mark.parametrize("species,length_ft", [
    ("ball", 4.5),
    ("burmese", 12),
    ("boa", 8),
])
def test_length_is_positive(species, length_ft):
    assert length_ft > 0
```

??? run "Run a parametrize example"
    ```python
    import pytest

    with open("test_snakes.py", "w") as file:
        file.write(
            "import pytest\n"
            "\n"
            "@pytest.mark.parametrize(\"species,length_ft\", [\n"
            "    (\"ball\", 4.5),\n"
            "    (\"burmese\", 12),\n"
            "    (\"boa\", 8),\n"
            "])\n"
            "def test_length_is_positive(species, length_ft):\n"
            "    assert length_ft > 0\n"
        )

    pytest.main(["-v", "test_snakes.py"])
    ```

</div>

<div class="pfg-section" markdown="block">

## Testing for exceptions

`pytest.raises()` is a context manager that asserts the code inside its `with` block raises a specific exception — a way to test the [`try`/`except`](../errors.md#catch-with-tryexcept) paths in your own code, not just the successful ones.

```python-ref
def test_invalid_length_raises():
    with pytest.raises(ValueError):
        float("not a number")
```

??? run "Run a testing for exceptions example"
    ```python
    import pytest

    with open("test_snakes.py", "w") as file:
        file.write(
            "import pytest\n"
            "\n"
            "def test_invalid_length_raises():\n"
            "    with pytest.raises(ValueError):\n"
            "        float(\"not a number\")\n"
        )

    pytest.main(["-v", "test_snakes.py"])
    ```

</div>
