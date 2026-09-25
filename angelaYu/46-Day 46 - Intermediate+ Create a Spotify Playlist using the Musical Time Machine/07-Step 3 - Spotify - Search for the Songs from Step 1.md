# Step 3 - Spotify - Search for the Songs from Step 1

---

### 1. Track Search with a Year Filter

```python
song_uris = []
year = date.split("-")[0]

for song in song_titles:
    result = sp.search(q=f"track {song} year {year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"'{song}' isn't on Spotify — skipped.")
    else:
        song_uris.append(uri)
```

* `sp.search` returns nested JSON: `["tracks"]["items"]` is the hit list.
* The **URI** (`spotify:track:…`) is the song's ID for every later API call.
* `try/except IndexError` handles the not-on-Spotify case without aborting the loop.

---

### Summary Checklist

1. Search = `track <name> year <year>`.
2. Collect URIs; skip the gaps.
