import requests
import datetime

api_key = "ch923770114252378354871662131257"

url = "http://partners.api.skyscanner.net/apiservices/pricing/v1.0"

headers = {
   "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
   "X-Forwarded-For": "client1",
   "Accept": "application/json"
}

parameters = {
    "country": "KR",
    "currency": "USD",
    "locale": "kr-KO",
    "originplace": "ICN",
    "destinationplace": "PUS",
    "outbounddate": "2017-05-05",
    "adults": 1,
    "locationschema": "Iata",
    "apiKey": api_key,
}

api_data = requests.post(url, headers=headers, data=parameters)

print api_data.status_code
print api_data.text
print api_data.headers




# The following snippet DOES work

#import requests
#import datetime


#tomorrow = datetime.date.today() + datetime.timedelta(days=1)

#api_key = "ch945078126210363693834878936219"

#url = "http://api.skyscanner.net/apiservices/pricing/v1.0/"

#headers = {
#   "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
#   "Accept": "application/json"
#}

#payload = {
#    "apiKey": api_key,
#    "country": "DE",
#    "currency": "EUR",
#    "locale": "en-US",
#    "originplace": "BRU",
#    "destinationplace": "MAD",
#    "outbounddate": str(tomorrow),
#    "adults": 1,
#    "locationschema": "Iata",
#
#}

#r = requests.post(url, headers=headers, data=payload)

#print r.status_code
#print r.text
#print r.headers
