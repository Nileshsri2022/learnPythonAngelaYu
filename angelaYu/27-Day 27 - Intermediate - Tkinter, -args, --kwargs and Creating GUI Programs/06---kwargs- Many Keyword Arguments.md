# kwargs- Many Keyword Arguments

---

### 1. Unlimited *Keyword* Arguments

```python
def calculate(n, **kwargs):
    print(kwargs)            # {'add': 3, 'multiply': 2}
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    print(n)

calculate(2, add=3, multiply=5)   # 25
```

`**kwargs` collects extra **keyword** arguments into a **dictionary**: keyword → value.

---

### 2. Safe Access

Use `.get()` instead of `[]` — a missing keyword returns `None` instead of raising
`KeyError`:

```python
n += kwargs.get("add", 0)     # default 0 if 'add' wasn't passed
```

---

### 3. Why This Explains Tkinter

`Label(text="hi", font=("Arial", 24), bg="black")` — Tkinter's widgets accept any of
dozens of optional settings because their `__init__` takes `**kwargs` and applies whatever
arrives. Now every odd-looking library call makes sense.

---

### Summary Checklist

1. `**kwargs` = dict of keyword arguments.
2. `kwargs.get(key, default)` for safe reads.
3. Widgets and configs are powered by `*args`/`**kwargs`.
