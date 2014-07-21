from urllib2 import Request, urlopen
import json
from random import randrange

from flask import Flask, render_template, request

from settings import NUM_INGREDIENT_LISTS, NUM_INGREDIENTS, API_KEY, PROJECT


app = Flask(__name__)


# TODO: Probably wanna add some exception handling in general
@app.route('/')
def bartenderPage():
    ingredient_list = open("data/ingredients.csv", 'r').read().split(';')

    ingredients = []
    for _ in xrange(NUM_INGREDIENT_LISTS):
        ingredients.append([ingredient_list.pop(randrange(len(ingredient_list))) for _ in xrange(NUM_INGREDIENTS)])

    ingredients = {'ing{0}'.format(index): sublist for index, sublist in enumerate(ingredients, start=1)}
    return render_template('bartender.html', **ingredients)


@app.route('/recommend', methods=['POST'])
def recommend_beer():
    return render_template('result.html', result=_parse_response(_send_ingredients(request)))


def _generate_data(request):
    return str.encode(json.dumps({
        "Id": "score00001",
        "Instance": {
            "FeatureVector": {
                "Ing1": request.form['ing1'],
                "Ing2": request.form['ing2'],
                "Ing3": request.form['ing3'],
                "Ing4": request.form['ing4'],
                "Style": "0",
            },
            "GlobalParameters": {
            }
        }
    }))


def _send_ingredients(request):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(API_KEY)}
    req = Request(PROJECT, data=_generate_data(request), headers=headers)
    return urlopen(req).read()


def _parse_response(result):
    # Grab only the recommended beer from the response. (+2 to exclude leading ',"' and -2 to exclude trailing ']"')
    return result[result.rindex(',') + 2:-2]


if __name__ == '__main__':
    app.run()