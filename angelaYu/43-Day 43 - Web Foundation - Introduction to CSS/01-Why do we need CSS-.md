# Why do we need CSS

---

### 1. HTML Alone Is Ugly

HTML tells the browser what things *are* — headings, paragraphs, images. **CSS
(Cascading Style Sheets)** tells it how things *look*: colours, fonts, spacing, layout.

Toggle the CSS off on any site and you get the 1994 web: black text on white, default
blue links.

---

### 2. The Syntax

```css
selector {
    property: value;
}

h1 {
    color: red;
    font-size: 48px;
}
```

* **Selector** — *which* elements to style.
* **Declaration block** — `{ property: value; }` pairs — *how* to style them.

---

### Summary Checklist

1. CSS = presentation layer, separate from HTML structure.
2. Rule = selector + declarations.
