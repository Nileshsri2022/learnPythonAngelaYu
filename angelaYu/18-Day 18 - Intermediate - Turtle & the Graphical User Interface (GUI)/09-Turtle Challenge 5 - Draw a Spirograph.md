# Turtle Challenge 5 - Draw a Spirograph

---

### 1. The Task

A **spirograph**: circles drawn at regular rotations around a centre point, each in a
random RGB colour — a hypnotic geometric flower.

---

### 2. The Solution

```python
import random
import turtle
from turtle import Turtle

turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)          # draw a circle of radius 100
        timmy.setheading(timmy.heading() + size_of_gap)   # rotate a bit

draw_spirograph(5)
```

* `circle(radius)` — draws a full circle with the current heading.
* `heading()` — the turtle's current angle; adding the gap rotates the *next* circle.
* `360 / gap` circles fill the full turn.

---

### Summary Checklist

1. Spirograph = circles + small rotations between them.
2. `heading() + gap` accumulates the rotation across the loop.
3. Gap size controls the density of the pattern.
