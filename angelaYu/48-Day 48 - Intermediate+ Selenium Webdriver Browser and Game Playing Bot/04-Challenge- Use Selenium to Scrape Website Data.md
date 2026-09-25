Here is a structured breakdown of this challenge lesson on scraping website data.

---

### 1. The Challenge

Reproduce Day 47's Amazon price scrape, but with a live Selenium browser instead of
`requests` + BeautifulSoup:

```python
price_dollars = chrome_driver.find_element(By.CLASS_NAME, "a-price-whole")
price_cents   = chrome_driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(f"Price: {price_dollars.text}{price_cents.text}")
```

* At recording time Amazon split the price across two classes (`a-price-whole` +
  `a-price-fraction`) — combine the texts.
* No headers needed: it *is* a real browser.

---

### Summary Checklist

1. Same DevTools workflow: inspect → find the class → Selenium it.
2. No captcha workarounds required — Selenium looks human.
