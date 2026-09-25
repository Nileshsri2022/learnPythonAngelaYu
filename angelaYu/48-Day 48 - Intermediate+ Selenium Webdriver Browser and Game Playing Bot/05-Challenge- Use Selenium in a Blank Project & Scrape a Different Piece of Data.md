Here is a structured breakdown of this challenge on setting up Selenium in a blank project.

---

### 1. The Challenge

In a brand-new file `interaction.py`, fetch the **Wikipedia main page** and print the
number of articles in English (the "6,900,000+ articles" link).

---

### 2. Inspect Before You Code

```html
<div id="articlecount">
  <a href="/wiki/Special:Statistics">6 902 000+ articles</a>
</div>
```

The anchor tag has no id, class or name — but its parent `<div>` has a unique **id**, and
the anchor is the first `<a>` inside it.

---

### 3. The Solution

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# #articlecount a  -> the first <a> inside the element with id="articlecount"
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

driver.quit()
```

* `#` means *id* in a CSS selector; a space means *descendant of*.
* `find_element` (singular) returns only the **first** matching anchor — the div actually
  contains two, and the second is "About Wikipedia".

---

### 4. Setup Reminder

The blank project needs Selenium installed (`pip install selenium`) and Chrome present.
The driver is created, the page fetched, the element located, the text printed.

---

### 5. Where This Is Heading

So far we can *read* a page. The next lesson adds the two actions that make automation
useful: **clicking** links/buttons and **typing** into fields.

> **Tip:** Use `find_element` whenever you want a single item, and `find_elements` when you
> want to loop over many — mixing them up is the most common Selenium bug.

---

### Summary Checklist

1. New project + `pip install selenium` (reuse the package once installed).
2. `#id descendant` CSS selector reaches anonymous elements by their container.
3. `.text` extracts the visible value.
4. Next: interacting with the page — click and type.
