import requests
import json

lat = 48.724114
lon = 2.259434
alt = 100
passes = 2
baseurl = "http://api.open-notify.org/iss-pass.json"
query = "lat=" + str(lat) + "&lon=" + str(lon) + "&alt=" + str(alt) + "&n=" + str(passes)


req = requests.get(baseurl, params=query)
dldata = req.text
#print(dldata)

data = json.loads(dldata)

response = data['response']
print(response)
