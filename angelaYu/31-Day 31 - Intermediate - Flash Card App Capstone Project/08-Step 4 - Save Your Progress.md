Here is a structured breakdown of Step 4 — saving progress.

---

### 1. The Spec

* ✔-marked words must **stay learned** across app restarts.
* On ✔: rewrite the deck file **without** that word.
* On startup: load `words_to_learn.csv` if it exists; otherwise start from
  `french_words.csv`.

---

### 2. The Persistence Pattern

```python
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:                       # first ever run
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
```

And on every known word:

```python
def is_known():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()
```

* Day 30's exception pattern (try/except/else) selects the starting deck.
* The whole remaining deck is re-dumped after each ✔ — small file, no cleverness needed.

> **Note:** `index=False` drops Pandas' row-number column from the CSV.

---

### Summary Checklist

1. Two files: the original deck and the shrinking to-learn deck.
2. Startup chooses via FileNotFoundError; ✔ rewrites the deck.
