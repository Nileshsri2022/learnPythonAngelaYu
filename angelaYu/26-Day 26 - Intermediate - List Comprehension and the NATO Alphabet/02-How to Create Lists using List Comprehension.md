Here is a structured breakdown of this lesson on list comprehension.

---

### 1. The Pattern

A list comprehension builds a list **in one expression**:

```python
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]     # [2, 3, 4]
```

Read it right-to-left: *for every `n` in `numbers`, put `n + 1` in the new list.*

It replaces this classic loop:

```python
new_list = []
for n in numbers:
    new_list.append(n + 1)
```

---

### 2. Comprehension with Conditions

`if` **after** the loop filters which items enter:

```python
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]      # Alex, Beth, Dave
long_upper = [name.upper() for name in names if len(name) > 5]
# CAROLINE, ELEANOR, FREDDIE
```

> **Warning:** Order matters! `if` *before* the `for` is a different construct
> (if/else per item): `[n if n > 0 else 0 for n in nums]`. Filtering puts the `if`
> **after** the `for`.

---

### Summary Checklist

1. `[expression for item in iterable]` — the Pythonic loop-in-a-line.
2. Add `if condition` after the loop to filter.
3. Any expression fits, including method calls like `.upper()`.
