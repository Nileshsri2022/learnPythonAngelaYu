# Score Keeping and Changing the Ball Speed

---

### 1. The `Scoreboard`

```python
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
```

Two score attributes, big arcade numerals at each half.

---

### 2. Speeding the Ball Up

Decrease the frame delay on every paddle hit — smaller sleep = faster game:

```python
time.sleep(ball.move_speed)     # starts at 0.1

# in Ball.bounce_x():
self.move_speed *= 0.9          # 10% faster per paddle hit
```

And on a miss, reset it:

```python
def reset_position(self):
    self.goto(0, 0)
    self.move_speed = 0.1
    self.bounce_x()
```

---

### Summary Checklist

1. Scoreboard: two scores, `clear()` + rewrite, `l_point()`/`r_point()`.
2. Speed control lives in `move_speed` — tuned via `sleep()`.
3. Every rally gets a little faster; every point resets the pace.
