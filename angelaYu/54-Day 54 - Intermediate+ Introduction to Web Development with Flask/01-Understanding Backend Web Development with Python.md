# Understanding Backend Web Development with Python

---

### 1. Front-End vs Back-End

Days 41–44 taught the **front-end** — HTML (structure), CSS (style), JavaScript
(behaviour). That's the pretty shop window.

A website with *functionality* also needs a **back-end**: the business logic, the
calculations, the data. Python shines here.

| Term | Meaning |
|------|---------|
| Front-end | what the user sees and clicks |
| Back-end | server-side logic, data, security |
| **Full-stack** | comfortable with both sides |

---

### 2. Frameworks

A **framework** is pre-written code for the chores every site has. Popular Python
back-end frameworks: Flask, Django, Bottle, Pyramid.

* **Flask** — small, flexible, beginner-friendly; great for small/medium projects.
* **Django** — batteries-included; better for large commercial projects.

> **Note:** A *library* is something **you** call; a **framework** calls **you**. With
> `requests` you say *go fetch this*. With Flask you write functions and tell Flask
> *when a user hits this URL, run this* — the framework does the calling.

---

### 3. The Three Components of a Backend

| Component | Analogy (restaurant) | Job |
|-----------|---------------------|-----|
| **Client** | front of house | the browser/user making requests |
| **Server** | the kitchen | a computer online 24/7 that receives requests and responds |
| **Database** | the larder | a souped-up spreadsheet storing the site's data |

Flow for `google.com`:

1. Client types the URL → request crosses the internet.
2. Server responds with HTML/CSS/JS files.
3. Browser renders them.

For data-driven pages (e.g. *your* Eventbrite tickets), the server also **fetches from the
database**, pours that data into the HTML/CSS/JS, and sends the finished bundle back.
The client never talks to the database directly.

---

### 4. Why Learn This Now

The end-to-end pattern is:

```text
user request → server logic → database → rendered page → user
```

Over the next days you build each piece from scratch — first a server (Flask), then
templates (Jinja), then forms, databases, authentication and deployment.

---

### Summary Checklist

1. Front-end = HTML/CSS/JS; back-end = logic + data; full-stack = both.
2. Libraries are called by you; frameworks call your code.
3. Flask for small projects and learning; Django for big ones.
4. Backend = client + server + database, like front-of-house, kitchen and larder.
5. The client only ever sees the final rendered response.
