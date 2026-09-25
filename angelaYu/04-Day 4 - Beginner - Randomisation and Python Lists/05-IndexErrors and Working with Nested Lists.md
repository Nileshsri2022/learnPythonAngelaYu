# IndexErrors and Working with Nested Lists

---

### 1. The `IndexError`

If you ask for an index the list doesn't have, Python crashes:

```python
states_of_america = ["Delaware", "Pennsylvania", "…", "Hawaii"]
print(len(states_of_america))     # 50 items in the list
print(states_of_america[49])      # Hawaii  ✅ (last valid index is 49!)
print(states_of_america[50])      # IndexError: list index out of range ❌
```

A 50-item list has indexes `0`…`49`. Index 50 is *beyond the end* — there is nothing there.

---

### 2. The Off-By-One Error

The sneakiest version of this bug uses `len()` directly as an index:

```python
number_of_states = len(states_of_america)   # 50
print(states_of_america[number_of_states])  # IndexError! 50 is one past the end
print(states_of_america[number_of_states - 1])  # Hawaii ✅ — the classic -1 fix
```

> **Warning:** This bug hides in large lists where you're not looking at the data.
> Every time you index with a length, think: **length is one more than the last index**.

---

### 3. Nested Lists

A list can contain **other lists** — a bit like spreadsheet rows:

```python
dirty_dozen = [
    ["Strawberries", "Spinach", "Kale"],      # fruits & vegetables
    ["Apples", "Grapes", "Peaches"]           # …another group
]
print(dirty_dozen[0])      # ["Strawberries", "Spinach", "Kale"]
print(dirty_dozen[0][1])   # Spinach — first the row, then the item
```

**Two** sets of square brackets: `list[row][column]` — the first index picks the inner
list, the second picks the item inside it.

---

### Summary Checklist

1. `IndexError: list index out of range` = you asked for an index that doesn't exist.
2. Last valid index = `len(list) - 1`.
3. Nested lists are indexed with `[outer][inner]`.
