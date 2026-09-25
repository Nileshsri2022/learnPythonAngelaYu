# What is API Authentication and Why Do We Need to Authenticate Ourselves?

Day 33–34 used free APIs. Today the data gets expensive — and that changes how you
have to ask for it.

---

### 1. Why Some APIs Charge

An API is often a company **selling data**. Weather is the example: it looks simple,
but OpenWeatherMap runs **4,000+ weather stations**, analyses satellite images and
pays for servers, electricity and staff to turn all of that into a forecast for every
city in the world. Nobody gives that away for free to a commercial app.

| Data | Typically | Why |
|------|-----------|-----|
| Trivia questions, ISS position | Free | Cheap to produce, low value |
| Weather, financial data | Free tier + paid tiers | Expensive to produce, high value |

Almost everyone offers a **free tier** for testing and learning — charging only makes
sense once *your* app has real users.

---

### 2. The Problem: Free Tiers Get Abused

Anyone can claim "I'm just learning" — including a 1,000-person company. So providers
hand every user a **personal key**.

> An **API key** is like your account number *and* password combined. It lets the
> provider track how much you use, authorise your access, and cut you off when you
> go over the limit.

Different providers authenticate in different ways, but most involve some form of
API key. (Day 37 shows the more advanced variant: sending the key in a **header**
instead of a parameter.)

---

### 3. Where You Have Seen This Before

On Day 33 a bad request returned `404`. Authenticated APIs add a new failure mode:

```python
{"cod": 401, "message": "Invalid API key..."}
```

* **401 Unauthorized** — the key is wrong, misspelled, or missing.
* That is always the first thing to check when an authenticated call fails.

---

### Summary Checklist

1. APIs are frequently a way of **selling data** that is costly to collect.
2. Free tiers exist for learning and testing; heavy use moves you to paid tiers.
3. An **API key** identifies *you*, meters your usage, and can be revoked.
4. Most providers authenticate with a key (often as a parameter) — some use headers.
5. A failed authenticated request usually means a bad key → **401**.
