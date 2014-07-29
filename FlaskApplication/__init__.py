from urllib2 import Request, urlopen
import json
from random import randrange

from flask import Flask, render_template, request, abort

from settings import NUM_INGREDIENT_LISTS, NUM_INGREDIENTS, API_KEY, PROJECT


app = Flask(__name__)


@app.route('/')
def bartenderPage():
    try:
        with open("FlaskApplication/data/ingredients.csv", 'r') as f:
            ingredient_list = f.read().split(';')
            if not ingredient_list:
                raise EOFError
        ingredients = []
        # Generate the ingredients list to be displayed
        for _ in xrange(NUM_INGREDIENT_LISTS):
            ingredients.append([ingredient_list.pop(randrange(len(ingredient_list))) for _ in xrange(NUM_INGREDIENTS)])

        # Magic to generate kwarg dict
        ingredients = {'ing{0}'.format(index): sublist for index, sublist in enumerate(ingredients, start=1)}
        return render_template('bartender.html', **ingredients)
    except (IOError, EOFError):
        #TODO: add custom page for errors
        abort(500)


@app.route('/recommend', methods=['POST'])
def recommend_beer():
    #TODO: deal with possible exceptions
    return render_template('result.html', result=_parse_response(_send_ingredients(request)))


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/about')
def about():
    return render_template('about.html')


def _generate_data(request):
    #TODO: Find out what exceptions can occur here
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
    #TODO: Find out what exceptions can occur here
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(API_KEY)}
    req = Request(PROJECT, data=_generate_data(request), headers=headers)
    return urlopen(req).read()


def _parse_response(result):
    #TODO: exception handling
    # Grab only the recommended beer from the response. (+2 to exclude leading ',"' and -2 to exclude trailing ']"')
    return result[result.rindex(',') + 2:-2]


if __name__ == '__main__':
    app.run(debug="true")