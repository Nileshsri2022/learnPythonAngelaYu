Here is a structured breakdown of this lesson on Tkinter layout managers.

---

### 1. The Three Layout Managers

```python
# pack — stack against an edge, in order
label.pack(side="left")

# place — exact pixel coordinates
label.place(x=100, y=200)

# grid — rows and columns
label.grid(column=1, row=1)
```

| Manager | Best for | Weakness |
|---------|----------|----------|
| `pack()` | simple vertical/horizontal stacks | limited control |
| `place()` | pixel-perfect positioning | breaks on resize |
| `grid()` | forms and aligned panels | — the usual choice |

---

### 2. Grid in Practice

```python
window.config(padx=20, pady=20)

label.grid(column=0, row=0)
button.grid(column=1, row=0)
entry.grid(column=2, row=0)

# A widget can span multiple columns:
button2.grid(column=1, row=1, columnspan=2)
```

> **Warning:** Never mix `grid()` and `pack()` in the **same window** — pick one
> manager per container.

---

### Summary Checklist

1. `pack` stacks, `place` pins pixels, `grid` aligns in rows/columns.
2. `padx`/`pady` on the window and widgets adds whitespace.
3. `columnspan` merges cells.
