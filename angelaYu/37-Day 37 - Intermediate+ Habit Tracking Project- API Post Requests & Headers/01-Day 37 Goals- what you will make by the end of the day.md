# Day 37 Goals: what you will make by the end of the day

Day 37 adds the rest of the HTTP verbs — **POST, PUT and DELETE** — plus
**header-based authentication**, and uses them to build a **habit tracker**.

---

### 1. The Inspiration

Simone Giertz's physical habit tracker: tap today's date every day you keep a habit,
and the **unbroken streak** makes you want to keep going. This project builds the
digital version with an API called **Pixela**.

Pixela records more than done/not-done — it records *intensity*. Track kilometres
cycled, minutes meditated or pages read, and each day's square is lighter or darker
according to the value, giving you a year-at-a-glance heat map.

```text
Jan  ░ ▒ █ ▒ ░ ▒ █ █ …
Feb  █ ▒ ░ ░ ▒ █ ▒ ░ …
```

---

### 2. What You Will Learn

| Topic | Why the habit tracker needs it |
|-------|-------------------------------|
| **POST** requests | Create a user, create a graph, add a pixel for today |
| **PUT** requests | Update an existing pixel (you logged the wrong number) |
| **DELETE** requests | Remove a pixel that should not be there |
| **Headers** | Advanced authentication — the token travels in the request header, not the URL |

```python
headers = {"X-USER-TOKEN": TOKEN}
requests.post(url=pixela_endpoint, json=user_params)          # create user
requests.put(url=f"{pixel_endpoint}/{today}", headers=headers, json={"quantity": "5"})
requests.delete(url=f"{pixel_endpoint}/{today}", headers=headers)
```

---

### Summary Checklist

1. POST creates, PUT updates, DELETE removes — the full CRUD set on a REST API.
2. Sensitive credentials can go in **headers** instead of the URL/params.
3. Habit trackers work because of **streaks**: don't break the line.
4. Pixela plots quantity as colour intensity — a year of data at a glance.
5. You design the habit; today's project is the logging tool.
