Here is a structured breakdown of this lesson on finding elements with Selenium.

---

### 1. The Locator Strategy

```python
from selenium.webdriver.common.by import By

price = chrome_driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)                       # visible text of the element

form = chrome_driver.find_element(By.ID, "articleCount")
link = form.find_element(By.TAG_NAME, "a")   # search inside an element
```

| By.… | matches |
|------|---------|
| `ID` | id attribute |
| `CLASS_NAME` | class |
| `TAG_NAME` | tag |
| `CSS_SELECTOR` | any CSS selector |
| `XPATH` | XML path expressions |

* `find_element` → first match; `find_elements` → list of all.
* `.text` gives the rendered text (unlike BeautifulSoup, you're seeing what a user sees).

---

### 2. Selenium vs BeautifulSoup

Selenium can *scrape*, but its real power is **interacting** — and it sees the page
*after* JavaScript runs. For pure scraping of static HTML, Day 45's stack is lighter.

---

### Summary Checklist

1. `find_element(By.…, value)` — first match; `By` covers id/class/tag/CSS/XPath.
2. Elements can be searched within elements.
