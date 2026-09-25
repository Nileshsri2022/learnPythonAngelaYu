Here is a structured breakdown of this lesson on the first Flask server.

---

### 1. The Smallest Possible Server

```bash
pip install Flask
```

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

Run it, then open `http://127.0.0.1:5000/` — "Hello, World!", served by your Python.

---

### 2. The Three Moving Parts

| Piece | Job |
|---|---|
| `Flask(__name__)` | create the app object |
| `@app.route("/")` | "when a GET arrives at `/`, call the function below" |
| `app.run(debug=True)` | start listening (port 5000); debug = auto-reload |

The function's **return value is the response body**.

---

### Summary Checklist

1. Route decorator binds a URL path to a function.
2. `debug=True` restarts the server on every save.
