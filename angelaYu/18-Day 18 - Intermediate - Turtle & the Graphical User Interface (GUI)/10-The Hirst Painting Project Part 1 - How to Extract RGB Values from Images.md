# The Hirst Painting Project Part 1 - How to Extract RGB Values from Images

---

### 1. The Goal

Damien Hirst's spot paintings are grids of coloured dots. The plan:

1. Extract the dominant colours from a photo of a real Hirst painting.
2. Use them as the palette for your own dot painting.

---

### 2. The `colorgram` Package

Install it (PyPI from Day 16), then extract colours from the image:

```bash
pip install colorgram.py
```

```python
import colorgram

rgb_colors = []
colors = colorgram.extract('hirst.jpg', 30)   # pull 30 colours

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)
```

* `extract(image, n)` returns the `n` most prominent colours.
* Each colour's `.rgb` exposes `.r`, `.g`, `.b` — collected as tuples.

> **Tip:** Manually drop near-white/background colours from the list before painting —
> you want *spots*, not the gallery wall.

---

### Summary Checklist

1. `colorgram.extract()` turns an image into colour objects.
2. Palette stored as a list of `(r, g, b)` tuples.
3. Curation matters — remove the background tones.
