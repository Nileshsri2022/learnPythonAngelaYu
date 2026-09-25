# Quiz Project Part 2- Creating the List of Question Objects from the Data

---

### 1. The Raw Data

The starting file provides a list of `[text, answer]` pairs:

```python
question_data = [
    ["A slug's blood is green.", "True"],
    ["The loudest animal is the African Elephant.", "False"],
    # ...
]
```

---

### 2. Mapping the Data into Objects

Loop the data and construct one `Question` per pair:

```python
question_bank = []
for question in question_data:
    question_text = question[0]
    question_answer = question[1]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
```

Or the compact version (unpacking while iterating):

```python
question_bank = [Question(q[0], q[1]) for q in question_data]
```

The `question_bank` is what the quiz engine will consume — a list of proper objects.

---

### Summary Checklist

1. Raw data → loop → construct → `question_bank` of `Question` objects.
2. The data's *shape* stays in one place; the engine never sees raw lists.
3. This conversion step is the standard bridge between data and OOP design.
