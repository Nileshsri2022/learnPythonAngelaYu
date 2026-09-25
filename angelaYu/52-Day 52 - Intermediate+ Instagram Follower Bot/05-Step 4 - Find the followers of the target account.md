Here is a structured breakdown of this lesson on finding the target account's followers.

---

### 1. Go to the Target Profile

```python
def find_followers(self):
    self.driver.get(f"{BASE_URL}/{self.similar_account}/")

    # the followers link is an <a href="/account/followers/"> that opens a modal
    followers_link = WebDriverWait(self.driver, 15).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "followers"))
    )
    followers_link.click()

    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']"))
    )
```

* On Instagram the followers list opens in a **modal dialog** (`div[role='dialog']`), not a
  new page — the URL does not change.
* The dialog is a **scrollable container**: scrolling it loads more accounts (infinite
  scroll).

---

### 2. Scroll Inside the Modal

Scrolling the *page* does nothing here — you must scroll the dialog element itself:

```python
dialog = self.driver.find_element(By.CSS_SELECTOR, "div[role='dialog']")

for _ in range(5):                       # each scroll loads another page of people
    self.driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight", dialog
    )
    time.sleep(2)                        # let the next batch render
```

* `execute_script()` runs raw JavaScript in the page — the escape hatch for anything
  Selenium's API doesn't cover.
* `scrollTop = scrollHeight` jumps to the bottom of the container.

---

### 3. Collect the Follow buttons

```python
buttons = dialog.find_elements(By.CSS_SELECTOR, "button")

follow_buttons = [b for b in buttons if b.text == "Follow"]
print(f"{len(follow_buttons)} accounts to follow")
```

Filtering by button **text** keeps you from clicking "Following" (would unfollow!) or
"Requested".

---

### 4. Rate Limits Show Up Here

If you scroll too fast, Instagram shows *"You've followed too many people — try again
later"* inside the modal. Detect it and stop:

```python
if "try again later" in dialog.text.lower():
    print("Rate limited - stopping.")
    return
```

---

### Summary Checklist

1. Navigate to `instagram.com/<account>/` and click the followers link.
2. The list lives in a `role="dialog"` modal — wait for it.
3. Scroll the **modal element** with `execute_script("arguments[0].scrollTop = …")`.
4. Filter to buttons whose text is exactly `"Follow"`.
5. Watch for the rate-limit message.
