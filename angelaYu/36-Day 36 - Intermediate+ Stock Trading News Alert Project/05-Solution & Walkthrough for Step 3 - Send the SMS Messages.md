Here is a structured walkthrough of Step 3 — sending the SMS messages.

---

### 1. One Message per Article

```python
from twilio.rest import Client

client = Client(os.environ.get("TWILIO_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="+1234567890",
        to="+911234567890",
    )
    print(message.status)
```

* Loop the formatted list — three coherent alerts, not one giant SMS.
* Twilio credentials come from environment variables (Day 35).

---

### 2. The Pipeline Complete

```
Alpha Vantage ──▶ ±5%? ──▶ NewsAPI ──▶ format ──▶ Twilio SMS
   (prices)       (gate)   (context)   (f-string)  (delivery)
```

Each stage is independently testable — print at every stage while developing, then wire
the real sender last.

---

### Summary Checklist

1. Three APIs, one script, zero secrets in code.
2. Runnable version: [`main.py`](main.py)
