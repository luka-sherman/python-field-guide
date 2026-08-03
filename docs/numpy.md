# :material-matrix:{ .lg .middle } NumPy library

**NumPy** (imported as `np`) is Python's standard library for fast numeric arrays — the foundation nearly every other data or scientific library in Python is built on. It's a third-party package (`pip install numpy`), not part of the standard library. A NumPy `ndarray` looks similar to a `list`, but every element is the same type and math operations apply to the whole array at once, instead of one item at a time.

| Type | Holds | Math operations |
|------|-------|------------------|
| `list` | Any mix of types | Element-by-element, usually with a loop |
| `ndarray` | One type, fixed size | Applied to the whole array at once ("vectorized") |

## Creating arrays

`np.array()` builds an `ndarray` from an existing list — every value gets converted to the same type.

```python-ref
import numpy as np

lengths_ft = np.array([4.5, 12, 8, 6])
print(lengths_ft)
print(lengths_ft.dtype)
```

### Building arrays without a list

`np.zeros(n)` builds an array of `n` zeros as a starting point to fill in later. `np.arange(stop)` counts up from `0` to (but not including) `stop`, just like the built-in `range()` — with an optional start and step, exactly like `range()` too.

```python-ref
np.zeros(4)      # array([0., 0., 0., 0.])
np.arange(4)     # array([0, 1, 2, 3])
np.arange(0, 10, 2)    # array([0, 2, 4, 6, 8])
```

??? run "Run a creating arrays example"
    All the examples above, combined into one script:

    ```python
    import numpy as np

    lengths_ft = np.array([4.5, 12, 8, 6])
    print(lengths_ft)
    print(lengths_ft.dtype)

    import numpy as np

    print(np.zeros(4))
    print(np.arange(4))
    print(np.arange(0, 10, 2))
    ```

## Array operations

A math operation on an array applies to every element at once — no loop required, and considerably faster than looping over a plain list.

```python-ref
import numpy as np

lengths_ft = np.array([4.5, 12, 8, 6])
lengths_m = lengths_ft * 0.3048

print(lengths_m)
```

### Aggregating an array

Collapses an entire array down to a single summary number. `.mean()`, `.max()`, `.min()`, and `.sum()` — the same idea as Python's built-in `sum()` and `max()`, but computed directly on the array without converting it back to a list first.

```python-ref
lengths_ft = np.array([4.5, 12, 8, 6])
lengths_ft.mean()    # 7.625
lengths_ft.max()     # 12.0
lengths_ft.sum()     # 30.5
```

### Filtering with a boolean mask

Comparing an array to a number produces a same-size array of `True`/`False` values — a **boolean mask**. Indexing the array with that mask keeps only the elements where it's `True`. This is the standard way to filter a NumPy array, instead of writing an explicit loop with an `if` inside it.

```python-ref
lengths_ft = np.array([4.5, 12, 8, 6])
lengths_ft > 7             # array([False, True, True, False])
lengths_ft[lengths_ft > 7]  # array([12., 8.])
```

??? run "Run an array operations example"
    All the examples above, combined into one script:

    ```python
    import numpy as np

    lengths_ft = np.array([4.5, 12, 8, 6])
    lengths_m = lengths_ft * 0.3048

    print(lengths_m)

    import numpy as np

    lengths_ft = np.array([4.5, 12, 8, 6])
    print(lengths_ft.mean())
    print(lengths_ft.max())
    print(lengths_ft.sum())

    import numpy as np

    lengths_ft = np.array([4.5, 12, 8, 6])
    mask = lengths_ft > 7
    print(mask)
    print(lengths_ft[mask])
    ```
