# Other Tkinter Widgets- Radiobuttons, Scales, Checkbuttons and more

---

### 1. A Tour of Widgets

```python
# Text — multi-line text area
text = tkinter.Text(height=5, width=30)
text.focus()                      # cursor starts here
text.insert(tkinter.END, "Example text")

# Spinbox — number selector with arrows
spinbox = tkinter.Spinbox(from_=0, to=10, width=5)

# Scale — slider
scale = tkinter.Scale(from_=0, to=100, orient="horizontal")

# Checkbutton — on/off box
checked_state = tkinter.BooleanVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state)

# Radiobutton — choose one of several
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state)
```

Each widget is an object with its own options (`height`, `width`, `text`, `variable`…)
— configured exactly like Labels and Buttons via keyword arguments.

---

### 2. The Takeaway

You don't memorise widgets — you **look them up** (tkdocs.com or the Python docs) when a
UI needs one. The API pattern is always: construct with options, place with a layout
manager, react with callbacks.

---

### Summary Checklist

1. Text, Spinbox, Scale, Checkbutton, Radiobutton cover most simple UIs.
2. Shared state with widgets via `BooleanVar`/`IntVar`.
3. Docs-reading (Day 18 skill) is how you learn any new widget.
