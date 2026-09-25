# Jumping over Hurdles with Variable Heights

---

### 1. The Challenge

Hurdle 4 randomises **everything**: the number of hurdles, their positions **and their
heights**. A fixed `jump()` (which moves up exactly once) can no longer clear the taller
walls — the robot must climb **as high as each wall requires**.

---

### 2. The Key Insight

`jump()` becomes a `while` loop itself: **keep climbing while there is still wall ahead**:

```python
def jump():
    turn_left()
    while wall_on_right():     # climb up while a wall blocks the right
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():    # come back down while the front is open
        move()
    turn_left()
```

* Climbing: while there's a **wall on the right**, keep moving up.
* At the top: step right, turn, and descend **while the front is clear**.
* Land, face forward, and the main loop handles the rest.

---

### 3. Full Solution

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
```

---

### Summary Checklist

1. Variable heights → make the **climb** conditional: `while wall_on_right():`.
2. Descent is also a loop: `while front_is_clear():`.
3. Nested loops (a `while` inside a `while`) are perfectly legal — each level checks
   its own condition.
