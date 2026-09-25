# Day 22 Goals- what you will make by the end of the day

---

### 1. Skills Covered on Day 22

* Applying **everything** from Days 18–21 to a new game from scratch
* Two-player **key bindings**
* **Bounce logic** — reversing movement components on collision
* **Score keeping** and game restarts

---

### 2. The Project: Pong

Two paddles, one ball, first to miss loses the round:

1. 800×600 black screen.
2. Right paddle: `Up`/`Down` keys; left paddle: `w`/`s` keys.
3. Ball bounces off top/bottom walls and both paddles.
4. Paddle miss → opponent scores → ball resets to centre.
5. Speed up slightly on every paddle hit.

---

### Summary Checklist

1. Same building blocks as Snake: Turtle + OOP + events + coordinates.
2. New concept: bouncing = *negate* the movement direction.
3. Four classes: `Paddle`, `Ball`, `Scoreboard`, plus `main.py`.
