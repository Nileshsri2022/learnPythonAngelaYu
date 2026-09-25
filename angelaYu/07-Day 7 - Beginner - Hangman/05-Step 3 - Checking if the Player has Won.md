# Step 3 - Checking if the Player has Won

---

### 1. The Problem

So far one guess = one pass. A real game keeps asking **until the word is fully revealed**.
Also, a new guess must not wipe out previously revealed letters (the current code rebuilds
`display` from the single current guess — previous correct letters are lost).

---

### 2. The Fixes

**1 — Keep revealed letters:** initialise `display` **once, before** the loop, and never
re-blank it. Only positions matching a guess get overwritten:

```python
display = []
for _ in range(word_length):
    display += "_"
```

**2 — Loop until the blanks are gone:** a `while` loop that ends when no `_` remains:

```python
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
```

---

### 3. The Pattern

* The **game loop** condition is the *win condition*: `"_" not in display`.
* Because `display` is only *updated* (never recreated), correct guesses accumulate
  across turns — guess `a`, then `r`, and both stay visible.

---

### Summary Checklist

1. Set up `display` **before** the loop; only mutate it inside.
2. `while not end_of_game:` keeps the game running.
3. Win check: no underscores left → `You win.`
