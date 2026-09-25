Here is a structured walkthrough of the data-fetching solution.

---

### 1. Feeding the Existing Pipeline

Day 17's quiz engine consumed a list of `Question` objects. Only the construction loop
changes to match the API's field names:

```python
question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))
```

* `question["question"]` — the API's text field.
* `question["correct_answer"]` — `"True"` or `"False"` as strings.

This is the OOP payoff again: **the engine doesn't care where data came from.**

---

### 2. First Run Reveals a Problem

Some questions arrive looking like:

```
&quot;Southern Cross&quot; is the name of the UK&#039;s flag.
```

Those `&quot;` / `&#039;` are **HTML entities** — the next lesson fixes them.

---

### Summary Checklist

1. Swap dict keys; the `Question`/`QuizBrain` classes stay untouched.
2. Raw API text needs entity decoding before display.
