# The Hurdles Loop Challenge

---

### 1. The Challenge

In **Reeborg's World** (Hurdle 1), the robot must jump **6 hurdles** in a row to reach the
goal. Available robot commands: `move()` and `turn_left()`. Jumping over one hurdle means:
climb up, over, and back down — i.e. `move`, `turn_left`, `move`, `turn_left`... but
there's no `turn_right()`!

---

### 2. Building the Pieces

**Turn right = turn left three times.** Wrap it in a function:

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
```

**Jumping one hurdle:**

```python
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    turn_left()
```

**Doing it six times** — a `for` loop with `range()`:

```python
for step in range(6):
    jump()
```

Without functions and loops this would take dozens of nearly identical lines; with them
it's ~15 readable ones.

> **Tip:** The goal of the challenge is to **minimise lines while keeping the code
> readable** — "we're programmers; we're born to be lazy" (the good kind of lazy).

---

### Summary Checklist

1. Missing `turn_right()`? Build it from three `turn_left()` calls inside a function.
2. A `jump()` function packages the over-and-down sequence.
3. `for step in range(6): jump()` repeats it for all six hurdles.
