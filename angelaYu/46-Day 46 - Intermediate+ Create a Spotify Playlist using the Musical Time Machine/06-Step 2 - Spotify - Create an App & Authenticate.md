# Step 2 - Spotify - Create an App & Authenticate

---

### 1. Create the App

1. developer.spotify.com/dashboard → **Create app** → name it.
2. Note the **Client ID** and **Client Secret**.
3. Add a **Redirect URI** (e.g. `http://example.com`) — where Spotify sends you after
   the consent screen.

---

### 2. Authenticate with Spotipy

```bash
pip install spotipy
```

```python
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]
```

* **OAuth** = you consent once in the browser; Spotify issues a token your code uses.
* `scope` declares *what* the token may do — request the minimum.
* `token.txt` caches the token so you don't re-consent every run.

> **Warning:** the client secret and `token.txt` are secrets — environment variables +
> gitignore, never literals.

---

### Summary Checklist

1. App on the dashboard → ID + secret + redirect URI.
2. `SpotifyOAuth` handles the whole token dance.
