# Challenge 1 - Working with Images and Setting up the Canvas

---

### 1. Padding + Canvas + Logo

```python
import tkinter
from tkinter import Canvas

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
```

* Same canvas pattern as the Pomodoro (Day 28): sized canvas, `PhotoImage`,
  `create_image` at the centre.
* `padx=50, pady=20` on the **window** gives the whole app breathing room.

---

### Summary Checklist

1. App icon/logo = canvas + `PhotoImage` + `create_image`.
2. Window-level padding frames everything.
