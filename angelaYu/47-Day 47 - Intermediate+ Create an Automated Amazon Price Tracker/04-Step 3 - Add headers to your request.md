Here is a structured breakdown of this lesson on request headers.

---

### 1. Why Amazon Says No to Bare Requests

Amazon serves bot-detected clients a **captcha page** instead of the product —
`response.status_code` may even be `503`. Your Python client is identifiable: the
`User-Agent` header literally says `python-requests/2.x`.

---

### 2. Disguise the Request

```python
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(URL, headers=header)
```

* Copy a real browser's headers from DevTools → Network → first request → Request Headers.
* `Accept-Language` pins the site language so selectors stay predictable.

> **Warning:** This is the polite minimum, not an invisibility cloak — respect robots.txt
> and keep request rates low (Day 45).

---

### Summary Checklist

1. Blocked or captcha'd → add browser-like headers.
2. Copy them from DevTools, not from memory.
