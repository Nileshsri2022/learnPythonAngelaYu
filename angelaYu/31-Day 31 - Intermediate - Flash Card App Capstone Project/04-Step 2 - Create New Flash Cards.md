Here is a structured breakdown of Step 2 — creating new flash cards.

---

### 1. The Task

Load `french_words.csv` (`French,English` columns), pick a **random word**, show it:

1. `pandas.read_csv` → DataFrame → `to_dict(orient="records")` gives a list of
   dictionaries — `{"French": "poitrine", "English": "breast"}`.
2. `random.choice(cards)` picks one.
3. `next_card()` configures the title ("French") and the word.

---

### 2. The Shape of the Data

```python
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
# [{'French': 'poitrine', 'English': 'breast'}, ...]
```

`orient="records"` — *each row becomes one dict* — the nested-data pattern from Day 9,
arriving straight from Pandas (Day 25).

---

### Summary Checklist

1. CSV → DataFrame → list-of-dicts — the standard data pipeline.
2. `random.choice` picks the card; `itemconfig` writes it.
