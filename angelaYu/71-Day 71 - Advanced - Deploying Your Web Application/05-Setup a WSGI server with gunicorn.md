Here is a structured breakdown of this lesson on setting up a WSGI server with gunicorn.

---

### 1. Why Not `flask run` in Production?

The Flask development server that's been printing warnings all along is:

* single-threaded and slow (one request at a time),
* not built for hostile internet traffic,
* explicitly labelled *"do not use in production"*.

Production needs a **WSGI server** — an interface between a real web server and your Flask
app. **Gunicorn** is the standard choice on Linux hosts.

---

### 2. Install and Test Locally

```bash
pip install gunicorn
gunicorn main:app
```

* `main:app` = the file `main.py` (`main`) and the Flask instance inside it (`app`).
* Default: binds to `127.0.0.1:8000`, so visit `http://127.0.0.1:8000`.

---

### 3. Tell the Host How to Start It

A **Procfile** (no extension) in the project root:

```text
web: gunicorn main:app
```

| Piece | Meaning |
|-------|---------|
| `web:` | the process type — a web server the platform will route traffic to |
| `gunicorn` | the WSGI server |
| `main:app` | module:Flask-instance |

Some platforms use a start command field or a `render.yaml`/`fly.toml` instead — same idea.

---

### 4. Important: `main:app`, Not `main:main`

If your Flask object is called something else (`application`, `server`), the Procfile must
match:

```python
app = Flask(__name__)      # -> gunicorn main:app
```

---

### 5. Bind to the Right Port and Turn Debug Off

```python
if __name__ == "__main__":
    app.run(debug=False)          # local convenience only
```

In production, **remove `debug=True`** (and preferably the `__main__` block entirely, or
guard it), and make sure the app doesn't hard-code a port — the host sets `$PORT` and tells
gunicorn where to listen:

```text
web: gunicorn main:app --bind 0.0.0.0:$PORT
```

(Several platforms inject the binding automatically; check the provider's docs.)

---

### 6. Workers (Optional)

```bash
gunicorn main:app --workers 4
```

Each worker handles requests independently — a rough starting point is
`(2 × CPU cores) + 1`. More workers = more concurrent users, at the cost of memory.

---

### Summary Checklist

1. `flask run` is for development only; production uses gunicorn.
2. `gunicorn main:app` = module `main.py`, Flask object `app`.
3. A `Procfile` (`web: gunicorn main:app`) tells the host how to launch it.
4. Debug mode off; let the platform supply the port.
5. Add gunicorn to `requirements.txt` or the deploy will fail to start.
