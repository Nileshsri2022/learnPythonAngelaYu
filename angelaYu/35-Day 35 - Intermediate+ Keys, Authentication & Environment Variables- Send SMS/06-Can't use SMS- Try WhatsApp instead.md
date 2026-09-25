# Can't use SMS- Try WhatsApp instead

---

### 1. Why WhatsApp?

Twilio's trial SMS can be region-restricted or cost money. The **WhatsApp sandbox** is
free: join your sandbox by sending the join code to Twilio's WhatsApp number, then swap
the prefixes:

```python
message = client.messages.create(
    body="It's going to rain today. ☔",
    from_="whatsapp:+14155238886",     # Twilio sandbox number
    to="whatsapp:+911234567890",       # your WhatsApp-enabled number
)
```

Everything else — SID, token, `create()` — is identical. Only the address scheme
changes.

---

### Summary Checklist

1. Same Twilio API, `whatsapp:` prefix on from/to.
2. Join the sandbox once from your phone, then it just works.
