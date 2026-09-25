Here is a structured breakdown of this lesson on the Blog Capstone Project, part 1.

---

### 1. The Project

A simple blog with two page types:

| Page | Route | Content |
|------|-------|---------|
| **Post list** | `/` or `/blog` | every post's title + subtitle + a "Read" link |
| **Post detail** | `/post/<int:index>` | that one post's title, subtitle and full body |

Same layout and styling everywhere; only the data changes — one template each, not one
HTML file per post.

---

### 2. Step 1 — Get the Data

Fetch a JSON list of posts (npoint.io bin, or the course's endpoint):

```python
import requests
from flask import Flask, render_template

app = Flask(__name__)

BLOG_URL = "https://api.npoint.io/YOUR_BIN_ID"
response = requests.get(BLOG_URL)
all_posts = response.json()
```

Each post: `{"id": 1, "title": "…", "subtitle": "…", "body": "…"}`.

> **Note:** In part 2 these posts will live in a database and come with images; for now the
> JSON API is a stand-in.

---

### 3. Step 2 — The List Page

```python
@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=all_posts)
```

```html
{% for post in posts %}
    <h1>{{ post.title }}</h1>
    <h2>{{ post.subtitle }}</h2>
    <a href="{{ url_for('show_post', index=post.id) }}">Read</a>
{% endfor %}
```

* `url_for('show_post', index=post.id)` builds `/post/1`, `/post/2`, … for each card.
* The loop is the whole reason there's only one list template.

---

### 4. Step 3 — The Detail Page

```python
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in all_posts:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)
```

```html
<h1>{{ post.title }}</h1>
<h2>{{ post.subtitle }}</h2>
<p>{{ post.body }}</p>
```

> **Tip:** Return a 404 when the id doesn't exist (`abort(404)`), otherwise a mistyped URL
> renders an empty page with `post = None`.

---

### 5. Step 4 — Navigation

```html
<a href="{{ url_for('get_all_posts') }}">← Back to all posts</a>
```

Reuse `header`/`footer` blocks across templates (part 2 introduces Jinja *template
inheritance* with `{% extends %}` and `{% block %}` to stop repeating the layout).

---

### 6. Definition of Done

* [ ] `/` lists every post's title + subtitle.
* [ ] Each "Read" link goes to `/post/<id>` and shows that post's body.
* [ ] No hard-coded URLs — `url_for` everywhere.
* [ ] Same layout, different content, one template per page type.

---

### Summary Checklist

1. Two routes, two templates, one data source.
2. `{% for post in posts %}` renders the list; `url_for` builds the links.
3. The detail route looks the post up by id and passes just that post.
4. This is Jinja's payoff: content is data, not duplicated markup.
