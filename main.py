import spoonacular
import os
import flask
import twitter
from flask import request

app = flask.Flask(__name__, template_folder='./templates')


@app.route("/", methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        dish = spoonacular.get_random_recipe()['dish']
        imageRecipe = spoonacular.get_random_recipe()['imageRecipe']
        sourceName = spoonacular.get_random_recipe()['sourceName']
        nameRecipe = spoonacular.get_random_recipe()['nameRecipe']
        ingredients = spoonacular.get_random_recipe()['ingredients']
        prepTime = spoonacular.get_random_recipe()['prepTime']
        url = spoonacular.get_random_recipe()['url']
    else:
        dish = spoonacular.get_recipe()['dish']
        imageRecipe = spoonacular.get_recipe()['imageRecipe']
        sourceName = spoonacular.get_recipe()['sourceName']
        nameRecipe = spoonacular.get_recipe()['nameRecipe']
        ingredients = spoonacular.get_recipe()['ingredients']
        prepTime = spoonacular.get_recipe()['prepTime']
        url = spoonacular.get_recipe()['url']

    return flask.render_template("index.html", tweets=twitter.get_tweet(dish)['tweet'], username=twitter.get_tweet(dish)['username'],
                                 created_at=twitter.get_tweet(dish)['created_at'], recipe=nameRecipe, image=imageRecipe,
                                 ingredients=ingredients, time=prepTime, url=url, sourceName=sourceName,
                                 length=len(ingredients))


app.run(
    port=int(os.getenv('PORT', 8081)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
