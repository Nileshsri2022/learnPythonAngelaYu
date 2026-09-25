# Challenge 2 - Search for a Website in the Password Manager

---

### 1. The `find_password` Function

```python
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,
                                message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",
                                message=f"No details for {website} exists.")
```

Three outcomes, each handled: file missing → info dialog; site found → show
credentials; site unknown → friendly miss.

---

### 2. The Upgrade in Action

The manager went from *write-only* to a **queryable database**:

```text
Website: [google] [Search]
→ pop-up: Email: me@mail.com / Password: abc
```

A dict key-lookup plus dialogs — the JSON structure from lesson 5 doing all the work.

---

### Summary Checklist

1. Search = `json.load` + membership check + `showinfo`.
2. Every branch gets a user-facing response, never a traceback.
3. Fully upgraded version: [`main.py`](main.py)
