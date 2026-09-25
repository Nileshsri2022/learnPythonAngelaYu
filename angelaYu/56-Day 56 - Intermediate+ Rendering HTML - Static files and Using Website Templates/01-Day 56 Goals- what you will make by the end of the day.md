Here is a structured breakdown of this lesson on the goals for Day 56.

---

### 1. What Today Adds

Yesterday we returned HTML as Python strings — painful and unmaintainable. Today we do it
properly:

| Topic | Payoff |
|-------|--------|
| **Rendering HTML files** | `render_template("index.html")` instead of giant strings |
| **Static files** | local images, CSS, videos served from a `static/` folder |
| **Website templates** | use free HTML/CSS templates and wire them into Flask |

---

### 2. The Final Project: A Personal Name Card

Nobody hands out paper business cards anymore. Today's project is a **digital name card**:

* your name in a big heading,
* an avatar image,
* links to your social/professional pages,
* a beautiful background and styling from a free template.

The goal is to prove you can take *any* HTML/CSS website off the shelf and serve it from a
Python server after a small amount of path fixing.

---

### 3. The Two Magic Folder Names

Flask is a framework, so it has rules:

```
my-personal-site/
├── server.py            # the Flask app
├── templates/           # HTML files MUST live here
│   └── index.html
└── static/              # CSS, images, JS, videos MUST live here
    ├── styles.css
    └── images/
```

Get these names right and most of the wiring just works.

---

### Summary Checklist

1. `render_template()` for HTML files; `static/` for assets.
2. Folder names `templates` and `static` are mandatory, lowercase, at project root.
3. Free templates (HTML5 UP, etc.) can be dropped in — you fix the paths, not the design.
4. Deliverable: your own name-card site served by Flask.
