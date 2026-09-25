Here is a structured breakdown of Step 6 — Twilio notifications.

---

### 1. The Notification Manager

```python
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ.get("TWILIO_SID"),
                             os.environ.get("TWILIO_AUTH_TOKEN"))

    def send_sms(self, message_body):
        message = self.client.messages.create(
            body=message_body,
            from_=os.environ.get("TWILIO_FROM"),
            to=os.environ.get("TWILIO_TO"),
        )
        print(message.status)
```

* The manager isolates delivery — swap SMS for email/WhatsApp without touching the
  deal logic (Day 40 does exactly that for email).

---

### 2. Part 1 Complete

Sheet → search → compare → notify. Part 2 adds users, sign-ups and email.

---

### Summary Checklist

1. Notifications behind a class = swappable delivery channel.
2. Runnable version: [`main.py`](main.py)
