Here is a structured breakdown of this lesson on using website templates.

---

### 1. Standing on Designers' Shoulders

Free HTML template galleries (html5up.net, templated.co, …) give complete, responsive,
beautifully-designed sites. The workflow:

1. Download a template — it arrives as `index.html` + an assets folder.
2. Move `index.html` → `templates/`, the assets → `static/`.
3. **Repoint every asset link** in the HTML to the `/static/...` paths.
4. Serve it with `render_template` — done, a professional site in minutes.

---

### 2. The Customisation Pass

* Swap the text for yours.
* Replace images (keep the filenames, or update links).
* Tweak the CSS colours — small changes, big difference.

> **Tip:** open DevTools and fix broken links one by one; each 404 in the Flask log
> names the file that didn't load.

---

### Summary Checklist

1. Download → restructure (templates/ + static/) → repoint links → serve.
2. Follow the 404s until the page renders perfectly.
