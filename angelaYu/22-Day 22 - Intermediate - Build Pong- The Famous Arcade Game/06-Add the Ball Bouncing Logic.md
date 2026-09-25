Here is a structured breakdown of this lesson on the ball bouncing logic.

---

### 1. Bouncing Off Top and Bottom Walls

When the ball touches the top or bottom edge, **reverse the vertical component**:

```python
if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()
```

```python
# in Ball
def bounce_y(self):
    self.y_move *= -1      # flip direction: up ↔ down

def bounce_x(self):
    self.x_move *= -1      # flip direction: left ↔ right
```

Multiplying by −1 flips the sign: a ball rising at `y_move = 10` now falls at `y_move = −10`,
while its horizontal motion continues — that's a bounce.

---

### 2. Why Attributes Beat Hard-Coding

Because direction lives in `x_move`/`y_move`, *every* bounce in the whole game — walls,
paddles — is a sign flip. No heading maths, no special cases.

---

### Summary Checklist

1. Wall check: `ycor()` beyond ±280 → `bounce_y()`.
2. Bounce = `*= -1` on the relevant movement component.
3. Keep speed and direction as attributes you can flip.
