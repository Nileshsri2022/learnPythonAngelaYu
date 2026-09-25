Here is a structured breakdown of this lesson on `*args` and `**kwargs` in decorators.

---

### 1. The Problem

A wrapper that calls `function()` breaks the moment the wrapped function takes
arguments. The fix: accept anything, forward everything:

```python
def logging_decorator(function):
    def wrapper(*args, **kwargs):          # catch all positional/named args
        print(f"You called {function.__name__}{args}")
        result = function(*args, **kwargs)  # forward them untouched
        print(f"It returned: {result}")
        return result
    return wrapper

@logging_decorator
def add(a, b):
    return a + b

add(2, 3)   # logs: You called add(2, 3) / It returned: 5
```

* `*args` — extra positional arguments, as a tuple.
* `**kwargs` — extra keyword arguments, as a dict.
* Unpack with the same `*`/`**` when forwarding.

---

### 2. Where You've Seen It

Flask's own decorators do exactly this — `@app.route` wraps your view function whatever
its signature (that's how `<name>` path variables reach it).

---

### Summary Checklist

1. `wrapper(*args, **kwargs)` → call `function(*args, **kwargs)`.
2. Any decorator now works on any function.
