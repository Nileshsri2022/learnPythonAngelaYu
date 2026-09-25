# Turtle Challenge 4 - Generate a Random Walk

---

### 1. The Task

The turtle wanders randomly — random direction changes, random colours, thick line
(`pensize`), reasonable speed.

---

### 2. The Solution

```python
import random
from turtle import Turtle

timmy = Turtle()
timmy.pensize(15)
timmy.speed("fastest")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]

for _ in range(200):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
```

* `setheading(angle)` sets an absolute heading: `0` = east, `90` = north, `180` = west,
  `270` = south.
* Choosing from the four cardinal directions keeps the walk tidy.

---

### Summary Checklist

1. Random walk = loop of (move, random turn, random colour).
2. `setheading()` with `[0, 90, 180, 270]` gives clean 90° zig-zags.
3. `speed("fastest")` for long drawings — otherwise you'll watch paint dry.
