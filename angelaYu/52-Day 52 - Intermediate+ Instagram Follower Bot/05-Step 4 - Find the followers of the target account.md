Here is a structured breakdown of this lesson on collecting the followers.

---

### 1. Open the Followers Modal

```python
self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")

followers_link = self.driver.find_element(
    By.PARTIAL_LINK_TEXT, "followers")
followers_link.click()
```

The followers modal shows ~12 accounts; the rest load **as you scroll**.

---

### 2. Scroll the Modal Until All Are Loaded

```python
modal = self.driver.find_element(By.CLASS_NAME, "isgrP")   # scrollable div

while True:
    self.driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    time.sleep(2)
    followers = self.driver.find_elements(By.CLASS_NAME, "FPmhX")
    if len(followers) >= TARGET_COUNT:
        break

usernames = [f.get_attribute("title") for f in followers]
```

* `execute_script` runs JavaScript in the page — the only way to scroll a div that
  isn't the window.
* Loop: scroll → recount → stop when the count stops growing.

---

### Summary Checklist

1. Modal lists load lazily — scroll to fetch.
2. `execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", el)`.
