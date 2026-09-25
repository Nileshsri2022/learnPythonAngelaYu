Here is a structured breakdown of Step 6 — detecting when the player crosses.

---

### 1. The Finish-Line Check

```python
if player.is_at_finish_line():
    player.go_to_start()
    car_manager.level_up()
    scoreboard.increase_level()
```

* The player's own `is_at_finish_line()` method (`ycor() > 280`) answers the question.
* Crossing = reset position + speed up cars + level up the display — three objects
  coordinated by one `if` in `main.py`.

---

### 2. The Game Loop Shape

```python
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # collision + finish-line checks
```

Every frame: try to spawn, move what exists, then check the two game states.

---

### Summary Checklist

1. Finish = y beyond the top margin.
2. Level-up is a chain: reset turtle, faster cars, bigger number.
3. Spawning happens *inside* the loop — traffic is continuous.
