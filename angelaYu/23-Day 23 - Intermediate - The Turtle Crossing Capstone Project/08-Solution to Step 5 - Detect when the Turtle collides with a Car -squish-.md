Here is a structured breakdown of Step 5 — car collision detection.

---

### 1. The Check

In the game loop, measure the player against every car:

```python
for car in car_manager.all_cars:
    if player.distance(car) < 25:
        game_is_on = False
        scoreboard.game_over()
```

---

### 2. Choosing the Threshold

Cars are 40px long and 20px tall; the turtle ~20×20. `distance()` measures between
*turtle reference points* (centres), so a threshold of **25** feels fair:

* too small → impossible overlaps go unnoticed (you survive inside a car),
* too big → deaths from near-misses feel unjust.

Game feel = choosing constants by playtesting, not geometry.

---

### Summary Checklist

1. Collision = `player.distance(car) < 25` for every car, every frame.
2. Thresholds are tuned constants — adjust until the game feels right.
