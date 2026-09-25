# How to Find and Select Elements on a Website with Selenium

---

### 1. The Same Job as Day 47, in Three Lines

Selenium drives a real browser, so it *is* a real user as far as Amazon is concerned —
no special headers needed.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(AMAZON_PRODUCT_URL)

price_dollars = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")

print(f"The price is {price_dollars.text}.{price_cents.text}")
driver.quit()
```

* `find_element(...)` returns a **WebElement**, not text.
* Add `.text` to read the visible content.
* Class names change — right-click → **Inspect** to confirm today's markup.

---

### 2. Locator Strategies

Import the `By` helper class once:

```python
from selenium.webdriver.common.by import By
```

| Locator | Example | Best for |
|---------|---------|----------|
| `By.ID` | `find_element(By.ID, "submit")` | unique, stable hooks |
| `By.NAME` | `find_element(By.NAME, "q")` | form inputs |
| `By.CLASS_NAME` | `find_element(By.CLASS_NAME, "a-price-whole")` | styled blocks |
| `By.CSS_SELECTOR` | `find_element(By.CSS_SELECTOR, ".documentation-widget a")` | drilling down when nothing is unique |
| `By.XPATH` | `find_element(By.XPATH, '//*[@id="..."]')` | last resort — always works |
| `By.LINK_TEXT` | `find_element(By.LINK_TEXT, "Content portals")` | anchor text |
| `By.PARTIAL_LINK_TEXT` | `find_element(By.PARTIAL_LINK_TEXT, "portals")` | part of anchor text |
| `By.TAG_NAME` | `find_element(By.TAG_NAME, "time")` | generic elements |

> **Note:** `find_element` (singular) returns the **first** match; `find_elements`
> (plural) returns a **list** of every match — e.g.
> `driver.find_elements(By.CSS_SELECTOR, ".event-widget time")`.

---

### 3. Reading Element Properties

```python
search_bar = driver.find_element(By.NAME, "q")

print(search_bar.tag_name)                    # 'input'
print(search_bar.get_attribute("placeholder"))  # 'Search'
print(search_bar.size)                        # {'height': 40, 'width': 46}
print(search_bar.text)                        # visible text
```

* `.tag_name`, `.text`, `.size` are properties.
* `.get_attribute("href")` / `("placeholder")` / `("class")` fetch any HTML attribute.

---

### 4. CSS Selectors & XPath in Practice

For an anchor tag with no id, class or name:

```python
# inside <div class="documentation-widget"> ... <a>Docs</a>
docs_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(docs_link.text)

# Chrome DevTools → right-click element → Copy → Copy XPath
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.get_attribute("href"))
```

> **Tip:** Prefer a CSS selector or `By.ID`/`By.NAME` when possible — XPaths captured from
> DevTools break the moment the page structure changes.

---

### Summary Checklist

1. `from selenium.webdriver.common.by import By` unlocks all locator strategies.
2. `find_element` → one element; `find_elements` → list of elements.
3. Elements return as WebElement objects; use `.text`, `.size`, `.get_attribute()`.
4. CSS selectors drill through nesting when nothing is unique.
5. XPath always works — but copy it from DevTools and treat it as a last resort.
6. Selenium is far shorter than requests + Beautiful Soup for dynamic pages.
