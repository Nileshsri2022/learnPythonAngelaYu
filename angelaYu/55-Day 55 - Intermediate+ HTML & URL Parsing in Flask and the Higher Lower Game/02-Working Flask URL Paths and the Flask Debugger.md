# Working Flask URL Paths and the Flask Debugger

---

### 1. Routes So Far

```python
@app.route("/")
def home():
    return "Hello, world!"

@app.route("/bye")
def say_bye():
    return "Bye!"
```

Different path → different function. The decorator is what *binds* the URL to the
function (and it lives on the `app` object — an instance of the `Flask` class).

---

### 2. Variable Rules: Capturing Parts of the URL

Angle brackets turn part of the path into a **variable** passed to your function:

```python
@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"

@app.route("/username/<name>/1")
def greet_two(name):
    return f"Hello {name}, you're visitor number 1!"
```

* Visit `/username/Angela` → `Hello Angela!`
* Any extra path segments after the variable are ignored by the route matcher.
* URL variables arrive as **strings** by default.

---

### 3. Converters: Typed URL Variables

```python
@app.route("/username/<path:name>")        # keeps slashes: "Angela/1/2"
@app.route("/post/<int:post_id>")          # integer
@app.route("/price/<float:amount>")        # float
@app.route("/files/<path:filepath>")       # path, slashes included
@app.route("/colour/<any(red, green, blue):shade>")   # enumerated values
```

Without a converter, `/post/abc` matches and you'd have to convert by hand; with
`int:`, Flask returns a 404 for non-numeric paths before your code runs.

---

### 4. Debug Mode

```python
if __name__ == "__main__":
    app.run(debug=True)
```

| Debug feature | Benefit |
|---------------|---------|
| Auto-reloader | save the file → server restarts itself (no more stop/start) |
| Interactive debugger | error pages show the traceback *and* a live Python console |
| Debug mode on the app | extra development-time checks |

> **Note:** If your route changes and the browser shows *404 Not Found*, the server is
> still running the old code — that's exactly what the auto-reloader fixes.

---

### 5. Using the Interactive Debugger

Deliberate error:

```python
@app.route("/username/<name>")
def greet(name):
    return f"Hello {name + 12}"      # TypeError: can only concatenate str
```

The error page shows the traceback and a **console** (protected by a PIN printed in your
terminal — it stops strangers on the internet from executing code in your app). In that
console you can inspect variables:

```text
>>> name
'Angela'
```

and experiment until you find the fix (`str(12)` here).

> **⚠️ Warning:** The debugger PIN exists for a reason. Never leave `debug=True` on a
> publicly deployed site.

---

### Summary Checklist

1. `@app.route("/path")` binds URLs to functions.
2. `<name>` captures a path segment; `<converter:name>` types it
   (`int`, `float`, `path`, `any(...)`).
3. Extra path segments are ignored unless the converter consumes them.
4. `app.run(debug=True)` gives auto-reload + the interactive debugger.
5. The debugger console is PIN-protected — keep debug mode off in production.
