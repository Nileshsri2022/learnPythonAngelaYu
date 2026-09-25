# Day 44 Project - Motivational Poster Website

---

### 1. The Task

Recreate the classic motivational poster: an image in a black frame with white padding,
a bold title and a caption — pure box-model CSS.

---

### 2. The Solution

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Motivation</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="poster">
        <img src="mountains.jpg" alt="Misty mountains">
        <h1>KEEP CLIMBING</h1>
        <p>The view gets better with every step.</p>
    </div>
</body>
</html>
```

```css
body {
    background-color: #111;
}

.poster {
    width:          500px;
    margin:         50px auto;      /* centred horizontally */
    padding:        20px 20px 0;
    background-color: white;
    border:         5px solid #eee;
    text-align:     center;
    font-family:    'Libre Baskerville', serif;
}

.poster img {
    width: 100%;
}

.poster h1 {
    font-size: 3rem;
    color: black;
}

.poster p {
    color: grey;
    padding-bottom: 20px;
}
```

* Descendant selectors (`.poster img`) style children without extra classes.
* `margin: 50px auto` — the classic centring trick.

---

### Summary Checklist

1. Padding inside the white frame, border as the edge, margin to centre.
2. Runnable versions: [`motivational_poster.html`](motivational_poster.html) + [`style.css`](style.css)
