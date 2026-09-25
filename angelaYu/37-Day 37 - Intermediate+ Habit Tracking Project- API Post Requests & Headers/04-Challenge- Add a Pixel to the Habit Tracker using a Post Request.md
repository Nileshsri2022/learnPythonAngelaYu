# Challenge: Add a Pixel to the Habit Tracker using a Post Request

Pixela step 4: put a coloured square on the graph for today.

---

### 1. Read the Docs, Then Build the Endpoint

The pixel endpoint nests the whole path and is mostly placeholders:

```text
/v1/users/<username>/graphs/<graph-id>
```

```python
GRAPH_ID = "graph1"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
```

---

### 2. The Request Body

```python
today = "20200925"                 # yyyyMMdd — a string, not a number

pixel_data = {
    "date": today,
    "quantity": "9.74",            # also a string; becomes the pixel's intensity
}

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)
```

| Field | Rule |
|-------|------|
| `date` | **Four** digits year, **two** month, **two** day — `yyyyMMdd`, as a string |
| `quantity` | Must match the graph's `type`: `float` graph → `"9.74"`, `int` graph → `"25"` |
| `headers` | The same `{"X-USER-TOKEN": TOKEN}` dictionary as the graph request |

Refresh `.../graphs/graph1.html` and your first pixel appears — lighter for small
values, denser for large ones. The page also shows totals, minimum, maximum and an
average, so the graph becomes a statistics dashboard for free.

---

### 3. Make It a Real Habit Tracker

Typing the date by hand every day defeats the purpose. That is the next lesson:
`datetime.strftime()` fills it in programmatically.

---

### Summary Checklist

1. Pixel endpoint = `…/users/<username>/graphs/<graph-id>` — POST creates the pixel.
2. `date` must be `yyyyMMdd` (8 characters) and a **string**.
3. `quantity` is a string, and it must obey the graph's declared `type`.
4. Reuse the `headers` token; don't re-create the graph (comment that call out).
5. Verify by refreshing the graph's `.html` page — colour intensity shows quantity.
