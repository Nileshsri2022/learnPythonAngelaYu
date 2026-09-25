# Step 3 - Flip the Cards!

---

### 1. The Spec

* After 3 seconds, the card flips: background → back image, title → "English",
  word → the English translation, text colour → white.
* Pressing ✘ or ✔ immediately shows the next card **and cancels any pending flip**.

---

### 2. The Timing Bug to Avoid

If `next_card()` doesn't cancel the previous `after`, an old flip fires mid-card —
French word suddenly flipping to a *previous* English word. Hence:

```python
def next_card():
    global flip_timer
    window.after_cancel(flip_timer)     # kill the stale countdown first
    current_card = random.choice(to_learn)
    ...
    flip_timer = window.after(3000, flip_card)
```

Every scheduled callback needs a lifecycle: store the ID, cancel before rescheduling.

---

### Summary Checklist

1. Flip = itemconfig on image + title + word + colour.
2. `after_cancel` before every new card — timing bugs are state bugs.
