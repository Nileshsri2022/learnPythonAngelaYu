# Write the Ball Class and Make the Ball Move

---

### 1. The `Ball` Class

```python
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
```

* Movement is **diagonal**: every frame adds `x_move` to x and `y_move` to y.
* Storing movement as attributes is the key — *bouncing* will just flip their signs.

---

### 2. Animating It

```python
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
```

The Snake frame loop again — update, delay, move.

---

### Summary Checklist

1. Ball = small circle turtle with `x_move`/`y_move` speed attributes.
2. `move()` = position + speed each frame.
3. Diagonal motion falls out of adding to both axes.
