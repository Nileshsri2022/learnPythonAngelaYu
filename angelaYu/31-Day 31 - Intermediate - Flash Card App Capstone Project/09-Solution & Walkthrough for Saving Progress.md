# Solution & Walkthrough for Saving Progress

---

### 1. The Complete Data Flow

```text
startup:   words_to_learn.csv exists? ──no──▶ french_words.csv (all words)
                     │yes
                     ▼
           to_learn = list of dicts
                     │
app loop:  next_card() → 3s → flip_card()
             │✔                     │✘
             ▼                      ▼
   remove + to_csv()          next_card()
   (deck shrinks forever)
```

---

### 2. The Final Code Touches

```python
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
```

* `index=False` — no stray unnamed column in the saved CSV.
* When `to_learn` is empty, `pandas.DataFrame([]).to_csv` writes an empty file —
  the app has taught you *everything* it has.

---

### 3. The Capstone Wrap-Up

Four steps, four familiar patterns: UI (Day 27/28), data pipeline (Day 25/26),
timers (Day 28), persistence + exceptions (Day 30). Nothing new — everything combined.

---

### Summary Checklist

1. ✔ rewrites the deck; ✘ leaves it alone; startup picks the right file.
2. Runnable version: [`main.py`](main.py) (needs the course's images + CSVs)
