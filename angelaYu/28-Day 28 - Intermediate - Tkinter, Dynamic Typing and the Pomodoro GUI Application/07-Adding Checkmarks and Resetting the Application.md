Here is a structured breakdown of this lesson on checkmarks and reset.

---

### 1. Checkmarks

Each completed **work** session adds a ✔:

```python
def count_down(count):
    ...
    if count == 0:
        global reps
        if reps % 2 == 0:                  # a work block just finished
            checks_label.config(text="✔" * (reps // 2))
        window.after(500, start_timer)     # auto-start the next session
```

* `"✔" * n` — string repetition builds the progress marks.
* Chaining `after` → `start_timer` → `count_down` makes the app run unattended.

---

### 2. Resetting

```python
def reset_timer():
    global reps, timer
    window.after_cancel(timer)      # stop the scheduled tick!
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checks_label.config(text="")
```

The detail everyone misses: **`after_cancel(timer)`** — without it, the pending
`count_down` call keeps ticking after the reset (a classic ghost-timer bug). Store the ID
`after()` returns and cancel it.

---

### Summary Checklist

1. ✔ marks = completed work sessions, drawn by string repetition.
2. Auto-advance sessions with `after` → `start_timer`.
3. Reset must **cancel the scheduled callback** and restore all state.
4. Runnable version: [`main.py`](main.py) (needs the course's `tomato.png`)
