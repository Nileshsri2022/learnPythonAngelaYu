# Day 23 Goals: what you will make by the end of the day

Day 23 starts the second capstone project: **Turtle Crossing** — a lane-dodging game
in the spirit of *Crossy Road*.

---

### 1. The Game

A busy multi-lane highway runs across the screen, with **randomly generated cars**
driving horizontally. The player controls a turtle that can only move **forwards**,
and must reach the far side without being hit.

| Event | What happens |
|-------|--------------|
| Player reaches the other side | `level += 1` — **all cars speed up**, turtle resets to the start |
| Turtle collides with a car | **Game over** |

---

### 2. Why This Project

It deliberately revisits almost everything from the first three weeks:

* **Classes & inheritance** — a `CarManager` that spawns many `Car` objects (Day 16–21)
* **Objects from classes** — cars, the player, the scoreboard (Day 17–19)
* **Turtle coordinates & the game loop** — `y` increases upwards, screen updates,
  collision detection (Day 20–22)

> **Tip:** Get the starter code and pick your difficulty in the next lecture. If you get
> stuck, the following lectures walk through the solution **one step at a time** —
> try each step yourself first.

---

### Summary Checklist

1. Turtle Crossing = the *Crossy Road* pattern: move forwards, dodge traffic, level up.
2. Reaching the far side speeds the cars up and resets the player.
3. Hitting a car ends the game.
4. The project is designed to test classes, inheritance, objects and turtle coordinates.
