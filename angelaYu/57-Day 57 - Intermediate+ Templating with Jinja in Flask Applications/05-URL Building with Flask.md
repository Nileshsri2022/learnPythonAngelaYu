Here is a structured breakdown of this lesson on URL building.

---

### 1. url_for in Templates

```html
<a href="{{ url_for('get_all_posts') }}">Go to blog</a>
<a href="{{ url_for('show_post', num=3) }}">Post 3</a>
```

`url_for('function_name', …)` builds the URL **from the route function's name** —
rename a path later and every link updates itself.

---

### 2. url_for for Static Files Too

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
```

This was the mystery syntax from Day 56 — now it's official: `url_for` never writes a
URL by hand again.

---

### Summary Checklist

1. Links point at *functions*, not strings.
2. Refactor-proof navigation.
