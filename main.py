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

dishes = ['French Fries', 'Dosa', 'Caesar Salad', 'Pound Cake', 'Samosa', 'Margherita Pizza', 'Tacos', 'Paneer Tikka']
tweets = []

dish = dishes[random.randint(0, 7)]
for tweet in Cursor(auth_api.search, tweet_mode="extended", q=dish + '-filter:retweets', lang="en").items(50):
    tweets.append(tweet.full_text)

app = flask.Flask(__name__, template_folder='./templates')


@app.route("/")
def index():
    return flask.render_template("index.html", tweets=tweets[random.randint(0, len(dishes)-1)])


app.run(
    port=int(os.getenv('PORT', 5500)),
    debug=True
)
