Here is a structured breakdown of this lesson on the three ways to add CSS.

---

### 1. Inline (avoid)

```html
<p style="color: red;">Red text</p>
```

Styles one element via a `style` attribute — mixes presentation into structure.

---

### 2. Internal `<style>` Tag

```html
<head>
    <style>
        p { color: red; }
    </style>
</head>
```

Styles one page — good for quick demos.

---

### 3. External Stylesheet (the way)

```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

```css
/* styles.css */
p {
    color: red;
}
```

* One file styles the whole site; cached by the browser; clean separation of concerns.

---

### 4. Cascade Order

When rules collide, **inline > internal > external**, and within the same sheet, the
*last* rule wins. Hence "cascading".

---

### Summary Checklist

1. Three injection points; external stylesheet wins professionally.
2. Conflicts resolve by specificity and order.
