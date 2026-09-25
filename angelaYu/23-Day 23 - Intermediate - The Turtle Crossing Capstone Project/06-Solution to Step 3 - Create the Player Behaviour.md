# Solution to Step 3 - Create the Player Behaviour

---

### 1. The `Player` Class

```python
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)          # face north

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
```

* `setheading(90)` once at start — `forward()` then always moves **up**.
* `is_at_finish_line()` returns a Boolean — the main loop asks, the player answers
  (the Day 17 QuizBrain pattern).

---

### 2. The Binding

```python
screen.listen()
screen.onkey(player.move_up, "Up")
```

---

### Summary Checklist

1. Player = turtle facing north with a fixed step size.
2. Finish detection as a method returning True/False.
3. `go_to_start()` doubles as the reset on level-up.
