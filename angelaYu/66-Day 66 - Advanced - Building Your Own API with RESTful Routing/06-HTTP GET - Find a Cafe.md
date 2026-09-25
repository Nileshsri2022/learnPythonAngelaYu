Here is a structured breakdown of this lesson on the `GET /search` endpoint.

---

### 1. The Endpoint

`GET /search?location=London` → every cafe in London.

The location arrives as a **query parameter** (the part after `?`), not as part of the path:

```python
from flask import request


@app.route("/search")
def search_cafes():
    query_location = request.args.get("location")

    cafes = db.session.execute(
        db.select(Cafe).where(Cafe.location == query_location)
    ).scalars().all()

    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
```

| Piece | Meaning |
|-------|---------|
| `request.args` | the query-string dictionary |
| `.get("location")` | returns `None` if the caller forgot the parameter |
| `404` | the resource (cafes in that city) does not exist |

---

### 2. Query Parameter vs URL Variable

| Style | Example | Use for |
|-------|---------|---------|
| URL variable | `/cafe/2` | identifying **one** specific resource |
| Query parameter | `/search?location=London` | **filtering/options** on a collection |

Rule of thumb: if it narrows down a list, it's a query parameter.

---

### 3. Case and Partial Matches

`==` is exact and case-sensitive. Friendlier searching:

```python
from sqlalchemy import func

cafes = db.session.execute(
    db.select(Cafe).where(func.lower(Cafe.location) == query_location.lower())
).scalars().all()
```

For partial matches, use `Cafe.name.ilike(f"%{term}%")`.

---

### 4. Return Codes

| Situation | Status |
|-----------|--------|
| found | `200` with `{"cafes": [...]}` |
| location valid but no cafes | `404` with an explanatory error object |
| `location` parameter missing | `400 Bad Request` — the caller made a mistake |

```python
if not query_location:
    return jsonify(error={"Bad Request": "Please provide a location, e.g. ?location=London"}), 400
```

> **Tip:** An API that explains *why* it failed saves its consumers hours — include a
> machine-readable key (`error`) and a human message.

---

### Summary Checklist

1. `request.args.get("location")` reads the query string.
2. Filter with `.where(Cafe.location == …)`.
3. `200` + list when found; `404` + explanation when empty; `400` for a missing parameter.
4. Query parameters are for filtering; path variables identify a resource.
