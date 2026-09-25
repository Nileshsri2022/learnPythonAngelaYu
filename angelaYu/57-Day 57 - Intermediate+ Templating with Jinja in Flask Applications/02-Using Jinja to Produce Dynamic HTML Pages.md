Here is a structured breakdown of this lesson on dynamic pages with Jinja.

---

### 1. Passing Data to a Template

```python
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 9)
    return render_template("index.html", num=random_number)
```

```html
<!-- templates/index.html -->
<h1>Hello World, this is number {{ num }}</h1>
{% if num > 5 %}
    <p>Big number!</p>
{% else %}
    <p>Small number!</p>
{% endif %}
```

* `render_template(file, key=value, …)` — every keyword argument becomes a variable
  in the template.
* `{{ }}` = print; `{% %}` = logic. Refresh the page — the number changes: the page
  is now **dynamic**.

---

### Summary Checklist

1. Keyword args in, variables in the template.
2. `{{ }}` displays, `{% %}` controls.
