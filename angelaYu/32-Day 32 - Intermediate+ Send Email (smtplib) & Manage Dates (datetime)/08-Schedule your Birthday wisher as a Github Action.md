Here is a structured breakdown of scheduling the script with GitHub Actions.

---

### 1. Why GitHub Actions?

Your script only sends birthdays when *you* run it. A **GitHub Actions workflow** runs it
in the cloud on a schedule — free for public repos.

---

### 2. The Workflow

`.github/workflows/birthday.yml`:

```yaml
name: Birthday Wisher
on:
  schedule:
    - cron: '0 9 * * *'     # 09:00 UTC every day
  workflow_dispatch: {}     # manual run button

jobs:
  send-wishes:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install pandas
      - run: python main.py
        env:
          MY_EMAIL: ${{ secrets.MY_EMAIL }}
          MY_PASSWORD: ${{ secrets.MY_PASSWORD }}
```

* `cron: '0 9 * * *'` — standard cron syntax: minute hour day month weekday.
* Credentials live in **repo secrets** (Settings → Secrets → Actions), never in code —
  Day 35 covers environment variables in depth.

---

### Summary Checklist

1. `schedule.cron` = free daily execution in the cloud.
2. Secrets keep the app password out of the repo.
