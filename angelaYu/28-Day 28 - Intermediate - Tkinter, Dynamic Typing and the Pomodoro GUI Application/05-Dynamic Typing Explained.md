Here is a structured breakdown of this lesson on dynamic typing.

---

### 1. What Dynamic Typing Means

Python checks types **at runtime**, and a name can point to *any* type over its life:

```python
n = 5            # int
n = "five"       # str — perfectly legal
```

vs. statically-typed languages (Java, C++) where a variable's type is fixed forever.

---

### 2. The Power and the Danger

```python
# Power: flexible functions
def add(a, b):
    return a + b

add(2, 3)        # 5
add("a", "b")    # "ab" — same operator, different types

# Danger: type errors surface only when the code runs
def display_time(count):
    return f"{count // 60}"    # crashes if count is a string
```

The Pomodoro timer is a live case study: `count - 1` breaks the moment `count` arrives
as text, and `f"{seconds:02d}"` demands an int. Mixing `str(count)` with ints silently
corrupts state.

---

### 3. Taming It

* Convert deliberately at boundaries: `int(entry.get())`, `str(score)`.
* Keep one canonical type per variable's purpose.
* Day 34 introduces **type hints** (`def f(x: int) -> str:`) — documentation the editor
  can check.

---

### Summary Checklist

1. Types attach to *values*, not names — variables can be retyped.
2. Flexibility = runtime type errors instead of compile errors.
3. Convert explicitly; later, document with type hints.
