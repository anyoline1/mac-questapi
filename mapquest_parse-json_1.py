import urllib.parse
import requests

url = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Roma, Italy"
dest = "Frascati, Italy"
key = "nGxZiSfV2snH1320hSDRrEETHTbTcmC4"

url = url + urllib.parse.urlencode ({"key" :key, "from" :orig, "to" :dest})
json_data = requests.get(url).json()
print(json_data)

