Here is a structured breakdown of this lesson on documenting your API.

---

### 1. An API Without Docs Is Unusable

Nobody can guess that the price update endpoint is `PATCH /update-price/22?new_price=…`.
Documentation *is* part of the product — write it as if a stranger has to integrate with
you tomorrow.

---

### 2. The Minimum Table

| Method | Endpoint | Parameters | Auth | What it does |
|--------|----------|-----------|------|--------------|
| `GET` | `/random` | – | – | one random cafe |
| `GET` | `/all` | – | – | every cafe |
| `GET` | `/search` | `location` (query) | – | cafes in a location |
| `POST` | `/add` | form fields (name, location, …) | – | create a cafe |
| `PATCH` | `/update-price/<cafe_id>` | `new_price` (query) | – | change the coffee price |
| `DELETE` | `/report-closed/<cafe_id>` | `api_key` | ✅ | remove a closed cafe |

---

### 3. Document Every Response

For each endpoint, show:

* the success status and a **sample JSON body**,
* the error statuses and their bodies (`400`, `403`, `404`),
* a copy-pasteable example request (`curl` or Postman).

````markdown
### GET /search?location=London

**200 OK**
```json
{"cafes": [{"id": 2, "name": "Cafe Mocha", "location": "London", …}]}
```

**404 Not Found**
```json
{"error": {"Not Found": "Sorry, we don't have a cafe at that location."}}
```
````

---

### 4. Put It Where Users Will Find It

| Option | Good for |
|--------|----------|
| The `/` home page of the API | quick, human-friendly, zero setup |
| `README.md` in the repo | developers already there |
| A docs page (`/docs`) rendered from a template | nicest for larger APIs |
| OpenAPI / Swagger | industry standard, generates clients |

The course approach: render a documentation page from a Flask template, listing each
endpoint with its example request and response.

---

### 5. Maintenance Rules

* Update the docs in the **same commit** as the code change.
* Keep example values realistic (real locations, real prices).
* Note authentication requirements prominently — nothing wastes more time than a `403`
  nobody warned you about.

---

### Summary Checklist

1. Every endpoint documented: method, path, params, auth, success and error responses.
2. Include sample JSON and a copy-paste example request.
3. Serve docs at a discoverable place (`/`, README, `/docs`).
4. Docs drift fast — update them with the code, or they become lies.
