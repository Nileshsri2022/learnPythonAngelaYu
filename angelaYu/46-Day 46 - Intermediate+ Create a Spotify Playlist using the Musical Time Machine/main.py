"""
Day 46 Project: Musical Time Machine.

Enter any date, and this script scrapes the Billboard Hot 100 chart from
that week and turns it into a private Spotify playlist in your account.

Credentials come from environment variables:
    SPOTIPY_CLIENT_ID / SPOTIPY_CLIENT_SECRET  (developer.spotify.com dashboard)
"""

import os

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ---------------------------------------------------------------- Step 1: scrape
date = input("Which year do you want to travel to? Type the date (YYYY-MM-DD): ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

# Billboard redesigns its markup now and then: if this list comes back empty,
# inspect the chart page and update the selector.
song_titles = [tag.getText().strip()
               for tag in soup.select("li h3#title-of-a-story")]
print(f"Found {len(song_titles)} songs from {date}.")

# ------------------------------------------------------- Step 2: authenticate
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

# ---------------------------------------------------------- Step 3: search
year = date.split("-")[0]
song_uris = []
for song in song_titles:
    result = sp.search(q=f"track {song} year {year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"'{song}' isn't on Spotify — skipped.")
    else:
        song_uris.append(uri)

# --------------------------------------------- Step 4: create playlist + add
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
print(f"Done! Added {len(song_uris)} songs to '{date} Billboard 100'.")
