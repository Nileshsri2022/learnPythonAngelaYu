Here is a structured breakdown of this lesson on rendering HTML from Flask.

---

### 1. Return Markup, Not Just Words

```python
@app.route("/")
def home():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph.</p>"

@app.route("/<name>")
def greet(name):
    return f"<h1>Hello {name.title()}!</h1>"
```

The returned string **is** the response body — if it contains HTML, the browser
renders it. f-strings inject data (the path variable) into the markup.

---

### 2. Inline Styles Work Too

Until templates arrive (Day 56), style with inline CSS exactly as in Day 43's
"inline styles" lesson — same rules, same limitations.

---

### Summary Checklist

1. `return "<h1>…</h1>"` — Flask serves whatever string you give it.
2. f-strings = your template engine for today.
