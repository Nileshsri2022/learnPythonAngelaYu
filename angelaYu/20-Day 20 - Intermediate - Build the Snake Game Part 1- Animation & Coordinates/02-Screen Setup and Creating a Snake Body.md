# Screen Setup and Creating a Snake Body

---

### 1. Setting Up the Screen

```python
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)      # turn off automatic animation (used for smooth movement)
```

* Keyword arguments (`width=600`) make the setup self-documenting.
* `tracer(0)` freezes automatic drawing — we control when the screen refreshes
  (essential for flicker-free game animation).

---

### 2. Creating the Snake Body

The starting snake is **three squares** — three separate `Turtle` objects:

```python
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()          # no drawing lines — pure game pieces
    new_segment.goto(position)
    segments.append(new_segment)
```

* Each segment is its own **instance** (Day 19) with its own coordinates.
* `penup()` so the pieces move without leaving trails.

---

### Summary Checklist

1. `Screen` = the game window; `setup/bgcolor/title` configure it.
2. `tracer(0)` + manual updates = smooth animation.
3. Snake body = a **list** of turtle instances placed at spaced coordinates.
