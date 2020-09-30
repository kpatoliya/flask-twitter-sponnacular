import json
import os
import flask
import random
import requests
from flask import request
from tweepy import OAuthHandler, API, Cursor
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv('CON_KEY')
consumer_secret = os.getenv('CON_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_SECRET')

spoonacular_api = os.getenv('SPOONACULAR_KEY')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

dishes = ['French Fries', 'Pasta', 'Caesar Salad', 'Pound Cake', 'Samosa', 'Pizza', 'Tacos',
          'Paneer Tikka']

app = flask.Flask(__name__, template_folder='./templates')


@app.route("/", methods=['POST', 'GET'])
def index():
    tweets = []
    username = []
    created_at = []
    if request.method == 'POST':
        dish = request.form['foodItem']
    else:
        dish = dishes[random.randint(0, 7)]

    ingredients = []
    content = requests.get("https://api.spoonacular.com/recipes/complexSearch?query=" + dish
                           + "&apiKey=" + spoonacular_api)
    json_response = json.loads(content.text)
    randomRecipe = random.randint(0, len(json_response['results']) - 1)
    idRecipe = str(json_response['results'][randomRecipe]['id'])
    imageRecipe = json_response['results'][randomRecipe]['image']

    recipeInfo = requests.get("https://api.spoonacular.com/recipes/" + idRecipe + "/information?includeNutrition=false"
                                                                                  "&apiKey=" + spoonacular_api)
    json_response2 = json.loads(recipeInfo.text)
    sourceName = json_response2['sourceName']
    nameRecipe = json_response2['title']
    url = json_response2['sourceUrl']
    prepTime = json_response2['readyInMinutes']
    for i in range(0, len(json_response2['extendedIngredients'])):
        ingredients.append(json_response2['extendedIngredients'][i]['original'])

    for status in Cursor(auth_api.search, tweet_mode="extended", q=dish + '-filter:retweets', lang="en").items(50):
        tweets.append(status.full_text)
        username.append(status.user.screen_name)
        created_at.append(status.created_at)

    randomSelectInt = random.randint(0, 49)
    return flask.render_template("index.html", tweets=tweets[randomSelectInt], username=username[randomSelectInt],
                                 created_at=created_at[randomSelectInt], recipe=nameRecipe, image=imageRecipe,
                                 ingredients=ingredients, time=prepTime, url=url, sourceName=sourceName,
                                 length=len(ingredients))


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
