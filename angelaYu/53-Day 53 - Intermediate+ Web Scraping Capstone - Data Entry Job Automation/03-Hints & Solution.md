Here is a structured breakdown of this lesson on the hints and solution.

---

### 1. Solution Skeleton

```python
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# ---- Step 1: scrape all pages of listings -------------------------------
listings = []
for page in range(1, 3):
    response = requests.get(f"{LISTINGS_URL}{page}/")
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.select(".property-card")
    for card in cards:
        address = card.select_one(".property-address").text.strip()
        price   = card.select_one(".price-reduced").text.split("|")[0].strip()
        link    = card.select_one(".property-card-link")["href"]
        listings.append({"address": address, "price": price, "link": link})

# ---- Step 2: feed the Google Form ----------------------------------------
driver = webdriver.Chrome()
FORM_URL = "https://forms.gle/your-form"

for entry in listings:
    driver.get(FORM_URL)
    driver.find_element(By.CSS_SELECTOR, "input[aria-label='Address']").send_keys(entry["address"])
    driver.find_element(By.CSS_SELECTOR, "input[aria-label='Price']").send_keys(entry["price"])
    driver.find_element(By.CSS_SELECTOR, "input[aria-label='Link']").send_keys(entry["link"])
    driver.find_element(By.XPATH, "//span[text()='Submit']").click()
    driver.find_element(By.XPATH, "//a[text()='Submit another response']").click()
```

* Form inputs accept `aria-label` selectors — more readable than `entry.123` ids.
* Capstone rules apply: selectors go stale; DevTools is your debugger.

---

### Summary Checklist

1. Scrape every page into dicts; then form-fill from the dicts.
2. Runnable version: [`main.py`](main.py)
