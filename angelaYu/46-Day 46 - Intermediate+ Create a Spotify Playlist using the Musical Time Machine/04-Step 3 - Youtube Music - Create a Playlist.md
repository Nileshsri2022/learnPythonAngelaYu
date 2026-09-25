Here is a structured breakdown of this lesson on creating a YouTube Music playlist.

---

### 1. Create the Playlist

```python
playlist_id = yt.create_playlist(
    title=f"{date} Billboard 100",
    description="Made by a Python time machine",
    privacy_status="PRIVATE",
)
```

* Returns the playlist ID used by every later call.
* `privacy_status`: `"PRIVATE"`, `"PUBLIC"` or `"UNLISTED"`.

---

### 2. Search and Add

```python
for song in song_titles:
    results = yt.search(query=f"{song} {year}", filter="songs")
    if results:
        yt.add_playlist_items(playlist_id, [results[0]["videoId"]])
```

Search per title, take the first hit, append its video ID to the playlist.

---

### Summary Checklist

1. `create_playlist` → ID → `add_playlist_items` per song.
2. Same shape as the Spotify flow — only auth differs.
