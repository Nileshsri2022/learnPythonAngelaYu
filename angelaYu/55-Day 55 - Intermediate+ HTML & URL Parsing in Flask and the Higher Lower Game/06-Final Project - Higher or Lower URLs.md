# Final Project - Higher or Lower URLs

---

### 1. The Project

A website built purely out of **routes**:

| URL | Response |
|-----|----------|
| `/` | *Guess a number between 0 and 9* (h1, centred, on a coloured background) |
| `/3` | *Too low, try again!* |
| `/7` | *Too high, try again!* |
| `/5` (the answer) | *You found me!* + a celebration GIF |

Everything the user "types" is the path segment of the URL.

---

### 2. Step 1 — Type the Path

```python
import random
from flask import Flask

app = Flask(__name__)
ANSWER = random.randint(0, 9)
```

> **Note:** In a real app the answer would live in a session/database (Days 63+). A
> module-level constant is fine for a one-player toy.

---

### 3. Step 2 — The Route

```python
@app.route("/")
def home():
    return ('<h1 style="text-align:center; color:red">'
            "Guess a number between 0 and 9</h1>")

@app.route("/<int:guess>")
def guess_number(guess):
    if guess < ANSWER:
        return '<h1 style="color:blue">Too low, try again!</h1>'
    if guess > ANSWER:
        return '<h1 style="color:blue">Too high, try again!</h1>'
    return ('<h1 style="color:green">You found me!</h1>'
            '<img src="https://media.giphy.com/media/…/giphy.gif" width="300">')
```

* `<int:guess>` means non-numeric paths 404 automatically, and `guess` arrives as an
  `int` — no casting.
* Each branch returns its own HTML; Flask serves it verbatim.
* An escaped `%` or a favicon request can produce stray routes — they'll just 404.

---

### 4. Step 3 — Debug Mode While You Build

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Change a colour, hit save, refresh the browser — the auto-reloader restarts the server for
you, and any traceback turns into the interactive debugger.

---

### 5. Going Further

* Add `/favicon.ico` handling to silence the browser's automatic request.
* Keep a score: ask for the player's name first (`/@<name>/3`) — URL variables in action.
* Style it properly with a `<style>` block instead of inline CSS.
* Restart the game with a `/reset` route.

---

### Summary Checklist

1. Path segment = the player's guess; `<int:guess>` converts it for you.
2. Three branches → three different HTML responses.
3. Images/GIFs are just `<img src="…">` inside the returned string.
4. `debug=True` while developing: auto-reload plus the debugger.
5. Anything stateful (the answer, the score) needs a home — a constant today, a session or
   database later.
