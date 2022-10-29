googleapikey = 'API_KEY_HERE'

import requests

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=38.926371%2C-77.035854&radius=1500&type=movie_theater&key=" + googleapikey

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
#the results of the call should be stored in data variable now

print(response.text)