# Solution & Walkthrough for the Automated Birthday Wisher

---

### 1. The Solution

```python
import datetime as dt
import pandas
import random
import smtplib

my_email = "your@gmail.com"
password = "app_password"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row
                  for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
```

---

### 2. The Techniques

* **Dictionary comprehension over `iterrows()`** (Day 26): `(month, day)` tuples as keys —
  the birthday lookup becomes one `in` check.
* **Mail merge** (Day 24): `replace("[NAME]", ...)`.
* **SMTP** (this morning): subject + body.
* The script is idempotent and runs daily; scheduling comes next.

---

### Summary Checklist

1. `(month, day)` tuple keys make the date match trivial.
2. Template → replace → send = the whole project.
3. Runnable version: [`main.py`](main.py) (+ templates + sample CSV)
