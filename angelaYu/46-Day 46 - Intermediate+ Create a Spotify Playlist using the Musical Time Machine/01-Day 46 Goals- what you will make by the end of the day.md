# Day 46 Goals- what you will make by the end of the day

---

### 1. The Musical Time Machine

A mixtape of the hits from a particular period of your life is a time machine in
audio form. Today's project automates it:

> "Pick a date → get the **Billboard Hot 100** from that day → create a **Spotify
> playlist** with all 100 songs."

---

### 2. The Pipeline

| Step | Tool |
|------|------|
| 1. Scrape the Hot 100 for a date | `requests` + BeautifulSoup (Day 45) |
| 2. Authenticate with Spotify | Spotipy + OAuth |
| 3. Search each song | Spotify search API |
| 4. Create playlist + add tracks | Spotify playlists API |

---

### Summary Checklist

1. Scraping feeds an API — the two superpowers combine.
2. Input: a date. Output: a playlist.
