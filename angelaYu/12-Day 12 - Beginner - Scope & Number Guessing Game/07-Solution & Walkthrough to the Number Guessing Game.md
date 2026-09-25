Here is a structured walkthrough of the Number Guessing Game solution.

---

### 1. The Structure

Three functions + global constants, with **no `global` keyword anywhere** — state flows
through parameters and return values:

```python
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(guess, answer, turns):
    """Check the answer, return the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
```

---

### 2. Scope Decisions Worth Noticing

* `EASY_LEVEL_TURNS` / `HARD_LEVEL_TURNS` — **constants** (read-only globals).
* `answer`, `turns`, `guess` — **locals of `game()`**, passed into helpers.
* `check_answer()` **returns** the updated turns — the caller owns its own state.

---

### Summary Checklist

1. Difficulty → constants; game state → function locals.
2. Helpers receive state as parameters and return updates — no `global`.
3. `return` doubles as an early exit (`return` with no value ends `game()` on a loss).
4. Runnable version: [`number_guessing_game.py`](number_guessing_game.py)
