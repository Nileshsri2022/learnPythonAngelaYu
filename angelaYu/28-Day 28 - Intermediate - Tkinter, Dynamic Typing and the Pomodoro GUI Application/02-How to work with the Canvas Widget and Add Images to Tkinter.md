Here is a structured breakdown of this lesson on the Canvas widget and images.

---

### 1. The Canvas

A free-form drawing surface inside the window:

```python
import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=200, height=224, bg="green", highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)   # x, y = centre
canvas.create_text(100, 130, text="00:00", fill="white",
                   font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)
```

* `PhotoImage` — Tkinter's image class (PNG/GIF).
* `create_image(x, y, image=...)` — placed by its **centre** coordinates.
* `create_text(...)` — the timer text drawn *on top of* the image.
* `highlightthickness=0` — removes the default border.

---

### Summary Checklist

1. Canvas items (images, text, shapes) are created with `create_*` methods.
2. Text over an image = two canvas items, image first.
3. The canvas participates in `grid()` like any widget.
