# Step 2 - Youtube Music - Re-use your Browser's Requests to Authenticate

---

### 1. An Alternative Backend

Before the Spotify steps, the course shows the same pipeline on **YouTube Music** using
the `ytmusicapi` library — useful if you don't have Spotify.

```bash
pip install ytmusicapi
```

---

### 2. Reusing Your Browser's Login

YouTube Music has no official public API, so `ytmusicapi` impersonates *your* logged-in
browser: you copy request headers from DevTools into a config file, and every call is
then made as you.

```bash
ytmusicapi browser
```

```python
from ytmusicapi import YTMusic

yt = YTMusic("browser.json")     # headers copied from your browser
```

> **Warning:** these headers contain your session credentials — treat `browser.json`
> like a password (gitignore it).

---

### Summary Checklist

1. No official API? Reuse browser credentials via `ytmusicapi`.
2. Header files = secrets — never commit them.
