from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def bartenderPage():
    f = open("data/ingredients.csv", 'r')
    ingFile = f.read()
    ingredientList = ingFile.split(';')
    ingredients = []

    for x in range(0,8):
        from random import randint
        idx = randint(0, len(ingredientList) - 1)
        ingredients.append(ingredientList[idx])

    return render_template('bartender.html', ingredients=ingredients)

if __name__ == '__main__':
    app.run(debug=True)