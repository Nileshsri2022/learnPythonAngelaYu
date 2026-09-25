Here is a structured walkthrough of Blackjack Hint 9 — refactoring and calling `calculate_score()`.

---

### 1. Compute Both Scores

Call the new function for each hand and store the results:

```python
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
```

---

### 2. The Immediate Game-Over Check

Some outcomes end the game before any drawing happens:

```python
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
```

* `0` = blackjack (either side)
* over 21 = player busted

Note the `or` chain (Day 3's logical operators) and the **flag variable** `is_game_over`
that the main loop watches.

---

### 3. Refactoring as You Go

The lesson also tidies up: repeated print blocks get grouped, and the score/score-printing
lines are consolidated. **Refactor early, refactor often** — every new feature is a good
moment to reorganise what's already working.

---

### Summary Checklist

1. Scores are computed through one function for both hands.
2. Blackjack (0) or a bust (> 21) ends the game immediately via a flag.
3. Keep refactoring as the program grows — never let it rot.
