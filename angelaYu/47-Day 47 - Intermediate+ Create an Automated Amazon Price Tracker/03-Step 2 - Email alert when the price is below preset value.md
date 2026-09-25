# Step 2 - Email alert when the price is below preset value

---

### 1. Compare and Notify

```python
import smtplib

BUY_PRICE = 10000   # your target, in the product's currency

if price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ.get("MY_EMAIL"),
                         password=os.environ.get("MY_EMAIL_PASSWORD"))
        connection.sendmail(
            from_addr=os.environ.get("MY_EMAIL"),
            to_addrs=os.environ.get("MY_EMAIL"),
            msg=f"Subject:Amazon Price Alert!\n\n{product_title} is now "
                f"{price_tag.getText()}\n{URL}".encode("utf-8"),
        )
```

* Everything here is Day 32's `smtplib` pattern — login via app password from env vars.
* The message body carries the title, the current price and the link: one click from
  alert to checkout.

---

### Summary Checklist

1. `if price < target:` → smtplib alert.
2. Message = title + price + URL.
