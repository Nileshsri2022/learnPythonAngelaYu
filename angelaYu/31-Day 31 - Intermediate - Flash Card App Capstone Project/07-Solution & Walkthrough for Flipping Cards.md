# Solution & Walkthrough for Flipping Cards

---

### 1. The Complete Behaviour

```python
flip_timer = window.after(3000, func=flip_card)

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title_text, text="French", fill="black")
    canvas.itemconfig(card_word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title_text, text="English", fill="white")
    canvas.itemconfig(card_word_text, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    next_card()

def is_unknown():
    next_card()

unknown_button.config(command=is_unknown)
known_button.config(command=is_known)
```

---

### 2. The Interactions

* ✔ (`is_known`) — the word is **removed from `to_learn`** before drawing the next card.
* ✘ (`is_unknown`) — simply advances; the word stays in the deck.
* Both paths cancel the pending flip first — the stale-timer bug is structurally
  impossible now.

---

### Summary Checklist

1. One `next_card()` behind both buttons — different cleanup, same advance.
2. The deck is just a Python list; "learning" = `remove()`.
