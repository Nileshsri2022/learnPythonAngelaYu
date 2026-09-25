# Logical Operators

---

### 1. The Three Logical Operators

They combine or flip Boolean conditions **in a single line of code**:

| Operator | Rule | Example |
|----------|------|---------|
| `and` | `True` only if **both** sides are `True` | `a > 10 and a < 13` |
| `or` | `True` if **at least one** side is `True` | `a < 10 or a > 13` |
| `not` | **Inverts** the Boolean | `not a > 15` |

---

### 2. `and` — Both Must Be True

```python
a = 12
print(a > 10 and a < 13)   # True  (both sides True)
print(a > 15 and a < 13)   # False (one side False)
```

`True and True` → `True`; anything with a `False` → `False`.

---

### 3. `or` — At Least One True

```python
a = 12
print(a < 10 or a > 13)    # False (both sides False)
print(a < 10 or a == 12)   # True  (one side True is enough)
```

`False or False` → `False`; every other combination → `True`.

---

### 4. `not` — Flip It

```python
print(not a > 15)   # True — because a > 15 is False
```

---

### 5. Why This Matters

Logical operators replace clumsy **nested** code with a single readable condition:

```python
# Nested version
if size == "L":
    if add_pepperoni == "Y":

# One-line version with and
if size == "L" and add_pepperoni == "Y":
```

---

### Summary Checklist

1. `and` → both conditions must be `True`.
2. `or` → at least one condition `True`.
3. `not` → inverts the result.
4. Use them to combine conditions on **one line** instead of nesting.
