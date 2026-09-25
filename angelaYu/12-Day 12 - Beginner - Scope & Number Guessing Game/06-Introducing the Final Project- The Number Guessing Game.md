Here is a structured breakdown of the Day 12 final project briefing — the Number Guessing Game.

---

### 1. First Project Built Completely Solo

No starter code this time — just the requirements. Read them, flowchart the logic (Day 7
skill), then build.

---

### 2. The Requirements

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': 
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high / Too low / You got it!
You've run out of guesses, you lose.
```

1. Pick a random number between 1 and 100 (in constant scope territory!).
2. Difficulty selects attempts: **easy = 10**, **hard = 5** — as global constants.
3. Loop: each wrong guess tells **too high** or **too low** and decrements attempts.
4. Correct guess → win message revealing the answer; attempts exhausted → game over.
5. The game structure should use functions — e.g. `check_answer()`, `set_difficulty()`, `game()`.

---

### 3. Hints Before You Start

* `random.randint(1, 100)` for the answer (both bounds included — Day 4).
* The remaining-attempts count and the answer need careful scoping decisions.
* Don't use `global` — pass values as parameters and **return** the updates.

---

### Summary Checklist

1. Requirements → flowchart → functions → loop.
2. Difficulty values belong in **constants**.
3. Attempt your own build for at least an hour before any walkthrough.
