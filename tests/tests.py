from src.utils import create_lyric, download_lyrics, merge_files, download_lyrics
import os
import sys

sys.path.append(os.path.abspath(os.path.join("..", "config")))


files = './data/drake_lyrics.txt'


def test_random_lyric():
    assert create_lyric(files) == 'Printing a lyric...'


def test_download_lyric():
    assert download_lyrics(['My Turn', 'Harder Than Ever'],
                           'Lil Baby') == 'Saved files....'
