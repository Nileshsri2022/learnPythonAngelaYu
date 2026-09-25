Here is a structured breakdown of this lesson on decorators and the @ syntax.

---

### 1. A Decorator by Hand

```python
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello!")

# @delay_decorator is exactly equivalent to:
say_hello = delay_decorator(say_hello)
```

The decorator takes a function, returns an upgraded version (here: one that waits
2 seconds first). The **@ syntax** is just shorthand for the reassignment.

---

### 2. A Practical One: Timing

```python
def speed_calc_decorator(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print(f"{function.__name__} took {end - start:.6f}s")
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10_000_000):
        pass
```

That's `@app.route("/")` too: Flask's decorator wraps your function so a request
triggers it. You now understand the `@` — it will appear on every Flask route.

---

### Summary Checklist

1. Decorator = function → wrapped function; `@` = the shorthand.
2. `@app.route` is a decorator — the mystery `@` is solved.
3. Runnable version: [`main.py`](main.py)
