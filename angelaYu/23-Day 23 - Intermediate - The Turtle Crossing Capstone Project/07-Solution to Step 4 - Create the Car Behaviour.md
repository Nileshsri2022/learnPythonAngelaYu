# Solution to Step 4 - Create the Car Behaviour

---

### 1. The `CarManager` Class

```python
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:                       # spawn only sometimes
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
```

---

### 2. The Key Decisions

* **Random spawn chance** (1-in-6 per frame) creates irregular traffic — not a wall of
  cars, but a stream.
* `backward(speed)` — cars face east by default, so backing up = driving left.
* Speed lives on the manager; `level_up()` raises it for **all** cars at once.

---

### Summary Checklist

1. Cars = stretched square turtles collected in a list.
2. Spawn randomness → natural gaps in traffic.
3. One `car_speed` attribute drives every car; levels increase it.
