from src.utils import create_lyric
import os
import sys

sys.path.append(os.path.abspath(os.path.join("..", "config")))


files = './data/drake_lyrics.txt'


def test_random_lyric():
    assert create_lyric(files) == 'Tweeting a lyric...'
