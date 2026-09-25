# Day 40 Goals: what you will make by the end of the day

Part 2 of the capstone: turn yesterday's personal tool into **Flight Club** — a real
product with **sign-ups**, a user list, and emails to everyone at once.

> *First rule of Flight Club: you do not talk about Flight Club.*

---

### 1. From Tool to Product

Part 1 had a user base of exactly one: you. Jack's Flight Club charges money for
essentially the same pipeline — a spreadsheet of destinations, a daily search, and
deals in your inbox. Today you build your own version of that.

```text
Part 1                                Part 2
sheet of my destinations + prices  →  + a `users` sheet
  → search flights for me            →  search flights once
  → SMS to me                        →  email *every* customer
```

---

### 2. What You Will Build

| Piece | How it works |
|-------|--------------|
| **Sign-up** | A text-based flow asks for first name, last name, email |
| **Validation** | Re-prompt while an email is missing an `@`, then confirm "Welcome, Angela" |
| **User store** | Each new customer is added as a row in a Google Sheets `users` tab |
| **Notification** | `smtplib` / `EmailMessage` loops over the user list and emails everyone the deals |

```python
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name, self.last_name, self.email = first_name, last_name, email

def send_emails(users, deals):
    for user in users:                       # one email per customer
        message = f"Subject: Flight deals\n\nDear {user.first_name},\n{deals}"
        ...
```

---

### Summary Checklist

1. Sign-up collects name + email with a simple validation loop.
2. Customers live in a separate `users` sheet — your first "database".
3. `smtplib`/`EmailMessage` sends the daily deals to every subscriber.
4. Same idea as commercial services (Jack's Flight Club) — you own the code.
5. Capstone complete: Google Sheets + flight API + email/SMS + OOP in one product.
