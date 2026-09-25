# Step 4 - Youtube Music - Search and Add Songs to the Playlist

---

### 1. Matching Era to Query

A song named "Ice" from 2000 and one from 2021 both exist — appending the **year** to
the search query is what keeps the playlist period-accurate:

```python
results = yt.search(query=f"{song} {year}", filter="songs")
```

* `filter="songs"` ignores videos, albums and playlists.
* Skipping unfound songs (rather than crashing) keeps a 100-song run unattended.

---

### Summary Checklist

1. Query = title + year; filter to songs only.
2. Handle misses gracefully — old charts have gaps on streaming.
