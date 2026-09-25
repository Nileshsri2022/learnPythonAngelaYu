# Day 31 Goals- what we will make by the end of the day

---

### 1. The Project: French/English Flash Cards

A language-learning card that flips:

* Shows a **French** word in white on green for 3 seconds.
* Flips to **English** on the same card.
* ✘ = "didn't know" → next card; ✔ = "knew it" → **removed from the deck forever**.
* Known words are saved to CSV — your deck shrinks as you learn.

It combines everything from Days 27–30: Tkinter UI, canvas text, timers (`after`),
CSV/Pandas, JSON-style state, and exception handling.

---

### 2. The Four Steps

| Step | Feature |
|------|---------|
| 1 | UI — canvas card + ✘/✔ buttons |
| 2 | Cards from `french_words.csv` |
| 3 | Flip card after 3s (`after`) |
| 4 | Save progress — learned words leave the deck |

---

### Summary Checklist

1. The Intermediate GUI block (Days 27–31) ends with this capstone.
2. Every mechanic is a now-familiar pattern in a new combination.
