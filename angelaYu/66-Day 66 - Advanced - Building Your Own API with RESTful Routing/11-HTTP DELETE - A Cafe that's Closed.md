# HTTP DELETE - A Cafe that's Closed

---

### 1. The Endpoint

`DELETE /report-closed/22?api_key=TopSecretAPIKey` → remove a closed cafe.

```python
API_KEY = "TopSecretAPIKey"

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key != API_KEY:
        return jsonify(error={"Forbidden": "Sorry, that's not the valid api key."}), 403

    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found."}), 404

    db.session.delete(cafe)
    db.session.commit()
    return jsonify(success="Deleted the cafe."), 200
```

---

### 2. Why This Endpoint Needs a Key

Deleting is destructive. Not every client should be allowed to do it, so the endpoint
demands an **API key** — a shared secret passed with the request.

| Status | Meaning |
|--------|---------|
| `403 Forbidden` | key wrong or absent — the server refuses |
| `404` | key fine, but no such cafe |
| `200` | deleted |

> **⚠️ Warning:** This `?api_key=…` style is deliberately simple for learning. Real APIs
> send keys in a **header** (`api-key: …` / `Authorization: Bearer …`), store them in
> environment variables, and never commit them to GitHub.

```python
import os
API_KEY = os.environ.get("CAFE_API_KEY")
api_key = request.headers.get("api-key")
```

---

### 3. The Delete Itself

```python
cafe = db.session.get(Cafe, cafe_id)
db.session.delete(cafe)
db.session.commit()
```

Same pattern as add/update — find, act, commit. Nothing else in the database is affected
(one row, one record).

---

### 4. Testing the Three Paths

| Request | Expected |
|---------|----------|
| `DELETE /report-closed/22?api_key=TopSecretAPIKey` | `200`, cafe gone from `/all` |
| `DELETE /report-closed/22` (no key) | `403` |
| `DELETE /report-closed/9999?api_key=…` | `404` |

---

### 5. Order of Checks Matters

Check the **key first**, then existence: leaking "cafe 9999 exists" to an unauthorised
caller is information you don't owe them.

---

### Summary Checklist

1. `methods=["DELETE"]`; the id identifies which record to remove.
2. Compare the supplied key against your own, returning `403` on mismatch.
3. `db.session.delete()` + `commit()` removes exactly that row.
4. Prefer headers + environment variables over query-string keys in real projects.
