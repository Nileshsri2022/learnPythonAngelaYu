# Class based Tkinter UI

---

### 1. Wrapping the UI in a Class

Instead of module-level widgets, the whole interface becomes a `QuizInterface` class:

```python
import tkinter

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280,
            text="Question text here",
            fill=THEME_COLOR, font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_image,
                                          highlightthickness=0,
                                          command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_image,
                                           highlightthickness=0,
                                           command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()
```

---

### 2. Why a Class?

* Widgets become `self.` attributes — any method can update them.
* The quiz engine is injected: `QuizInterface(quiz_brain)` — **dependency injection**,
  keeping UI and logic decoupled.
* `mainloop()` moves into the constructor: constructing the object *runs the app*.

---

### Summary Checklist

1. UI class = widgets as attributes + handler methods.
2. The engine arrives as a constructor argument.
3. `get_next_question()` draws the first card before `mainloop()`.
