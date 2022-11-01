import requests

placesapikey = ''

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=38.926371%2C-77.035854&radius=1500&type=movie_theater&key=" + placesapikey

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()

print(response.text)

mapsapikey = ''

urlmap = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:ChIJteUORR_It4kRVXponJBr4BM&destination=place_id:ChIJQcMN5SDIt4kRZZq8cQVIjU0&key=" + mapsapikey

payload={}
headers = {}

response = requests.request("GET", urlmap, headers=headers, data=payload)

directions = response.json()

data2 = response.json()

print(response.text)
