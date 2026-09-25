Here is a structured breakdown of this lesson on rendering HTML with Flask.

---

### 1. Right Now, Flask Wraps Your Text in a Bare Body

```python
return f"Hello {name}!"
```

View-source shows Flask stuffed the string into `<body>` with no structure. Fine for a
test; not a website.

---

### 2. Return Real HTML

Flask returns whatever string you give it — so give it HTML:

```python
@app.route("/")
def home():
    return "<h1 style='text-align: center'>Hello, World!</h1>"
```

Refresh → the heading is centred because the browser parsed the tags and the **inline CSS**
exactly as it would on a static page. Everything from Days 41–44 works here.

---

### 3. Multiple Elements and Multiline Strings

```python
@app.route("/")
def home():
    return ('<h1 style="text-align: center">Hello!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://media.giphy.com/media/…/giphy.gif" width="200">')
```

* Python's **implicit string concatenation** joins adjacent literals — press Enter inside
  the parentheses and PyCharm inserts the backslash/continuation for you.
* `<img>` is a self-closing tag: it needs `src` (and looks better with `width`), and
  animated GIFs render just like images.

> **Tip:** Watch your quote nesting. If the outer string uses `"`, use `'` inside the HTML
> attributes — or the other way round — otherwise the string terminates early.

---

### 4. Read It in DevTools

Chrome → Elements shows:

```html
<body>
  <h1 style="text-align: center">Hello, World!</h1>
  <p>This is a paragraph.</p>
  <img src="…" width="200">
</body>
```

You wrote the content; the browser built the document.

---

### 5. Why This Is Only a Stepping Stone

Returning markup as one long Python string gets ugly fast — no syntax highlighting, no
reuse, no separation of concerns. **Templates** (Day 56) fix that: keep the HTML in its own
file and let Flask fill in the blanks.

---

### Summary Checklist

1. Flask accepts HTML in the return value — tags, attributes and inline CSS all work.
2. Chain adjacent string literals to keep long markup readable.
3. `<img src="…" width="…">` renders pictures and GIFs.
4. Match outer/inner quotes when embedding attributes.
5. This works, but templates are the clean way — that's tomorrow.
