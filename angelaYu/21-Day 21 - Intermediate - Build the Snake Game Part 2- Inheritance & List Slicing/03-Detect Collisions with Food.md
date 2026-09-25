Here is a structured breakdown of this lesson on detecting collisions with food.

---

### 1. The `Food` Class

A food is a small blue circle that is also a turtle — **inheritance in action**:

```python
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)   # half-size
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
```

---

### 2. Detecting the Bite

In `main.py`'s game loop — a **distance check** between head and food:

```python
if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
```

`distance(other_turtle)` measures in pixels; anything under 15 counts as "eaten".

On a bite, three things happen: food **relocates**, snake **grows** (`extend()` adds a
segment at the tail's position), scoreboard **increments**.

---

### Summary Checklist

1. `Food(Turtle)` — child class with a `refresh()` behaviour.
2. Collision = `snake.head.distance(food) < 15`.
3. One bite = relocate + extend + score — three objects coordinating.
