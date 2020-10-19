import tweepy
import random
import datetime
import time

consumer_key = "IeEXn5xhZ6ZBo698wZ6gzr4yT"
consumer_secret = "E0geMmb5kRSwYc675fBUTXwU7L1c0a1Ea2eZhrWg6eJCAexdyu"
key = "1317586105789710336-L9gKQL7Ww6eufpb2lodY0I7NCXFl8o"
secret = "qW9Sw8UkcMVKNHV0xp8iSzuakNgNz3vimzgqTGtOnn3l1"

fortune_list = open("Fortunes.txt", "r")
fortunes = fortune_list.readlines()
length = len(fortunes)

random_fortune = random.randint(0, length)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
while True:
    if 11 <= datetime.datetime.now().hour <= 13:
        api.update_status(fortunes[random_fortune] + "#FortuneTelling")

    time.sleep(1.75 * 3600)
