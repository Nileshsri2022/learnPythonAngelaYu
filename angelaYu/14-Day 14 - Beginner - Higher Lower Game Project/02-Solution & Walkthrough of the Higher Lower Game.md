Here is a structured walkthrough of the Higher Lower Game solution.

---

### 1. The Data

Each account is a dictionary; the game data is a list of them:

```python
data = [
    {"name": "Instagram", "follower_count": 346, "description": "Social media platform", "country": "United States"},
    {"name": "Cristiano Ronaldo", "follower_count": 215, "description": "Footballer", "country": "Portugal"},
    # …many more
]
```

---

### 2. The Helper Functions

```python
import random
from game_data import data

def get_random_account():
    """Return a random account from the data."""
    return random.choice(data)

def format_data(account):
    """Format the account into a printable line."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Return True if the guess was correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
```

---

### 3. The Game Loop

```python
def game():
    score = 0
    game_should_continue = True
    account_a = get_random_account()

    while game_should_continue:
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs_logo)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            account_a = account_b        # winner stays; B becomes the new A
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()
```

The elegant trick: after a correct guess, **`account_b` becomes the new `account_a`** —
the loop's variables slide forward one round.

---

### Summary Checklist

1. Random accounts, formatted for display; B re-rolled until it differs from A.
2. `check_answer()` returns a Boolean the loop acts on.
3. Correct → score up, B slides into A's slot; wrong → final score shown.
4. Runnable version: [`higher_lower.py`](higher_lower.py) (+ [`game_data.py`](game_data.py))
