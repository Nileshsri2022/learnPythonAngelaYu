Here is a structured breakdown of this challenge on combining Jinja templating with APIs.

---

### 1. The Challenge

Build a `/guess/<name>` route that calls two free, no-auth APIs and renders the prediction:

| URL | Response |
|-----|----------|
| `/guess/Angela` | *Hey Angela, I think you are female, and maybe 63 years old.* |

* `https://api.genderize.io?name=angela` → `{"name":"angela","gender":"female","probability":…}`
* `https://api.agify.io?name=angela` → `{"name":"angela","age":63,"count":…}`

---

### 2. The Route

```python
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get("https://api.genderize.io", params={"name": name})
    age_response = requests.get("https://api.agify.io", params={"name": name})

    gender = gender_response.json()["gender"]
    age = age_response.json()["age"]

    return render_template("guess.html", name=name, gender=gender, age=age)
```

* `params={...}` handles URL encoding for you (`/guess/Mary Jane` → `Mary%20Jane`).
* `.json()` turns the response body into a dictionary; index it like any other dict (Day 9).

---

### 3. The Template

```html
<body>
    <h1>Hey {{ name.title() }},</h1>
    <h2>I think you are {{ gender }},</h2>
    <h3>And maybe {{ age }} years old.</h3>
</body>
```

* `{{ name.title() }}` capitalises the name — you can call Python methods inside the
  braces, just like in Python.
* `name` in the template is the keyword argument from `render_template`, not the raw URL
  segment (rename it `person_name` if the shadowing feels confusing).

---

### 4. Gotchas

| Symptom | Cause | Fix |
|---------|-------|-----|
| `TypeError: 'NoneType' is not subscriptable` | the API doesn't know the name → `"gender": null` | check for `None` and say "no idea" |
| `KeyError: 'age'` | name not in agify's dataset | `.get("age", "unknown")` |
| Slow page | two sequential HTTP calls | fine here; `concurrent.futures` later |

```python
gender = data.get("gender")
if gender is None:
    return render_template("guess.html", name=name, gender="a mystery person", age="?")
```

---

### 5. How to Think When Stuck

This exercise is deliberately open-ended — the workflow (read the API docs, inspect the
JSON, pass values to a template) is the *actual skill*. Pause, break it into pieces, test
each piece in isolation, and only then glue them together.

---

### Summary Checklist

1. `/guess/<name>` calls genderize.io and agify.io, then renders the results.
2. Pass query parameters with `requests.get(url, params={...})`.
3. `{{ }}` can call methods, e.g. `name.title()`.
4. Real APIs return `null` for unknown names — always handle it.
5. Combining APIs + templates is the core pattern behind most web apps.
