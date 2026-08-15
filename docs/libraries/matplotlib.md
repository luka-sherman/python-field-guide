---
description: >-
  Creating charts in Python with matplotlib: line plots, bar charts, scatter plots,
  subplots, and saving figures to a file.
---

# :material-chart-line:{ .lg .middle } matplotlib library

**matplotlib** (its plotting interface imported as `plt`) is Python's foundational library for creating charts — line plots, bar charts, scatter plots — directly from plain Python data. It's a third-party package, not part of the standard library, but it's the base most other Python plotting tools are built on top of. Like [Pillow](pillow.md) and [OpenCV](opencv.md), matplotlib produces visual output — a chart shown in a window or saved to a file — which can't be shown inside this site's browser sandbox, so the examples below aren't runnable here. Copy them into a local `.py` file and run them with `python` to see the results.

## Install

```bash
pip install matplotlib
```

## Import

matplotlib's plotting interface lives in its `pyplot` submodule, conventionally imported under the alias `plt` — used throughout this page and in virtually every codebase that imports it.

```python-ref
import matplotlib.pyplot as plt
```

**Python plotting libraries**

- **matplotlib** — the standard, most widely used choice: complete control over every element of a chart, at the cost of more code for a fully polished result.
- **seaborn** — built directly on matplotlib, with better default styling and shorter code for common statistical charts (distributions, correlations).
- **plotly** — produces interactive, zoomable charts meant for dashboards and notebooks, at the cost of a heavier dependency.
- **pandas' own `.plot()`** — a one-line shortcut directly on a [DataFrame or Series](pandas.md#working-with-a-dataframe), which calls matplotlib underneath without a separate import.

For everyday charts, matplotlib offers the most control and the widest compatibility — most other Python plotting tools are either built on it or modeled after it.

| Concept | What it is |
|---------|------------|
| Figure | The overall canvas a chart is drawn on — created automatically by the first plotting call, or explicitly with `plt.subplots()`. |
| Axes | One individual chart within a figure, holding the actual plotted data, labels, and title. A figure can hold more than one. |
| `plt.show()` | Opens the current figure in a window — the way to view a chart while running a script locally. |
| `plt.savefig()` | Writes the current figure to an image file instead of (or as well as) showing it. |
| Legend | A key mapping each line or bar's color back to its `label`, built from every `label=` passed to a plotting call. |
| Subplot | One of several Axes arranged in a grid within a single figure, for showing more than one chart at once. |

## Line plots

`plt.plot(x, y)` draws a line connecting a series of x/y points — matplotlib's most basic and most common chart, given two equal-length sequences of numbers.

```python-ref
import matplotlib.pyplot as plt

years = [0, 1, 2, 3, 4]
length_ft = [0.8, 1.5, 2.3, 2.9, 3.2]

plt.plot(years, length_ft)
plt.show()
```

### Labels and title

`plt.xlabel()`, `plt.ylabel()`, and `plt.title()` label a chart's axes and give it a heading — without them, a chart is just numbers with no explanation of what they mean.

```python-ref
plt.plot(years, length_ft)
plt.xlabel("years since hatching")
plt.ylabel("length (ft)")
plt.title("ball python growth")
plt.show()
```

### Multiple lines and a legend

Calling `plt.plot()` more than once before `plt.show()` draws every line onto the same figure. Passing `label=` to each call, then `plt.legend()`, adds a key showing which line is which.

```python-ref
ball_length_ft = [0.8, 1.5, 2.3, 2.9, 3.2]
burmese_length_ft = [1.0, 2.8, 5.5, 7.9, 9.5]

plt.plot(years, ball_length_ft, label="ball python")
plt.plot(years, burmese_length_ft, label="burmese python")
plt.legend()
plt.show()
```

??? warning "matplotlib remembers the current figure"
    `plt.plot()` always draws onto whatever figure is currently active — which is exactly what makes stacking multiple lines onto one chart work, but it also means two *unrelated* charts plotted back to back in the same script land on top of each other unless you close out the current one first. `plt.show()` does this for you; calling `plt.figure()` before the next plot works too.

    ```python-ref
    plt.plot(years, ball_length_ft)
    plt.show()          # closes this figure

    plt.plot(years, burmese_length_ft)
    plt.show()          # starts and shows a separate, second figure
    ```

## Bar charts

`plt.bar(labels, values)` draws one bar per label — suited to comparing a value across categories, rather than showing change over a continuous range the way a line plot does.

```python-ref
import matplotlib.pyplot as plt

species = ["burmese", "rock", "ball", "blood"]
lengths_ft = [4.5, 12, 5, 3.5]

plt.bar(species, lengths_ft)
plt.ylabel("length (ft)")
plt.show()
```

## Scatter plots

`plt.scatter(x, y)` plots individual points instead of connecting them with a line — suited to showing the relationship between two measurements without implying an order between them.

```python-ref
import matplotlib.pyplot as plt

lengths_ft = [4.5, 12, 5, 3.5, 8, 6.2]
weights_lb = [3, 45, 4, 2, 15, 9]

plt.scatter(lengths_ft, weights_lb)
plt.xlabel("length (ft)")
plt.ylabel("weight (lb)")
plt.show()
```

## Subplots

`plt.subplots(rows, cols)` returns a `Figure` and a grid of `Axes` objects, for placing more than one chart side by side instead of calling `plt.show()` separately for each. Each `Axes` in the grid gets its own `.plot()`/`.bar()`/`.scatter()` and its own `.set_title()`, rather than the `plt.`-prefixed functions used above.

```python-ref
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2)

axes[0].plot(years, ball_length_ft)
axes[0].set_title("growth")

axes[1].bar(species, lengths_ft)
axes[1].set_title("length by species")

plt.show()
```

## Saving a figure

`plt.savefig(filename)` writes the current figure to a file instead of opening a window — the way to produce a chart image for a report, a webpage, or anywhere a live Python process won't be running to show it.

```python-ref
import matplotlib.pyplot as plt

plt.plot(years, ball_length_ft, label="ball python")
plt.plot(years, burmese_length_ft, label="burmese python")
plt.xlabel("years since hatching")
plt.ylabel("length (ft)")
plt.title("growth by species")
plt.legend()
plt.savefig("growth_comparison.png")
```
