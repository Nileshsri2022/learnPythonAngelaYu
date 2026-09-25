# Step 4 - Retrieve your customer emails

---

### 1. Reading the Users Tab

```python
data_manager = DataManager()
customer_email_list = [user["email"] for user in data_manager.get_customer_emails()]
```

* A list comprehension (Day 26) flattens the users into just the email column.
* Like destinations, users live entirely in the sheet — no database, no auth system.

---

### 2. personalised vs. Broadcast

The course variant sends a generic deal blast to everyone; an easy extension is
per-user target prices (add a column to the form, filter per user).

---

### Summary Checklist

1. `[u["email"] for u in users]` — your mailing list.
2. Extending the schema = adding a column, not code.
