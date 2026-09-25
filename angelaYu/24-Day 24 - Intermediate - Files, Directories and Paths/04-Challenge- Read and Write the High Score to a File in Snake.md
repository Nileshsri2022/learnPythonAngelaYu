Here is a structured breakdown of the high-score challenge and its solution.

---

### 1. The Challenge

Persist the snake high score: **read** it from `data.txt` at startup, **write** it back
whenever it's beaten.

---

### 2. The Solution

```python
# scoreboard.py
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
```

And `game_over()` becomes a message while the loop calls `reset()` and keeps playing.

* Read happens **once**, in the constructor.
* Write happens **only when the record is broken** — no pointless disk writes.

---

### Summary Checklist

1. Constructor reads; reset compares, updates and writes.
2. Numbers go to files as strings — `int()` in, f-string out.
3. Snake now has persistent progress.
