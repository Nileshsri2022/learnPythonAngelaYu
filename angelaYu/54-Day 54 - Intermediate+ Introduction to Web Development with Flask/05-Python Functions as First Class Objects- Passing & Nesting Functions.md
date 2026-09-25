Here is a structured breakdown of this lesson on functions as first-class objects.

---

### 1. Recap: What a Function Has

* Functionality (a block of code).
* Inputs (parameters).
* Outputs (`return`) — which can be fed into another function.

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
```

---

### 2. Functions Are First-Class Objects

In Python, a function is just another object — it can be passed as an argument exactly
like an `int`, `str` or `float`.

```python
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

print(calculate(multiply, 2, 3))   # 6
print(calculate(add, 2, 3))        # 5
```

* `multiply` (no brackets) is the **function object** being handed over.
* `calc_function(n1, n2)` is where it gets **called**.

> **Note:** `calculate` is a **higher-order function** — it takes another function as an
> input. This is the idea behind Day 19's higher-order functions.

---

### 3. Nested Functions

Functions can be defined inside other functions:

```python
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()


outer_function()      # I'm outer  /  I'm inner
nested_function()     # NameError: name 'nested_function' is not defined
```

* The inner function is only in scope *inside* the outer one (indentation = nesting).
* Calling it from outside raises `NameError`.

---

### 4. Returning a Function

A function can return another function — *without* calling it:

```python
def outer_function():
    def inner_function():
        print("I'm inner")
    return inner_function          # note: no parentheses


my_function = outer_function()     # nothing printed yet
my_function()                      # now it prints "I'm inner"
```

---

### 5. Why This Matters for Flask

These four facts —

1. functions take inputs and return outputs,
2. functions are first-class objects,
3. functions can be nested,
4. functions can be returned from functions,

— are exactly what you need to understand **decorators**, which is the `@app.route("/")`
syntax you've been using since your first Flask app.

---

### Summary Checklist

1. Functions are objects: pass them by name, call them with parentheses.
2. A function that takes/returns a function is a higher-order function.
3. Nested functions live only inside their parent — call them from within.
4. Returning a function returns the object; adding `()` would call it instead.
5. These four properties are the foundation of decorators (next lesson).
