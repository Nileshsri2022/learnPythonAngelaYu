Here is a structured breakdown of this lesson on URL paths and the debugger.

---

### 1. Path Variables

```python
@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"

@app.route("/username/<path:username>")
def profile(username):
    return f"Profile of {username}"
```

* `<name>` captures the URL segment and passes it to the function as a parameter.
* Converters: `<int:id>`, `<path:rest>` (slashes allowed), `<string:...>`.
* Now `mysite.com/angela` greets Angela — routing *with* data.

---

### 2. The Flask Debugger

```python
app.run(debug=True)
```

A crash no longer kills the server: the browser shows a full **traceback** with the
offending line, and variables at each frame. The server also **auto-reloads** on save.

---

### Summary Checklist

1. `/<param>` reads the URL into a function argument.
2. `debug=True` = live tracebacks + auto-reload.
