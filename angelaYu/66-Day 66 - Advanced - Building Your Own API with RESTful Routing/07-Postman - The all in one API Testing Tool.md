Here is a structured breakdown of this lesson on Postman.

---

### 1. Why Not Just Use a Browser?

A browser can only really do `GET`. The API also has `POST`, `PATCH` and `DELETE`, plus
headers, JSON bodies and API keys — none of which you can type into an address bar.

**Postman** is a client for talking to APIs: pick the method, set the URL, add a body,
send, and inspect the raw response.

---

### 2. The Workflow

| Field | What to enter |
|-------|---------------|
| Method | GET / POST / PATCH / DELETE |
| URL | `http://127.0.0.1:5000/random` |
| Body (POST/PATCH) | `x-www-form-urlencoded` for form fields, or `raw → JSON` for a JSON payload |
| Params | key/value pairs for query strings (`location` = `London`) |
| Headers | e.g. `api-key` for protected routes |

Send, then read the **status code**, **time** and **body** panes.

---

### 3. What to Check in Every Response

1. **Status code** — 200/201/400/403/404 as expected.
2. **Body** — valid JSON, correct keys, real data.
3. **Headers** — `Content-Type: application/json`.
4. **Error paths** — deliberately send bad input and confirm the error is helpful.

---

### 4. Collections and Environments

* Save requests into a **collection** — your API's living test suite.
* Use **environments/variables** so `{{base_url}}` works for local and deployed versions.
* Write **tests** in the *Tests* tab (assert status code, assert JSON field) and run the
  whole collection at once — a smoke test after every change.

```javascript
pm.test("status is 200", () => pm.response.to.have.status(200));
pm.test("has a cafe", () => pm.response.json().should.have.property("cafe"));
```

---

### 5. Alternatives

`curl` (terminal), Insomnia, Thunder Client (VS Code), or plain `requests` in a script.
The concepts are identical — Postman just makes them visual.

---

### Summary Checklist

1. Postman sends any HTTP method with params, headers and a body.
2. Always test the happy path *and* the error paths.
3. Save requests in collections; parameterise URLs with environments.
4. Postman collections double as regression tests for your API.
