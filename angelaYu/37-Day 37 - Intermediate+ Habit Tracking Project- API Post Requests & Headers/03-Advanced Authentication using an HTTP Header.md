# Advanced Authentication using an HTTP Header

Pixela step 2 creates the graph that will hold your habit — and it fails the first
time, which is exactly how this lesson teaches **header authentication**.

---

### 1. The New Endpoint

The URL grows with the resource you are working on:

```text
https://pixe.la/v1/users                       ← the user (step 1)
https://pixe.la/v1/users/<username>/graphs     ← that user's graphs (step 2)
```

```python
USERNAME = "angela"
TOKEN = "mytoken1234567890"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
```

---

### 2. The Graph Configuration

```python
graph_config = {
    "id": "graph1",              # letters first, then letters/digits, 1–16 chars
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",             # "int" for whole numbers (pages), "float" for km
    "color": "ajisai",           # purple — colour names are Japanese, copy them!
}
```

The colour strings are poetic Japanese names (`momiji` = autumn leaves,
`shibafu` = grass, `sara` = sky, `ajisai` = hydrangea). Typos here are easy, so copy
them from the docs.

---

### 3. It Fails — Because the Token Is Missing

Posting `graph_config` gets back:

```python
{"message":"...the user angela does not exist... or the token is wrong..."}
```

The token is *not* in the body. Step 1 put it there; step 2 expects it in the
**request header**.

---

### 4. Why Headers Beat Query Strings

Day 36 sent the news API key as a URL parameter:

```text
https://newsapi.org/v2/everything?...&apiKey=abcdef&q=tesla
```

Everything secret ends up in the URL — visible in browser history, server logs and to
anything sniffing requests. (HTTPS encrypts the trip, but not what your own browser
or proxies can see.) NewsAPI itself recommends the alternatives:

* `X-Api-Key` **HTTP header**, or
* `Authorization` header.

Think of a posted letter: the **header** carries the address/logo (metadata), the
**body** is the actual message. Authentication belongs in the header.

```python
headers = {"X-USER-TOKEN": TOKEN}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)                     # Success. Let's start tracking!
```

> `headers=` is a keyword argument (`**kwargs`) — no autocomplete, and the trailing
> **s** matters. Spell it `headers`.

---

### 5. Check Your Graph

Visit `https://pixe.la/v1/users/<username>/graphs/<graph-id>.html` — in the lecture:
`.../users/angela/graphs/graph1.html`. Your empty graph is live and waiting for data.

---

### Summary Checklist

1. Resources nest in the URL: `/users` → `/users/<name>/graphs` → pixels.
2. `graph_config` needs `id`, `name`, `unit`, `type` and `color`.
3. Graph `id`: 1–16 chars, starting with a letter; colours are Japanese words.
4. Authenticate with `headers={"X-USER-TOKEN": TOKEN}` — not a URL parameter.
5. Headers keep secrets out of logs and URLs; `requests` takes them as `headers=`.
6. Verify the graph at `<graph-url>.html`.
