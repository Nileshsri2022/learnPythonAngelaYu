# Font Properties

---

### 1. The Big Four

```css
h1 {
    font-family: "Helvetica Neue", Arial, sans-serif;  /* typeface */
    font-size:   32px;                                 /* size */
    font-weight: bold;      /* or 100–900: thin → black */
    font-style:  italic;
    text-align:  center;    /* left | right | center | justify */
}
```

* `font-family` falls back left→right until the browser finds one it has; always end
  with a generic family (`sans-serif`, `serif`, `monospace`).
* `font-weight` — 400 = normal, 700 = bold.
* Web-safe stacks: sans-serif (Arial/Helvetica), serif (Georgia/Times), monospace
  (Courier) — or load any font from fonts.google.com with a `<link>`.

---

### Summary Checklist

1. family, size, weight, style, alignment.
2. Always provide a fallback font chain.
