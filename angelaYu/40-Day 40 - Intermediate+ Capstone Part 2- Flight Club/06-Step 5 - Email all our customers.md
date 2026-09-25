Here is a structured breakdown of Step 5 — emailing all customers.

---

### 1. The Email Sender

```python
import smtplib
import os

class NotificationManager:
    def send_emails(self, emails, message_body, cheapest_flight):
        for email in emails:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(os.environ.get("MY_EMAIL"),
                                 os.environ.get("MY_PASSWORD"))
                connection.sendmail(
                    from_addr=os.environ.get("MY_EMAIL"),
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n"
                        f"{message_body}\n{cheapest_flight}"
                )
```

* Day 32's SMTP pattern, looped over the customer list.
* Message = generic deal line + flight details.

---

### 2. Capstone Complete

Form → sheet → search → compare → SMS/email → community. Every concept from Days 1–39
is in this program — that's what makes it a capstone.

---

### Summary Checklist

1. smtplib inside a `for email in emails:` loop.
2. Runnable version: [`main.py`](main.py)
