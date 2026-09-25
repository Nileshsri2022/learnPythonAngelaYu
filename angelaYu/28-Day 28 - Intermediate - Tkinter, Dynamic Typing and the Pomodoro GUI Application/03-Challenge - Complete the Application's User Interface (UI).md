# Challenge - Complete the Application's User Interface (UI)

---

### 1. The Target Layout

```text
[row 0]            TIMER (label, columnspan=3)
[row 1]   Start    CANVAS(tomato)    Reset
[row 2]            ✔ ✔               (label, columnspan=3)
```

Constants for the colours and session lengths:

```python
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```

---

### 2. Key Pieces

* Timer label: `title_label.config(fg=GREEN)` colours the text per session type.
* Buttons: `command=start_timer` / `command=reset_timer` (names, not calls!).
* Checkmark label: `checks_label.config(text="✔" * reps)` — string repetition.

> **Tip:** Build the UI with placeholder functions first (`def start_timer(): pass`),
> get the grid right, then fill in behaviour.

---

### Summary Checklist

1. `grid()` with `columnspan=3` for full-width rows.
2. Colours/fonts/sessions as ALL_CAPS constants.
3. Placeholder-first layout building is a pro workflow.
