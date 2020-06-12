from urllib2 import urlopen
import json
import csv

def getRows(data):
	return []

url = "https://hd1-units.herokuapp.com/covid?days=0&suffix=json"
data = urllib2.urlopen('url').read()
data = json.loads(data)

fname = "coronacountry.csv"
with open(fname, 'wb') as outputfile:
	csvoutput = csv.writer(outputfile)
	csvoutput.writerows(getRows(data))

