Here is a structured breakdown of this lesson on checking the answer.

---

### 1. Buttons Feed the Engine

```python
def true_pressed(self):
    is_right = self.quiz.check_answer("True")
    self.give_feedback(is_right)

def false_pressed(self):
    is_right = self.quiz.check_answer("False")
    self.give_feedback(is_right)
```

```python
# in QuizBrain — now fully type-hinted
def check_answer(self, user_answer: str) -> bool:
    correct_answer = self.current_question.answer
    if user_answer.lower() == correct_answer.lower():
        self.score += 1
        return True
    else:
        return False
```

* The engine returns a **Boolean**; the UI decides how to *show* it — logic and
  presentation stay separated.
* `current_question` is stored in `next_question()` so `check_answer` can reach the
  answer without re-indexing.

---

### Summary Checklist

1. Handlers pass the pressed answer to `check_answer("True"/"False")`.
2. The engine returns True/False; feedback is the UI's job.
