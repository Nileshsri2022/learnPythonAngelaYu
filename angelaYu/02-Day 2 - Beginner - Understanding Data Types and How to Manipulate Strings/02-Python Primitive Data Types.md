Here is a structured breakdown of everything covered in this lesson on Python's primitive data types.

---

### 1. The Four Primitive Data Types

| Type | Name | Example | Written as |
|------|------|---------|------------|
| `str` | String | `"Hello"` | Quotes around characters |
| `int` | Integer | `123` | Whole numbers, no quotes |
| `float` | Floating point | `3.14159` | Decimal numbers |
| `bool` | Boolean | `True` / `False` | Capitalised, no quotes |

```python
print(type("Hello"))   # <class 'str'>
print(type(123))       # <class 'int'>
print(type(3.14159))   # <class 'float'>
print(type(True))      # <class 'bool'>
```

---

### 2. Strings (`str`)

A string is a **string of characters**, always created with quotes. Individual characters
can be pulled out with **subscripting** — square brackets containing an **index**:

```python
print("Hello"[0])   # H
print("Hello"[4])   # o
```

> **Warning:** Programmers count from **zero**. The *first* character is at index `0`,
> the second at index `1`, and so on.

---

### 3. Integers (`int`)

Whole numbers, positive or negative, no decimal point. You can write large numbers with
underscores for readability — Python ignores them:

```python
print(123_456_789)   # 123456789
```

---

### 4. Floats (`float`)

Numbers with a decimal point. Even `2.0` is a float.

---

### 5. Booleans (`bool`)

Only two possible values — `True` or `False` (capital first letter in Python):

```python
is_raining = True
```

---

### 6. Data Types Have Rules — The `TypeError`

`len()` counts the characters of a **string** — it can't count the "digits" of an int:

```python
len("hello")   # 5  ✅
len(12345)     # TypeError: object of type 'int' has no len() ❌
```

A **TypeError** happens when you give a function data of the wrong type. The fix is
**type conversion** — the topic of the next lesson.

---

### Summary Checklist

1. Four primitive types: **str, int, float, bool** — check any of them with `type()`.
2. Strings can be subscripted with `[index]`, counting from **0**.
3. Underscores make big ints readable (`123_456_789`).
4. Wrong type into a function → **TypeError**.
