Here is a structured walkthrough of Blackjack Hint 13 — the `compare()` function.

---

### 1. All the Outcomes in One Function

With both final scores known, a single comparison function settles the game. Remember:
**0 means blackjack**, so it's checked *first*:

```python
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

print(compare(user_score, computer_score))
```

---

### 2. The Order of Checks Matters

| Order | Check | Why |
|-------|-------|-----|
| 1 | draw | equal scores (both 0 handled after) |
| 2 | computer blackjack | strongest loss |
| 3 | user blackjack | strongest win |
| 4–5 | busts | over 21 loses unless both bust → draw caught earlier |
| 6–7 | plain higher score | the ordinary outcome |

Because `compare` **returns** strings (Day 10), the caller simply prints the result.

---

### Summary Checklist

1. Centralise win/lose logic in one function — don't scatter `if`s around the file.
2. Blackjack-as-0 makes the checks clean and ordered.
3. `return` the outcome; print it at the call site.
