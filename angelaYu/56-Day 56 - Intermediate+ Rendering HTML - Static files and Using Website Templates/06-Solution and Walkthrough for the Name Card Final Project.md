Here is a structured breakdown of the walkthrough for the Name Card final project.

---

### 1. Set Up and Drop the Template In

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
```

Then:

1. Create `templates/` and `static/`.
2. Move `index.html` → `templates/`.
3. Move `assets/` and `images/` → `static/`.

---

### 2. First Run: HTML Only

The page loads with no styling and no images — expected. Fix the paths by find & replace:

| Find | Replace |
|------|---------|
| `assets/` | `static/assets/` |
| `images/` | `static/images/` |

Save and reload; the CSS and images arrive.

> **Note:** Seeing the *previous* project's CSS is the browser cache, not a bug — Shift +
> refresh (hard reload) to pull the new static files.

---

### 3. The Trailing-Slash Bug

One image (the avatar) stays missing. The replacement dropped a slash, leaving something
like:

```html
<img src="static/imagesavatar.png">      <!-- wrong -->
<img src="static/images/avatar.png">     <!-- right -->
```

Find it, fix it, reload.

---

### 4. Make It Yours

1. **Avatar** — move your photo into `static/images/`, rename the old placeholder out of
   the way and update the `src`.
2. **Background** — the CSS composes a gradient *over* `images/bg.jpeg`. Rather than edit
   the CSS, download a nice photo (Unsplash is a good free source), rename it `bg.jpeg` and
   replace the placeholder.
3. **Text and links** — update the `<h1>`, the social `href`s and the footer.
4. **Title** — change `<title>` so the tab shows your name.
5. Hard reload after each static-file swap.

---

### 5. Also Noticed Along the Way

| Error | Cause | Fix |
|-------|-------|-----|
| `Address already in use` | another Flask server running on port 5000 | stop the other app, rerun |
| Stale styling | Chrome cache | Shift + refresh |
| Blurry gradient images | template's licensed placeholders | replace with your own images |

---

### 6. Done

You're serving a designer-quality template from a Python server, with your own content —
achieved with HTML, CSS and just enough Flask. Apply the same recipe to a portfolio site:
screenshot your projects, link each one, publish.

> **Tip:** Keep the template credit in the footer for personal use; buy the commercial
> licence if you're using it to sell something.

---

### Summary Checklist

1. Two folders + two find-and-replaces gets a template running on Flask.
2. Hard reload (Shift + refresh) whenever static files change.
3. Replace placeholders *by filename* to avoid touching CSS.
4. Fix broken paths one by one via the DevTools console 404s.
5. Personalise text, avatar, background, title — then ship it.
