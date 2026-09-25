Here is a structured breakdown of this lesson on URL building with Flask.

---

### 1. The Problem with Hard-Coded Links

```html
<a href="/blog">Go to blog</a>
```

Works — until you rename the route to `/posts`. Now every template holding that string is
broken, and you have to grep the whole project.

---

### 2. `url_for()` — Let Flask Build the URL

```html
<a href="{{ url_for('get_blog') }}">Go to blog</a>
```

* `url_for` is available in **every** Jinja template.
* It takes the **name of the view function** (not the route string) as its first argument.
* Flask looks the function up and generates the correct URL for it.

> **Tip:** Rename the route and nothing breaks — `url_for` follows the function, not the
> path.

---

### 3. Passing Arguments

If the route has a variable part, pass it as a keyword argument:

```python
@app.route("/blog/<int:number>")
def get_blog(number):
    print(number)
    return render_template("blog.html", posts=all_posts)
```

```html
<a href="{{ url_for('get_blog', number=3) }}">Go to blog #3</a>
```

Clicking it requests `/blog/3`; the value arrives in the function's `number` parameter.
That value can then be printed, used to filter data, or handed to another template.

---

### 4. `url_for` Works for Static Files Too

```html
<link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
<img src="{{ url_for('static', filename='images/avatar.png') }}" alt="avatar">
```

* The `'static'` endpoint is built in.
* `filename=` is relative to the `static/` folder.
* Flask generates `/static/styles.css` — so the link keeps working if the app is ever
  mounted under a sub-path (e.g. `/myapp/static/styles.css`).

---

### 5. Why Bother?

| Hard-coded | `url_for` |
|------------|-----------|
| Breaks when paths change | Follows the view function |
| Must be edited in every template | One source of truth |
| Breaks if deployed under a subfolder | Always generates the right prefix |

---

### Summary Checklist

1. `{{ url_for('function_name') }}` builds links from view functions.
2. Extra keyword arguments become URL variables: `url_for('get_blog', number=3)`.
3. `url_for('static', filename='…')` for CSS/images/JS.
4. Use it everywhere — it's the difference between a template and a fragile one.
