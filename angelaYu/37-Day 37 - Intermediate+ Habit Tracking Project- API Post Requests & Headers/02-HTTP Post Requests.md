# HTTP Post Requests

The habit tracker starts here: creating **your user account** on Pixela with the first
HTTP verb beyond `GET`.

---

### 1. The Four Verbs

| Verb | Meaning | Example |
|------|---------|---------|
| `GET` | *Give me* data | Fetch the weather, the ISS position |
| `POST` | *Here is* data — save something new | Create a Pixela user, post a tweet |
| `PUT` | *Update* existing data | Change a value in a spreadsheet |
| `DELETE` | *Remove* data | Delete a post |

With GET you care about the response body. With POST you mainly care **whether it
worked** — the response is usually just a status message.

```python
requests.get(url, params={...})        # ask for data
requests.post(url, json={...})         # send data
```

---

### 2. Step 1 of Pixela: Post a New User

Pixela's "get started" guide has six steps; step 1 POSTs to the user endpoint:

```python
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": "mytoken1234567890",    # your own secret — 8 to 128 characters
    "username": "angela",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)                 # the response as plain text is enough here
```

* The data travels in the request **body**, passed with the `json=` keyword argument.
* The **token** is a key you generate yourself. It is used for every later request —
  it is effectively your Pixela password. Store it safely.
* Usernames must be unique; the docs' required fields are all mandatory.

---

### 3. Reading the Response

A successful run prints a success message; running it a second time prints something
like *"this user already exists"*. Saying `no` to the terms or being a minor returns a
different explanation. That is the point — the response text tells you **why** a POST
failed, which is exactly what you need while learning a new API.

Once the user exists, **comment out** that request: the account is created, and
re-posting it would only produce errors.

---

### Summary Checklist

1. GET reads, POST creates, PUT updates, DELETE removes.
2. `requests.post(url, json=payload)` — the payload is the request body.
3. Pixela step 1 needs `token`, `username`, `agreeTermsOfService`, `notMinor`.
4. Your self-generated `token` (8–128 chars) is your password for every next call.
5. Print `response.text` while experimenting — failures explain themselves.
