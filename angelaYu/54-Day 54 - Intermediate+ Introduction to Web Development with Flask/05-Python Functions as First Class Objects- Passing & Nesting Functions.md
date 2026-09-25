Here is a structured breakdown of this lesson on functions as first-class objects.

---

### 1. The Four Function Powers

```python
def greet():          # 1. functionality
    return "Hello!"

def run_function(f):  # 2. pass a function as an argument
    return f()

def outer():          # 3. nest a function
    def inner():
        return "I'm inside!"
    return inner      # 4. return it *without* calling it

my_greeting = outer() # my_greeting IS inner
print(my_greeting())
```

* Functions are objects: assignable, passable, returnable — **no parentheses** when
  passing/returning (you move the function itself, not its result).
* `outer()` returns the inner function; `outer()()` calls it.

---

### Summary Checklist

1. Functions = objects: pass, nest, return them.
2. No parentheses = hand over the function; parentheses = call it.
