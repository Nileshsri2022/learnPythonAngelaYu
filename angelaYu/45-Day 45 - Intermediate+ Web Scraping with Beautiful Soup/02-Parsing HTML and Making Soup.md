# Parsing HTML and Making Soup

---

### 1. Install and Import

```bash
pip install beautifulsoup4
```

```python
from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)        # <title>My Website</title>
print(soup.title.string) # My Website
print(soup.prettify())   # indented, readable HTML
```

* `"html.parser"` — Python's built-in parser (also `lxml` / `html5lib`, faster but
  separate installs).
* `prettify()` pretty-prints the whole tree — your map of the site.

---

### 2. Tags Are Objects

```python
print(soup.a)            # first <a> tag
print(soup.li)           # first <li> tag
print(soup.p)            # first <p> tag
```

Every tag you can name becomes an attribute of `soup` — always returning the **first**
match.

---

### Summary Checklist

1. `BeautifulSoup(html, "html.parser")` turns HTML into a searchable tree.
2. `soup.title` / `soup.p` give the first matching tag.
