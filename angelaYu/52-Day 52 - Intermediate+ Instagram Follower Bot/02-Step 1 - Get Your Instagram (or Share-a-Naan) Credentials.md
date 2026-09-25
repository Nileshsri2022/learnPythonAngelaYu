Here is a structured breakdown of this lesson on credentials.

---

### 1. Credentials as Environment Variables

```python
import os

USERNAME = os.environ.get("IG_USERNAME")
PASSWORD = os.environ.get("IG_PASSWORD")
```

* Instagram aggressively bot-detects — a fresh account from a datacenter IP will trip
  it. Use your own account and expect friction.
* Better still: run against the practice clone so a mistake costs nothing.

> **Warning:** credential-stuffing and mass-following breach Instagram's ToS —
> automation practice, not growth strategy.

---

### Summary Checklist

1. Secrets in env vars.
2. Practice clone > real account.
