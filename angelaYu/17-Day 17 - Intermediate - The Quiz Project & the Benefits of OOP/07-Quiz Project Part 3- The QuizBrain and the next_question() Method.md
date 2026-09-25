Here is a structured breakdown of Quiz Project Part 3 — the QuizBrain and `next_question()`.

---

### 1. A Controller Class

`QuizBrain` owns the quiz **state** (the question list and where we are in it) and all
quiz **behaviour**:

```python
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        return user_answer
```

* Constructed **with** the question bank: `QuizBrain(question_bank)`.
* `question_number` tracks progress — state lives on the object, not in global variables.

---

### 2. Why a Separate Class?

Separation of concerns: `Question` = *one piece of data*; `QuizBrain` = *the running quiz*.
Each class is small, understandable, and independently reusable.

---

### Summary Checklist

1. `QuizBrain` stores the bank + a position counter.
2. `next_question()` displays the current question, increments the counter, returns the answer.
3. Controllers hold state + behaviour; models just hold data.
