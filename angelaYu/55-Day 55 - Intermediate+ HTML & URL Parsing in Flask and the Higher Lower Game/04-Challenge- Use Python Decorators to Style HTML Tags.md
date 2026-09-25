Here is a structured breakdown of this challenge on styling HTML tags with decorators.

---

### 1. The Challenge

Turn this:

```python
@app.route("/bye")
def say_bye():
    return "Bye!"
```

into bold + emphasised + underlined text — **without** writing the tags by hand. Instead,
write three decorators (`make_bold`, `make_emphasis`, `make_underline`) and stack them:

```python
@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye!"
```

---

### 2. Reminder: The Plain Version

Wrapping the string manually would work but is typo-prone:

```python
return "<u><em><b>Bye!</b></em></u>"
```

---

### 3. The Solution

Each decorator wraps the returned text in one pair of tags:

```python
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper
```

Stacked decorators apply **bottom-up**, so `make_underline` runs first, then
`make_emphasis`, then `make_bold`. Result:

```html
<b><em><u>Bye!</u></em></b>
```

---

### 4. Order Matters

```python
@make_bold
@make_emphasis
def f(): ...
```

is the same as `make_bold(make_emphasis(f))`. Swap the order and you swap the nesting —
harmless for `<b>`/`<em>`, essential to remember for decorators that *do* things (logging,
auth checks) rather than just wrapping text.

> **Tip:** The decorator must sit **under** `@app.route(…)` so the route registers the
> fully decorated function. Flask's route decorator ends up outermost, as shown above.

---

### 5. Why Bother?

You now have three reusable pieces of presentation logic. Adding bold to twenty different
routes is one extra line each — the copy-paste version would be twenty chances to make a
typo.

---

### Summary Checklist

1. Write one decorator per tag; each returns the wrapped function's text inside the tags.
2. Stack them under `@app.route(...)`.
3. Decorators apply bottom-up.
4. Order matters for behaviour-changing decorators even when it looks harmless here.
