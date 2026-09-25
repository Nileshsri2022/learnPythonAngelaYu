Here is a structured breakdown of the Hirst Painting project, Part 2 — drawing the dots.

---

### 1. The Painting Logic

A 10×10 grid of 20-pixel dots with 50-pixel spacing, drawing left-to-right then jumping
back (without drawing!) to the start of the next row:

```python
import random
import turtle
from turtle import Turtle

turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
              (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
              (198, 91, 17), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (160, 142, 158), (54, 45, 50),
              (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89)]

timmy.setheading(225)      # move to the bottom-left corner first
timmy.forward(300)
timmy.setheading(0)

for dot_count in range(1, 101):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:            # end of a row
        timmy.setheading(270)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
```

---

### 2. The Techniques Inside

* `dot(size, color)` — stamps a dot *without needing pendown*.
* `dot_count % 10 == 0` — the modulo trick (Day 3!) detecting end-of-row.
* Pen stays **up** the entire time — pure stamping, no lines.

---

### Summary Checklist

1. `dot()` stamps colour; `penup()` keeps the canvas clean.
2. Every 10th dot → carriage return with `setheading()` manoeuvres.
3. Real extracted palette → a genuine Hirst-style artwork.
