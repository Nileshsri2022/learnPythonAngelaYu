# Bootstrap Components

---

### 1. Components Are Copied, Not Invented

Every component has a docs page with a copy-paste snippet: find the one that matches your
design, paste, then replace the content (`src`, `alt`, text, links).

---

### 2. Buttons

```html
<button class="btn btn-success">Ok</button>
<a class="btn btn-primary" href="#">Download</a>
```

* `btn` + a colour class; colour names hint at meaning:

| Class | Meaning / typical use |
|-------|----------------------|
| `btn-primary` | main action (Go, Buy, Download) |
| `btn-success` | confirm (Ok) |
| `btn-danger` | destructive |
| `btn-warning` | caution |
| `btn-outline-*` | hollow variants |

One class swap changes the whole look — hover animation, padding, corners included.

---

### 3. Cards

The docs' card snippet gives you image + title + text + link in a bordered box:

```html
<div class="card" style="width: 18rem;">
    <img src="images/dog.png" class="card-img-top" alt="dog">
    <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
</div>
```

Cards are exactly what testimonials and pricing plans are built from.

---

### 4. Navbars

Bootstrap navbars are responsive out of the box:

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">TinDog</a>
        <!-- at narrow widths this collapses into a hamburger menu -->
    </div>
</nav>
```

Examples page → *Headers* has larger, more elaborate versions. Copy one, delete the menu
items you don't need, rename the rest (`Link` → `About`, `Dropdown` → `Pricing`).

---

### 5. The JavaScript Bundle Is Not Optional

Paste a navbar and click the hamburger at a narrow width: nothing happens. Cause: the
**Bootstrap JS bundle** is missing.

```html
<!-- just before </body> -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
```

With it: dropdowns, toggles, collapses, modals all work. You don't need to know
JavaScript to use it.

---

### 6. Customising a Snippet

| Task | How |
|------|-----|
| Remove a nav item | delete that `<li>` |
| Deactivate a button | it already has `class="disabled"` — remove it to re-enable |
| Rename a link | edit the anchor text |
| Move a button right | add utilities, e.g. `ms-auto` |

Later, your own `style.css` (linked *after* Bootstrap's CSS) overrides bootstrap styling —
that's how the TinDog gradient and fonts are applied.

---

### Summary Checklist

1. Docs → Components → copy the snippet → replace the content.
2. `btn` + a colour class for buttons; `.card` for boxed content.
3. Navbars are responsive by default (hamburger on small screens).
4. Always include the JS bundle before `</body>`, or interactivity breaks.
5. Customise by editing the snippet; override styles in your own CSS file.
