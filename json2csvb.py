from urllib.request import urlopen
import json
import csv


def getRows(data):
	return []


url = "https://hd1-units.herokuapp.com/covid?days=0&suffix=json"
data = urlopen(url).read()
data = json.loads(data)
fname = "coronareport.csv"


with open(fname, mode='w') as outputfile:
	csvoutput = csv.writer(outputfile)
	for key ,value in data.items():
		csvoutput.writerow([key,value])