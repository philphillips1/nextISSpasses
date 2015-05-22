import requests
import json
import datetime


# you can get lat&lon from wikipedia from the nearest train 
# station or so
lat = 48.724114
lon = 2.259434
# altitude is just BS
alt = 100
# how many future passes, further passes are less precise and can change
passes = 2
baseurl = "http://api.open-notify.org/iss-pass.json"
query = "lat=" + str(lat) + "&lon=" + str(lon) + "&alt=" + str(alt) + "&n=" + str(passes)


req = requests.get(baseurl, params=query)
dldata = req.text
#print(dldata)

data = json.loads(dldata)

response = data['response']
#print(response)

for i in response:
  #print(i)
  duration = i['duration']
  risetime = i['risetime']
  begintime = lambda x:datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S')
  endtime = lambda x, y:datetime.datetime.fromtimestamp(x + y).strftime('%Y-%m-%d %H:%M:%S') 
  print("Station pass starts at: {0} and ends at: {1}".format(begintime(risetime),endtime(risetime, duration)))

