Here is a structured breakdown of Step 7 — the scoreboard and game over.

---

### 1. The `Scoreboard`

Displays the **level** (not a point count) top-right, and GAME OVER on a squish:

```python
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
```

---

### 2. Wiring It All Together

```python
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
```

---

### Summary Checklist

1. Scoreboard shows levels; `clear()` + rewrite on every change.
2. main.py coordinates: spawn, move, collide, finish — the whole game in ~20 lines.
3. Runnable full game: [`main.py`](main.py) (+ `player.py`, `car_manager.py`, `scoreboard.py`)
