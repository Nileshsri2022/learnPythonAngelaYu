Here is a structured breakdown of this lesson on API authentication.

---

### 1. Why Authenticate?

Free, public endpoints serve generic data. Personalised, valuable data (your weather,
your stocks, your accounts) requires the API to know **who is asking** — and to meter,
limit or bill you accordingly. Authentication = proving your identity with a **key**.

---

### 2. How Keys Work

1. Register with the provider → they issue a long random string (your **API key**).
2. Attach it to every request (header, query parameter or body — their docs say which).
3. The provider tracks usage against your key.

> **Warning:** A leaked API key is a leaked credit card for that service. Never commit
> keys to GitHub — that's what environment variables (later today) are for.

---

### Summary Checklist

1. Authentication gates valuable data and enforces quotas.
2. Key = identity + metering; treat it as a secret.
