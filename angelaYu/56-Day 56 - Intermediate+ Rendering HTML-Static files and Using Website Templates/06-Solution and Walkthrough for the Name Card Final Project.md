Here is a structured breakdown of this lesson on the solution walkthrough.

---

### 1. The Walkthrough Steps

1. **Restructure** the downloaded template: `index.html` into `templates/`, its
   `assets/` contents into `static/css`, `static/js`, `static/img`.
2. **Repoint** links: `assets/css/main.css` → `/static/css/main.css` for every
   stylesheet, script and image.
3. **Serve** it: `return render_template("index.html")`.
4. **Customise**: your name, title, blurb, links, images.
5. Watch the Flask log for 404s — each one is a link you missed.

---

### 2. Key Code

```python
@app.route("/")
def home():
    return render_template("index.html")
```

The template does the rest. Notice how little Python a good site needs.

---

### Summary Checklist

1. Move → repoint → serve → customise.
2. Runnable version: [`main.py`](main.py) + [`templates/index.html`](templates/index.html)
