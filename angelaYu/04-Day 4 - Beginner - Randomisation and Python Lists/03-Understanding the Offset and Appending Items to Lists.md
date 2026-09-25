# Understanding the Offset and Appending Items to Lists

---

### 1. What is a List?

A **list** is a **data structure** — a way of organising and storing data. Single variables
hold one value each; a list holds **many related values in order** (e.g. all 50 US states,
or the order of people in a queue).

```python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
```

* Starts with `[`, ends with `]`, items separated by commas.
* Items can be **any data type**, even mixed — strings, numbers, booleans.

---

### 2. Indexing and the Offset

Access a single item with square brackets and its **index** — and remember, counting
**starts at 0**:

```python
print(states_of_america[0])    # Delaware   (first item)
print(states_of_america[3])    # Georgia    (fourth item)
```

The index is called the **offset** because it counts how far the item sits from the start
of the list. That's also why you can edit an item in place:

```python
fruits = ["Apple", "Peach", "Pear"]
fruits[0] = "Banana"     # replaces Apple with Banana
```

And to get the *last* item without knowing the list's length:

```python
print(fruits[-1])   # Pear — negative indexes count from the end
```

---

### 3. Adding Items: `append()` and `extend()`

**`append()`** adds **one** item to the end of the list:

```python
fruits = ["Apple", "Peach", "Pear"]
fruits.append("Strawberry")
# ["Apple", "Peach", "Pear", "Strawberry"]
```

**`extend()`** adds **many** items (one list onto another):

```python
fruits.extend(["Grape", "Mango"])
# ["Apple", "Peach", "Pear", "Strawberry", "Grape", "Mango"]
```

> **Note:** `append()` adds its argument as a *single* item — appending a list would put
> a whole list *inside* your list. Use `extend()` when you want the items themselves.

---

### Summary Checklist

1. Lists store **ordered**, related data — `["a", "b", "c"]`.
2. Index (offset) starts at **0**; negative indexes count from the end.
3. `list.append(x)` adds one item; `list.extend([x, y])` adds several.
