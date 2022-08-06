import os
import sys
from os import environ

from flask import Flask

import bot

sys.path.append(os.path.abspath(os.path.join("..", "config")))


app = Flask(__name__)


@app.route("/")
def home():
    bot.tweet_lyric('./data/drake_lyrics.txt')
    return "Tweeting a lyric"


app.run(host='0.0.0.0', port=environ.get('PORT'))
