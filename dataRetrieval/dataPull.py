import urllib2
import csv
import json

baseUrl = 'http://api.brewerydb.com/v2/beers?key=ec5e49c0708c445bab360c5cf5a37a62'
response = urllib2.urlopen(baseUrl).read()

jsonResponse = json.loads(response)
dataFile = open('data.csv', 'wb')
missingStyle = 0
missingIngredients = 0
totalPages = jsonResponse["numberOfPages"]
print(totalPages)

for x in range(1, totalPages):
	print(x)
	url = baseUrl + "&p=" + str(x)
	response = urllib2.urlopen(url).read()

	jsonResponse = json.loads(response)
	beerJsonData = jsonResponse["data"]

	for beer in beerJsonData:

		if("name" in beer):
			beerName = beer["name"]
			beerId = beer["id"]
			beerStyle = ""

			if("style" in beer and "name" in beer["style"]):
				beerStyle = beer["style"]["name"]
			else:
				missingStyle += 1
				continue

			ingredientsURL = 'http://api.brewerydb.com/v2/beer/' + beerId + '/ingredients?key=ec5e49c0708c445bab360c5cf5a37a62'
			ingredientsResponse = urllib2.urlopen(ingredientsURL).read()
			ingredientsJSON = json.loads(ingredientsResponse)
			ingredients = []

			if("data" in ingredientsJSON):
				ingredientsData = ingredientsJSON["data"]

				for ingredient in ingredientsData:
					ingredients.append(ingredient["name"].encode('utf-8'))
			else:
				missingIngredients += 1
				continue

			ingredients.append(beerStyle.encode('utf-8'))
			wr = csv.writer(dataFile, quoting=csv.QUOTE_ALL)
			wr.writerow(ingredients[:5])

print("Total Beers: " + str(len(jsonData)))
print("missingIngredients: " + str(missingIngredients))
print("missingStyle: " + str(missingStyle))
dataFile.close()