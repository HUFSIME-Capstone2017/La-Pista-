import json
import requests

api_key = "AIzaSyAMQ-x96aS6dyp_Txngu7SJZhELW2c7SDM"
url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
headers = {'content-type': 'application/json'}

dep = ["ICN", "FCO", "LHR", "MAD", "CDG"]

arr = ["ICN", "FCO", "LHR", "MAD", "CDG"]


for i in range(1,16):
    for a in dep:
        for b in arr:
            if a != b:
                if i < 10:
                    params = {
                        "request": {
                            "slice": [
                                {
                                    "origin": a,
                                    "destination": b,
                                    "date": "2017-05-" + "0" + str(i),
                                    "maxStops": 1,
                                    "maxConnectionDuration": 3000,
                                }
                            ],
                            "passengers": {
                                "adultCount": 1,
                                "childCount": 0,
                            },
                            "solutions": 1,
                            "refundable": False,
                            "saleCountry": "US",
                        }
                    }
                    response = requests.post(url, data=json.dumps(params), headers=headers)
                    data = response.json()
                    price = data["trips"]["tripOption"][0]["saleTotal"]
                    print(a + " " + b + " " + "0" + str(i) + " " + price)

                else:
                    params = {
                        "request": {
                            "slice": [
                                {
                                    "origin": a,
                                    "destination": b,
                                    "date": "2017-05-" + str(i),
                                    "maxStops": 1,
                                    "maxConnectionDuration": 3000,
                                }
                            ],
                            "passengers": {
                                "adultCount": 1,
                                "childCount": 0,
                            },
                            "solutions": 1,
                            "refundable": False,
                            "saleCountry": "US",
                        }
                    }
                    response = requests.post(url, data=json.dumps(params), headers=headers)
                    data = response.json()
                    price = data["trips"]["tripOption"][0]["saleTotal"]
                    print(a+" "+b+" "+str(i)+" "+price)