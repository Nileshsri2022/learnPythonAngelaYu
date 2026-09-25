# Buttons, Entry, and Setting Component Options

---

### 1. Buttons

```python
def button_clicked():
    print("I got clicked")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()
```

* `command=` — the higher-order callback pattern (Day 19): pass the function **name**,
  no parentheses.

---

### 2. Entry (single-line text input)

```python
input_field = tkinter.Entry(width=10)
input_field.pack()

def button_clicked():
    user_text = input_field.get()      # read what the user typed
    my_label.config(text=user_text)    # update the label
```

---

### 3. Updating Widgets with `.config()`

`config()` changes an existing widget's options after creation — text, colour, whatever:

```python
my_label.config(text="New text!")
window.config(padx=20, pady=20)       # padding on the window itself
```

---

### Summary Checklist

1. `Button(command=function_name)` wires clicks to callbacks.
2. `Entry.get()` reads input; `.config()` updates widgets in place.
3. Padding options (`padx`, `pady`) give layouts breathing room.
