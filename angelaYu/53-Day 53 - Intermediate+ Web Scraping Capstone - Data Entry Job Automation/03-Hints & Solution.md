# Hints & Solution

---

### 1. Hint 1 — Scrape First, Automate Second

Do the two halves as separate scripts before combining them:

```python
# step one: verify the scrape in isolation
for address, price, link in zip(addresses, prices, links):
    print(f"{price:>8} | {address[:40]:<40} | {link[:50]}")
```

If the printed data is clean, only then move on to typing it into a form.

---

### 2. Hint 2 — Match Parallel Lists by Index

The three scraped lists must stay aligned. `zip()` pairs them positionally:

```python
listings = list(zip(addresses, prices, links))   # [(addr, price, link), ...]
```

If a listing card lacks a price, the lists lengths differ and every subsequent record
shifts. A quick guard:

```python
assert len(addresses) == len(prices) == len(links), "lists out of sync!"
```

---

### 3. Hint 3 — Forms Need Fresh Elements

Each `driver.get(FORM_URL)` reloads the page; the input elements must be re-queried, and
the Submit button must be re-found too:

```python
for address, price, link in listings:
    driver.get(FORM_URL)

    fields = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    fields[0].send_keys(address)
    fields[1].send_keys(price)
    fields[2].send_keys(link)

    driver.find_element(By.XPATH, "//span[text()='Submit']").click()
    time.sleep(1)              # let the submission land before the next one
```

---

### 4. Hint 4 — Wait for the Confirmation

Instead of `sleep(1)`, wait for the thank-you text — it guarantees the submission was
accepted:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Your response has been recorded')]"))
)
```

---

### 5. The Complete Solution

```python
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform"

# ---- 1. scrape ----------------------------------------------------------
soup = BeautifulSoup(requests.get(ZILLOW_URL).text, "html.parser")

links = [a["href"] for a in soup.select("a.property-card-link")]
prices = [clean_price(p.getText()) for p in soup.select(".PropertyCardWrapper__StyledPriceLine")]
addresses = [a.getText().strip() for a in soup.select("address")]

listings = list(zip(addresses, prices, links))
print(f"Found {len(listings)} listings")

# ---- 2. submit ----------------------------------------------------------
driver = webdriver.Chrome()

for address, price, link in listings:
    driver.get(FORM_URL)

    fields = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    fields[0].send_keys(address)
    fields[1].send_keys(price)
    fields[2].send_keys(link)

    driver.find_element(By.XPATH, "//span[text()='Submit']").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Your response has been recorded')]")
        )
    )

driver.quit()
print("All listings submitted.")
```

---

### 6. Extending the Project

* Multi-page scraping: loop page numbers, appending to `listings`.
* Put the form ID and URLs in constants at the top.
* Log each submission so you can resume if the run dies half-way (count the ones you've
  done and skip them next time).

---

### Summary Checklist

1. Build and verify the scrape before adding Selenium.
2. `zip()` the lists and assert equal lengths.
3. Re-fetch inputs on every form load; wait for the "response has been recorded" text.
4. Log each submission — resumability is the difference between a script and a tool.
