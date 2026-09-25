# Hurdles Challenge using While Loops

---

### 1. The Challenge

In Hurdle 3 the hurdles are **random**: their number, and their positions change every
restart. A `for step in range(6): jump()` is now useless — the robot can't know in advance
how many jumps are needed. This is exactly what `while` loops are for: **keep going until
the goal is reached**.

---

### 2. Reeborg's Condition Functions

Reeborg provides Boolean checks (found in the *conditions* tab of its keyboard):

* `at_goal()`
* `wall_in_front()`
* `front_is_clear()`
* Negations with `not` — `not front_is_clear()`, `not at_goal()` …

---

### 3. Solution

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
```

* The **outer `while`** runs until the robot is at the goal — however many hurdles there are.
* The **inner `if`/`else`** decides each step: jump over a wall when there is one, otherwise advance.

> **Warning:** Going *around* the hurdles instead of following the dotted path may pass
> the level — but that's cheating the challenge. The point is the `while` + `if` pattern.

---

### Summary Checklist

1. Unknown repetitions → `while`, not `for`.
2. Combine `while not at_goal():` with `if wall_in_front():` for each step.
3. Reuse yesterday's skills: `turn_right()` and `jump()` stay as functions.
