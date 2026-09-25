# Turtle Challenge 2 - Draw a Dashed Line

---

### 1. The Task

A dashed line: alternate between **drawing** and **moving without drawing**.

---

### 2. The Solution

```python
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
```

* `penup()` — lift the pen: moves leave no trace.
* `pendown()` — lower it: drawing resumes.

The penup/pendown pair is how *all* gap effects work (and later, jumping around the
canvas without leaving lines).

---

### Summary Checklist

1. Dashes = forward, penup, forward, pendown, repeat.
2. `penup()`/`pendown()` toggle the drawing state.
3. Loop body = one full dash+gap unit.
