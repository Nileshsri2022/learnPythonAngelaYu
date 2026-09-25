Here is a structured breakdown of Hangman Step 4 — keeping track of the player's lives.

---

### 1. The Problem

Wrong guesses need a **cost**, or the player can brute-force the alphabet. Hangman's cost:
**6 lives**, and each wrong guess draws the next stage of the little man (ASCII art stages
`6` = empty gallows down to `0` = complete drawing = game over).

---

### 2. The Changes

**Create a `lives` variable** and a `stages` list of the ASCII art:

```python
lives = 6
```

**Inside the game loop — punish wrong guesses:**

```python
if guess not in chosen_word:
    lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose.")
```

**Print the matching art stage** after every turn:

```python
print(stages[lives])
```

* Correct guess → `lives` unchanged → same art stage.
* Wrong guess → `lives` drops → drawing progresses.
* `stages[0]` (complete hangman) appears exactly when `lives` hits 0.

---

### Summary Checklist

1. `lives = 6`, decremented only when `guess not in chosen_word`.
2. Loss check inside the `if` — the game must stop the moment lives hit 0.
3. `stages[lives]` maps the life count straight onto the right ASCII art.
