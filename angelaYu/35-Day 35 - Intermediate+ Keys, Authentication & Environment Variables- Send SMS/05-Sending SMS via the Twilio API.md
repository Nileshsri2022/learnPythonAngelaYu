Here is a structured breakdown of this lesson on sending SMS via Twilio.

---

### 1. Twilio Setup

Sign up at twilio.com → get three values:

* **Account SID** — your account id
* **Auth Token** — your password for the API
* A **from** number (trial gives you one)

```bash
pip install twilio
```

---

### 2. Sending a Message

```python
from twilio.rest import Client

account_sid = "YOUR_SID"
auth_token = "YOUR_TOKEN"

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="It's going to rain today. Remember to bring an umbrella ☔",
    from_="+1234567890",       # your Twilio number
    to="+911234567890",        # your phone number
)
print(message.status)
```

* Twilio is itself an API — the SDK wraps authenticated HTTP POSTs.
* `from_` (trailing underscore) avoids clashing with Python's keyword.

---

### Summary Checklist

1. SID + token authenticate; `messages.create()` sends.
2. Trial accounts can only text **verified** numbers.
3. WhatsApp variant: `from_="whatsapp:+14155238886"`, `to="whatsapp:+..."`.
