import random
import time
import random
import time
import sys
import tweepy
import credentials
import os
# from os import environ


CONSUMER_KEY = credentials.CONSUMER_KEY
CONSUMER_SECRET = credentials.CONSUMER_SECRET
ACCESS_KEY = credentials.ACCESS_KEY
ACCESS_SECRET = credentials.ACCESS_KEY_SECRET
FORECAST_APIKEY = credentials.FORECAST_APIKEY

# use this when you've set the keys as environment variables later
# CONSUMER_KEY = environ['CONSUMER_KEY']
# CONSUMER_SECRET = environ['CONSUMER_SECRET']
# ACCESS_KEY = environ['ACCESS_KEY']
# ACCESS_SECRET = environ['ACCESS_SECRET']
# FORECAST_APIKEY = environ['FORECAST_APIKEY']


sys.path.append(os.path.abspath(os.path.join("..", "config")))


def create_lyric(filename: str) -> str:
    """
    This function prints a random line from the file specified by filename which is drake lyrics in this case. It also exludes lines that have specific words in a list

    The function takes one argument, filename.

    Args:
        filename:str: Pass the name of the file to be opened

    Returns:
        The contents of each line in the file.

    Doc Author:
        Ifeanyi
    """
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
                return line
                # time.sleep(5)
            else:
                pass


def tweet_lyric():
    # this will tweet a drake lyric every 30 minutes.
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    tweet = create_lyric('./data/drake_lyrics.txt')
    api.update_status(tweet)
    time.sleep(1800)


if __name__() == " __main__":
    tweet_lyric

# tweet_lyric()


# print(create_lyric('./data/drake_lyrics.txt'))
