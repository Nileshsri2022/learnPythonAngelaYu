Here is a structured breakdown of this challenge lesson on scraping on your own.

---

### 1. The Challenge

Blank project, new website, new piece of data — the full workflow without hand-holding:

1. Open the site in Chrome, decide what you want.
2. Right-click → Inspect → find the element's id/class.
3. `driver.get(URL)` → `find_element(By.…, …)` → `.text`.
4. Run, iterate on the selector until the right data prints.

---

### 2. Why This Drill Matters

Selector-hunting in DevTools is **the** core Selenium skill — every bot on the next
days is 10% Python and 90% finding the right element.

---

### Summary Checklist

1. Inspect → locate → select → extract.
2. Practice on any site you like.
