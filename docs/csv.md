# csv

The **`csv`** module reads and writes CSV ("comma-separated values") files — a plain-text table format that spreadsheets and databases can both open. It ships with Python, so no install is needed. Every example below actually runs in your browser: Pyodide gives each page its own in-memory filesystem, so `open()` works exactly like it would on a real computer, just without anything being saved outside this page.

| Tool | Reads/writes rows as | Use it for |
|------|----------------------|------------|
| `csv.writer` | A list per row | Writing plain rows of values |
| `csv.reader` | A list per row | Reading plain rows of values |
| `csv.DictWriter` | A dict per row | Writing rows keyed by column name |
| `csv.DictReader` | A dict per row | Reading rows keyed by column name |

## Writing CSV files

`csv.writer` wraps an open file and turns each list you pass to `.writerow()` into one comma-separated line.

```python
import csv

with open("snakes.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["species", "length_ft"])
    writer.writerow(["ball", 4.5])
    writer.writerow(["burmese", 12])

print("wrote snakes.csv")
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Writing multiple rows at once

Takes a list of rows and writes them all in one call.
{: .pt-subheading }

```python-ref
rows = [["ball", 4.5], ["burmese", 12], ["boa", 8]]
writer.writerows(rows)
```

</summary>

`.writerows()`, instead of looping over `.writerow()` yourself.

```python
import csv

rows = [["ball", 4.5], ["burmese", 12], ["boa", 8]]

with open("snakes.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["species", "length_ft"])
    writer.writerows(rows)
```

</details>

## Reading CSV files

`csv.reader` gives back each row as a plain list of strings — including the header row, which is usually skipped over explicitly.

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
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Reading rows as dictionaries

Uses the first row as column names automatically, so each row comes back as a `dict`.
{: .pt-subheading }

```python-ref
for row in csv.DictReader(file):
    row["species"]      # "ball"
    row["length_ft"]    # "4.5" — still a string, not a float
```

</summary>

You can look up values by column name instead of by position. Every value is still read as a plain string — convert it (e.g. with `float()`) if you need to do math on it.

```python
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

</details>
