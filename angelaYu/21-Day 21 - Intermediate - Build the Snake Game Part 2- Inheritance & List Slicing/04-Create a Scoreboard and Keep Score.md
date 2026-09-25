Here is a structured breakdown of this lesson on creating the scoreboard.

---

### 1. A Turtle That Writes

Turtles can draw **text** instead of lines. The `Scoreboard` class inherits `Turtle` and
uses `write()`:

```python
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()                 # erase the old text first!
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
```

---

### 2. The Details That Matter

* `hideturtle()` — we want the *text*, not a visible turtle arrow.
* `penup()` + `goto(0, 270)` — position text near the top edge.
* `clear()` before rewriting — otherwise scores smear on top of each other.
* `write(text, align, font)` — the signature from the turtle docs (reading docs pays off!).

---

### Summary Checklist

1. Scoreboard = a turtle with `score` state and `write()` behaviour.
2. Update pattern: increment → `clear()` → write.
3. `game_over()` writes centred text when a collision is detected.
