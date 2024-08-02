import requests
import json
import sys
datum = sys.argv[1]
response = requests.get(f'http://svatky.adresa.info/json?date={datum}')
data = response.json()

print(data)
print (data[0]['name'])
print(str(data[0]['date']) + ' - svatek ma ' + data[0]['name'])

day = input('Zadej den ve formatu DD: ')
month = input('Zadej mesic ve formatu MM: ')
def better_get_name(day, month):
    url = f'http://svatky.adresa.info/json?date={day}{month}'
    response = requests.get(url)
    #  pripadne jde i vyuzit params parameter funkce get, ten bere slovnik specifikujici parametry
    # response = requests.get(url, params={'date': day + month})
    return response.json()[0]['name']

print(better_get_name(day, month))


