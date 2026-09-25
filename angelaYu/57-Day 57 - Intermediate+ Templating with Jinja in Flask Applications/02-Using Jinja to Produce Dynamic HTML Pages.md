Here is a structured breakdown of this lesson on producing dynamic HTML pages with Jinja.

---

### 1. From a String to a Template

Start with the usual Flask app, then create `templates/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Website</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
```

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
```

The HTML file is now a **template** — a page with slots that code can fill.

---

### 2. `{{ … }}` — Evaluate and Insert

Plain text between the tags is literal:

```html
<h1>5 * 6</h1>          <!-- renders "5 * 6" -->
<h1>{{ 5 * 6 }}</h1>    <!-- renders "30" -->
```

Double curly braces tell Jinja: *evaluate this as a Python expression and put the result
here.*

---

### 3. Passing Data from the Server

Anything requiring an `import` (like `random`) should be computed in Python, then handed
to the template:

```python
import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number)
```

Everything after the template name is a **keyword argument** — Flask collects them into
the template context (the `**context` in the signature), so each one needs a **name** and a
**value**:

```html
<h3>Your lucky number is {{ num }}</h3>
```

Refresh and the number changes — the template is re-rendered on every request.

---

### 4. Challenge: A Footer That Ages Well

Outdated copyright footers are everywhere ("© 2019"). Fix yours forever:

```python
import datetime

@app.route("/")
def home():
    current_year = datetime.datetime.now().year      # or datetime.date.today().year
    return render_template("index.html", num=random_number, year=current_year)
```

```html
<footer>
    <p>Copyright {{ year }}. Built by Your Name.</p>
</footer>
```

The year is now computed at request time — it will never be stale again.

---

### 5. Nesting Templates in Folders

```python
return render_template("blog/post.html", post=post)   # templates/blog/post.html
```

---

### Summary Checklist

1. HTML in `templates/` is a template you can fill with code.
2. `{{ expression }}` evaluates and inserts.
3. Compute imports/values in Python and pass them as keyword arguments.
4. Use them in the template by the **argument name**.
5. `datetime.now().year` gives you a self-updating copyright footer.
