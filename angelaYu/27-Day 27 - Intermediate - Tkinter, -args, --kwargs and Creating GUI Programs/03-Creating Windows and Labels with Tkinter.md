# Creating Windows and Labels with Tkinter

---

### 1. The Smallest Tkinter Program

```python
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# A Label widget
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()          # place it on the window

window.mainloop()        # keep the window on screen, listening
```

* `tkinter.Tk()` — the window object.
* `Label(...)` — a text widget; `pack()` makes it visible (layout comes later).
* `mainloop()` — the program's event loop; it must be the **last** line.

> **Note:** You'll often see `from tkinter import *` in old tutorials — avoid it;
> import explicitly like every other module.

---

### Summary Checklist

1. Window → widgets → `mainloop()`.
2. A widget only appears once a layout manager (`pack`/`grid`/`place`) places it.
