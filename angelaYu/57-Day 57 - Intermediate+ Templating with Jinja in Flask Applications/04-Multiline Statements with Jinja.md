Here is a structured breakdown of this lesson on multiline Jinja statements.

---

### 1. Loops and Conditionals

```html
{% for post in posts %}
    <h2>{{ post["title"] }}</h2>
    <p>{{ post["subtitle"] }}</p>
{% endfor %}

{% if posts %}
    <p>{{ posts|length }} posts found.</p>
{% endif %}
```

Every `{% if %}` / `{% for %}` needs its `{% endif %}` / `{% endfor %}` — the HTML in
between renders once per iteration.

---

### 2. Feeding the Loop

```python
BLOGS_URL = "https://api.npoint.io/…"      # npoint.io = free JSON hosting
response = requests.get(BLOGS_URL)
all_posts = response.json()

@app.route("/blog")
def blog():
    return render_template("blog.html", posts=all_posts)
```

* npoint.io hosts a JSON list you can edit in a browser — stand-in for a database
  until Day 67.
* Jinja even takes Python filters: `|length`, `|title`, `|upper`.

---

### Summary Checklist

1. `{% for %}…{% endfor %}` renders lists into HTML.
2. Data from anywhere (API, list, DB) → template variable.
