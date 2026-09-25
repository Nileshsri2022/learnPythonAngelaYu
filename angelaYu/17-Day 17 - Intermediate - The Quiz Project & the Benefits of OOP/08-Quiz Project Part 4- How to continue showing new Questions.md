Here is a structured breakdown of Quiz Project Part 4 — looping until the quiz is done.

---

### 1. A `still_has_questions()` Method

The QuizBrain can answer its own "are we done?":

```python
def still_has_questions(self):
    return self.question_number < len(self.question_list)
```

Returns a Boolean — exactly what a `while` condition wants.

---

### 2. The Game Loop

```python
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
```

The loop keeps asking while there's fuel; when `question_number` reaches the list length,
`still_has_questions()` flips to `False` and the loop ends.

---

### Summary Checklist

1. `while quiz.still_has_questions():` — the object reports its own completion.
2. The final score line uses the object's state — no extra bookkeeping.
3. Methods that return Booleans (`has_x`, `is_x`) make loops read like English.
