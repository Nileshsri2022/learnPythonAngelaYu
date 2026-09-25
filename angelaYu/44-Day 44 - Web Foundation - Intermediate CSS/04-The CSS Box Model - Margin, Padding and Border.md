Here is a structured breakdown of this lesson on the CSS box model.

---

### 1. Everything Is a Box

Every element is a box of four layers, from inside out:

```
┌───────────────────────────── margin ─────────────────────────┐
│  ┌───────────────────────── border ───────────────────────┐  │
│  │  ┌────────────────────── padding ──────────────────┐   │  │
│  │  │                  content                        │   │  │
```

* **content** — text/image.
* **padding** — transparent space *inside* the border.
* **border** — the edge: width, style, colour.
* **margin** — transparent space *outside* the border, pushing neighbours away.

---

### 2. In Code

```css
p {
    border: 3px solid black;      /* width style colour */
    padding: 20px;                /* all sides */
    margin: 40px;
}
```

Each layer also has per-side properties: `margin-top`, `padding-left`, …

---

### Summary Checklist

1. content → padding → border → margin, inside out.
2. `border: width style colour` shorthand; per-side variants exist.
