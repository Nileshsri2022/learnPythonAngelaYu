Here is a structured breakdown of this lesson on CSS colours.

---

### 1. The colour property, Four Ways

```css
h1 { color: red; }                        /* named */
h2 { color: #4a90d9; }                    /* hex: RR GG BB */
h3 { color: rgb(74, 144, 217); }          /* rgb(red, green, blue) 0-255 */
p  { color: rgba(74, 144, 217, 0.5); }    /* + alpha = transparency */
```

* Hex and RGB are the same numbers in different clothes: `#4a` = `74` in hex.
* `alpha` runs 0 (invisible) → 1 (solid).

---

### 2. Picking Colours

Google "color picker" gives you a live eyedropper with hex + RGB values. Colour
palettes (e.g. coolors.co) help you pick sets that work together.

---

### Summary Checklist

1. Same colour, four notations — hex and rgb dominate in practice.
2. Alpha adds transparency.
