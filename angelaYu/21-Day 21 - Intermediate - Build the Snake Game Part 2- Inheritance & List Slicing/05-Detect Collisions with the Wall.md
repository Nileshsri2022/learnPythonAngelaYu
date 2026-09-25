# Detect Collisions with the Wall

---

### 1. The Boundary Check

The screen is 600×600, so the walls sit at ±300. Using a safety margin of 280, the head
escaping the box ends the game:

```python
# in main.py's game loop
if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
        or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    scoreboard.game_over()
    game_is_on = False
```

Four comparisons chained with `or` (Day 3) — head beyond **any** wall = collision.

---

### 2. Why a Margin?

Checking at exactly 300 means the head visually *overlaps* the wall before detection.
280 triggers just before contact — game feel beats geometric purity.

---

### Summary Checklist

1. Wall collision = head's x **or** y outside ±280.
2. `or` chain across all four boundaries.
3. On collision: show GAME OVER, stop the loop.
