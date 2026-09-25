Here is a structured breakdown of this lesson on building the complaint bot.

---

### 1. Log In to X

```python
def tweet_at_provider(self):
    self.driver.get("https://x.com/login")

    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "text"))
    ).send_keys(X_EMAIL)
    self.driver.find_element(By.XPATH, "//span[text()='Next']").click()

    # X asks for a username only on some flows
    click_if_present(self.driver, By.NAME, "text")

    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    ).send_keys(X_PASSWORD)
    self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='LoginForm_Login_Button']").click()
```

* X's DOM leans on `data-testid` attributes — far more stable than class names.
* Expect a possible "unusual activity" challenge; solve it once by hand and persist the
  profile.

---

### 2. Compose the Tweet

```python
message = (
    f"Hey {X_HANDLE}, why is my internet speed {self.down}down/{self.up}up "
    f"when I pay for {self.promised_down}down/{self.promised_up}up?"
)

tweet_box = WebDriverWait(self.driver, 15).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']"))
)
tweet_box.click()
tweet_box.send_keys(message)              # or use ActionChains for emoji/line breaks
```

For multi-line tweets or emoji, Selenium's `sendKeys` can be flaky — `ActionChains`
handles them:

```python
from selenium.webdriver.common.action_chains import ActionChains
ActionChains(self.driver).send_keys(message).perform()
```

---

### 3. Post It

```python
self.driver.find_element(
    By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']").click()
```

---

### 4. Decide Before You Post

```python
if self.down < self.promised_down or self.up < self.promised_up:
    bot.tweet_at_provider()
else:
    print("Speeds are fine today — no complaint needed.")
```

Posting daily regardless is spam; posting only when the numbers are genuinely bad keeps
the account healthy and the message credible.

> **⚠️ Warning:** Automation on X may breach its terms and trigger rate limits or locks.
> Practise on the course clone; if you automate a real account, post rarely and keep the
> content factual.

---

### Summary Checklist

1. Two-step X login (email → Next → password → Log in); `data-testid` selectors are your
   friends.
2. Compose with an f-string comparing actual vs promised speeds; `ActionChains` for
   special characters.
3. Click the Post button with `data-testid='tweetButtonInline'`.
4. Only tweet when the measurement is actually below contract — and expect a captcha once.
