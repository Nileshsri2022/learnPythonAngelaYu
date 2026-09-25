Here is a structured breakdown of this lesson on Bootstrap layout.

---

### 1. Container → Row → Column

```html
<div class="container">
    <div class="row">
        <div class="col">One third</div>
        <div class="col">One third</div>
        <div class="col">One third</div>
    </div>
</div>
```

* `container` — centred, padded page wrapper.
* `row` — a horizontal line of columns.
* `col` — each row holds **12 column units**; equal `col`s split it evenly.

---

### 2. Responsive Widths

```html
<div class="col-lg-3 col-md-6">Card</div>
```

| Breakpoint | Screen | Effect |
|---|---|---|
| `col-lg-3` | ≥ 992px | takes 3/12 (a quarter) |
| `col-md-6` | ≥ 768px | takes 6/12 (a half) |
| below | phone | takes the full 12 (stacked) |

Add breakpoint classes and the same markup rearranges itself from phone to desktop.

---

### Summary Checklist

1. Row = 12 units; cols consume units.
2. `col-{breakpoint}-{units}` = responsive by construction.
