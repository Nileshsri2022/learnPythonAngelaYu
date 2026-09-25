Here is a structured breakdown of this lesson on PUT and DELETE.

---

### 1. The Full CRUD Cycle

```python
# PUT — update one pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{TODAY}"
new_pixel_data = {
    "quantity": "8",
}
update_response = requests.put(url=update_endpoint, json=new_pixel_data,
                               headers=headers)

# DELETE — remove one pixel
delete_response = requests.delete(url=update_endpoint, headers=headers)
print(delete_response.text)
```

| Verb | Meaning | URL |
|------|---------|-----|
| POST | create | `…/graphs/graph1` |
| PUT | update | `…/graphs/graph1/<date>` |
| DELETE | remove | `…/graphs/graph1/<date>` |
| GET | read | `…/graphs/graph1` |

The endpoint identifies the *resource*; the verb identifies the *action* — the REST idea
you'll build yourself on Day 66.

---

### Summary Checklist

1. PUT updates, DELETE removes — same auth header as always.
2. Resource in the URL, action in the method.
3. Runnable version: [`main.py`](main.py)
