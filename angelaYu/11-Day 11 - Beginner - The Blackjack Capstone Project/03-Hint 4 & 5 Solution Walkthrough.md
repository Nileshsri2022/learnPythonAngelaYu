# Hint 4 & 5 Solution Walkthrough

---

### 1. Hint 4: Create a `deal_card()` Function

Uses the `random` module to return one card from the deck:

```python
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
```

Note it **returns** the card (Day 10) rather than printing it — the caller decides
where the card goes.

---

### 2. Hint 5: Deal Two Cards to Each Player

Lists collect the hands:

```python
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
```

`for _ in range(2)` — the underscore says the loop variable isn't used; we just want
**two iterations**.

---

### Summary Checklist

1. `deal_card()` = a function with an output: one random card per call.
2. Hands live in two lists, filled with `append()` in a 2-iteration loop.
3. Deal *both* players inside the same loop — no duplicated code.
