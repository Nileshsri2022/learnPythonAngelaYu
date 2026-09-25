# Step 2 - Replacing Blanks with Guesses

---

### 1. The Problem

The player shouldn't see the word — they should see **blanks**, one `_` per letter, with
correct guesses revealed in place:

```text
Word: aardvark     Guess: a     Display: a _ _ _ _ a _
```

---

### 2. The Solution

**Create a `display` list of blanks**, one per letter of the word:

```python
display = []
for _ in range(len(chosen_word)):
    display += "_"
```

**When the guess matches a letter, fill every matching position** — using `range(len(...))`
so you have both the index *and* the letter:

```python
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
```

**Show the display** without Python's list formatting:

```python
print(f"{' '.join(display)}")
```

> **Note:** `display += "_"` appends to a list (list `+`/`+=` concatenates) — the same
> trick as `display.append("_")`.
>
> **Note 2:** `' '.join(list)` glues the items together with spaces — a list is not
> printable-friendly on its own.

---

### Summary Checklist

1. Blanks live in a **list** so they can be updated by position.
2. `for position in range(len(word)):` gives index + letter — needed to write back into `display`.
3. `join()` turns the list into a readable string for the player.
