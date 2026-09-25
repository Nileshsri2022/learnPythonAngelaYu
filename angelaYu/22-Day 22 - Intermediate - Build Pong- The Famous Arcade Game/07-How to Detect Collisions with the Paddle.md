Here is a structured breakdown of this lesson on detecting paddle collisions.

---

### 1. The Detection

Distance alone isn't enough — a fast ball can pass a paddle's centre. Combine a **distance
check** with an **x-position check**:

```python
if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
    ball.bounce_x()

if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
    ball.bounce_x()
```

* `distance < 50` — the ball is close to the paddle's body.
* `xcor() > 340` — it's actually *at* the right edge (rules out weird mid-screen hits).

---

### 2. The Response

`bounce_x()` flips the horizontal direction — the ball heads back toward the other side,
vertical motion untouched (which preserves the angle of deflection).

> **Tip:** Because the ball moves 10px per frame, generous thresholds (50px) keep the
> physics feeling fair at this speed.

---

### Summary Checklist

1. Paddle hit = close **and** at the correct edge.
2. Respond with `bounce_x()` only.
3. Two checks — one per paddle, mirrored.
