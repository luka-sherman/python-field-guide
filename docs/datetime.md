# datetime

The **`datetime`** module is Python's standard library for working with dates and times — logging when an observation happened, measuring how long ago it was, or formatting a date for display. It ships with Python, so no install is needed.

| Class | Holds | Example |
|-------|-------|---------|
| `date` | A calendar date, no time of day | `date(2026, 7, 23)` |
| `time` | A time of day, no date | `time(14, 30)` |
| `datetime` | A date and time together | `datetime(2026, 7, 23, 14, 30)` |
| `timedelta` | A duration — the gap between two dates/times | `timedelta(days=7)` |

## Creating dates and times

`date.today()` and `datetime.now()` read the current date (and time) directly from the system clock, so the value changes every time the code runs.

```python
from datetime import date, datetime

today = date.today()
now = datetime.now()

print(today)
print(now)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Creating a specific date

Pass the year, month, and day as plain integers to build a specific `date`.
{: .pt-subheading }

```python-ref
observed = date(2026, 7, 23)    # 2026-07-23
```

</summary>

Useful for logging when a past observation actually happened, instead of reading today's date off the system clock.

```python
from datetime import date

observed = date(2026, 7, 23)
print(observed)
print(observed.year, observed.month, observed.day)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Formatting with `strftime`

Turns a `date` or `datetime` into a custom-formatted string.
{: .pt-subheading }

```python-ref
observed = date(2026, 7, 23)
observed.strftime("%B %d, %Y")    # "July 23, 2026"
```

</summary>

`strftime` ("string format time") — `%B` is the full month name, `%d` the zero-padded day, `%Y` the four-digit year. It's the standard way to control exactly how a date is displayed.

```python
from datetime import date

observed = date(2026, 7, 23)
print(observed.strftime("%B %d, %Y"))
print(observed.strftime("%Y-%m-%d"))
```

</details>

## Date arithmetic

A `timedelta` represents a span of time, and adding one to a `date` or `datetime` shifts it forward (or backward, with a negative value) — the standard way to compute "a week from now" or "30 days ago."

```python
from datetime import date, timedelta

observed = date(2026, 7, 23)
next_checkup = observed + timedelta(days=14)

print(next_checkup)
```

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Difference between two dates

Subtracting one `date` from another gives back a `timedelta`.
{: .pt-subheading }

```python-ref
first_seen = date(2026, 7, 23)
last_seen = date(2026, 8, 6)
last_seen - first_seen    # timedelta(days=14)
```

</summary>

Its `.days` attribute is the number of days between them — handy for measuring how long something has been tracked.

```python
from datetime import date

first_seen = date(2026, 7, 23)
last_seen = date(2026, 8, 6)
gap = last_seen - first_seen

print(gap)
print(gap.days)
```

</details>

<details markdown="block" class="pt-collapsible">
<summary markdown="block">

### Parsing a string with `strptime`

The reverse of `strftime` — reads a date out of a string.
{: .pt-subheading }

```python-ref
datetime.strptime("2026-07-23", "%Y-%m-%d")    # datetime(2026, 7, 23, 0, 0)
```

</summary>

`strptime` ("string parse time") takes the same format codes describing how that string is laid out. This is how a date typed by a user, or read from a CSV file, gets turned back into a real `datetime` you can do arithmetic on.

```python
from datetime import datetime

parsed = datetime.strptime("2026-07-23", "%Y-%m-%d")
print(parsed)
print(parsed.year)
```

</details>
