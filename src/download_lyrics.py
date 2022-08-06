from lyricsgenius import Genius
import os
from os import environ

TOKEN = environ.get("GENIUS_ACCESS_TOKEN")
genius = Genius(TOKEN, timeout=15, retries=3)


artist = genius.search_artist(
    "J. Cole", max_songs=1000, sort="title", include_features=True)
genius.excluded_terms = ["(Remix)", "(Live)"]
print(artist.songs)
artist.save_lyrics(format='txt')
