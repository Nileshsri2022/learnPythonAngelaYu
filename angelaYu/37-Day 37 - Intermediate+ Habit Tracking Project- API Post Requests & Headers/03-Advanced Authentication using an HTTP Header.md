Here is a structured breakdown of this lesson on header authentication.

---

### 1. Why Headers?

Query parameters appear in URLs — logs, caches, browser history. **Headers** travel with
the request invisibly — the professional place for credentials.

---

### 2. Creating a Graph with a Header

```python
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": "abc1234567890",
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(graph_response.text)
```

* `X-USER-TOKEN` — Pixela's custom auth header; requests passes any dict of headers.
* Your graph is now viewable at `https://pixe.la/v1/users/<user>/graphs/graph1.html`.

---

### Summary Checklist

1. Headers = authenticated requests without leaking tokens in URLs.
2. `requests.post(url, json=..., headers=...)` — both in one call.
