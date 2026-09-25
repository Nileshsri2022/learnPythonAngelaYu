Here is a structured breakdown of this lesson on the capstone requirements.

---

### 1. Part 1 — Scrape with requests + Beautiful Soup

Fetch the Zillow clone and pull **price**, **address** and **listing link** out of every
property card.

```python
import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
```

Inspect one card to learn the selectors — they carry useful class hooks:

```html
<a class="property-card-link" href="https://www.zillow.com/homedetails/…">
<div class="PropertyCardWrapper__StyledPriceLine">$2,895/mo</div>
<address class="StyledPropertyCardDataArea-c11n-8-84-3__sc-10e22w8-0">2650 Steiner St…</address>
```

```python
links = [a.get("href") for a in soup.select("a.property-card-link")]
prices = [p.getText() for p in soup.select(".PropertyCardWrapper__StyledPriceLine")]
addresses = [a.getText().strip() for a in soup.select("address")]
```

---

### 2. Clean the Data Before You Type It

Raw scraped strings are messy — clean them once, in Python, not in your head:

```python
def clean_price(raw: str) -> str:
    """'$2,895/mo' or '$2,895+ 1bd' -> '2895'"""
    return raw.split("/")[0].replace("$", "").replace(",", "").strip()
```

* `.split("/")[0]` drops `/mo` and any bonus text.
* Stripping `$` and `,` leaves a number Google Sheets treats as numeric.

> **Tip:** Zip the parallel lists into one list of records (Day 9):
> `list(zip(addresses, prices, links))` — otherwise your addresses and prices will drift
> out of sync once a card is missing an element.

---

### 3. Part 2 — Submit with Selenium

Create a **Google Form** with three short-answer questions: *Address*, *Price*,
*Link*. Then:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSf…/viewform"

driver = webdriver.Chrome()
driver.get(FORM_URL)

inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")

for address, price, link in listings:
    driver.get(FORM_URL)                      # fresh copy of the form each time
    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    inputs[0].send_keys(address)
    inputs[1].send_keys(price)
    inputs[2].send_keys(link)
    driver.find_element(By.XPATH, "//span[text()='Submit']").click()
```

* Google Forms `input` elements have no useful names — index order *is* the mapping
  (Address, Price, Link), so keep the question order fixed.
* Re-fetch the inputs after `driver.get()` — the old references go stale.

---

### 4. Deliver a Spreadsheet

Google Forms → **Responses** tab → *Link to Sheets* creates a live spreadsheet of every
submission. That spreadsheet *is* the deliverable for the client.

---

### 5. Definition of Done

* [ ] Every listing on page 1 extracted (count them!).
* [ ] Data cleaned: numeric prices, plain addresses, absolute links.
* [ ] One form submission per listing, no duplicates.
* [ ] Responses sheet shows the same count as the scrape.

---

### Summary Checklist

1. requests + BS4 for the scraping half; Selenium for the form half.
2. `.select()` with class hooks; clean `$`, `,` and `/mo` off prices.
3. Zip the three lists into records so fields can't drift apart.
4. Re-`get()` and re-find the inputs for each submission.
5. Verify counts match between scrape and Responses sheet.
