# Turtle Challenge 3 - Drawing Different Shapes

---

### 1. The Task

Draw a **triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon**,
each in a different colour.

---

### 2. The Key Insight — Exterior Angles

Every polygon's exterior angles sum to **360°**. A shape with `n` sides turns
`360 / n` degrees at each corner:

```python
import random
from turtle import Turtle

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)
```

One loop inside another: the outer loop picks the shape (3→10 sides) and colour; the
inner loop draws it.

---

### Summary Checklist

1. Turn angle = `360 / number_of_sides`.
2. Triangle through decagon with one parameterised function.
3. Nested loops: one for the series, one for the shape.
