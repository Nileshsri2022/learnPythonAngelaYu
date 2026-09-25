Here is a structured breakdown of this lesson on rendering HTML files.

---

### 1. The Project Structure Flask Expects

```
my_project/
├── main.py
├── templates/
│   └── index.html
└── static/
```

The folder must be named **templates** — Flask finds it by convention.

---

### 2. render_template

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
```

* `render_template("index.html")` reads the file, (later: substitutes variables) and
  returns it as the response.
* The string-returning days are over — HTML lives in HTML files now.

---

### Summary Checklist

1. `templates/index.html` + `render_template()`.
2. Convention over configuration: the folder name is load-bearing.
