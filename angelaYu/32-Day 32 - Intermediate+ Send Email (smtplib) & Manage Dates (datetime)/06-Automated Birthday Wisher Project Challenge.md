Here is a structured breakdown of the Birthday Wisher challenge.

---

### 1. The Requirements

```
birthdays.csv: name,email,year,month,day
letter_1/2/3.txt: "Dear [NAME], Happy birthday!..."
```

1. Read `birthdays.csv` (Day 25 skills).
2. `datetime.now()` gives today's month and day.
3. Anyone matching → pick a random `letter_N.txt`, `replace("[NAME]", name)`.
4. Send it via SMTP.

---

### 2. Hints

* `pandas` or the `csv` module both work — dict-style rows are easiest.
* Compare **month AND day** (not the year!).
* The letter swap is the mail-merge `replace` trick from Day 24.

---

### Summary Checklist

1. CSV in → date match → template fill → email out.
2. Everything is a previous day's skill in a new combination.
