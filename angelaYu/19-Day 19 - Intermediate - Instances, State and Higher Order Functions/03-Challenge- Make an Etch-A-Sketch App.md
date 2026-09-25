Here is a structured breakdown of the Etch-A-Sketch challenge.

---

### 1. The Task

Recreate Etch-A-Sketch: the **arrow keys** steer the drawing, `W/S/A/D` clear it:

* `w` = forwards, `s` = backwards, `a` = counter-clockwise, `d` = clockwise, `c` = clear.

---

### 2. The Solution

```python
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()          # erase this turtle's drawings
    tim.penup()
    tim.home()           # back to centre
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear_screen, key="c")
screen.exitonclick()
```

Five bindings, five tiny callback functions — each a higher-order registration into
`screen.onkey`.

---

### Summary Checklist

1. Each key gets its own zero-argument callback.
2. `heading()` +/− 10 turns without moving.
3. `clear()` + `home()` = the shake-to-erase of Etch-A-Sketch.
4. Runnable version: [`etch_a_sketch.py`](etch_a_sketch.py)
