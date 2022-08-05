import random
import time
import random
import time
import sys
# import tweepy
# import credentials
import os
# from os import environ


# CONSUMER_KEY = credentials.CONSUMER_KEY
# CONSUMER_SECRET = credentials.CONSUMER_SECRET
# ACCESS_KEY = credentials.ACCESS_KEY
# ACCESS_SECRET = credentials.ACCESS_KEY_SECRET
# FORECAST_APIKEY = credentials.FORECAST_APIKEY

# CONSUMER_KEY = environ['CONSUMER_KEY']
# CONSUMER_SECRET = environ['CONSUMER_SECRET']
# ACCESS_KEY = environ['ACCESS_KEY']
# ACCESS_SECRET = environ['ACCESS_SECRET']
# FORECAST_APIKEY = environ['FORECAST_APIKEY']


sys.path.append(os.path.abspath(os.path.join("..", "config")))

# consumer_key = 'yourkeyhere'
# consumer_secret = 'yourkeyhere'
# access_token = 'yourkeyhere'
# access_token_secret = 'yourkeyhere'
# auth = tw.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tw.API(auth, wait_on_rate_limit=True)


def create_lyric(filename: str) -> str:
    """
    The print_random_lines function prints a random line from the file specified by filename.
       The function takes one argument, filename.

    Args:
        filename:str: Pass the name of the file to be opened

    Returns:
        The number of lines in the file

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
            # remove the strings from the dataset
            if line != "" and strings not in line:  # and len(line) > 10:
                print(line)
                time.sleep(5)
            else:
                pass


# def tweet_quote():
#     # interval = 60 * 60 * 12 # tweet every 12 hours
#     auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#     auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#     api = tweepy.API(auth)
#     tweet = create_lyric('./data/drake_lyrics.txt')
#     api.update_status(tweet)
#     time.sleep(1800)

# tweet_quote()

print(create_lyric('./data/drake_lyrics.txt'))
