# Challenge - Build a Kanye Quotes App using the Kanye Rest API

---

### 1. The Task

A Tkinter window with Kanye's face; every button click fetches a fresh quote from
**kanye.rest** and displays it on the image.

---

### 2. The Solution

```python
import requests
import tkinter

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)

window = tkinter.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=300, height=414)
background_img = tkinter.PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE",
                                width=250, font=("Arial", 20, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = tkinter.PhotoImage(file="kanye.png")
kanye_button = tkinter.Button(image=kanye_img, highlightthickness=0,
                              command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
```

* API + GUI: the callback fetches and `itemconfig` displays.
* `width=250` on the canvas text wraps long quotes.

---

### Summary Checklist

1. Click → GET → parse → itemconfig — APIs inside event loops.
