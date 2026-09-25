# Choose Your Difficulty

---

### 1. The Task

A starting-screen prompt: `easy`, `medium` or `hard` — mapped to the cars' starting speed
via global constants:

```python
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

EASY_SPEED = STARTING_MOVE_DISTANCE          # 5
MEDIUM_SPEED = STARTING_MOVE_DISTANCE + 5    # 10
HARD_SPEED = STARTING_MOVE_DISTANCE + 10     # 15
```

The chosen value becomes the `CarManager`'s initial speed; each level adds
`MOVE_INCREMENT`.

---

### 2. The Pattern

* Difficulty selection = **constants + a lookup** — no logic changes anywhere else.
* `screen.textinput()` (Day 19) collects the choice before the game loop starts.

---

### Summary Checklist

1. Difficulty = different constant, same code.
2. Levels multiply the effect — each crossing makes all cars faster.
