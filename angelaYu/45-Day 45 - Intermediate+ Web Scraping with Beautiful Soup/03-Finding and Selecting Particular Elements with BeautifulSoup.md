# Finding and Selecting Particular Elements with BeautifulSoup

---

### 1. find_all — the Workhorse

```python
all_anchor_tags = soup.find_all(name="a")     # every <a>, as a list
```

`soup.a` only gives the first; `find_all` gives **all** matches.

---

### 2. Getting Text and Attributes

```python
for tag in all_anchor_tags:
    print(tag.getText())     # the visible text
    print(tag.get("href"))   # any attribute's value
```

* `getText()` — text inside the tag.
* `tag.get("href")` — dictionary-style lookup of an attribute (safer than `tag["href"]`,
  returns `None` instead of erroring).

---

### 3. Searching by Class, ID, or CSS Selector

```python
soup.find_all(name="p", class_="heading")     # <p class="heading">
soup.find(id="specific-id")
soup.find_all(href="https://example.com")     # by any attribute

soup.select("p a")          # CSS selector: <a> inside <p>
soup.select_one(".heading") # first match of a CSS selector
```

> **Note:** `class_` with a trailing underscore — `class` is a reserved Python keyword.

---

### Summary Checklist

1. `find_all` returns a list; `find`/`select_one` return one.
2. `.getText()` for text, `.get("attr")` for attributes, `.select()` for CSS selectors.
