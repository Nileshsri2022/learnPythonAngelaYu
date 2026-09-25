# Challenge 1 - Handling Exceptions in the Password Manager

---

### 1. The Crashes to Fix

1. **Save/Search before any file exists** → `FileNotFoundError`.
2. The user's first save must *create* the file.

---

### 2. The Solutions

**On save:**

```python
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}                        # nothing saved yet
finally:
    data.update(new_data)
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
```

**On search:**

```python
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    messagebox.showinfo(title="Error", message="No Data File Found.")
```

* Empty-file `json.load` also raises (`JSONDecodeError`) — deleting the file or an empty
  `data.json` must be survivable too.

---

### Summary Checklist

1. Missing-file is an *expected* state for first runs — catch it, don't crash.
2. `finally` carries the write-back on save.
3. Every file touchpoint gets its own guard.
