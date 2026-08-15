---
description: >-
  Reading and writing CSV files in Python with the csv module: csv.writer, csv.reader,
  and DictReader, with runnable examples.
---

# :material-file-delimited-outline:{ .lg .middle } csv library

The **`csv`** module reads and writes CSV ("comma-separated values") files — a plain-text table format that spreadsheets and databases can both open. Every example below actually runs in your browser: Pyodide gives each page its own in-memory filesystem, so `open()` works exactly like it would on a real computer, just without anything being saved outside this page.

## Install

`csv` ships with Python's standard library — nothing to install.

## Import

The whole module is used through the `csv.` prefix, so a plain import is all you need.

```python-ref
import csv
```

| Tool | Reads/writes rows as | Use it for |
|------|----------------------|------------|
| `csv.writer` | A list per row | Writing plain rows of values |
| `csv.reader` | A list per row | Reading plain rows of values |
| `csv.DictWriter` | A dict per row | Writing rows keyed by column name |
| `csv.DictReader` | A dict per row | Reading rows keyed by column name |

## Writing CSV files

`csv.writer` wraps an open file and turns each list you pass to `.writerow()` into one comma-separated line.

```python-ref
import csv

with open("snakes.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["species", "length_ft"])
    writer.writerow(["ball", 4.5])
    writer.writerow(["burmese", 12])

print("wrote snakes.csv")
```

??? tip "Writing multiple rows at once"
    Takes a list of rows and writes them all in one call — `.writerows()`, instead of looping over `.writerow()` yourself.

    ```python-ref
    rows = [["ball", 4.5], ["burmese", 12], ["boa", 8]]
    writer.writerows(rows)
    ```

??? run "Run a writing CSV example"
    All the examples above, combined into one script:

    ```python
    import csv

    with open("snakes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["species", "length_ft"])
        writer.writerow(["ball", 4.5])
        writer.writerow(["burmese", 12])

    print("wrote snakes.csv")

    import csv

    rows = [["ball", 4.5], ["burmese", 12], ["boa", 8]]

    with open("snakes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["species", "length_ft"])
        writer.writerows(rows)
    ```

## Reading CSV files

`csv.reader` gives back each row as a plain list of strings — including the header row, which is usually skipped over explicitly.

```python-ref
import csv

with open("snakes.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["species", "length_ft"])
    writer.writerow(["ball", 4.5])
    writer.writerow(["burmese", 12])

with open("snakes.csv", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        print(row)
```

### Reading rows as dictionaries

Uses the first row as column names automatically, so each row comes back as a `dict`. You can look up values by column name instead of by position. Every value is still read as a plain string — convert it (e.g. with `float()`) if you need to do math on it.

```python-ref
for row in csv.DictReader(file):
    row["species"]      # "ball"
    row["length_ft"]    # "4.5" — still a string, not a float
```

??? run "Run a reading CSV example"
    All the examples above, combined into one script:

    ```python
    import csv

    with open("snakes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["species", "length_ft"])
        writer.writerow(["ball", 4.5])
        writer.writerow(["burmese", 12])

    with open("snakes.csv", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            print(row)

    import csv

    with open("snakes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["species", "length_ft"])
        writer.writerow(["ball", 4.5])
        writer.writerow(["burmese", 12])

    with open("snakes.csv", newline="") as file:
        for row in csv.DictReader(file):
            print(row["species"], float(row["length_ft"]))
    ```
