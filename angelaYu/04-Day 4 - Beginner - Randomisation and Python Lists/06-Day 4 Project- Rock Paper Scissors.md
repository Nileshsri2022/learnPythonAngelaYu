Here is a structured breakdown of the Day 4 final project — Rock Paper Scissors.

---

### 1. What the Program Does

```
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
0

You chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

You win!
```

The rules: **rock beats scissors, scissors beats paper, paper beats rock**; identical
choices are a draw.

---

### 2. The Logic, Step by Step

1. Get the user's choice as an **int**.
2. Validate it — anything outside `0–2` loses immediately (invalid input).
3. Computer picks with `random.randint(0, 2)`.
4. Print the right **ASCII art** for both choices (art is stored in three variables —
   print them *without* quotes, they're variables, not strings).
5. Compare with a chain of `if`/`elif`/`else` and announce the result.

---

### 3. Solution

```python
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]   # a list groups the three choices

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice < 0 or user_choice > 2:
    print("Invalid number, you lose!")
else:
    print("You chose:\n" + game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:\n" + game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose")
    else:
        print("It's a draw")
```

> **Tip:** Storing the art in a **list** and indexing with the choice number removes
> three separate if-statements for printing — that's lists paying you back already.

---

### Summary Checklist

1. `random.randint(0, 2)` is the computer's hand.
2. The game logic is pure Day 3: chained conditionals with `and`.
3. A list of images indexed by the choice keeps the code DRY.
4. Runnable version: [`rock_paper_scissors.py`](rock_paper_scissors.py)
