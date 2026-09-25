# Create a Snake Class & Move to OOP

---

### 1. Extracting a `Snake` Class

All snake-related state and behaviour moves into `snake.py`:

```python
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
```

Note the constants in **ALL_CAPS** — global scope constants (Day 12).

---

### 2. The Clean Main File

`main.py` now reads like the game's story:

```python
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
```

* `from snake import Snake` — your own file as a module (Day 4/7).
* The plan: three classes in three files — `Snake`, `Food`, `Scoreboard` — each
  managing exactly one thing.

---

### Summary Checklist

1. Encapsulation: the snake owns its segments and its movement.
2. Constants (positions, distances) at module top in ALL_CAPS.
3. main.py = setup + game loop + object coordination only.
