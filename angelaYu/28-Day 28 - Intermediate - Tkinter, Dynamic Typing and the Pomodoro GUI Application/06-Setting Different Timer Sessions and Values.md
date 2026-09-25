Here is a structured breakdown of this lesson on the different timer sessions.

---

### 1. The Session Cycle

`reps` counts every timer start; the cycle repeats work → short break, with every 4th
work slot followed by a **long** break:

```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:                       # every 4th work session done
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:                     # even = break time
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:                                   # odd = work time
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
```

The modulo (Day 3!) sequences the whole schedule.

---

### 2. Why Colour + Text Switch

`title_label.config(text=..., fg=...)` re-skins the app per session — the user always
knows whether to work or rest.

---

### Summary Checklist

1. One `reps` counter drives the whole cycle via `% 8` / `% 2`.
2. Session type = colour + label + length.
