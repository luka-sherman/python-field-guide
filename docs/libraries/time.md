---
description: >-
  Reading the system clock, pausing execution, and measuring elapsed time in Python with the
  time module.
---

# :material-clock-outline:{ .lg .middle } time library

[Official documentation :material-open-in-new:](https://docs.python.org/3/library/time.html){ target="_blank" }

The **`time`** module reads the system clock, pauses a program for a set number of seconds, and measures how long a piece of code takes to run.

| | `time` | [`datetime`](datetime.md) |
|---|---|---|
| Focus | The system clock, code timing, and pausing execution. | Calendar dates, date arithmetic, and human-readable date/time values. |
| Time format | A Unix timestamp — a plain float counting seconds since the epoch. | High-level objects — `date`, `time`, `datetime`, `timedelta`. |
| Timezone support | Limited — relies on the system's local time. | Full — handles timezone-aware dates and conversions. |
| Common uses | <ul><li>Benchmarking how long code takes to run</li><li>Pausing a program with `sleep()`</li></ul> | <ul><li>Logging when something happened</li><li>Calculating an age or a deadline</li><li>Date arithmetic</li></ul> |

<div class="pfg-section" markdown="block">

## Setup { data-card-link="skip" }

`time` ships with Python's standard library — nothing to install. The whole module is used through the `time.` prefix, so a plain import is all you need.

```python-ref
import time
```

| Function | Returns | Example |
|----------|---------|---------|
| `time()` | Seconds since the epoch, as a float | `1785024000.0` |
| `sleep(seconds)` | Pauses the program, returns `None` | `sleep(2)` |
| `perf_counter()` | A high-resolution timer, for measuring durations | `perf_counter()` |
| `localtime()` | The current time as a `struct_time` | `localtime()` |
| `strftime(format, t)` | A `struct_time` formatted as a string | `strftime("%H:%M", localtime())` |

</div>

<div class="pfg-section" markdown="block">

## Reading the clock

`time()` returns the number of seconds since the epoch[^epoch] — a single float that always increases, useful for a timestamp or for logging when an observation happened.

```python-ref
import time

print(time.time())
```

[^epoch]: The epoch is a fixed reference point, midnight, January 1, 1970 (UTC). "Seconds since the epoch" is just a plain number, not tied to any calendar, which is why it's easy to compare or subtract.

</div>

<div class="pfg-section" markdown="block">

## Pausing execution

`sleep()` pauses the program for the given number of seconds before continuing to the next line. Useful for spacing out repeated `print()` calls, or waiting between requests to an external service.

```python-ref
import time

print("checking on the burmese python...")
time.sleep(1)
print("still there.")
```

??? run "Run a pausing example"
    All the examples above, combined into one script:

    ```python
    import time

    print(time.time())

    import time

    print("checking on the burmese python...")
    time.sleep(1)
    print("still there.")
    ```

</div>

<div class="pfg-section" markdown="block">

## Measuring elapsed time

`perf_counter()` reads a high-resolution timer meant for measuring durations, not for reading the wall-clock date — call it before and after a block of code, then subtract the two readings to get the elapsed time in seconds.

```python-ref
import time

start = time.perf_counter()
total = sum(range(1_000_000))
elapsed = time.perf_counter() - start

print(elapsed)
```

??? note "Why not time() for this?"
    `time()` tracks the system clock, which can jump backward or forward (a clock sync, daylight saving). `perf_counter()` is unaffected by that — it only ever counts forward, which makes it the right tool for timing how long code takes to run.

??? run "Run a measuring elapsed time example"
    All the examples above, combined into one script:

    ```python
    import time

    start = time.perf_counter()
    total = sum(range(1_000_000))
    elapsed = time.perf_counter() - start

    print(elapsed)
    ```

</div>

<div class="pfg-section" markdown="block">

## Formatting the current time

`localtime()` returns a `struct_time` — the current date and time broken into named fields (`tm_year`, `tm_hour`, `tm_min`, and so on). `strftime()` turns one into a custom-formatted string, using the same format codes as [`datetime`'s `strftime`](datetime.md#formatting-with-strftime): `%H` the zero-padded hour, `%M` the zero-padded minute.

```python-ref
import time

now = time.localtime()
time.strftime("%H:%M", now)    # "14:30"
```

??? tip "Reaching for datetime instead"
    `time` works with a `struct_time`, a plain tuple of fields, which has no date arithmetic of its own — no adding a week, no subtracting two times. For anything beyond formatting the current moment, the [`datetime`](datetime.md) module's `date` and `datetime` objects are the better fit.

??? run "Run a formatting example"
    All the examples above, combined into one script:

    ```python
    import time

    now = time.localtime()
    print(time.strftime("%H:%M", now))
    ```

</div>
