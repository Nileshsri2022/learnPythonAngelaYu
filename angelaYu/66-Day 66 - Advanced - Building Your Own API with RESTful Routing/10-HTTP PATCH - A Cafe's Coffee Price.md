Here is a structured breakdown of this lesson on the `PATCH /update-price/<cafe_id>` endpoint.

---

### 1. The Endpoint

`PATCH /update-price/22?new_price=£4.20` → change one cafe's coffee price.

```python
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found."}), 404

    new_price = request.args.get("new_price")
    if not new_price:
        return jsonify(error={"Bad Request": "Missing ?new_price=…"}), 400

    cafe.coffee_price = new_price        # change ONE field, nothing else
    db.session.commit()
    return jsonify(success="Successfully updated the coffee price."), 200
```

---

### 2. Why the Price Is a Query Parameter Here

| Where the data lives | Example | Purpose |
|----------------------|---------|---------|
| Path variable | `/update-price/<cafe_id>` | identifies the resource |
| Query parameter | `?new_price=£4.20` | the change to apply |

Real APIs often send the new value in a JSON body instead:

```python
data = request.get_json()
cafe.coffee_price = data["new_price"]
```

The path-vs-parameter logic stays identical.

---

### 3. SQLAlchemy's Object-Database Mapping

```python
cafe = db.session.get(Cafe, cafe_id)   # SELECT … WHERE id = café_id
cafe.coffee_price = "£4.20"            # change the Python attribute
db.session.commit()                    # UPDATE cafes SET coffee_price = …
```

You never write SQL: read the row into an object, set the **attribute**, commit. This is
the payoff of the OOP lessons — the database row behaves like any other object.

---

### 4. Status Codes

| Case | Response |
|------|----------|
| updated | `200` + success message |
| unknown id | `404` + "cafe not found" |
| missing price parameter | `400` + "provide ?new_price=" |
| wrong method (`GET`) | `405` Method Not Allowed |

---

### 5. Testing in Postman

1. `GET /all` — note the current price of a cafe.
2. `PATCH /update-price/<id>?new_price=£5.00` — expect `200`.
3. `GET /all` again — the price is the only thing that changed.
4. Re-run with a bogus id (`9999`) — expect the `404` and its message.

---

### Summary Checklist

1. `methods=["PATCH"]` plus `<int:cafe_id>` in the path.
2. `db.session.get(Cafe, id)` → attribute assignment → `commit()`.
3. Guard both the missing record (`404`) and the missing parameter (`400`).
4. Verify with a second `GET` that only the intended field changed.
