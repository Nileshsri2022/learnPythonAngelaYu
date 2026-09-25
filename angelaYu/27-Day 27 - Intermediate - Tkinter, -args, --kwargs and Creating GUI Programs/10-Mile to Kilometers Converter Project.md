Here is a structured breakdown of the Mile → Km converter project.

---

### 1. The Design (grid layout)

```
is equal to
[entry] Miles  →  [label0] Km   [Calculate]
```

* Row 0: label / label / label across three columns.
* Row 1: entry / button / result label.

---

### 2. The Solution

```python
import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609344, 2)
    result_label.config(text=f"{km}")

miles_input = tk.Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = tk.Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = tk.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
```

* The maths is trivial (× 1.609); the lesson is **wiring UI → function → UI update**:
  `.get()` reads the entry, `.config(text=...)` updates the result.

---

### Summary Checklist

1. Widgets created, then `.grid()`-ed into place.
2. Button callback: read input → compute → config the output label.
3. Runnable version: [`main.py`](main.py)
