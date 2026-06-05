import urllib.request
import json
 
url1 = "https://api.weather.gov/points/40.1934,-85.3864"
 
with urllib.request.urlopen(url1) as r:
    data1 = json.loads(r.read().decode())
 
url2 = data1["properties"]["forecast"]
 
with urllib.request.urlopen(url2) as r:
    data2 = json.loads(r.read().decode())
 
periods = data2["properties"]["periods"]
 
for period in periods:
    print(period["name"])
    print(str(period["temperature"]) + "F")
    print(period["detailedForecast"])
    print()
