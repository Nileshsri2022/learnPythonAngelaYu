# The Python Dictionary- Deep Dive

---

### 1. What is a Dictionary?

Like a real dictionary: you look up a **word** (key) and find its **definition** (value).
Dictionaries group and **tag** related pieces of information:

```python
programming_dictionary = {
    "Bug": "An error in a program that prevents it from running as expected.",
    "Function": "A block of reusable code that performs a task.",
    "Loop": "The action of doing something over and over again.",
}
```

* Written with `{}`, each entry is `key: value`, separated by commas.
* Keys act like the *labels*; values are the actual data.

---

### 2. Looking Things Up

Retrieve a value with square brackets — using the **key**, not an index:

```python
print(programming_dictionary["Bug"])
# An error in a program that prevents it from running as expected.
```

> **Warning:** Looking up a key that doesn't exist raises a **KeyError** — unlike a
> list's IndexError, it's about missing *labels*, not positions.

---

### 3. Adding and Editing Entries

Assign to a key — new key = add; existing key = overwrite:

```python
programming_dictionary["Loop"] = "A sequence of instructions that repeats."  # edit
programming_dictionary["Variable"] = "A name attached to a piece of data."   # add
```

---

### 4. Looping Through a Dictionary

Looping yields the **keys**; use them to reach the values:

```python
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
```

---

### 5. Lists vs. Dictionaries

| | List | Dictionary |
|---|------|-----------|
| Ordered by | index number (0, 1, 2…) | key (any label you choose) |
| Lookup | `list[3]` | `dict["name"]` |
| Best for | ordered collections | labelled, related data |

---

### Summary Checklist

1. `{key: value}` pairs; fetch with `dict[key]`.
2. Assigning to a key adds or overwrites.
3. `for key in dict:` loops the keys.
4. Missing key → `KeyError`.
