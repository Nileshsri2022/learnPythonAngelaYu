# Challenge 2 - Use grid() and columnspan to Complete the User Interface

---

### 1. The Target

```text
row 0:                 [logo canvas]
row 1:  Website:       [entry.............] [search*]
row 2:  Email/Username:[entry.............]
row 3:  Password:      [entry......] [Generate Password]
row 4:                 [Add............]
```

**`columnspan`** lets the Add button (and entries) stretch across columns:

```python
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")
```

* `columnspan=2` — the widget occupies two grid cells.
* `sticky="ew"` — stretch east-west to fill the merged cell.

---

### 2. Layout Thinking

* Labels in column 0; inputs in columns 1–2.
* Widgets line up *because* the grid enforces alignment — no pixel maths.

---

### Summary Checklist

1. `columnspan` + `sticky` widen inputs and buttons.
2. Grid alignment is why forms look tidy with zero effort.
