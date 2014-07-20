from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def bartenderPage():
    f = open("data/ingredients.csv", 'r')
    ingFile = f.read()
    ingredientList = ingFile.split(';')
    ing1 = []
    ing2 = []
    ing3 = []
    ing4 = []

    for x in range(0,2):
        from random import randint
        idx = randint(0, len(ingredientList) - 1)
        ing1.append(ingredientList[idx])

    for x in range(0,2):
        from random import randint
        idx = randint(0, len(ingredientList) - 1)
        ing2.append(ingredientList[idx])

    for x in range(0,2):
        from random import randint
        idx = randint(0, len(ingredientList) - 1)
        ing3.append(ingredientList[idx])

    for x in range(0,2):
        from random import randint
        idx = randint(0, len(ingredientList) - 1)
        ing4.append(ingredientList[idx])

    return render_template('bartender.html', ing1=ing1, ing2=ing2, ing3=ing3, ing4=ing4)

@app.route('/recommend', methods=['POST'])
def recommend_beer():
    import urllib2
    import json 

    data =  {
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
            }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/76c97bb7c7f640719cd92db28794a965/services/3a865a07cfd94e25b18374d30a41fda7/score'
    api_key = 'X2p6hUG+5fgzfoTSGEDBiGsiYHRBE2ee1atd2fcppVhx9C8vtUUy4EXnjn/qDPeJ5Ty+4EItCf5mXZI8aMxMcQ==' # You can obtain the API key from the publisher of the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib2.Request(url, body, headers) 
    response = urllib2.urlopen(req)
    result = response.read() 
    if result.endswith("]"): result = result[:-1]
    if result.startswith("["): result = result[1:]
    resultList = result.split(",")

    recommendation = resultList[-1][:-1][1:]

    return render_template('result.html', result=recommendation)

if __name__ == '__main__':
    app.run()