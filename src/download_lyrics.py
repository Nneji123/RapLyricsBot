from lyricsgenius import Genius
import os
import sys
from os import environ
sys.path.append(os.path.abspath(os.path.join("..", "config")))


TOKEN = environ.get("GENIUS_ACCESS_TOKEN")
genius = Genius(TOKEN, timeout=30, retries=3)


# artist = genius.search_artist(
#     "J. Cole", max_songs=1000, sort="title", include_features=True)
# genius.excluded_terms = ["(Remix)", "(Live)"]
# print(artist.songs)
# artist.save_lyrics(format='txt')

lists = ['Donda', 'Donda 2']
artist = "Kanye West"


for words in lists:

    album = genius.search_album(words, artist)
    album.save_lyrics(words.replace(" ", "_"), 'txt')
