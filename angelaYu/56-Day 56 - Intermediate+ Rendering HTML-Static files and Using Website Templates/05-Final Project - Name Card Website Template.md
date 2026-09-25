Here is a structured breakdown of the Day 55-56 project — Name Card Website.

---

### 1. The Task

Serve a personal "name card" site through Flask: a styled HTML page with your name,
job title, a short intro and links — built from a template-style layout, with the CSS
in `static/`.

---

### 2. The Structure

```
Day 56/
├── main.py                     # Flask app: renders the card
├── templates/
│   └── index.html              # the name card page
└── static/
    └── css/style.css           # its styling
```

Run `python3 main.py` → http://127.0.0.1:5000/ shows the card. The solution
walkthrough (lecture 06) does the same with a downloaded template: restructure into
`templates/` + `static/`, repoint asset links, customise the content.

---

### Summary Checklist

1. Flask project = main.py + templates/ + static/.
2. Files for this version: [`main.py`](main.py), [`templates/index.html`](templates/index.html), [`static/css/style.css`](static/css/style.css)
