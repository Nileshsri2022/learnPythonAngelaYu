# __name__ and __main__ - Special Attributes built into Python

---

### 1. `Flask(__name__)` — What Is That Argument?

`Flask` needs exactly one required input: the **import name**.

```python
app = Flask(__name__)
```

Print it and you get:

```python
print(__name__)      # __main__
```

`__name__` is a special built-in attribute that holds the name of the current module.

---

### 2. The Rule

| How the file is being used | `__name__` equals |
|---------------------------|-------------------|
| Run directly (script, `Run` button, interactive prompt) | `"__main__"` |
| Imported by another module | the module's name, e.g. `"random"` |

```python
import random
print(random.__name__)   # 'random'  (imported)
print(__name__)          # '__main__' (this file is being run)
```

---

### 3. The `if __name__ == "__main__":` Guard

```python
if __name__ == "__main__":
    app.run()
```

* "Only start the server if this file is being **run directly**."
* If `hello.py` is imported by another module, the guard is skipped — the server doesn't
  start as a side effect of importing (important for tests and for larger apps).

---

### 4. `flask run` vs `app.run()`

| | `flask run` | `app.run()` |
|---|-------------|-------------|
| Needs `FLASK_APP` env var | ✅ | ❌ |
| Start | terminal command | PyCharm's Run button |
| Stop | `Ctrl + C` | the usual Stop button |

`app.run()` does exactly the same job as `flask run`, but it lets you use the IDE's normal
run/stop controls.

---

### 5. Why Flask Needs It

Flask uses the import name to locate templates, static files and the module itself. Passing
`__name__` says "the app lives here, in the currently running file" — as opposed to a file
that has merely been imported.

---

### Summary Checklist

1. `__name__` is `"__main__"` when the file is run directly, otherwise the module name.
2. `Flask(__name__)` = "here is where this app lives".
3. `if __name__ == "__main__": app.run()` starts the server only for direct runs.
4. `app.run()` ≈ `flask run`, minus the environment variable, plus PyCharm's run/stop
   buttons.
