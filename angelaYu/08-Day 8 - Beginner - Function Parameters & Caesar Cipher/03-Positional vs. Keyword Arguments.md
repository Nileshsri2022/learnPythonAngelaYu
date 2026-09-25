Here is a structured breakdown of everything covered in this lesson on positional vs. keyword arguments.

---

### 1. Functions with Multiple Inputs

Separate parameters with commas:

```python
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
```

Now there are two ways to supply the arguments.

---

### 2. Positional Arguments

Values are matched **by position** — first argument goes to the first parameter, and so on:

```python
greet_with("Angela", "London")
# Hello Angela
# What is it like in London?
```

> **Warning:** Position is everything. Swap them and the meaning silently breaks:

```python
greet_with("London", "Angela")
# Hello London
# What is it like in Angela?   ← nonsense, but no error!
```

---

### 3. Keyword Arguments

Match values to parameters **by name**, so order doesn't matter:

```python
greet_with(location="London", name="Angela")
# Hello Angela
# What is it like in London?
```

Keyword arguments make calls self-documenting — especially useful for functions with many
parameters.

---

### Summary Checklist

1. Multiple parameters: `def f(a, b):` — comma-separated.
2. **Positional** = matched by order (can silently misalign).
3. **Keyword** = matched by name (`name="Angela"`), immune to reordering.
