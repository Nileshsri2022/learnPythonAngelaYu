Here is a structured breakdown of this lesson on Python decorators and the `@` syntax.

---

### 1. What Is a Decorator?

A **decorator** is a function that wraps another function and gives it extra
functionality — running code before it, after it, modifying how often it's called, or
adding behaviour the original author never wrote.

Motivation: adding the same extra behaviour (a delay, logging, timing) to many functions
by copy-paste is a maintenance nightmare.

---

### 2. The Pattern

```python
import time
from functools import wraps


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)             # do something BEFORE
        function()                # call the original
        # ...and/or something AFTER
    return wrapper_function       # no parentheses — return the function itself
```

Use it three ways:

```python
@delay_decorator                  # 1. syntactic sugar
def say_hello():
    print("hello")


def say_bye():
    print("bye")


say_bye = delay_decorator(say_bye)   # 2. the long way — same thing

decorated = delay_decorator(lambda: print("hi"))   # 3. on any callable
decorated()
```

Both forms are equivalent; the `@` is just nicer to read — it's *syntactic sugar*.

---

### 3. Running It

```python
say_hello()      # waits 2 seconds, then "hello"
say_bye()        # name resolution picks the decorated version
```

Decorators can also:

* run the function **twice**,
* **measure** its runtime,
* **retry** it when it fails (Day 49's resilience wrapper).

---

### 4. Decorators That Take Arguments

When the wrapped function has inputs, the wrapper must pass them along:

```python
def retry(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception:
            return function(*args, **kwargs)     # one retry
    return wrapper


@retry
def greet(name):
    print(f"Hello {name}")


greet("Ada")      # the wrapper forwards the argument
```

* `*args, **kwargs` accept whatever the original function expects.
* `@wraps` keeps the original function's `__name__` and docstring (otherwise it becomes
  `wrapper`, which breaks debugging).

---

### 5. Back to Flask

```python
@app.route("/")
def home():
    return "Hello, World!"
```

Read it as: "take `home`, register it with Flask so it runs when someone requests `/`".
`@app.route` isn't delaying or wrapping output — it *registers a route* — but the mechanics
are identical to `delay_decorator`: a function receives your function and does something
with it.

---

### Summary Checklist

1. Decorator = function that wraps a function to add/change behaviour.
2. The decorated function is passed in; the wrapper is returned *without* parentheses.
3. `@decorator` is syntactic sugar for `func = decorator(func)`.
4. Wrappers for functions with inputs need `*args, **kwargs` (and `@wraps`).
5. Flask's `@app.route("/")` is a decorator that registers the function as a URL handler.
