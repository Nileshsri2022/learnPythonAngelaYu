Here is a structured breakdown of Quiz Project Part 5 — checking answers and keeping score.

---

### 1. State for Scoring

Add a score attribute to the constructor:

```python
def __init__(self, q_list):
    self.question_number = 0
    self.score = 0
    self.question_list = q_list
```

---

### 2. Checking the Answer

Split the responsibilities — `next_question()` asks, `check_answer()` judges:

```python
def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    self.check_answer(user_answer, current_question.answer)

def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
        self.score += 1
        print("You got it right!")
    else:
        print("That's wrong.")
    print(f"The correct answer was: {correct_answer}.")
    print(f"Your current score is: {self.score}/{self.question_number}\n")
```

`.lower()` on both sides makes the comparison case-insensitive — small UX touch, big
friendliness.

---

### Summary Checklist

1. Score lives on the object and updates inside `check_answer()`.
2. Feedback prints after every question — right or wrong.
3. Each method does one job; the caller just loops.
