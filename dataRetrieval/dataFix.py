import csv
with open('beerData.csv', 'rbU') as csvfile:
	reader = csv.reader(csvfile)

	for row in reader:
		newRow = [""] * 5

		if row[4] == '':

			i = 0
			label = row[0]

			while label != "":
				label = row[i]
				i += 1

			label = row[i-2]
			newRow[4] = label

			for x in range(0,4):
				if row[x] != label:
					newRow[x] = row[x]
		else:
			newRow = row

		with open('beerData2.csv', 'ab') as csvfilewrite:
			writer = csv.writer(csvfilewrite, quoting=csv.QUOTE_ALL)
			writer.writerow(newRow)
