# Bootstrap Layout

---

### 1. Container → Row → Columns

```html
<div class="container">
    <div class="row">
        <div class="col">One</div>
        <div class="col">Two</div>
        <div class="col">Three</div>
    </div>
</div>
```

* **container** — the wrapper, adds margins and a max width.
* **row** — a horizontal band.
* **col** — items; bootstrap divides the row's width equally between them.

Three `col`s → 33 % each; six → 16.6 % each. No CSS written.

---

### 2. Containers and Breakpoints

| Class | Behaviour |
|-------|-----------|
| `container` | fixed max-width, changes by screen size, with side margins |
| `container-sm/md/lg/xl` | 100 % width *up to* that breakpoint, fixed above it |
| `container-fluid` | always 100 % width, edge to edge |

Bootstrap breakpoints (width of the **viewport**):

| Suffix | Typical device | Min width |
|--------|----------------|-----------|
| (none) | phone | < 576 px |
| `sm` | large phone | ≥ 576 px |
| `md` | tablet / iPad | ≥ 768 px |
| `lg` | laptop | ≥ 992 px |
| `xl` | desktop | ≥ 1200 px |
| `xxl` | big desktop / TV | ≥ 1400 px |

> **Note:** Suffixes are **minimums** — `col-md-4` means "4/12 wide on medium screens
> *and larger*", not "on medium only".

---

### 3. Sized Columns: The 12-Column Grid

Every row is 12 columns wide. `col-N` claims N of them:

```html
<div class="row">
    <div class="col-2">Sidebar — 2/12</div>
    <div class="col-4">Content — 4/12</div>
    <div class="col-6">Content — 6/12</div>
</div>
```

| Class | Width |
|-------|-------|
| `col-1` … `col-12` | 8.3 % … 100 % |
| `col-6` | 50 % |

---

### 4. Multiple Breakpoints per Element

```html
<div class="col-lg-4 col-md-8 col-sm-12">
```

* On `lg` and up → 4/12 wide (e.g. three cards side by side).
* On `md` → 8/12 wide.
* On `sm` and below → 12/12, full width (stacked).

This is how you build *responsive* layouts without writing media queries: mobile-first
stacking by default, wider arrangements as the screen grows.

---

### 5. Design Pattern

```html
<div class="container">
    <div class="row">
        <div class="col-lg-4 col-md-6">Card 1</div>
        <div class="col-lg-4 col-md-6">Card 2</div>
        <div class="col-lg-4 col-md-12">Card 3</div>
    </div>
</div>
```

Three columns on desktop, two on tablet, one on mobile. Bootstrap handles sums > 12 by
wrapping items onto the next line.

---

### Summary Checklist

1. `container` → `row` → `col`, always in that order.
2. Unqualified `col` splits the row equally.
3. `col-N` claims N of 12 columns (6 = half, 4 = a third, 3 = a quarter).
4. Breakpoint suffixes are minimums; combine them for responsive behaviour.
5. You rarely need media queries — the grid does the responsive work.
