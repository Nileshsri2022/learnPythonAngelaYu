# The Benefits of OOP- Use Open Trivia DB to Get New Questions

---

### 1. The Payoff

Because the quiz engine consumes **Question objects**, the data source can change without
touching `QuizBrain` at all. The course's `data.py` fetches fresh questions from the
**Open Trivia Database** (opentdb.com):

```python
# data.py — new question format from the API
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
question_data = response.json()["results"]
# each item: {"question": ..., "correct_answer": ..., ...}
```

---

### 2. The Only Change Needed

The construction loop adapts to the new *field names* — nothing else:

```python
question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))
```

`QuizBrain` is untouched. That's the **benefit of OOP**: boundaries between data, model
and engine mean each part can evolve independently.

---

### Summary Checklist

1. Same engine, new data source — change one loop, keep the classes.
2. Decoupled design = easy swaps, easy tests, easy reuse.
3. Your quiz now has effectively unlimited questions. 🌍
