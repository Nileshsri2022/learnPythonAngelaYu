# What is HTML

---

### 1. HyperText Markup Language

* **HyperText** — text with links to other text.
* **Markup** — *annotations* that tell the browser what each piece of text **is**.

A piece of text wrapped in annotations is an **element**:

```html
<h1>I'm a top-level heading</h1>
```

* `<h1>` — opening **tag**
* `I'm a top-level heading` — content
* `</h1>` — closing tag (same name + a slash)

The browser doesn't display the tags — it *obeys* them.

---

### 2. The HTML Boilerplate

Every page starts from this scaffold (VS Code: `!` + Tab):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My First Page</title>
</head>
<body>
    <h1>Hello, world!</h1>
</body>
</html>
```

* `head` — invisible metadata: charset, title (browser tab), links.
* `body` — everything the visitor actually sees.

---

### Summary Checklist

1. Element = opening tag + content + closing tag.
2. Boilerplate first: doctype, html, head, body.
3. Head is for the machine; body is for the human.
