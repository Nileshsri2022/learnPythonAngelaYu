Here is a structured breakdown of this lesson on GitHub Actions automation.

---

### 1. The Workflow

`.github/workflows/rain_alert.yml`:

```yaml
name: Rain Alert
on:
  schedule:
    - cron: '30 1 * * *'    # 07:00 IST daily
  workflow_dispatch: {}

jobs:
  check-rain:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install requests twilio
      - run: python main.py
        env:
          OWM_API_KEY: ${{ secrets.OWM_API_KEY }}
          TWILIO_SID: ${{ secrets.TWILIO_SID }}
          TWILIO_AUTH_TOKEN: ${{ secrets.TWILIO_AUTH_TOKEN }}
```

* `cron: '30 1 * * *'` = 01:30 UTC = 07:00 India time — always write cron in **UTC**.
* Secrets are set under **Settings → Secrets and variables → Actions**; the workflow
  injects them as environment variables.

---

### Summary Checklist

1. Scheduled workflow = free, reliable daily execution.
2. Secrets → env vars → `os.environ.get()` — the full secret path end-to-end.
3. Runnable version: [`main.py`](main.py)
