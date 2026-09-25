Here is a structured breakdown of this lesson on scraping internet speeds.

---

### 1. Drive Speedtest

```python
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

SPEEDTEST_URL = "https://www.speedtest.net/"


def get_internet_speed(self):
    self.driver.get(SPEEDTEST_URL)

    # dismiss the cookie/consent wall if it shows up
    try:
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        ).click()
    except TimeoutException:
        pass

    # 1. press GO
    self.driver.find_element(By.CLASS_NAME, "start-text").click()

    # 2. wait for the result — this can take up to ~2 minutes
    WebDriverWait(self.driver, 180).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.result-container-speed"))
    )

    # 3. scrape the numbers
    self.down = float(self.driver.find_element(
        By.CSS_SELECTOR, "span.download-speed").text)
    self.up = float(self.driver.find_element(
        By.CSS_SELECTOR, "span.upload-speed").text)
```

> **Note:** Speedtest needs **Flash-free, JavaScript-heavy** rendering and takes time — this
> is exactly the "Selenium, not requests" case from Day 48.

---

### 2. Waits Are the Whole Game

| Wait | Why |
|------|-----|
| 5 s for the consent banner | optional element — swallow the timeout |
| Click `start-text` | begins the test |
| Up to 180 s for the result container | slow connections and busy servers |
| Then read `.text` | values appear only after the test completes |

Never use a fixed `time.sleep(60)` as your only strategy — wait for the *element*, not a
stopwatch (and 60 s may not even be enough).

---

### 3. Read the Result ID Too

Speedtest shows a **result ID** and a shareable URL. Grabbing it lets your tweet link to
the evidence:

```python
result_id = self.driver.find_element(By.CSS_SELECTOR, "div.share-result-container a").text
```

---

### 4. Store, Don't Print

Assign to `self.down` / `self.up` so `tweet_at_provider()` can use them, and print a
one-line summary for the log.

---

### Summary Checklist

1. `driver.get(speedtest.net)` → accept cookies → click `start-text`.
2. Wait for the result element (up to ~3 minutes), then scrape `.download-speed` and
   `.upload-speed`.
3. Convert text to `float` immediately; store on `self`.
4. Also capture the result ID/URL as evidence for the tweet.
5. Element waits beat fixed sleeps.
