"""
Day 45 Project: 100 Movies that You Must Watch.

Scrapes Empire Magazine's "100 Greatest Movies of All Time" list (via a
Wayback Machine snapshot, because the live page's markup has changed) and
writes every title to movies.txt, best movie first, so you can work
through them one by one.
"""

import requests
from bs4 import BeautifulSoup

URL = ("https://web.archive.org/web/20200518073855/"
       "https://www.empireonline.com/movies/features/best-movies-2/")

response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

# Every movie title lives in an <h3 class="title"> tag.
titles = [tag.getText() for tag in soup.find_all(name="h3", class_="title")]
titles.reverse()  # page ranks 100 -> 1; flip so #1 comes first

with open("movies.txt", mode="w", encoding="utf-8") as file:
    file.write("\n".join(titles))

print(f"Saved {len(titles)} movies to movies.txt.")
