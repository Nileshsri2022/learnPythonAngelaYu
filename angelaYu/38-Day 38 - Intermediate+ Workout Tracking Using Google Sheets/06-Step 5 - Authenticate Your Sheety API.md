Here is a structured breakdown of Step 5 — Sheety authentication.

---

### 1. Protecting the Sheet

By default a Sheety project is public — anyone with the URL can write to your sheet.
Sheety's **Bearer auth** fixes that:

1. In Sheety, set an auth token for the project.
2. Send it on every request:

```python
sheet_headers = {
    "Authorization": "Bearer YOUR_SECRET_TOKEN",
}

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,
                               headers=sheet_headers)
```

* `Authorization: Bearer <token>` — the standard HTTP auth header, same pattern as
  Day 37's `X-USER-TOKEN` but industry-standard.

---

### Summary Checklist

1. Never leave a writeable API public.
2. `Bearer` tokens in the `Authorization` header — the convention to remember.
