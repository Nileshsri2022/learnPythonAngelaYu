Here is a structured breakdown of the Blackjack rules and program requirements.

---

### 1. The Rules of Blackjack (21)

* Each card has a value; **score = sum of your cards**.
* Number cards = face value; **J/Q/K = 10**; **Ace = 11 or 1** (whatever saves you).
* **Blackjack** = an Ace + a 10-card in the first two cards — an instant win.
* Over **21 = bust** — you lose immediately.
* Dealer rules: must keep drawing until their score reaches **at least 17**.
* Draw = equal scores.

---

### 2. Simplified Deck for This Project

The program uses an **infinite deck** — every draw is a fresh random pick:

```python
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#        Ace  2 ………………  9   J   Q   K
```

* `deal_card()` = `random.choice(cards)` — no memory of what's been drawn.

---

### 3. The Ace Handling Rule (the famous hint!)

If the score goes over 21 and an **11** is in the hand, count that Ace as a **1** instead:

```python
if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
```

Score is computed with **`0` representing blackjack** in the score list so a natural
blackjack beats a plain 21.

---

### Summary Checklist

1. Score = sum of cards; goal is ≤ 21 and higher than the dealer.
2. Ace = 11, demoted to 1 when needed — the trickiest logic in the game.
3. Blackjack (Ace + 10-card) is encoded as score `0`.
4. Dealer draws until ≥ 17 — their entire "strategy".
