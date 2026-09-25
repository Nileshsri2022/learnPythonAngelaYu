# Step 1 - Create the User Interface (UI) with Tkinter

---

### 1. What to Build

```text
row 0:                 [title: French / English]
row 1:   [canvas: card_front.png / card_back.png with word text]
row 2:            [✘ button]        [✔ button]
```

* `BACKGROUND_COLOR = "#B1DDC6"` — the app's pastel green.
* Card = canvas with the card image; the word is canvas **text** on top.
* Flip = `canvas.itemconfig()` on the image *and* the text.

---

### 2. The Pieces to Reach For

* `tkinter.PhotoImage(file="card_front.png")` for both card faces.
* `canvas.create_image(...)`, `canvas.create_text(...)` — two tracked items.
* `LangButton` = plain `Button` with the ✘/✔ images.

> **Tip:** Same workflow as Day 28's UI — constants, canvas, grid, placeholder
> callbacks first.

---

### Summary Checklist

1. One canvas, two images, two text items — flip = reconfiguring all of them.
2. Buttons carry the cross/tick images.
