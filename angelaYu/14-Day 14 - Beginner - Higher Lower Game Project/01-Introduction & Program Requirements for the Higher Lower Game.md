# Introduction & Program Requirements for the Higher Lower Game

---

### 1. The Game

Like higherlowergame.com: two options are shown (e.g. Instagram vs. Cristiano Ronaldo)
and you guess **which has more followers**. Each correct answer bumps your score and pits
your account against a fresh challenger — one wrong guess ends the game.

```text
Compare A: Instagram, an online photo-sharing service.
Against B: Cristiano Ronaldo, Footballer.
Who has more followers? Type 'A' or 'B': A
You're right! Current score: 1.
```

---

### 2. The Requirements

* Data: a **list of dictionaries**, each `{"name": …, "follower_count": …, "description": …, "country": …}`
  — nesting from Day 9.
* Random choices with `random` (Day 4) — the new comparison card must differ from the last one.
* Keep score across rounds; a loop (Day 5/6) runs until the first wrong guess.
* Clear the screen between rounds so option A of the last round becomes option B.
* Structure the code in **functions** (`get_random_account`, `format_data`, `check_answer`, `game`).

---

### 3. Build Strategy

1. Flowchart the game loop (Day 7 skill).
2. Write the data + helper functions first.
3. Build the loop, then wire in the score and game-over logic.
4. Attempt it solo for at least an hour before the walkthrough.

---

### Summary Checklist

1. List-of-dicts data + random picks + a while loop = the whole game.
2. Functions keep each piece (data, display, check) isolated.
3. The game ends on the *first* wrong answer — score resets each run.
