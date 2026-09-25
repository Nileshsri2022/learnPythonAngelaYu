Here is a structured breakdown of Step 6 — environment variables.

---

### 1. Five Secrets, Zero in Code

This project has the most credentials so far — the moment to cement the habit:

```python
import os

APP_ID = os.environ.get("NIX_APP_ID")
API_KEY = os.environ.get("NIX_API_KEY")
SHEET_TOKEN = os.environ.get("SHEET_TOKEN")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
```

* PyCharm: Run Configuration → Environment variables.
* GitHub Actions: repo secrets injected as env vars.
* Anywhere you run it, the same code reads whatever that environment provides.

---

### Summary Checklist

1. Every credential from Day 35 onward: env vars, always.
2. Rotating a leaked secret is easy *only* if it never lived in the repo.
3. Runnable version: [`main.py`](main.py)
