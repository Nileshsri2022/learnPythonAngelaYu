# Defining and Calling Python Functions

---

### 1. Functions Are Everywhere Already

You've been *calling* built-in functions all along — `print()`, `input()`, `len()`,
`int()`, `range()`. You can always spot a function by **name + parentheses**. Each one
packages a piece of functionality with a name.

---

### 2. Defining Your Own Function

The `def` keyword defines a new function:

```python
def my_function():
    print("Hello")
    print("Bye")
```

* `def` — keyword that starts the definition.
* `my_function` — the name you choose (same naming rules as variables).
* `()` — empty for now (parameters come on Day 8).
* **Everything indented underneath is inside the function.**

---

### 3. Defining ≠ Running

**Crucially:** defining a function does **nothing** by itself. The body only runs when the
function is **called**:

```python
def my_function():
    print("Hello")
    print("Bye")

my_function()   # call it — NOW the two lines execute
```

Call it again and it runs again — that's the whole point: **write once, use many times.**

---

### 4. Why Bother?

* **Reuse** — ten lines of robot instructions become one `turn_right()` call.
* **Readability** — code is grouped by *what it does*.
* **Less duplication** — fix a bug once, in one place.

> **Tip:** Functions must be **defined before they are called** — Python runs the file
> top to bottom, so put the `def` above the call.

---

### Summary Checklist

1. `def name():` defines; `name()` calls.
2. Indented lines after the colon are the function's body.
3. Definition alone runs nothing — you must call it.
4. Functions exist to reuse and organise code.
