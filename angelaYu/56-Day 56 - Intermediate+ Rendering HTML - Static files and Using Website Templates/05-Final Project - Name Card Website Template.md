Here is a structured breakdown of this lesson on the Name Card final project.

---

### 1. The Assignment

Build a **personal name-card website** served by Flask:

* a big greeting (`<h1>`) with your name,
* a round avatar image,
* links to your social/professional profiles,
* a styled background — start from a free template and make it yours.

This is the classic "digital business card" every developer eventually wants.

---

### 2. Suggested Build Order

| Step | Action |
|------|--------|
| 1 | Pick a free template (HTML5 UP etc.) and download it |
| 2 | Create `templates/` and `static/` in the project |
| 3 | `index.html` → `templates/`; `assets/`, `images/` → `static/` |
| 4 | Find & replace `assets/` → `static/assets/`, `images/` → `static/images/` |
| 5 | `server.py`: home route returns `render_template("index.html")`, `debug=True` |
| 6 | Run, refresh, fix what looks broken |
| 7 | Replace the text, links, avatar and background image with your own |

---

### 3. Customising

```html
<h1>Hi, I'm Angela 👋</h1>

<a href="https://twitter.com/yourhandle">Twitter</a>
<a href="https://github.com/yourhandle">GitHub</a>
<a href="mailto:you@example.com">Email</a>
```

* Swap the avatar: drop your photo into `static/images/` and point the `src` at it.
* Swap the background: the CSS references e.g. `images/bg.jpeg` — **rename your image to
  `bg.jpeg`** and replace the placeholder instead of editing the CSS.
* Update the `<title>` so the browser tab says your name.

---

### 4. Things That Will Go Wrong (and the Fixes)

| Symptom | Cause | Fix |
|---------|-------|-----|
| No styling at all | paths not prefixed with `static/` | find & replace all asset paths |
| One image missing | a missed trailing `/` in a replacement | check that specific `src` |
| Changes don't appear | Chrome cached the CSS/image | hard reload (Shift + refresh) |
| `Address already in use` | another Flask app still running | stop it, then rerun |

---

### 5. Definition of Done

* [ ] Home page serves the template through Flask.
* [ ] All CSS/images load (DevTools console shows no 404s).
* [ ] Your name, photo, links and background are in place.
* [ ] Legal: attribution left in the footer, or a commercial licence purchased.

---

### Summary Checklist

1. Template → `templates/` + `static/`, paths fixed with find & replace.
2. Personalise the text, avatar, background and title.
3. Hard reload after touching static files; watch for 404s in DevTools.
4. You now know enough HTML, CSS and Flask to take *any* template and serve it — the recipe
   for a portfolio.
