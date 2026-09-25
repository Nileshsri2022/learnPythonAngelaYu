# Solution & Walkthrough for Creating the UI

---

### 1. The UI Code

```python
from tkinter import Tk, Canvas, PhotoImage, Button
import pandas

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_card_image = canvas.create_image(400, 263, image=card_front_img)
card_title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)

window.mainloop()
```

---

### 2. Why Track Item IDs?

`create_image` / `create_text` return **IDs** — stored so `itemconfig(id, ...)` can flip
the card later. That's the one new subtlety vs. earlier canvas work.

---

### Summary Checklist

1. Both card faces loaded up-front; front shown initially.
2. Item IDs (`canvas_card_image`, `card_title_text`, `card_word_text`) kept for flipping.
