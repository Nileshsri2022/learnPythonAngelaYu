Here is a structured breakdown of this lesson on measuring internet speeds.

---

### 1. speedtest.net via Selenium

Drive speedtest.net in the browser and read the result tokens after the test runs
(it takes ~30 seconds):

```python
go_button = self.driver.find_element(By.CSS_SELECTOR, ".js-start-test")
go_button.click()

time.sleep(45)   # let the test finish

self.down = float(self.driver.find_element(
    By.CLASS_NAME, "download-value").text)
self.up = float(self.driver.find_element(
    By.CLASS_NAME, "upload-value").text)
```

* `time.sleep` because the test genuinely takes time — no element to wait for yet.
* Alternative: the `speedtest-cli` package does it head-less (`st.download()`,
  `st.upload()`).

---

### Summary Checklist

1. Click start → wait → read download/upload values.
2. Selenium for the page, `speedtest-cli` if you'd rather skip the browser.
