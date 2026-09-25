# Hint 6-8 Solution Walkthrough

---

### 1. Hint 6: The Scoring Function

```python
def calculate_score(cards):
    """Take a list of cards and return the score."""
    return sum(cards)
```

`sum()` totals any list of numbers — the built-in we mirrored by hand on Day 5.

---

### 2. Hint 7: The Blackjack Check

A score of 21 with only two cards **is** a blackjack — encode it as `0`:

```python
    if sum(cards) == 21 and len(cards) == 2:
        return 0
```

Returning `0` makes blackjack *less than every other hand*, so comparisons later treat it
as unbeatable.

---

### 3. Hint 8: The Ace Demotion

Inside a `while` loop so it can fire repeatedly (multiple aces):

```python
    while sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
```

* `11 in cards` — the `in` operator checks list membership (Day 3/4).
* Each pass swaps one Ace from 11 down to 1 until the score is legal.

---

### Summary Checklist

1. `calculate_score()` = `sum()` + blackjack rule + ace rule.
2. Blackjack → `return 0`.
3. Aces demote 11 → 1 in a `while` loop until the bust is resolved.
