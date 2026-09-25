Here is a structured breakdown of everything covered in this lesson on mathematical operations in Python.

---

### 1. The Arithmetic Operators

| Operation | Symbol | Example | Result |
|-----------|--------|---------|--------|
| Addition | `+` | `7 + 3` | `10` |
| Subtraction | `-` | `7 - 3` | `4` |
| Multiplication | `*` | `3 * 2` | `6` |
| Division | `/` | `6 / 3` | `2.0` |
| Floor division | `//` | `6 // 3` | `2` |
| Exponent (power) | `**` | `2 ** 3` | `8` |

Note that multiplication uses the **asterisk `*`**, not `×`, and division uses the
**forward slash `/`**, not `÷`.

---

### 2. Division Always Returns a Float

```python
print(6 / 3)          # 2.0  — a float, even though it divides cleanly
print(type(6 / 3))    # <class 'float'>
```

Python does this **implicit type conversion** automatically: `/` always produces a float.

---

### 3. Floor Division `//`

The double-slash operator divides and then **removes all the decimal places**:

```python
print(6 // 3)   # 2
print(5 // 3)   # 1   (5 / 3 is 1.66… — everything after the point is wiped)
```

> **Warning:** `//` floors the number rather than rounding it — be careful when
> precision matters (e.g. scientific work).

---

### 4. Exponents `**`

Two asterisks mean "to the power of":

```python
print(2 ** 3)   # 8
```

---

### 5. Order of Operations (PEMDAS)

Python follows standard mathematical priority:

**P**arentheses → **E**xponents → **M**ultiplication/**D**ivision → **A**ddition/**S**ubtraction

```python
print(3 * 3 + 3 / 3)    # 10.0  (× and / before +)
print(3 * (3 + 3) / 3)  # 6.0   (parentheses first)
```

Use **parentheses** to make the order explicit and the code readable.

---

### Summary Checklist

1. `+ - * /` for add, subtract, multiply, divide; `**` for powers.
2. `/` always gives a **float**; use `//` when you want an int (decimal places chopped).
3. Python maths follows **PEMDAS** — parentheses win.
