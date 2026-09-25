# Detect Collisions with your own Tail

---

### 1. Growing the Snake

`extend()` (added in `Snake`) appends a new segment at the tail's current position — the
new segment is stationary until the follow-loop picks it up:

```python
def extend(self):
    self.add_segment(self.segments[-1].position())
```

---

### 2. The Tail Collision Check

Loop over every segment and measure the distance from the head:

```python
for segment in snake.segments:
    if segment == snake.head:
        continue          # skip the head itself!
    if snake.head.distance(segment) < 10:
        scoreboard.game_over()
        game_is_on = False
```

The bug to avoid: the head is **in** the segments list, and its distance to itself is 0 —
without skipping it, the game ends instantly. (In the course this is solved elegantly with
slicing — next lesson.)

---

### Summary Checklist

1. Growth = new segment at the tail's position via `position()`.
2. Tail collision = head within 10px of **any other** segment.
3. Always exclude the head from its own collision check.
