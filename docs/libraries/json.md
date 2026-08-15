---
description: >-
  Reading and writing JSON data in Python with the json module: json.load, json.dump, and
  working with nested data, with runnable examples.
---

# :material-code-json:{ .lg .middle } json library

The **`json`** module reads and writes JSON ("JavaScript Object Notation") data — a plain-text format built on nested dicts and lists, which makes it the standard way structured data moves between programs, files, and web APIs. Every example below actually runs in your browser: Pyodide gives each page its own in-memory filesystem, so `open()` works exactly like it would on a real computer, just without anything being saved outside this page.

## Install

`json` ships with Python's standard library — nothing to install.

## Import

The whole module is used through the `json.` prefix, so a plain import is all you need.

```python-ref
import json
```

| Tool | Converts | Use it for |
|------|----------|------------|
| `json.dump()` | A Python object → an open file | Saving data to disk |
| `json.load()` | An open file → a Python object | Loading data from disk |
| `json.dumps()` | A Python object → a string | Sending data somewhere, like an API request body |
| `json.loads()` | A string → a Python object | Parsing JSON text you already have in memory |

## Writing JSON files

`json.dump()` writes a Python object straight to an open file — a `dict` becomes a JSON object, a `list` becomes a JSON array, automatically.

```python-ref
import json

snake = {"species": "ball", "length_ft": 4.5, "venomous": False}

with open("snake.json", "w") as file:
    json.dump(snake, file)

print("wrote snake.json")
```

??? tip "Pretty-printing with indent"
    `json.dump()` writes everything on one line by default. Pass `indent=` to spread it across multiple, readable lines instead — handy when you'll open the file yourself later.

    ```python-ref
    with open("snake.json", "w") as file:
        json.dump(snake, file, indent=2)
    ```

??? run "Run a writing JSON example"
    All the examples above, combined into one script:

    ```python
    import json

    snake = {"species": "ball", "length_ft": 4.5, "venomous": False}

    with open("snake.json", "w") as file:
        json.dump(snake, file)

    print("wrote snake.json")

    with open("snake.json", "w") as file:
        json.dump(snake, file, indent=2)
    ```

## Reading JSON files

`json.load()` reads a file and reconstructs the original Python object — a JSON object comes back as a `dict`, a JSON array comes back as a `list`, with numbers and booleans already converted to `int`/`float`/`bool` instead of strings.

```python-ref
import json

with open("snake.json") as file:
    data = json.load(file)

print(data["species"])
print(data["length_ft"])
```

### Nested data

Unlike a [CSV file](csv.md), which is strictly flat rows and columns, JSON can nest a list or another object inside a value — so one record can hold something like a snake's full sighting history, not just single values per column.

```python-ref
snake = {
    "species": "ball",
    "length_ft": 4.5,
    "sightings": ["2024-03-15", "2024-06-02"]
}

with open("snake.json", "w") as file:
    json.dump(snake, file)

with open("snake.json") as file:
    data = json.load(file)

print(data["sightings"][0])    # "2024-03-15"
```

??? run "Run a reading JSON example"
    All the examples above, combined into one script:

    ```python
    import json

    snake = {"species": "ball", "length_ft": 4.5, "venomous": False}

    with open("snake.json", "w") as file:
        json.dump(snake, file)

    with open("snake.json") as file:
        data = json.load(file)

    print(data["species"])
    print(data["length_ft"])

    snake = {
        "species": "ball",
        "length_ft": 4.5,
        "sightings": ["2024-03-15", "2024-06-02"]
    }

    with open("snake.json", "w") as file:
        json.dump(snake, file)

    with open("snake.json") as file:
        data = json.load(file)

    print(data["sightings"][0])
    ```

## Working with strings instead of files

`json.dumps()`/`json.loads()` do the same conversion as `dump()`/`load()`, but to and from a string in memory rather than a file — the pair to reach for when the JSON is coming from somewhere other than disk, like an API response. The [`requests`](requests.md) library's own `.json()` method — covered on that page — is really just calling `json.loads()` on the response text for you.

```python-ref
import json

snake = {"species": "ball", "length_ft": 4.5}

text = json.dumps(snake)    # '{"species": "ball", "length_ft": 4.5}'
data = json.loads(text)     # back to {"species": "ball", "length_ft": 4.5}
```

??? run "Run a strings example"
    All the examples above, combined into one script:

    ```python
    import json

    snake = {"species": "ball", "length_ft": 4.5}

    text = json.dumps(snake)
    print(text)

    data = json.loads(text)
    print(data)
    ```
