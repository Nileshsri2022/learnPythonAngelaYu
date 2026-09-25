# Write the Paddle Class and Create the Second Paddle

---

### 1. The `Paddle` Class

One class, two instances — the OOP pattern from the turtle race (Day 19):

```python
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
```

Note the **constructor parameter** — position is passed in, not hard-coded.

---

### 2. Two Instances, Four Bindings

```python
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
```

Zero duplicated code — the second paddle is one more line.

---

### Summary Checklist

1. `Paddle(Turtle)` takes its starting `position` as an argument.
2. Methods use `self` — each paddle moves independently.
3. Player 2 gets `w`/`s`; Player 1 keeps the arrows.
