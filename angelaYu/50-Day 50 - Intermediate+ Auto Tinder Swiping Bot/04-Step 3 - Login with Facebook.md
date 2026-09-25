Here is a structured breakdown of this lesson on logging in via Facebook.

---

### 1. The Popup Window Problem

"Login with Facebook" opens a **separate popup window**. Selenium must switch to it:

```python
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)     # now typing goes to the popup

driver.find_element(By.ID, "email").send_keys(os.environ.get("FB_EMAIL"))
driver.find_element(By.ID, "pass").send_keys(os.environ.get("FB_PASSWORD"))
driver.find_element(By.NAME, "login").click()

driver.switch_to.window(base_window)   # switch back when the popup closes
```

* `driver.window_handles` is the list of open tabs/windows; index into it after the
  popup appears.
* Facebook credentials — env vars, never literals.

---

### Summary Checklist

1. `switch_to.window(handle)` before typing into a popup.
2. Switch back to `window_handles[0]` afterwards.
