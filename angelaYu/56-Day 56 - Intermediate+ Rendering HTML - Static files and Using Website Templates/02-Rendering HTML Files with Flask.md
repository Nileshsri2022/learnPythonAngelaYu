Here is a structured breakdown of this lesson on rendering HTML files with Flask.

---

### 1. Start From the Basics

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
```

Same three steps as Day 54: create the app, decorate a route, run it.

---

### 2. Create the HTML File

In PyCharm, *New → HTML File* gives you the boilerplate:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Angela</title>
</head>
<body>
    <h1>I'm Angela</h1>
</body>
</html>
```

---

### 3. The Rules: Templates Live in `templates/`

Flask will only find HTML in a folder named **`templates`** (lowercase), at the project
root:

```
my-personal-site/
├── server.py
└── templates/
    └── index.html
```

---

### 4. Render It

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
```

* Import `render_template` alongside `Flask`.
* Pass the **filename** relative to `templates/` — subfolders work too:
  `render_template("cv/angela.html")`.
* Flask reads the file and returns it as the HTTP response body.

---

### 5. Challenge: Serve Your Own Site

Take an HTML page you built on Days 41–43 (or a downloaded CV page) and render it:

1. Save it into `templates/` and shorten the filename (`angela.html`).
2. If it came from GitHub it may be `.htm` — rename to `.html`.
3. Point the route at it: `return render_template("angela.html")`.

The page renders — except the profile picture, which shows as a broken-image icon. That's
because the image is a **static file**, and Flask hasn't been told where those live yet.

---

### Summary Checklist

1. HTML files must sit in `templates/`.
2. `render_template("name.html")` replaces the giant-string return.
3. Paths inside the call are relative to `templates/`.
4. Broken images/CSS after rendering = static files not served yet (next lesson).
