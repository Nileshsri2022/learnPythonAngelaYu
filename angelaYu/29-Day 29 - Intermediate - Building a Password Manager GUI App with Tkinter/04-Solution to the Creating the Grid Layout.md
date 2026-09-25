# Solution to the Creating the Grid Layout

---

### 1. The Full UI Code

```python
from tkinter import Tk, Canvas, Label, Entry, Button, PhotoImage

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()          # cursor starts in the website field

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "your@email.com")   # pre-fill a default email

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
```

---

### 2. Nice Touches

* `focus()` — the cursor begins in the first field.
* `insert(0, ...)` — pre-fills the email so you type less.

---

### Summary Checklist

1. Every widget: create → `.grid(row, column, ...)`.
2. `focus()` and `insert()` reduce typing friction.
