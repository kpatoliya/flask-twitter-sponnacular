import json
import os
import flask
import random
from tweepy import OAuthHandler, API, Cursor
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv('CON_KEY')
consumer_secret = os.getenv('CON_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_SECRET')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

dishes = ['French Fries', 'Dosa', 'Caesar Salad', 'Pound Cake', 'Samosa', 'Margherita Pizza', 'Tacos',
              'Paneer Tikka']

app = flask.Flask(__name__, template_folder='./templates')


@app.route("/")
def index():

    tweets = []
    username = []
    created_at = []

    dish = dishes[random.randint(0, 7)]
    for status in Cursor(auth_api.search, tweet_mode="extended", q=dish + '-filter:retweets', lang="en").items(50):
        tweets.append(status.full_text)
        username.append(status.user.screen_name)
        created_at.append(status.created_at)

    randomSelectInt = random.randint(0, len(dishes) - 1)
    print(tweets[randomSelectInt])
    return flask.render_template("index.html", tweets=tweets[randomSelectInt], username=username[randomSelectInt],
                                 created_at=created_at[randomSelectInt], dish=dish)


app.run(
    port=int(os.getenv('PORT', 5000)),
    debug=True
)
