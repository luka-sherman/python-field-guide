# :material-api:{ .lg .middle } requests library

**`requests`** is a third-party library for fetching data over the internet — asking a website or API for information, the same way a browser does, but from inside a Python program. It's not part of the standard library, but it's the de facto standard for this in Python, favored over the built-in `urllib` for its much simpler syntax. Every example on this page makes a real network call, which this site's in-browser sandbox can't do — copy them into a local `.py` file and run them with `python` to see the results.

## Install

```bash
pip install requests
```

## Import

The whole module is used through the `requests.` prefix, so a plain import is all you need.

```python-ref
import requests
```

| Concept | What it is |
|---------|------------|
| Request | The message your program sends out, asking for (or sending) data at a specific URL. |
| Response | What comes back — a status code, some headers, and usually a body of data. |
| Endpoint | A specific URL a service exposes for a specific purpose, e.g. `/posts/1` for "post number 1." |
| Status code | A number summarizing what happened — `200` means success, `404` means "not found," and so on. |
| JSON | A text format for structured data — Python's `dict`/`list` nested together — that most web APIs send back. |
| Header | Extra metadata sent with a request or response, like the data format or an API key. |
| Query parameter | Extra options tacked onto a URL, like `?limit=5`, to filter or adjust what comes back. |
| Timeout | How long to wait for a response before giving up, rather than hanging forever. |

**Python HTTP libraries**

- **`requests`** — the standard choice for everyday HTTP calls: simple, readable, synchronous.
- **`urllib`** — built into the standard library, so no install needed, but noticeably more verbose for the same task.
- **`httpx`** — a newer library with a very similar API to `requests`, but adds support for `async`/`await`.
- **`aiohttp`** — built specifically for `async`/`await` from the ground up, aimed at programs making many requests at once.

For everyday use, `requests` offers the best balance of simplicity and capability — most tasks are one function call.

## Making a request

`requests.get(url)` sends a request and returns a `Response` object holding whatever came back.

```python-ref
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)   # 200
print(response.text)          # '{"userId": 1, "id": 1, "title": "...", "body": "..."}'
```

### Checking the status code

`.status_code` tells you whether the request actually succeeded before you try to use the data. The most common codes: `200` (success), `404` (that endpoint/resource doesn't exist), `401`/`403` (missing or invalid permission), `500` (the server itself failed). `.raise_for_status()` is a shortcut that raises an exception automatically for any failing code, instead of checking `.status_code` by hand every time.

```python-ref
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    print("success")
else:
    print(f"request failed: {response.status_code}")
```

```python-ref
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
response.raise_for_status()   # does nothing on 200, raises on a failing code
print("request succeeded")
```

### Parsing JSON

`.json()` converts a JSON response body directly into a Python `dict` or `list`. Most web APIs send their data back as JSON — text formatted so it maps directly onto Python's own `dict`/`list` structures, which is why `.json()` needs no extra parsing step. Once converted, the result works exactly like any other [dict](../collections.md#dictionaries) or [list](../collections.md#lists) you'd build by hand.

```python-ref
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
post = response.json()
print(post["title"])   # the post's title, as a plain Python dict lookup
```

```python-ref
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
post = response.json()

print(post["userId"])
print(post["title"])
print(post["body"])
```

### Query parameters

Pass a `params` dict instead of hand-building the URL's `?key=value` text yourself. `requests` builds the query string for you — including escaping special characters correctly — so `params={"postId": 1}` is both safer and easier to read than string-formatting the URL by hand.

```python-ref
response = requests.get(
    "https://jsonplaceholder.typicode.com/comments",
    params={"postId": 1},
)
# same as requesting .../comments?postId=1
```

```python-ref
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/comments",
    params={"postId": 1},
)
comments = response.json()
print(len(comments))
```

## Handling request errors

A network call can fail in ways that have nothing to do with your code — the [Bugs](../bugs.md#handling-errors) page covers `try`/`except` in general; a couple of exceptions are specific to `requests`.

| Exception | Happens when |
|-----------|---------------|
| `requests.exceptions.Timeout` | The server didn't respond within the time limit you set |
| `requests.exceptions.ConnectionError` | The request couldn't reach the server at all — no internet, wrong URL, server is down |
| `requests.exceptions.HTTPError` | Raised by `.raise_for_status()` when the response's status code indicates failure |

```python-ref
import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("the request took too long")
except requests.exceptions.ConnectionError:
    print("couldn't reach the server")
except requests.exceptions.HTTPError:
    print(f"request failed: {response.status_code}")
else:
    print(response.json())
```

Passing `timeout=5` (seconds) is worth doing on every request — without it, a request that never gets a response will hang your program indefinitely instead of raising `Timeout`.
