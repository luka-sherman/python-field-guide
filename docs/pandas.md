# pandas

**pandas** (imported as `pd`) is Python's standard library for tabular data — rows and columns, like a spreadsheet, with tools for filtering, sorting, and summarizing built in. It's a third-party package (`pip install pandas`), not part of the standard library, and is built on top of [NumPy](numpy.md).

| Type | Shape | Like |
|------|-------|------|
| `Series` | One column of labeled values | A single spreadsheet column |
| `DataFrame` | Many columns, sharing an index | A whole spreadsheet or table |

## Building a DataFrame

A `DataFrame` is most often built from a list of dicts — one dict per row, with matching keys becoming the column names.

```python
import pandas as pd

snakes = pd.DataFrame([
    {"species": "ball", "length_ft": 4.5, "venomous": False},
    {"species": "burmese", "length_ft": 12, "venomous": False},
])

print(snakes)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Building From a Dict of Lists

The same table can also be built from a single dict where each key maps to a whole column's worth of values.
{: .pt-subheading }

```python-ref
pd.DataFrame({
    "species": ["ball", "burmese"],
    "length_ft": [4.5, 12],
})
```

</summary>

The rows line up by position across every list, so all the lists need to be the same length.

```python
import pandas as pd

snakes = pd.DataFrame({
    "species": ["ball", "burmese"],
    "length_ft": [4.5, 12],
})

print(snakes)
```

</details>

## Working with a DataFrame

A single column pulled out of a `DataFrame` (with `df["column"]`) is a `Series` — comparing it to a value produces a boolean mask, exactly like a NumPy array, for filtering rows.

```python
import pandas as pd

snakes = pd.DataFrame([
    {"species": "ball", "length_ft": 4.5},
    {"species": "burmese", "length_ft": 12},
    {"species": "boa", "length_ft": 8},
])

big_snakes = snakes[snakes["length_ft"] > 5]
print(big_snakes)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Sorting Rows

Returns the `DataFrame` reordered by a column.
{: .pt-subheading }

```python-ref
snakes.sort_values("length_ft", ascending=False)    # rows reordered longest-first
```

</summary>

`.sort_values("column")` sorts ascending by default, or descending with `ascending=False`. Like most pandas operations, it returns a new `DataFrame` rather than reordering the original in place.

```python
import pandas as pd

snakes = pd.DataFrame([
    {"species": "ball", "length_ft": 4.5},
    {"species": "burmese", "length_ft": 12},
    {"species": "boa", "length_ft": 8},
])

print(snakes.sort_values("length_ft", ascending=False))
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Summarizing a Column

Calling `.mean()`, `.max()`, or similar directly on a column summarizes it down to a single number.
{: .pt-subheading }

```python-ref
snakes["length_ft"].mean()    # 8.166666666666666
snakes["length_ft"].max()     # 12.0
```

</summary>

The same way it would on a NumPy array — a `Series` supports the same aggregation methods.

```python
import pandas as pd

snakes = pd.DataFrame([
    {"species": "ball", "length_ft": 4.5},
    {"species": "burmese", "length_ft": 12},
    {"species": "boa", "length_ft": 8},
])

print(snakes["length_ft"].mean())
print(snakes["length_ft"].max())
```

</details>
