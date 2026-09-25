# How to Send Emails with Python using SMTP

---

### 1. How Email Travels

Your email client → your provider's **SMTP server** (Simple Mail Transfer Protocol) →
the recipient's provider → their inbox. Python speaks SMTP directly:

```python
import smtplib

my_email = "test@gmail.com"
password = "app_password_123"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()               # encrypt the connection
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="recipient@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
```

* Provider SMTP hosts: `smtp.gmail.com` (587), `smtp.yahoo.com`, `smtp.mail.yahoo.com`…
* `starttls()` — upgrade to TLS encryption.
* Message format: **`Subject:...\n\n`** then the body.

---

### 2. Gmail App Passwords

Google blocks plain password logins from "less secure apps". Create an **App Password**
(Google Account → Security → 2-Step Verification → App passwords) and use it as the
`password`.

---

### Summary Checklist

1. `SMTP(host)` → `starttls()` → `login()` → `sendmail()`.
2. `Subject:` line, blank line, then body.
3. Use app passwords, never your real account password.
