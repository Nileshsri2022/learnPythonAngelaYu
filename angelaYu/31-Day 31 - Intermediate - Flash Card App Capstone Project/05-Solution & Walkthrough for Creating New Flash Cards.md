# Solution & Walkthrough for Creating New Flash Cards

---

### 1. The Code

```python
import random
from tkinter import Tk, Canvas, PhotoImage, Button
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = []

try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    print("Missing data file")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title_text, text="French", fill="black")
    canvas.itemconfig(card_word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title_text, text="English", fill="white")
    canvas.itemconfig(card_word_text, text=current_card["English"], fill="white")
```

---

### 2. Details Worth Noticing

* The card is **global state** — `flip_card` needs to know which word to reveal.
* `window.after(3000, flip_card)` auto-flips after 3 seconds; the timer *ID* is kept
  so a new card cancels the pending flip (`after_cancel`) — Day 28's ghost-timer fix.

---

### Summary Checklist

1. `next_card()` shows French + schedules the flip.
2. Timer IDs are cancelled on every new card — no stale flips.
