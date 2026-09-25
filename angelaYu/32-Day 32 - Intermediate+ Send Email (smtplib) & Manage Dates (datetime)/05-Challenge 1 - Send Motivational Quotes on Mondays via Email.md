Here is a structured breakdown of Challenge 1 — Monday motivational emails.

---

### 1. The Task

Every Monday, email yourself a random quote from `quotes.txt`.

---

### 2. The Solution

```python
import datetime as dt
import smtplib
import random

now = dt.datetime.now()
weekday = now.weekday()          # 0 = Monday

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
```

* `readlines()` + `random.choice` — the quote picker.
* `weekday() == 0` gates the whole job to Mondays.

---

### Summary Checklist

1. Date check → file read → random pick → SMTP send.
2. Run daily (cron/GitHub Actions); it self-selects Mondays.
