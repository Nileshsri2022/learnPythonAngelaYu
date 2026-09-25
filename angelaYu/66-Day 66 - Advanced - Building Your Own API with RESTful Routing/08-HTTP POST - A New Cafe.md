# HTTP POST - A New Cafe

---

### 1. The Endpoint

`POST /add` → create a new cafe from submitted form data.

```python
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."}), 201
```

| Piece | Why |
|-------|-----|
| `methods=["POST"]` | the same URL can accept several verbs — you must declare them |
| `request.form.get(...)` | reads `x-www-form-urlencoded` form fields |
| `bool(...)` | checkboxes submit `"on"` or nothing — cast to a real boolean |
| `db.session.add()` + `commit()` | stage the row, then persist it |
| `201 Created` | the correct status for a successful creation |

---

### 2. If the Body Is JSON Instead

```python
data = request.get_json()
new_cafe = Cafe(**data)          # unpack the dict into keyword arguments
```

Postman: *Body → raw → JSON*. Form: *Body → x-www-form-urlencoded*.

---

### 3. Validate Before You Insert

```python
required = ["name", "location", "coffee_price"]
missing = [field for field in required if not request.form.get(field)]
if missing:
    return jsonify(error={"Bad Request": f"Missing fields: {', '.join(missing)}"}), 400
```

What happens without validation? `nullable=False` columns raise an `IntegrityError` — a
500 to the client and a stack trace in your log. A `400` with a clear message is far
better.

---

### 4. Test All Four Combinations

| Request | Expected |
|---------|----------|
| valid form | `201` + success message; cafe appears in `/all` |
| missing name | `400` + error message |
| duplicate name | `400` (unique constraint) — catch it and explain |
| GET on `/add` | `405 Method Not Allowed` |

---

### Summary Checklist

1. `methods=["POST"]` on the route; `request.form.get()` for fields.
2. Cast checkbox values to booleans before storing.
3. `db.session.add()` then `commit()`; respond `201 Created`.
4. Validate input and return `400` with a useful message rather than letting the DB throw.
