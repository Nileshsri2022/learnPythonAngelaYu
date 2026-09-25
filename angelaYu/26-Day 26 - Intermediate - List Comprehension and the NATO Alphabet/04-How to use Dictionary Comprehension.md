# How to use Dictionary Comprehension

---

### 1. The Pattern

Build a dictionary in one expression:

```python
{new_key: new_value for item in list}
{new_key: new_value for (key, value) in dict.items()}
{new_key: new_value for (key, value) in dict.items() if condition}
```

---

### 2. Examples

```python
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# from a list — name → name length
students_scores = {name: len(name) for name in names}
# {'Alex': 4, 'Beth': 4, 'Caroline': 8, ...}

# from a dict — keep only passed students
passed = {"Alex": 65, "Beth": 40, "Caroline": 82}
passed_students = {student: score for (student, score) in passed.items() if score >= 60}
# {'Alex': 65, 'Caroline': 82}
```

* Iterating `.items()` gives `(key, value)` tuples you unpack in the comprehension.
* The trailing `if` filters entries exactly like list comprehensions.

---

### Summary Checklist

1. `{key_expr: value_expr for item in iterable}`.
2. `.items()` + unpacking transforms existing dicts.
3. Filter with `if` after the loop.
