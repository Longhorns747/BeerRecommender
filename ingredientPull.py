import urllib2
import csv
import json

baseUrl = 'http://api.brewerydb.com/v2/ingredients?key=ec5e49c0708c445bab360c5cf5a37a62'
response = urllib2.urlopen(baseUrl).read()

jsonResponse = json.loads(response)
dataFile = open('data.csv', 'wb')
missingStyle = 0
missingIngredients = 0
totalPages = jsonResponse["numberOfPages"]
print(totalPages)

for x in range(1, totalPages + 1):
	print(x)
	url = baseUrl + "&p=" + str(x)
	response = urllib2.urlopen(url).read()

	jsonResponse = json.loads(response)
	ingredientJSONData = jsonResponse["data"]

	for ingredient in ingredientJSONData:
		if("name" in ingredient):
			ingredientName = ingredient["name"]

			with open("ingredients.csv", "a") as myfile:
				myfile.write(ingredientName + ",")