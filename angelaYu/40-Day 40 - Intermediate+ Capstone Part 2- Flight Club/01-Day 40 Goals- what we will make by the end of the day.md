Here is a structured breakdown of the Day 40 goals — Flight Club, Part 2.

---

### 1. Skills Covered on Day 40

* **Google Forms + Sheets** — collecting user sign-ups without a backend
* Reading a **users** sheet via Sheety
* Handling **no-direct-flight** destinations (searching via a stop-over)
* **Sending email** to all customers (Day 32's smtplib, industrialised)

---

### 2. The Project Upgrade

Day 39 alerts *you*. Day 40 makes it a product:

1. Friends sign up via a Google Form (first name, last name, email) feeding a `users` tab.
2. The deal search runs for every destination — including routes **without direct
   flights** (one stop-over).
3. Every deal under a user's target price is **emailed to every customer**.

```
Subject: Low price alert!

Only ₹45,000 to fly from DEL to CDG, out 2027-03-12.

Dear Nilesh,
...
```

---

### Summary Checklist

1. Users + deals + email = "Flight Club".
2. Capstone complete: your first multi-service product.
