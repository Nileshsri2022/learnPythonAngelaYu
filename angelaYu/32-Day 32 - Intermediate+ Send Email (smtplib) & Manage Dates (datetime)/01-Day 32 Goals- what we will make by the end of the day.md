# Day 32 Goals- what we will make by the end of the day

---

### 1. Skills Covered on Day 32

* **SMTP** — sending email programmatically via `smtplib`
* **`datetime`** — working with dates, times and weekday checks
* Combining both into scheduled, automated email jobs

---

### 2. The Project: Automated Birthday Wisher

* `birthdays.csv` holds name, email, year, month, day.
* The script checks every day: is today anyone's birthday?
* If yes → pick a random letter template, replace `[NAME]`, **email it**.
* Scheduled with **GitHub Actions** so it runs daily in the cloud, free.

Plus Challenge 1: Monday-morning motivational quote emails.

---

### Summary Checklist

1. Email + dates = the basis of all scheduled automation.
2. Gmail needs an **app password** (regular passwords are blocked).
3. GitHub Actions cron keeps a script alive without your machine.
