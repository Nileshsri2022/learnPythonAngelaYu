# Raising your own Exceptions

---

### 1. The `raise` Keyword

Your code can **throw** exceptions when its own rules are violated:

```python
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
```

* `raise ExceptionType("message")` — pick a built-in type (`ValueError`, `TypeError`,
  `KeyError`…) that matches the mistake.
* The message appears in the traceback, exactly like Python's own errors.

---

### 2. Why Raise Instead of Print?

* A printed warning is **ignorable**; an exception is a loud, catchable event.
* Calling code can `try`/`except` your exceptions and decide what to do — that's how
  libraries report problems to applications.

---

### Summary Checklist

1. `raise` = fail loudly with a typed, descriptive error.
2. Choose the exception type that names the problem class.
3. Exceptions are APIs: callers handle what you raise.
