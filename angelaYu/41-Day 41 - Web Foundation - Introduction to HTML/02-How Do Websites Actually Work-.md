# How Do Websites Actually Work

---

### 1. The Three Languages of the Front-End

| Language | Role | Analogy |
|----------|------|---------|
| **HTML** | structure & content | the skeleton |
| **CSS** | presentation & style | the clothing |
| **JavaScript** | behaviour & interactivity | the muscles |

Every website you've ever seen is these three, delivered as text files over HTTP.

---

### 2. What the Browser Does

It receives the HTML, parses it into a tree (**the DOM**), fetches linked CSS/JS/images,
applies the styles, runs the scripts, and paints the pixels. Writing HTML means writing
the instructions for that tree.

---

### Summary Checklist

1. HTML = structure; CSS = style; JS = behaviour.
2. The browser assembles the page from plain text files.
