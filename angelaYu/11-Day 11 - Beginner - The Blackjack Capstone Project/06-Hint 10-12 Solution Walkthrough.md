Here is a structured walkthrough of Blackjack Hints 10–12 — the drawing loops.

---

### 1. Hints 10–11: The User's Turn

While the game isn't over, offer another card; standing ends the user's turn:

```python
while not is_game_over:
    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_should_deal == "y":
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        if user_score == 0 or user_score > 21:
            is_game_over = True
    else:
        is_game_over = True
```

Every draw **re-scores** the hand — an ace may need re-demoting, and 21+ ends the loop.

---

### 2. Hint 12: The Dealer's Strategy

Once the user stands, the computer plays by its fixed rule — **draw while under 17**:

```python
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
```

* `!= 0` — a dealer blackjack (0) means they stop immediately.
* `< 17` — the house must keep hitting until at least 17.

---

### 3. Show the Final Hands

```python
print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
```

---

### Summary Checklist

1. User loop: draw or stand, re-scoring after every card.
2. Dealer loop: hit while score < 17 (and isn't blackjack).
3. Two different loops with different conditions — each player's strategy.
