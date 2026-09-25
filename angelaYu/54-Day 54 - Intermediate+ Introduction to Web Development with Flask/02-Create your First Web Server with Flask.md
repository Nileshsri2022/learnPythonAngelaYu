# Create your First Web Server with Flask

---

### 1. The Minimal Flask App

Straight from the Flask quickstart:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
```

* `Flask(__name__)` creates the app (the `__name__` argument tells Flask where the app
  lives — see the next note).
* The `@app.route("/")` decorator binds the **home route** (`/`) to the function below it.
* Whatever the function returns is what the browser receives.

---

### 2. Naming Your File

Name it `hello.py`, `main.py`, `server.py` — **never** the same name as a package you
import. A file called `requests.py` shadows the real `requests` package and produces the
baffling error:

```text
AttributeError: module 'requests' has no attribute 'get'
```

---

### 3. Install Flask — Three Ways

| Way | How |
|-----|-----|
| PyCharm light-bulb | hover the import → *Install package* |
| PyCharm settings | Preferences → Project → Python Interpreter → `+` → Flask |
| Terminal (**pip**) | `pip install Flask` |

`pip` installs anything from `pypi.org` by name — capitalisation is conventional:
`pip install Flask`.

---

### 4. Run the Server

```bash
# macOS / Linux
export FLASK_APP=hello.py
flask run

# Windows (cmd)
set FLASK_APP=hello.py
flask run
```

* `FLASK_APP` tells Flask which file holds the application.
* The output shows `Running on http://127.0.0.1:5000` — **127.0.0.1** is localhost (your
  own machine), **5000** is the default Flask port.
* A warning reminds you this is a *development* server — perfect for now, not for
  production.

> **Tip:** Click the link in PyCharm's terminal to open the site. Press `Ctrl + C` in the
> terminal to stop the server — if you don't, a second `flask run` on the same port fails.

---

### 5. What Flask Does With `return "Hello, World!"`

View-source in the browser shows full markup — Flask wrapped your string:

```html
<html><head></head><body>Hello, World!</body></html>
```

You only described *content*; the framework supplied the rest. That division of labour is
the whole point of a framework.

---

### Summary Checklist

1. `from flask import Flask` → `app = Flask(__name__)` → `@app.route("/")`.
2. Don't name your file after a library you import.
3. Install with pip, the light-bulb, or the interpreter settings.
4. `export/set FLASK_APP=hello.py` then `flask run`; visit `127.0.0.1:5000`.
5. `Ctrl + C` stops the dev server; Flask auto-wraps your return value in HTML.
