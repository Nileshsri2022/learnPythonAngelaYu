# Aaaand, we're off to the races!

---

### 1. The Game

1. A betting prompt: *who will win the race?* (pick a colour).
2. Six coloured turtle instances line up at the start.
3. On click, each turtle moves a **random** amount each frame until one crosses the line.
4. The result is compared against your bet.

---

### 2. The Solution

```python
import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:                 # finish line reached
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
```

* `screen.textinput()` — a GUI pop-up for the bet.
* Each loop pass, every instance advances by its **own** random amount — instance state
  and randomness making a race.

---

### Summary Checklist

1. One class (`Turtle`), six instances, independent positions = the race.
2. Finish detection = an `xcor()` coordinate check.
3. `while is_race_on:` — the flag pattern from Blackjack, reused.
