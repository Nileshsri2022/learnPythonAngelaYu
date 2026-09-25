Here is a structured breakdown of this lesson on `PUT` vs `PATCH`.

---

### 1. The Bicycle Analogy

A bike arrives from Amazon with a broken front wheel. Two ways to fix it:

| Option | What Amazon sends | HTTP equivalent |
|--------|-------------------|-----------------|
| Replace the whole bike | an entire new bicycle | **PUT** |
| Send just the wheel | one spare part | **PATCH** |

* **PUT** — you send the **complete** resource to replace the existing one.
* **PATCH** — you send **only the fields that change**.

---

### 2. Why PATCH Is Usually Better

* Less data over the wire (and less carbon, as Angela points out).
* No risk of accidentally wiping fields you forgot to include.
* Better matches what clients actually want to do — "change the coffee price", not
  "re-send the whole cafe".

---

### 3. The Same Endpoint, Different Verb

```python
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_coffee_price(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found."}), 404

    cafe.coffee_price = request.args.get("new_price")
    db.session.commit()
    return jsonify(success="Successfully updated the price."), 200
```

* Only `coffee_price` is touched — every other column keeps its value.
* A `PUT` version would need the client to send all eleven fields, or values would be
  overwritten with `None`.

---

### 4. Choosing the Verb

| Verb | Meaning | Send |
|------|---------|------|
| `PUT` | replace the whole resource | every field |
| `PATCH` | update part of the resource | just the changes |

> **Note:** In practice many APIs implement only `PATCH` for updates, and some use `PUT`
> leniently. The distinction is worth knowing — you'll be asked about it.

---

### 5. Always Handle the Missing Record

Both verbs get an id in the path, and ids can be wrong:

```python
if cafe is None:
    return jsonify(error={"Not Found": "…"}), 404
```

Without that check, `cafe.coffee_price = …` throws `AttributeError` and the client sees a
500 instead of a helpful 404.

---

### Summary Checklist

1. `PUT` = replace the entire resource; `PATCH` = update only the fields you send.
2. PATCH is more efficient and safer for small changes like a price.
3. Both need `methods=[...]` and a `404` guard for unknown ids.
4. Test with Postman: watch the field change in `/all` afterwards.
