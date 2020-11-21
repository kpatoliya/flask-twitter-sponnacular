import json
import os
import random
import controller
import requests
from dotenv import load_dotenv

load_dotenv()


def get_recipe():
    dishes = ['French Fries', 'Pasta', 'Caesar Salad', 'Pound Cake', 'Samosa', 'Pizza', 'Tacos',
              'Paneer Tikka']
    dish = dishes[random.randint(0, 7)]
    ingredients = []
    content = requests.get("https://api.spoonacular.com/recipes/complexSearch?query=" + dish
                           + "&apiKey=" + os.getenv('SPOONACULAR_KEY'))
    json_response = json.loads(content.text)
    if len(json_response['results']) == 0:
        content = requests.get("https://api.spoonacular.com/recipes/complexSearch?query="
                               + "&apiKey=" + os.getenv('SPOONACULAR_KEY'))
        json_response = json.loads(content.text)
        dish = ''
    randomRecipe = random.randint(0, len(json_response['results']) - 1)
    idRecipe = str(json_response['results'][randomRecipe]['id'])
    imageRecipe = json_response['results'][randomRecipe]['image']

    recipeInfo = requests.get("https://api.spoonacular.com/recipes/" + idRecipe + "/information?includeNutrition=false"
                                                                                  "&apiKey=" + os.getenv(
        'SPOONACULAR_KEY'))
    json_response2 = json.loads(recipeInfo.text)
    sourceName = json_response2['sourceName']
    nameRecipe = json_response2['title']
    url = json_response2['sourceUrl']
    prepTime = json_response2['readyInMinutes']
    for i in range(0, len(json_response2['extendedIngredients'])):
        ingredients.append(json_response2['extendedIngredients'][i]['original'])
    return {'dish': dish, 'imageRecipe': imageRecipe, 'sourceName': sourceName, 'nameRecipe': nameRecipe, 'url': url,
            'prepTime': prepTime, 'ingredients': ingredients}


def get_random_recipe():
    dish = controller.controller()
    ingredients = []
    content = requests.get("https://api.spoonacular.com/recipes/complexSearch?query=" + dish
                           + "&apiKey=" + os.getenv('SPOONACULAR_KEY'))
    json_response = json.loads(content.text)
    if len(json_response['results']) == 0:
        content = requests.get("https://api.spoonacular.com/recipes/complexSearch?query="
                               + "&apiKey=" + os.getenv('SPOONACULAR_KEY'))
        json_response = json.loads(content.text)
        dish = ''
    randomRecipe = random.randint(0, len(json_response['results']) - 1)
    idRecipe = str(json_response['results'][randomRecipe]['id'])
    imageRecipe = json_response['results'][randomRecipe]['image']

    recipeInfo = requests.get("https://api.spoonacular.com/recipes/" + idRecipe + "/information?includeNutrition=false"
                                                                                  "&apiKey=" + os.getenv(
        'SPOONACULAR_KEY'))
    json_response2 = json.loads(recipeInfo.text)
    sourceName = json_response2['sourceName']
    nameRecipe = json_response2['title']
    url = json_response2['sourceUrl']
    prepTime = json_response2['readyInMinutes']
    for i in range(0, len(json_response2['extendedIngredients'])):
        ingredients.append(json_response2['extendedIngredients'][i]['original'])
    return {'dish': dish, 'imageRecipe': imageRecipe, 'sourceName': sourceName, 'nameRecipe': nameRecipe, 'url': url,
            'prepTime': prepTime, 'ingredients': ingredients}