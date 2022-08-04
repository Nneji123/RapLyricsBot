import os
import sys

sys.path.append(os.path.abspath(os.path.join("..", "config")))

from ..bot import *


files = 'drake_lyrics.txt'

def test_random_lyric():
    assert print_random_lines(files) == "fi"