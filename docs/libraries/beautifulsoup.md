---
description: >-
  Parsing HTML in Python with BeautifulSoup: finding tags, reading attributes and text, and
  turning a page into structured data for web scraping.
---

# :material-pot-steam-outline:{ .lg .middle } BeautifulSoup library

[BeautifulSoup documentation :material-open-in-new:](https://www.crummy.com/software/BeautifulSoup/bs4/doc/){ .md-button target="_blank" }

BeautifulSoup is an open-source project maintained by volunteer contributors.

**BeautifulSoup** (imported from `bs4`) is a popular library for parsing HTML — turning a page's raw markup into something you can search by tag, class, or attribute instead of scanning raw text by hand. It's a third-party package, not part of the standard library, but it's the de facto standard for this in Python.

<div class="pfg-section" markdown="block">

## Setup { data-card-link="skip" }

```bash
pip install beautifulsoup4
```

BeautifulSoup's package name (`beautifulsoup4`) doesn't match its import name — it's imported from `bs4`.

```python-ref
from bs4 import BeautifulSoup
```

</div>

<div class="pfg-section" markdown="block">

## HTML and web pages

A web page's content is just text — a file written in **HTML** (HyperText Markup Language), where tags mark what each piece of text is: a heading, a paragraph, a link, an image. Tags nest inside each other to build up a whole page's structure, the same way a list can hold another list. A browser doesn't show you this markup directly — it reads the HTML and *renders* it, turning `<h1>Ball python</h1>` into large, bold text on screen instead of displaying the angle brackets themselves.

```html
<html>
  <body>
    <h1>Ball python</h1>
    <p class="range">West Africa</p>
  </body>
</html>
```

A website doesn't send a picture of its page — it sends this raw HTML text, the same way [requests](requests.md) fetches a JSON API's response. Every browser's "View Page Source" (or a right-click "Inspect") shows exactly this text for any page you're looking at, which is worth trying on a real site before scraping one — it's the same markup a scraper reads.

Web scraping is just skipping the rendering step. `requests.get(url).text` returns this same raw HTML a browser would've turned into a page, as a plain Python string. BeautifulSoup is what makes that string usable — a `BeautifulSoup` object rebuilds the tag structure a browser's rendering engine reads, so a program can search it by tag and attribute exactly as it appears in the markup, without drawing anything on screen.

</div>

<div class="pfg-section" markdown="block">

## Overview { data-card-link="skip" }

It only works with HTML that's already in hand — a file, a plain string, or the `.text` of a [requests](requests.md) response — it has no ability to fetch a page itself, which is why the two are almost always used together: `requests` gets the page, BeautifulSoup makes sense of it. Parsing needs no network access, so unlike `requests`, most examples on this page run directly in this site's browser sandbox; the last one, which fetches a real page, does not.

| Concept | What it is |
|---------|------------|
| Parser | The engine BeautifulSoup hands raw HTML to for reading — `"html.parser"` ships with Python and is used throughout this page; `"lxml"` parses faster but needs a separate install. |
| Tag | One HTML element, like `<p>` or `<a>`, along with its attributes and everything nested inside it. |
| Attribute | A `key="value"` pair inside a tag's opening bracket, like `href` on an `<a>` or `class` on a `<div>`. |
| Soup | The parsed document as a whole — the `BeautifulSoup` object itself, named for turning "tag soup" (real-world, sometimes-messy HTML) into something navigable. |

**Python HTML parsing libraries**

- **BeautifulSoup** — the standard choice for everyday scraping: forgiving of messy or broken HTML, with simple search methods.
- **lxml** — faster and stricter, and often used *underneath* BeautifulSoup as its parser rather than called directly.
- **html.parser** — built into the standard library, no install needed, and BeautifulSoup's default parser.
- **Scrapy** — a full crawling framework — queues, retries, following links across many pages — for jobs bigger than parsing a page already in hand.

For a single page already in hand, BeautifulSoup offers the best balance of simplicity and tolerance for messy markup — most tasks are a `find`/`find_all` call and a couple of attribute lookups.

</div>

<div class="pfg-section" markdown="block">

## Parsing HTML

`BeautifulSoup(html, "html.parser")` reads a string of HTML and returns a navigable object with the same tree structure as the page itself — call `.find()` on it, or walk straight to a tag as if it were an attribute, to reach any piece of it.

```python-ref
soup = BeautifulSoup(html, "html.parser")
soup.h2.text   # "Ball python" — the first <h2> found, however deep it's nested
```

```python-ref
from bs4 import BeautifulSoup

html = """
<div class="snake" data-length-ft="5">
    <h2 class="name">Ball python</h2>
    <p class="range">West Africa</p>
</div>
<div class="snake" data-length-ft="16">
    <h2 class="name">Burmese python</h2>
    <p class="range">Southeast Asia</p>
</div>
<div class="snake" data-length-ft="20">
    <h2 class="name">Rock python</h2>
    <p class="range">Sub-Saharan Africa</p>
</div>
"""
soup = BeautifulSoup(html, "html.parser")
print(soup.h2.text)
```

### Finding tags

`.find()` returns the first matching tag; `.find_all()` returns every match, as a list. Both take a tag name, and narrow further with `class_=` (a trailing underscore, since `class` alone is a reserved word in Python) or `attrs={...}` for any other attribute.

```python-ref
soup.find("div")                                    # first <div>, whatever its class
soup.find_all("div")                                # every <div>, as a list
soup.find_all("div", class_="snake")                # every <div class="snake">
soup.find("div", attrs={"data-length-ft": "20"})    # matched by any attribute
```

```python-ref
from bs4 import BeautifulSoup

html = """
<div class="snake" data-length-ft="5">
    <h2 class="name">Ball python</h2>
    <p class="range">West Africa</p>
</div>
<div class="snake" data-length-ft="20">
    <h2 class="name">Rock python</h2>
    <p class="range">Sub-Saharan Africa</p>
</div>
"""
soup = BeautifulSoup(html, "html.parser")

print(len(soup.find_all("div", class_="snake")))
print(soup.find("div", attrs={"data-length-ft": "20"}).h2.text)
```

??? tip "CSS selectors with select()"
    `.select()` finds tags the same way a stylesheet would target them — `"div.snake"` for a tag plus class, `"#id"` for an id, `"div > h2"` for a direct child — which can read more naturally than several `find_all()` keyword arguments once a query gets specific. It always returns a list, even for a single match.

    ```python-ref
    soup.select("div.snake")       # same tags as find_all("div", class_="snake")
    soup.select("div.snake h2")    # every <h2> nested inside a .snake div
    ```

    ```python-ref
    from bs4 import BeautifulSoup

    html = """
    <div class="snake" data-length-ft="5">
        <h2 class="name">Ball python</h2>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    print(soup.select("div.snake h2")[0].text)
    ```

??? warning "find() returns None when nothing matches"
    Chaining `.text` or `.get()` straight onto a `find()` call works fine until the tag isn't there — a redesigned page, a typo'd class name, an entry missing that one field — at which point it raises `AttributeError: 'NoneType' object has no attribute 'text'` instead of a clear "not found." Check for `None` before using the result.

    ```python-ref
    tag = soup.find("div", class_="venomous")
    if tag is not None:
        print(tag.text)
    else:
        print("not found")
    ```

    ```python-ref
    from bs4 import BeautifulSoup

    html = '<div class="snake"><h2>Ball python</h2></div>'
    soup = BeautifulSoup(html, "html.parser")

    tag = soup.find("div", class_="venomous")
    if tag is not None:
        print(tag.text)
    else:
        print("not found")
    ```

### Reading text and attributes

`.text` (or `.get_text()`) returns everything inside a tag as one string, including any nested tags' text. An attribute reads like a dict item — `tag["href"]` — or safely with `.get("href")`, which returns `None` instead of raising `KeyError` when the attribute isn't there. `.attrs` gives every attribute on a tag as a plain dict.

```python-ref
tag = soup.find("div", class_="snake")
tag.h2.text                  # "Ball python"
tag["data-length-ft"]        # "5" — always a string, even for a number
tag.get("data-length-ft")    # "5" — same thing, but None instead of KeyError if missing
tag.attrs                    # {"class": ["snake"], "data-length-ft": "5"}
```

```python-ref
from bs4 import BeautifulSoup

html = """
<div class="snake" data-length-ft="5">
    <h2 class="name">Ball python</h2>
    <p class="range">West Africa</p>
</div>
"""
soup = BeautifulSoup(html, "html.parser")

tag = soup.find("div", class_="snake")
print(tag.h2.text)
print(tag["data-length-ft"])
print(tag.get("origin"))
print(tag.attrs)
```

</div>

<div class="pfg-section" markdown="block">

## Extracting structured data

A page is rarely useful one tag at a time — the real value of `find_all()` is looping over its results to build a plain Python list, the same list-of-dicts shape as [Collections](../collections.md#dictionaries)' own snake catalog, ready to filter, sort, or save to a [CSV](csv.md) or [JSON](json.md) file.

```python-ref
snakes = []
for tag in soup.find_all("div", class_="snake"):
    snakes.append({
        "name": tag.h2.text,
        "length_ft": int(tag["data-length-ft"]),
        "range": tag.p.text,
    })
snakes   # [{"name": "Ball python", "length_ft": 5, "range": "West Africa"}, ...]
```

```python-ref
from bs4 import BeautifulSoup

html = """
<div class="snake" data-length-ft="5">
    <h2 class="name">Ball python</h2>
    <p class="range">West Africa</p>
</div>
<div class="snake" data-length-ft="16">
    <h2 class="name">Burmese python</h2>
    <p class="range">Southeast Asia</p>
</div>
<div class="snake" data-length-ft="20">
    <h2 class="name">Rock python</h2>
    <p class="range">Sub-Saharan Africa</p>
</div>
"""
soup = BeautifulSoup(html, "html.parser")

snakes = []
for tag in soup.find_all("div", class_="snake"):
    snakes.append({
        "name": tag.h2.text,
        "length_ft": int(tag["data-length-ft"]),
        "range": tag.p.text,
    })

for snake in snakes:
    print(snake)
```

</div>

<div class="pfg-section" markdown="block">

## Putting it together

BeautifulSoup only parses HTML that's already in hand — pairing it with [requests](requests.md) is what turns this into an actual web scraper. A handful of small functions cover most everyday tasks; write each one once, then reuse it on any page.

### Common tasks

Each function below wraps a single `find`/`find_all` call in a [function](../functions.md), returning a plain [list](../collections.md#lists) built with a [list comprehension](../collections.md#list-comprehension) — store the result in a variable and use it like any other value.

```python-ref
get_title(soup)            # "Ball python"
get_all_links(soup)        # ["https://en.wikipedia.org/wiki/Ball_python"]
get_all_headings(soup)     # ["Ball python"]
get_all_paragraphs(soup)   # ["West Africa"]
```

```python-ref
from bs4 import BeautifulSoup


def get_title(soup):
    return soup.title.text


def get_all_links(soup):
    return [a.get("href") for a in soup.find_all("a")]


def get_all_headings(soup):
    return [h.text for h in soup.find_all(["h1", "h2", "h3"])]


def get_all_paragraphs(soup):
    return [p.text for p in soup.find_all("p")]


html = """
<html>
<head><title>Ball python</title></head>
<body>
    <h1>Ball python</h1>
    <p>West Africa</p>
    <a href="https://en.wikipedia.org/wiki/Ball_python">read more</a>
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")

print(get_title(soup))
print(get_all_links(soup))
print(get_all_headings(soup))
print(get_all_paragraphs(soup))
```

### Scraping a real page

The same functions work unchanged on a real page — only the URL, and which tags you care about, change. `requests.get(url).text` fetches the page; `BeautifulSoup` parses it exactly as above. This makes a real network call, which this site's sandbox can't do — copy it into a local `.py` file, swap in any page's URL, and see what comes back.

```python-ref
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
title = get_title(soup)   # store a result the same way as any other variable
```

```python-ref
import requests
from bs4 import BeautifulSoup


def get_title(soup):
    return soup.title.text


def get_all_links(soup):
    return [a.get("href") for a in soup.find_all("a")]


def get_all_headings(soup):
    return [h.text for h in soup.find_all(["h1", "h2", "h3"])]


response = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")

title = get_title(soup)
links = get_all_links(soup)
headings = get_all_headings(soup)

print(title)
print(len(links), "links found")
print(headings)
```

</div>
