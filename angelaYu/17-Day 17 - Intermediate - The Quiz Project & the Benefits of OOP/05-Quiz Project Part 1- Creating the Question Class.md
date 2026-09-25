Here is a structured breakdown of Quiz Project Part 1 — creating the Question class.

---

### 1. The Blueprint for One Question

A quiz question is just *text + an answer* — a perfect little class:

```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

---

### 2. Turning Data into Objects

```python
new_q = Question("A slug's blood is green.", "True")
print(new_q.text)     # A slug's blood is green.
print(new_q.answer)   # True
```

This is the design habit to internalise: **represent each item of your data as an object**.
The quiz will hold a *list* of `Question` objects rather than raw tuples/dicts — objects
can later gain behaviour (shuffling, difficulty) without touching the quiz code.

---

### Summary Checklist

1. `Question` = two attributes: `text` and `answer`.
2. Construct one object per question.
3. Model data as classes when the data has identity and behaviour potential.
