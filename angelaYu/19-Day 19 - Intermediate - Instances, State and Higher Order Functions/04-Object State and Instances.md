# Object State and Instances

---

### 1. Each Instance Has Its Own State

Create two turtles — they carry **independent** state:

```python
from turtle import Turtle

tim = Turtle()
tom = Turtle()

tim.color("coral")
tim.setheading(90)      # facing north

tom.color("DarkOrchid")
tom.setheading(270)     # facing south
```

Same class, different objects, different data. An object's **state** is the current
values of all its attributes — and methods *change* state (`forward()` moves *that*
turtle only).

---

### 2. Why This Matters

Games are built on instance state: each enemy has its own position, each player their own
score. When you later write:

```python
segments = []
for _ in range(3):
    segment = Turtle("square")
    segments.append(segment)
```

…each segment is a separate instance whose position the game tracks individually — that's
the snake's body, right there.

---

### Summary Checklist

1. State = an object's attribute values at a moment in time.
2. Instances are independent — mutating one never touches another.
3. Multi-object programs = one class, many instances, each with state.
