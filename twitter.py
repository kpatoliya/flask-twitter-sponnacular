import os
import random

from tweepy import OAuthHandler, API, Cursor
from dotenv import load_dotenv

load_dotenv()


def get_tweet(dish):
    tweets = []
    username = []
    created_at = []
    auth = OAuthHandler(os.getenv('CON_KEY'), os.getenv('CON_SECRET'))
    auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_SECRET'))
    auth_api = API(auth)

    for status in Cursor(auth_api.search, tweet_mode="extended", q=dish + '-filter:retweets', lang="en").items(50):
        tweets.append(status.full_text)
        username.append(status.user.screen_name)
        created_at.append(status.created_at)

    randomSelectInt = random.randint(0, 49)

    return {'tweet': tweets[randomSelectInt], 'username': username[randomSelectInt], 'created_at': created_at[randomSelectInt]}