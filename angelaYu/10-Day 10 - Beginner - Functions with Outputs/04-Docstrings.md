# Docstrings

---

### 1. What is a Docstring?

A **docstring** is documentation written *inside* your function — a multi-line string on
the very first line of the body. It's what makes your functions show helpful pop-ups in
PyCharm, just like `len()` and other built-ins do:

```python
def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    return f"{f_name.title()} {l_name.title()}"
```

* Triple quotes `""" ... """` — can span multiple lines.
* Must be the **first statement** in the function body.

---

### 2. Why Bother?

* **Hover documentation** — editors show it when you (or teammates) call the function.
* **Forces clarity** — writing the description often reveals design problems.
* **Professional habit** — every serious codebase documents its functions this way.

> **Tip:** Hover over your own function name at the call site — if the pop-up shows your
> docstring, you've done it right.

---

### Summary Checklist

1. Docstring = `"""description"""` as the first line of a function.
2. It powers editor tooltips, just like built-in functions' docs.
3. Document every non-obvious function: what it takes, what it returns.
