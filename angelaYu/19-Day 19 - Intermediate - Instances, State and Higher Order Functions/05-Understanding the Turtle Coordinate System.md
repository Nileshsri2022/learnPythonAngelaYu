# Understanding the Turtle Coordinate System

---

### 1. The Canvas Coordinates

The turtle screen is a coordinate plane with the **origin (0, 0) in the centre**:

* **x** grows to the **right** (negative = left)
* **y** grows **up** (negative = down)
* Default window ≈ 800×600 → x from −400 to +400, y from −300 to +300

---

### 2. Reading and Setting Positions

```python
tim.position()        # e.g. (100.00, -50.00)
tim.goto(100, 200)    # move (draw line) to an exact point
tim.setx(-100)        # change only x
tim.sety(250)         # change only y
tim.home()            # back to (0, 0)
```

Coordinate thinking is what makes games possible — the snake *is* a list of positions,
checked against boundaries and food coordinates.

---

### Summary Checklist

1. Origin centre; x right, y up.
2. `position()` reads; `goto/setx/sety` place.
3. Every game mechanic on Days 20–23 reduces to coordinate checks.
