# Functions with Outputs

---

### 1. The Three Flavours of Functions

```python
# 1. Plain function — just does something
def greet():
    print("Hello")

# 2. Function with inputs — works with data you pass in
def greet_with(name):
    print(f"Hello {name}")

# 3. Function with OUTPUT — hands data back to the caller
def greet_and_return(name):
    return f"Hello {name}"
```

---

### 2. The `return` Keyword

`return` **sends a value back** to the line that called the function:

```python
def format_name(f_name, l_name):
    return (f_name + " " + l_name).title()

full_name = format_name("aDaM", "sMiTh")
print(full_name)          # Adam Smith
```

* Without `return`, the result exists only inside the function (`print` just *displays* it).
* With `return`, the caller can store it in a variable, do maths with it, pass it on…

> **Warning:** `return` **ends the function immediately** — any code after it in the
> body never runs.

---

### 3. Returning vs. Printing

| `print()` | `return` |
|-----------|----------|
| Shows text in the console | Hands a value back to the caller |
| Result is unusable afterwards | Result can be stored and reused |
| For humans | For other code |

Rule of thumb: functions should **return** data and let the caller decide whether to print it.

---

### Summary Checklist

1. `return value;` sends the function's output back to the call site.
2. Code after a `return` is unreachable.
3. `print` ≠ `return` — one is for displaying, the other for computing.
