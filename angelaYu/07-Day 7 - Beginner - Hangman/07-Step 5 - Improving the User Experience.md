Here is a structured breakdown of Hangman Step 5 — the finishing touches.

---

### 1. Practicing Modules Again

The starting file *deliberately breaks* by deleting `stages` and `word_list`. Your job:
import them from the provided files — practicing **imports** from Day 4:

```python
import random
from hangman_art import stages, logo
from hangman_words import word_list
```

* Your own `.py` files are modules too — `hangman_art.py` and `hangman_words.py` sit in
  the same folder and are imported by name.

---

### 2. UX Improvements

**Already-guessed feedback** — tell the player, without punishing them:

```python
if guess in display:
    print(f"You've already guessed {guess}")
```

**Clearer win/lose banners** — extra asterisks so the outcome stands out:

```python
print("****************************")
print("You lose.")
```

**Reveal the answer on loss** — the word the player was missing:

```python
print(f"The word was {chosen_word}.")
```

---

### 3. Final Polish

* Print the `logo` at startup.
* Guard `stages[lives]` so it never indexes below 0.
* Full runnable game: [`hangman.py`](hangman.py) (+ [`hangman_art.py`](hangman_art.py),
  [`hangman_words.py`](hangman_words.py))

---

### Summary Checklist

1. Your own files import exactly like `random` — `from file import name`.
2. Duplicate guesses get a friendly message, not a lost life.
3. Small touches (banners, revealed word) turn code into a *game*.
