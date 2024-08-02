import requests
import json
response = requests.get('http://api.kodim.cz/python-data/people')
data = json.loads(response.text)
data = response.json()
#jsou dve moznosti viz vyse

print(len(data))
informace = data[0].keys()
print (informace)
zeny = [osoba["gender"] for osoba in data if osoba["gender"]=="Female"]
muzi = [osoba["gender"] for osoba in data if osoba["gender"]=="Male"]

print(len(zeny))
print (len (muzi))
