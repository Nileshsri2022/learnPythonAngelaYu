Here is a structured breakdown of Hangman Step 1 — picking a random word and checking answers.

---

### 1. The Three TODOs

**TODO 1 — Pick a random word** from a list and print it (for now, so you can test):

```python
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
```

**TODO 2 — Ask the user for a guess**, in lowercase:

```python
guess = input("Guess a letter: ").lower()
```

**TODO 3 — Check the guess against every letter** of the word:

```python
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
```

---

### 2. What's New Here

* `random.choice(list)` — pick one random element (from Day 4).
* Looping through a **string** works exactly like looping through a **list** — a string
  is a sequence of characters.

> **Tip:** PyCharm collects your `# TODO` comments — open **View → Tool Windows → TODO**
> to see them listed and tick them off one by one.

---

### Summary Checklist

1. `random.choice()` selects the secret word.
2. `.lower()` normalises the guess.
3. `for letter in chosen_word:` compares the guess with each character — printing
   Right/Wrong per position.
