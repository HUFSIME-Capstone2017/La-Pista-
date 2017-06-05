import json
import requests

api_key = "AIzaSyAMQ-x96aS6dyp_Txngu7SJZhELW2c7SDM"
url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
headers = {'content-type': 'application/json'}

params = {
  "request": {
    "slice": [
      {
        "origin": "ICN",
        "destination": "FCO",
        "date": "2017-08-19",
        "maxStops": 2,
        "maxConnectionDuration": 1200,
      }
    ],
    "passengers": {
      "adultCount": 1,
      "childCount": 0,
    },
    "solutions": 10,
    "refundable": False,
    "saleCountry": "US",
  }
}

response = requests.post(url, data=json.dumps(params), headers=headers)
data = response.json()
#print data

a = data['trips']['tripOption'][0]['slice'][0]['segment'][0].get('connectionDuration', 'bar')
print(a)