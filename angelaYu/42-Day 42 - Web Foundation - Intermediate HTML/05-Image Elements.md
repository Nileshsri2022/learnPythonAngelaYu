Here is a structured breakdown of this lesson on image elements.

---

### 1. The Image Tag

```html
<img src="cake.jpg" alt="A three-layer chocolate birthday cake">
```

* `src` — where the image file lives (relative path or URL).
* `alt` — text shown if the image fails, and read aloud by screen readers.
* `img` is a **void element** — no closing tag, no content.

---

### 2. Sizing

```html
<img src="cake.jpg" alt="cake" height="200">
```

* Set either `height` or `width` — the browser scales the other to keep proportions.
* (Real styling is CSS's job, coming on Day 43.)

---

### Summary Checklist

1. `img src alt` — always include the alt text.
2. Void element: no content, no closing tag.
