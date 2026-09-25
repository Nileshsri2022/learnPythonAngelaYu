# Python Typing & Showing the Next Question in the GUI

---

### 1. The Bridge Method

The UI asks the engine for the next question and displays it:

```python
def get_next_question(self):
    self.canvas.config(bg="white")
    q_text = self.quiz.next_question()
    self.canvas.itemconfig(self.question_text, text=q_text)
```

* `quiz.next_question()` currently returns the text **and** prompts the console — the
  prompt is removed so the method purely *returns* `Q.1: text (True/False)?`.
* The canvas is reset to white before showing each new card.

---

### 2. The First Type Hint

```python
def __init__(self, quiz_brain: QuizBrain):
```

The `: QuizBrain` documents what the constructor expects — editor autocomplete and
readers benefit. (Full type-hint lesson in a moment.)

---

### Summary Checklist

1. UI methods call engine methods; results go to canvas items.
2. `next_question()` becomes a pure return (no input() inside a GUI!).
3. Type hints start appearing on public interfaces.
