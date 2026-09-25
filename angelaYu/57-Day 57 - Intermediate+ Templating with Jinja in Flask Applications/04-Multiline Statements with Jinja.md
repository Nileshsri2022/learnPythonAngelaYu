Here is a structured breakdown of this lesson on multiline statements with Jinja.

---

### 1. Beyond Single Expressions

`{{ }}` handles one expression. For loops and conditionals you need a different markup:

| Markup | Use |
|--------|-----|
| `{{ … }}` | print a value |
| `{% … %}` | run a **statement** (for, if, set…) — prints nothing itself |

Every block must be closed: `{% for %}` … `{% endfor %}`, `{% if %}` … `{% endif %}`.

---

### 2. Get Some Data (an API of Your Own)

npoint.io (or similar) gives you free JSON storage — create a bin, put a list of blog
posts in it, and fetch it like any API:

```json
[
  {"id": 1, "title": "The Life of Cactus", "subtitle": "Very interesting", "body": "…"},
  {"id": 2, "title": "Top 15 Things to Do When You're Bored", "subtitle": "…", "body": "…"},
  {"id": 3, "title": "Introduction to Intermittent Fasting", "subtitle": "…", "body": "…"}
]
```

```python
import requests
from flask import Flask, render_template

app = Flask(__name__)

BLOG_URL = "https://api.npoint.io/YOUR_BIN_ID"


@app.route("/blog")
def get_blog():
    response = requests.get(BLOG_URL)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)
```

---

### 3. Loop in the Template

```html
<h1>My Blog</h1>
{% for post in posts %}
    <h2>{{ post.title }}</h2>
    <h3>{{ post.subtitle }}</h3>
{% endfor %}
```

* `{% for post in posts %}` … `{% endfor %}` — one line of markup per Python line, opened
  and closed.
* Inside the loop, `{{ post.title }}` works exactly like Python dictionary access.
* Result: one `<h2>`/`<h3>` pair per post, with no per-post HTML file.

---

### 4. Conditionals Inside Loops

```html
{% for post in posts %}
    {% if post.id == 2 %}
        <h2>{{ post.title }}</h2>
        <h3>{{ post.subtitle }}</h3>
    {% endif %}
{% endfor %}
```

Only post #2 renders. (`{% else %}` works too, as you'd expect.)

---

### 5. Handy Extras

```html
{{ post.body|truncate(60) }}     <!-- filter, like a function call -->
{{ loop.index }}                  <!-- 1-based counter inside a for loop -->
{{ post.title|upper }}            <!-- '|' applies a filter -->
```

Jinja has no `import`, so anything complex (requests, datetime, calculations) belongs in
`server.py`, with only the finished values passed to the template.

---

### Summary Checklist

1. `{% %}` = statements; every one needs a closing tag (`endfor`, `endif`).
2. `{% for post in posts %}` loops over data passed from the server.
3. `{% if post.id == 2 %}` filters what renders.
4. Readable templates do the *presentation*; Python does the *computation*.
