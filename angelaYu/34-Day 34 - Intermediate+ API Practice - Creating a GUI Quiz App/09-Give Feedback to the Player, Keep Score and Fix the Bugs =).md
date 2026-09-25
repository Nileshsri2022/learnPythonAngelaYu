# Give Feedback to the Player, Keep Score and Fix the Bugs =)

---

### 1. Visual Feedback

The card flashes green (correct) or red (wrong) for a second:

```python
def give_feedback(self, is_right: bool):
    self.canvas.config(bg="#7CFC00" if is_right else "#FF5733")
    self.window.after(1000, self.get_next_question)
```

* Instant colour, then `after` schedules the next card — the timer pattern from
  Days 28/31, with its familiar ghost-timer fix if needed.

---

### 2. Score + End of Quiz

```python
def get_next_question(self):
    self.canvas.config(bg="white")
    self.score_label.config(text=f"Score: {self.quiz.score}")
    if self.quiz.still_has_questions():
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    else:
        self.canvas.itemconfig(self.question_text,
                               text="You've completed the quiz!")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
```

* Score label updates on every question.
* When the bank is exhausted: final message + **disabled buttons** (`state="disabled"`).

---

### 3. The Bug Fixes of the Day

* `input()` removed from the engine (GUI can't block).
* Timer IDs tracked/cancelled where `after` chains.
* Score shown *before* advancing so the update is visible.

---

### Summary Checklist

1. Green/red flash = immediate, wordless feedback.
2. `state="disabled"` freezes the app at quiz end.
3. Runnable version: [`main.py`](main.py) (+ `quiz_brain.py`, `question_model.py`,
   `data.py`, `ui.py`)
