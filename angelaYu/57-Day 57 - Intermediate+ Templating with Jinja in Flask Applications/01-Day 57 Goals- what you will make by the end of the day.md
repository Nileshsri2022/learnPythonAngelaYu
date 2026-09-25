Here is a structured breakdown of this lesson on the goals for Day 57.

---

### 1. The Problem: One Layout, Many Pages

A blog with 50 posts shouldn't need 50 HTML files. The **layout, styling and structure**
stay identical; only the title, subtitle and body change.

That's what a **templating language** is for — and Python's is called **Jinja**.

---

### 2. Jinja in One Line

Jinja lets you drop Python into HTML:

```html
<h1>{{ 5 * 6 }}</h1>        <!-- renders 30 -->
<h1>Hello {{ name }}!</h1>  <!-- name comes from the server -->
```

| Markup | Meaning |
|--------|---------|
| `{{ … }}` | evaluate an **expression** and insert it |
| `{% … %}` | **statement** — `if`, `for`, and friends |

---

### 3. Today's Roadmap

1. Render a template and pass variables into it (`render_template("index.html", num=42)`).
2. Dynamic values: random numbers, the current year in a footer.
3. **Challenge:** combine Jinja with APIs (agify.io + genderize.io predict age/gender from a name).
4. Multiline statements in Jinja: `{% for %} … {% endfor %}`, `{% if %} … {% endif %}`.
5. **URL building:** `url_for()` to generate links that never go stale.
6. **Final project:** a simple blog — post list page plus a detail page, one template each.

---

### 4. The Result

By the end of the day, clicking *Read* on any post goes to a page with the same layout and
styling for every post, but different content — computed at request time, not copied into
files.

---

### Summary Checklist

1. Jinja = templating language for Python; `{{ }}` inserts, `{% %}` controls.
2. `render_template("x.html", key=value)` passes data to the template.
3. Today's project: a blog with one layout and dynamic post content.
4. `url_for()` builds URLs from function names instead of hard-coded paths.
