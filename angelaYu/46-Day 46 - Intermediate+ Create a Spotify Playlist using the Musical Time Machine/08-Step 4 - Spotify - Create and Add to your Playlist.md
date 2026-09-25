# Step 4 - Spotify - Create and Add to your Playlist

---

### 1. Two API Calls

```python
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
)
sp.user_playlist_add_tracks(
    user=user_id,
    playlist_id=playlist["id"],
    tracks=song_uris,
)
```

1. `user_playlist_create` — makes the (private) playlist, returns its ID.
2. `user_playlist_add_tracks` — adds **all** URIs in one call.

Open Spotify → the playlist `{date} Billboard 100` is there, 100 songs of your past.

---

### Summary Checklist

1. Create once, add in bulk.
2. Runnable version: [`main.py`](main.py)
