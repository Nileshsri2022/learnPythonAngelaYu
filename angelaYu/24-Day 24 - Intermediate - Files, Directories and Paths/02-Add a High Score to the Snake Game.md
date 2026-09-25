Here is a structured breakdown of this lesson on adding a high score to the Snake game.

---

### 1. The In-Memory Version

The scoreboard tracks a high score *while the program runs*:

```python
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        ...

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
```

* Game over becomes a **reset**: score compares against the high score and restarts.
* The problem: close the window and the high score vanishes — the fix is files.

---

### Summary Checklist

1. High score = state that should outlive the program.
2. `int(data.read())` — files give strings; convert before comparing.
