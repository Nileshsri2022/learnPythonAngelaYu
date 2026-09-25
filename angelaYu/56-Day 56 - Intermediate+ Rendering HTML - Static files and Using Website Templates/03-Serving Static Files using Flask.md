# Serving Static Files using Flask

---

### 1. The Broken Pages

Render a real HTML page and the image and CSS are missing. Chrome DevTools → *Console*
shows why:

```text
GET http://127.0.0.1:5000/angela.png        404 (NOT FOUND)
GET http://127.0.0.1:5000/styles.css        404 (NOT FOUND)
```

The HTML asked for files next to the page; Flask isn't looking there.

---

### 2. The Rule: Static Files Live in `static/`

```text
my-personal-site/
├── server.py
├── templates/
│   └── angela.html
└── static/
    ├── angela.png
    └── styles.css
```

* Create the `static` folder (lowercase) at project root.
* Move every image, stylesheet, video, favicon and JS file into it.
* Update the paths inside your HTML: `src="angela.png"` → `src="static/angela.png"`.

```html
<link rel="stylesheet" href="static/styles.css">
<img src="static/angela.png" alt="profile photo">
```

Refresh → the image and styles load.

> **Note:** "9 out of 10 Flask projects" have exactly these two folders:
> `templates/` for HTML, `static/` for everything else.

---

### 3. Challenge: Purple Background

1. Create `static/styles.css`:

```css
body {
    background-color: purple;
}
```

2. Link it in the `<head>` of the template:

```html
<link rel="stylesheet" href="static/styles.css">
```

3. Reload — purple background.

---

### 4. Chrome Caches Static Files

Change purple → red, save, restart the server, refresh… still purple. Chrome kept the old
`styles.css` because static files rarely change, and re-downloading them wastes bandwidth.

**Fix: hard reload.**

| Platform | Shortcut |
|----------|----------|
| Windows / Linux | `Ctrl + Shift + R` (or Shift + click refresh) |
| macOS | `Cmd + Shift + R` (or Shift + click refresh) |

> **Tip:** When a CSS/image change "doesn't apply", hard reload *first*. Nine times out of
> ten it isn't your code.

---

### Summary Checklist

1. Static assets must live in `static/`; update `src`/`href` to `static/…`.
2. Link CSS from the `<head>` of the template.
3. 404s on images/CSS mean the path or the folder is wrong.
4. Chrome caches static files — hard reload (Shift + refresh) after editing them.
