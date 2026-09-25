# Sending SMS via the Twilio API

`print("Bring an umbrella")` only helps if you are looking at the terminal. **Twilio**
sends the same message to your actual phone.

---

### 1. What Twilio Is

An API service for **SMS, phone calls and virtual phone numbers** in any country —
also used for ordering systems, video apps and SMS-to-email. It costs money at scale
because Twilio maintains the carrier infrastructure, but a **trial account** gives you
about **$10 of credit with no credit card** to learn with.

---

### 2. Sign Up and Grab the Three Values

1. Sign up (verify your email **and** your phone number).
2. Answer the console questions: *Do you write code?* → yes; language → **Python**;
   goal → use Twilio in a project.
3. **Get a trial number** — a free US number is fine.
4. From the dashboard, collect:

| Value | What it is |
|-------|------------|
| `account_sid` | Your Twilio account ID |
| `auth_token` | Your Twilio secret token |
| Trial phone number | The `from` number that sends the SMS |

> On a trial account you can only text **verified** numbers (add them under
> *Verified Caller IDs*). Messages also arrive prefixed with
> *"Sent from your Twilio trial account."*

---

### 3. The Code (from the Programmable SMS Quickstart)

```bash
pip install twilio
```

```python
from twilio.rest import Client

account_sid = "your_sid"          # dashboard
auth_token = "your_token"         # dashboard
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="It's going to rain today. Remember to bring an umbrella ☔",
    from_="+1...",                # your Twilio trial number
    to="+44...",                  # your verified number
)
print(message.status)             # "queued" / "sent" = success
```

* `message.sid` existing means Twilio created the message; printing
  `message.status` is a clearer signal that it went out.
* The whole block sits **inside** the `if will_rain:` branch — no rain, no SMS.
* No Twilio account? Day 32's `smtplib` email works just as well.

---

### 4. Test It

Set your coordinates to somewhere it is raining right now (Bern, Switzerland in the
lecture) and run the script. Within seconds, the phone buzzes.

The last step for the day is scheduling: run the script **every morning at 07:00**
(PythonAnywhere or GitHub Actions) so the alert is waiting before you leave.

---

### Summary Checklist

1. Twilio = SMS/voice API; trial credit lets you test for free.
2. You need `account_sid`, `auth_token` and a Twilio phone number.
3. `Client(account_sid, auth_token).messages.create(body=…, from_=…, to=…)`.
4. Trial limits: verified recipients only, plus a trial prefix on each message.
5. Fire the SMS inside the `if will_rain:` block; verify with `message.status`.
6. Next: schedule the script to run daily (Day 35, later lesson).
