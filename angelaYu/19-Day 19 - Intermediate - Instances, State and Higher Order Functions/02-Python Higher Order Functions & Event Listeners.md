# Python Higher Order Functions & Event Listeners

---

### 1. Higher-Order Functions

A **higher-order function** is a function that *works with other functions* — taking one
as input or returning one. You've secretly used them forever:

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

# calculator is higher-order: it receives a FUNCTION as an argument
def calculator(n1, n2, func):
    return func(n1, n2)

result = calculator(3, 5, add)      # 8  — note: `add`, not `add()`
```

* Pass the function **by name** — `add` — not `add()` (which would call it immediately).

---

### 2. Event Listeners — a Real Use

GUIs are built on callbacks: *when this happens, call that function*.

```python
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()                       # start catching keyboard events
screen.onkey(fun=move_forwards, key="space")   # bind spacebar → move_forwards
screen.exitonclick()
```

* `onkey` is higher-order: `fun=` receives your function **without calling it**.
* The screen calls your function *later*, when the key is pressed — this is why you pass
  the name, not a call.

---

### Summary Checklist

1. Higher-order functions take functions as arguments (or return them).
2. Event listeners are the flagship example — behaviour registered, triggered later.
3. Pass `function_name`, never `function_name()`, into callbacks.
