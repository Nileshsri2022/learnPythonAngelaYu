Here is a structured breakdown of this lesson on serving static files.

---

### 1. The static Folder

```
my_project/
├── main.py
├── templates/index.html
└── static/
    ├── css/style.css
    ├── js/script.js
    └── img/avatar.jpg
```

Flask serves everything under `static/` at `/static/...` — no routes needed.

---

### 2. Referencing Static Files

```html
<link rel="stylesheet" href="static/css/style.css">
<img src="static/img/avatar.jpg" alt="My avatar">
```

or with Flask's URL builder (the robust way):

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

* The curly-brace syntax is Jinja (formally introduced on Day 57).
* Broken paths are the #1 cause of "my CSS isn't loading" — check the terminal's 404s.

---

### Summary Checklist

1. `static/` = CSS/JS/images, auto-served at `/static/...`.
2. `url_for('static', filename=…)` builds correct paths for you.
