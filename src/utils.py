import glob
import os
import random
import sys
from os import environ

from lyricsgenius import Genius

sys.path.append(os.path.abspath(os.path.join("..", "config")))


TOKEN = environ.get("GENIUS_ACCESS_TOKEN")
genius = Genius(TOKEN, timeout=30, retries=3)

# function for reading lines of a string


def create_lyric(filename: str):
    count = 0
    while True:
        with open(filename, encoding="utf8") as f:
            lines = f.readlines()
        for line in lines:
            count += 1
            rand_line = random.randint(0, len(lines) - 1)
            line = lines[rand_line]
            strings = ['Verse', 'Chorus', 'Interlude', 'Produced',
                       'Bridged', 'Intro', 'Outro']
            words = line.split()
            resultwords = [word for word in words if word.lower()
                           not in strings]
            if resultwords != "" and len(resultwords) > 10:
                return('Printing a lyric...')
            else:
                pass


def download_lyrics(albums: list, artist: str):
    for words in albums:

        album = genius.search_album(words, artist)
        album.save_lyrics(words.replace(" ", "_"), 'txt')
        print('Saved files....')


def merge_files(location: str):
    read_files = glob.glob(location+"*.txt")

    with open("./data/result.txt", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())
                print('Merged all files')


#download_lyrics(['My Turn', 'Harder Than Ever'], 'Lil Baby')
#merge_files("./")
