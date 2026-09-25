# Step 2 - Break down the Problem

---

### 1. The Decomposition

The game splits into five sub-problems (each becoming a class or function):

1. **Player** — turtle at bottom; `Up` moves it `MOVE_DISTANCE` north.
2. **Cars** — manager spawns rectangles at random y on the right; all move left; level
   increases speed.
3. **Collision** — head-to-car distance under a threshold → game over.
4. **Finish line** — turtle's `ycor()` past the top → reset + level up.
5. **Scoreboard** — level display, level-up message, GAME OVER.

---

### 2. Mapping to Classes

```text
main.py        — screen, loop, keybinding, condition checks
player.py      — class Player(Turtle): move(), go_to_start(), is_at_finish_line()
car_manager.py — class CarManager: create_car(), move_cars(), level_up()
scoreboard.py  — class Scoreboard(Turtle): update_level(), game_over()
```

Same architecture as Snake and Pong: a thin `main.py` coordinating independent classes.

---

### Summary Checklist

1. Decompose by *responsibility*, then decide the class per responsibility.
2. The main loop only orchestrates — classes own their behaviour.
