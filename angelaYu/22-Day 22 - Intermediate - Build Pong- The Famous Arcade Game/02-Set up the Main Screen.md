Here is a structured breakdown of this lesson on setting up the main screen.

---

### 1. The Setup

```python
from turtle import Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.exitonclick()
```

* Wider than tall (800×600) — paddles live on the left and right edges.
* Everything else you know from the Snake setup.

> **Note:** `tracer(0)` will be added once the ball starts moving — setup first,
> animation tuning later.

---

### Summary Checklist

1. `Screen` with black background, 800×600, titled Pong.
2. Screen dimensions define all future coordinate checks (±400, ±300).
