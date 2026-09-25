Here is a structured breakdown of the Day 57 project — Blog Capstone Part 1: Templating.

---

### 1. The Task

Stand up the **blog capstone**: a multi-page site with a proper template — home
(all posts), about, and contact — a shared header/footer, and nav links built with
`url_for`. Later parts add routing detail (Day 67), users and auth (Day 69).

---

### 2. The Shape of the App

```python
@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
```

```html
<!-- every page shares this header -->
<header>
    <a href="{{ url_for('get_all_posts') }}">My Blog</a>
    <a href="{{ url_for('about') }}">About</a>
    <a href="{{ url_for('contact') }}">Contact</a>
</header>
{% for post in posts %}
    <h2>{{ post["title"] }}</h2>
    <p>{{ post["subtitle"] }}</p>
{% endfor %}
```

* In the course this is built on a downloaded Bootstrap template — same restructure
  drill as Day 56, plus Jinja placeholders.

---

### Summary Checklist

1. Three routes, three templates, one shared header.
2. Project files: [`main.py`](main.py), [`templates/index.html`](templates/index.html), [`templates/about.html`](templates/about.html), [`templates/contact.html`](templates/contact.html)
