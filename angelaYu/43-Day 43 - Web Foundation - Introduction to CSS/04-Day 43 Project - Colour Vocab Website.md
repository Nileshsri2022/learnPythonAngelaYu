Here is a structured breakdown of the Day 43 project — Colour Vocab Website.

---

### 1. The Task

A page teaching colour vocabulary (in Hindi!) — each colour word styled *in its own
colour*, one `<h1>` title, external stylesheet.

---

### 2. The Solution

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Colour Vocabulary</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Important Colours in Hindi</h1>
    <h2 class="red-colour">लाल (laal)</h2>
    <h2 class="blue-colour">नीला (neela)</h2>
    <h2 class="green-colour">हरा (hara)</h2>
</body>
</html>
```

```css
/* style.css */
body {
    background-color: #eeeeee;
    font-family: Arial, sans-serif;
}

h1 {
    text-align: center;
}

.red-colour { color: red; }
.blue-colour { color: blue; }
.green-colour { color: green; }
```

* Classes map each heading to its colour — one rule per class, no inline styles.
* The external stylesheet keeps the HTML purely structural.

---

### Summary Checklist

1. Class per colour; one CSS file does all styling.
2. Runnable versions: [`colour_vocab.html`](colour_vocab.html) + [`style.css`](style.css)
