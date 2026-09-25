Here is a structured breakdown of this lesson on environment variables.

---

### 1. The Problem

Keys typed directly into code end up in screenshots, repos and logs — permanently.
**Environment variables** live in the *shell's* environment, outside any file:

```bash
export OWM_API_KEY="abc123"      # macOS/Linux
set OWM_API_KEY=abc123           # Windows
```

---

### 2. Reading Them in Python

```python
import os

api_key = os.environ.get("OWM_API_KEY")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
```

* The code contains only a *name* — the value arrives from the environment at runtime.
* Each machine/context supplies its own values: dev, cloud, CI.

---

### 3. Options in Practice

| Where | How |
|-------|-----|
| PyCharm | Run Configuration → Environment variables |
| PythonAnywhere | Web tab env vars |
| GitHub Actions | Repository **Secrets** → injected as env vars |

> **Warning:** `os.environ["KEY"]` raises `KeyError` when unset; `.get("KEY")` returns
> `None` — use `.get()` and fail with a clear message.

---

### Summary Checklist

1. Secrets belong in the environment, never in source.
2. `os.environ.get("NAME")` reads them.
3. Every hosting platform has its own place to define them.
