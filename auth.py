import os
import tweepy
from tweepy import OAuthHandler


CONSUMER_KEY = os.environ.get("CONSUMER_KEY") #hidden keys using os.environ.get("name") in .bashrc
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
OAUTH_TOKEN = os.environ.get("OAUTH_TOKEN")
OAUTH_TOKEN_SECRET = os.environ.get("OAUTH_TOKEN_SECRET")


def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth

def get_api():
    auth = get_auth()
    return tweepy.API(auth)

api = get_api()

#handles connecting to twitter