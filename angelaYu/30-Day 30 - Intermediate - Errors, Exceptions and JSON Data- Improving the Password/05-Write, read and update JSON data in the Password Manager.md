# Write, read and update JSON data in the Password Manager

---

### 1. Why JSON?

`data.txt` lines like `google | me@mail.com | abc` are readable but not **searchable**.
**JSON** (JavaScript Object Notation) stores structured data that maps directly onto
Python dictionaries:

```json
{"google": {"email": "me@mail.com", "password": "abc"}}
```

---

### 2. The Three Methods

```python
import json

# WRITE — dump a dict to a file
data = {"website": {"email": "x", "password": "y"}}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# READ — load a file into a dict
with open("data.json", "r") as f:
    data = json.load(f)

# UPDATE — read, modify, dump back
with open("data.json", "r") as f:
    data = json.load(f)
data["new_site"] = {"email": "a", "password": "b"}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

* `json.dump(obj, file)` — Python → file.
* `json.load(file)` — file → Python dict.
* Update = the read-modify-write cycle.

---

### 3. The Password Manager's New Save

```python
new_data = {website: {"email": email, "password": password}}
try:
    with open("data.json", "r") as f:
        data = json.load(f)            # existing entries
except FileNotFoundError:
    data = {}                          # first run — no file yet
data.update(new_data)
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

---

### Summary Checklist

1. JSON ↔ dict is the bridge between program state and disk.
2. `dump`/`load`/update cycle for persistent structured data.
3. `indent=4` keeps the file human-readable.
