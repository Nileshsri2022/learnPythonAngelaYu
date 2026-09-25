Here is a structured breakdown of the Day 20 goals — the Snake Game, Part 1.

---

### 1. Skills Covered on Day 20

* **Screen setup** with the Turtle `Screen` class
* **Animation** — making objects move smoothly frame by frame
* **OOP refactor** — extracting game behaviour into a `Snake` class
* **Key bindings** — controlling the snake with arrow keys

---

### 2. The Project: Snake (Nokia 3310 classic)

By the end of today the snake:

1. Appears as a body of three squares.
2. **Moves automatically** across the screen.
3. The tail follows the head around turns.
4. Turns **up / down / left / right** on the arrow keys.

Days 21–22 will add food, score, walls, tail collisions — but today is the
movement engine.

---

### Summary Checklist

1. Everything from Turtle (Day 18/19) + OOP (Day 16/17) combines into a game.
2. The core animation trick: segments *follow* the segment in front.
3. Build it procedurally first, then refactor into classes.
