Here is a structured breakdown of this lesson on adding Python packages and using PyPI.

---

### 1. PyPI — The Python Package Index

Others' code ships as **packages** on [pypi.org](https://pypi.org) — the app-store of
Python. Install into your project's interpreter straight from PyCharm (Settings →
Project → Python Interpreter → `+`) or the terminal:

```bash
pip install prettytable
```

---

### 2. Using an Installed Package

Import it and use its classes — OOP from someone else's blueprint:

```python
from prettytable import PrettyTable

table = PrettyTable()                 # construct an object
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"                     # modify an attribute

print(table)
```

```
+--------------+----------+
| Pokemon Name |   Type   |
+--------------+----------+
|    Pikachu   | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+
```

---

### Summary Checklist

1. `pip install package` (or PyCharm's package manager) pulls code from PyPI.
2. Installed packages give you new classes to import.
3. Reading a package's docs tells you its classes, methods and attributes.
