# How to Detect when the Ball goes Out of Bounds

---

### 1. Detecting a Miss

If the ball gets *past* a paddle's x-position, the point is lost:

```python
if ball.xcor() > 390:          # missed by the right paddle
    ball.reset_position()
    scoreboard.l_point()

if ball.xcor() < -390:         # missed by the left paddle
    ball.reset_position()
    scoreboard.r_point()
```

---

### 2. Resetting the Ball

```python
def reset_position(self):
    self.goto(0, 0)
    self.bounce_x()       # serve toward the player who just lost the point
```

* Back to centre, then **bounced toward the conceding side** — a subtle fairness touch.
* The game loop never stops: Pong keeps serving until you close the window.

---

### Summary Checklist

1. Out of bounds = `xcor()` beyond ±390 (past the paddles).
2. Miss → opponent's point + ball reset to centre.
3. Direction of the new serve comes from one more bounce.
