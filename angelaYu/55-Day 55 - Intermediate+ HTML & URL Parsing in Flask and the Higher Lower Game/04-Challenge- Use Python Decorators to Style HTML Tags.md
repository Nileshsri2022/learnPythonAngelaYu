Here is a structured breakdown of this challenge lesson on styling decorators.

---

### 1. The Challenge

Wrap route outputs in `<em>`, `<b>`, `<u>` — using decorators, not string literals:

```python
def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"
```

* Decorators **stack**: the bottom one wraps first; each outer layer adds its tags.
* Note `wrapper()` takes no arguments here — that's exactly the problem `*args`/`**kwargs`
  solve on the next lesson, when wrapped functions need inputs.

---

### Summary Checklist

1. Stacked decorators = nested wrappers, bottom-up.
2. Each decorator adds its markup around the return value.
