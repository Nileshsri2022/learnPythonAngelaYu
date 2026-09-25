Here is a structured breakdown of this lesson on Bootstrap components.

---

### 1. The Component Catalogue

getbootstrap.com documents them all; the daily drivers:

```html
<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">…</nav>

<!-- Buttons -->
<button class="btn btn-outline-light btn-lg">Sign up</button>

<!-- Card -->
<div class="card">
    <div class="card-header">Chihuahua</div>
    <div class="card-body"><h3>$0 / mo</h3><p>…</p></div>
</div>

<!-- Carousel (needs the Bootstrap JS bundle) -->
<div id="testimonials" class="carousel slide" data-bs-ride="false">…</div>
```

* Components compose: a card *inside* a column *inside* a row.
* Interactive ones (carousel, dropdown, collapse) require the JS `<script>` bundle
  before `</body>`.

---

### Summary Checklist

1. Navbar, buttons, cards, carousel — copy, tweak classes, ship.
2. JS bundle powers the interactive components.
