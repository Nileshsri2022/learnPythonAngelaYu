Here is a structured breakdown of this lesson on `__name__` and `__main__`.

---

### 1. The Special Attribute

Every module carries a `__name__`:

```python
print(__name__)
```

| How the file runs | `__name__` equals |
|---|---|
| directly (`python3 main.py`) | `"__main__"` |
| imported (`import main`) | `"main"` (the module name) |

---

### 2. The Two Idioms It Powers

```python
app = Flask(__name__)        # tell Flask this module is the app

if __name__ == "__main__":   # only when run directly, not when imported
    app.run(debug=True)
```

* `Flask(__name__)` — Flask needs a module to anchor to; `__name__` works no matter
  what your file is called.
* The `if` guard means `app.run()` fires only for direct runs — an importer gets the
  app object without starting a server.

---

### Summary Checklist

1. `__name__` = how the file was launched.
2. Guard dev/server-only code with `if __name__ == "__main__":`.
