Here is a structured breakdown of this lesson on scraping the product price.

---

### 1. Find the Price Element

Amazon wraps the price in a span: `<span class="a-offscreen">₹12,999.00</span>`
(and the whole block carries class `a-price`).

```python
import requests
from bs4 import BeautifulSoup

response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

price_tag = soup.find(name="span", class_="a-offscreen")
price = float(price_tag.getText().split("₹")[1].replace(",", ""))
```

* Scrape → string → strip currency → drop thousands separators → `float`.
* Markup varies by product/region — verify the class in DevTools.

---

### 2. Also Grab the Title

```python
title_tag = soup.find(name="span", id="productTitle")
product_title = title_tag.getText().strip()
```

You'll want it in the alert email so future-you knows what the deal even was.

---

### Summary Checklist

1. `.a-offscreen` holds the price text; clean it into a float.
2. Scrape the title too — emails need context.
