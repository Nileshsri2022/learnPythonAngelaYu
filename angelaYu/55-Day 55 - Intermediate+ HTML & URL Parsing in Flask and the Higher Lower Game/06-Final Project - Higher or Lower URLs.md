Here is a structured breakdown of the Day 55 project — Higher or Lower URLs.

---

### 1. The Task

The Higher or Lower guessing game (Day 12 reborn) — but played in the browser:
`/` asks for a guess of the random number; you guess by *typing the number into the
URL* (`/5`). Every guess answers **too high** / **too low** / **correct**, colour-coded.

---

### 2. The Solution

```python
import random
from flask import Flask

app = Flask(__name__)
random_number = random.randint(0, 9)

@app.route("/")
def guess_number():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='...gif...'>")

@app.route("/<int:guess>")
def check_guess(guess):
    global random_number
    if guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"
    elif guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>"
    else:
        random_number = random.randint(0, 9)   # new round
        return "<h1 style='color: green'>You got it!</h1>"
```

* `global random_number` — the route function mutates the module-level pick.
* The URL bar is the game's input device: routing + path variables + f-strings.

---

### Summary Checklist

1. State in a module-level variable; routes read and mutate it.
2. Runnable version: [`main.py`](main.py)
