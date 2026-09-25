# Variable Naming

---

### 1. The Golden Rule: Make It Readable

You *can* name a variable almost anything — `name`, `n`, `l` — as long as you use it
consistently. But `n` and `l` mean nothing when you come back to the code in 6 or 12 months.
**Pick names that describe the data they hold.**

---

### 2. The Naming Rules

```python
user_name = "Angela"   # ✅ multiple words joined with underscores
length1 = 10           # ✅ numbers are fine (but not first)
```

* **Multiple words:** separate them with an **underscore** — `user_name`.
  Spaces are **not allowed**: `user name` is a `SyntaxError`.
* **Numbers:** allowed in the name, but **not at the start** — `1length` is a `SyntaxError`.

> This style of `snake_case` naming is the Python convention.

---

### 3. Don't Reuse Function Names

Avoid naming variables after built-in functions like `print` or `input`:

```python
input = "Angela"   # bad idea
```

* The syntax highlighting immediately gets confused — it colours it like the function.
* It might still run, but it's very confusing and can break things later. Bad practice.

> **Tip:** Healthy variable names get highlighted in the *same colour* as your other
> variables. If the colour changes, you've probably shadowed a function name.

---

### 4. Typos Cause `NameError`s

If you define a variable `name` and later misspell it as `nama`:

```python
name = "Angela"
print(nama)   # NameError: name 'nama' is not defined
```

* Python is **not** spell-checking you — if you'd called it `nama` everywhere, it would work fine.
* A `NameError` means: *this name was never defined*. Check the line number in the error and fix the spelling.

---

### Summary Checklist

1. Readable, descriptive names beat short cryptic ones.
2. `snake_case` with underscores; no spaces; numbers never first.
3. Never name variables after functions (`print`, `input`, …).
4. `NameError` = a name that doesn't exist — usually a typo.
