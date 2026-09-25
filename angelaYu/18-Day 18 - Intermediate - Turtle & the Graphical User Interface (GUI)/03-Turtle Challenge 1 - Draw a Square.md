# Turtle Challenge 1 - Draw a Square

---

### 1. The Task

Make the turtle draw a **square** — the first shape every turtle programmer draws.

---

### 2. The Solution

```python
from turtle import Turtle

timmy = Turtle()

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)
```

* A square = **four** sides with a **90°** turn between them.
* `for _ in range(4):` — the underscore convention says the counter itself is unused.

> **Note:** `right(90)` turns the *turtle*; exterior angles are what matter for shapes.

---

### Summary Checklist

1. Shape = loop of (move, turn).
2. Square: 4 sides, right angles.
3. Underscore loop variable for "just repeat N times".
