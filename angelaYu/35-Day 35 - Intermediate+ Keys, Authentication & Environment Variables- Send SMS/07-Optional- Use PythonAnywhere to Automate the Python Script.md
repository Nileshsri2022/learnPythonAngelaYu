# Optional: Use PythonAnywhere to Automate the Python Script

A rain alert is only useful if it runs without you. This lecture puts `main.py` in the
cloud and schedules it for the morning.

---

### 1. Put the Script Online

1. Log in to **PythonAnywhere** (the same service used for the birthday wisher on Day 32).
2. Delete the old files (`letter_templates/`, `main.py`, `birthday.csv`).
3. Upload your new `main.py` — **directly in your home folder**, not nested inside
   other folders, otherwise you have to type the full path on every run.
4. Open a **Bash console** and run:

```bash
python3 main.py
```

---

### 2. The Free-Account Gotcha: Proxy Servers

The first run fails:

```text
ConnectionError: ... api.twilio.com ... Max retries exceeded
```

Free PythonAnywhere accounts reach the internet through a **proxy**, and the Twilio
client has to be told about it. The fix (documented in PythonAnywhere's own help page)
needs three extra lines:

```python
from twilio.http.http_client import TwilioHttpClient   # 1. import
import os                                              # (PyCharm will complain until you do)

proxy_client = TwilioHttpClient()                      # 2. build a proxy client
proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

client = Client(account_sid, auth_token, http_client=proxy_client)   # 3. pass it in
```

> Copy the exception into a search engine — the first result is PythonAnywhere's
> official article with this exact fix. Reading error messages is a developer skill.

---

### 3. Schedule It

1. **Tasks** tab → create (or reuse) a scheduled task.
2. Command: `python3 main.py`. Frequency: **daily**, time e.g. `07:00`.
3. ⚠️ PythonAnywhere schedules in **UTC** — convert to your local time. British
   Summer Time is UTC+1, so 06:00 UTC = 07:00 local.
4. Free accounts allow **one** task; upgrading removes that limit.
5. Test by setting the time to a minute from now, then check the phone.

---

### Summary Checklist

1. Upload `main.py` to PythonAnywhere and run it from a Bash console.
2. Free accounts use a proxy → Twilio needs `TwilioHttpClient` + `http_client=`.
3. Tasks tab schedules the command; free plans allow one task.
4. Scheduled times are **UTC** — do the timezone maths.
5. Leave the script running daily and the SMS arrives before you leave the house.
