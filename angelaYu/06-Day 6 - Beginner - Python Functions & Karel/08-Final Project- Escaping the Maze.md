# Final Project- Escaping the Maze

---

### 1. The Challenge

The robot starts at a **random position facing a random direction** inside a maze, and must
reach the goal — every single time, no matter where it starts. Hard-coded moves can't work.
You need an **algorithm**: a step-by-step strategy that guarantees success.

---

### 2. The Algorithm: Follow the Right Wall

Reeborg's world info reveals the winning strategy: **keep one hand on the right wall**.

1. If the **right side is clear** → turn right and go (hug the wall).
2. Else if the **front is clear** → go straight.
3. Else (dead end) → **turn left** and try again.

The robot doesn't "see" the maze — it just applies these three rules forever, and the rules
*guarantee* it eventually finds the exit.

---

### 3. Solution

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

> **Note:** In some maze variants the right-wall algorithm can loop forever if the
> robot starts facing along an open corridor — the course's version works reliably.
> If yours sticks, check the priority order of the three rules.

---

### Summary Checklist

1. Big problems need **algorithms**, not memorised move lists.
2. Right-wall follower: `right clear → turn right`, `front clear → move`, `else → turn left`.
3. One `while not at_goal():` + three-way `if`/`elif`/`else` = a maze solver.
4. Runnable version of all Reeborg solutions: [`reeborg_solutions.py`](reeborg_solutions.py)
