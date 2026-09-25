Here is a structured breakdown of this lesson on backend web development.

---

### 1. Where Your Code Will Live Now

Days 1–53 were scripts that run, print and finish. A **backend** is a program that runs
*forever*, listening for HTTP requests and sending responses — that's a **web server**.

```
Browser  --request-->  Server (your Python!)  --response-->  Browser
```

* **Frontend**: HTML/CSS/JS the browser renders (Days 41–44).
* **Backend**: the Python that decides *what* to send back.

---

### 2. Framework vs Library

| Library (requests, bs4) | Framework (Flask) |
|---|---|
| *you* call it when needed | *it* calls your code when a request arrives |
| your architecture | you follow its architecture |

---

### Summary Checklist

1. Backend = long-running listener responding to HTTP.
2. Frameworks invert control: they call you.
