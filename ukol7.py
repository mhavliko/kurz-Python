import requests
import json

#funkce vrati json str data stazena z API
def stahniApi(url):
  response = requests.get(url)
  return response.json()

#funkce ulozi json data do json souboru naformatovane
def ulozFormat(soubor,data):
  with open(soubor, mode='w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

#funkce vrati data z json souboru jako slovnik
def nactiJson(soubor):
  with open(soubor,mode='r', encoding= 'utf-8') as f:
    return json.load(f)

#funkce vrati pocet ruznych hodnot daneho klice
def pocetHodnot(data,klic):
  hodnoty = [postava[klic] for postava in data]
  hodnoty = set(hodnoty)
  return len(hodnoty)

#funkce vytahne z dat (ze seznamu slovniku) pouze data (slovniky) s danou hodnotou pro dany klic
def filtruj(data, klic, hodnota):
  return [postava for postava in data if postava[klic] == hodnota]

#funkce vrati ze seznamu slovniku hodnotu daneho klice pro slovnik s nejvyssi hodnotou porovnavaneho klice
def vyhledejNejvyssi(data,vyslednyKlic, porovnavanyKlic):
  vysledek = 0
  for postava in data:
    try:
      if postava[porovnavanyKlic] > vysledek:
        vysledek = postava[porovnavanyKlic]
        nejvyssi = postava[vyslednyKlic]
    except TypeError:
      pass
  return nejvyssi

ulozFormat('hp_characters.json',stahniApi('http://hp-api.herokuapp.com/api/characters'))
postavy = nactiJson('hp_characters.json')
klic = "patronus"
print(f'Celkem existuje {pocetHodnot(postavy,klic)} patronu.')
print(f'{len(filtruj(postavy, "alive", False))} postav jiz neni nazivu.')
ulozFormat("gryffindor.json", filtruj(postavy, "house", "Gryffindor"))
print(f'Nejstarsi postavou je {vyhledejNejvyssi(postavy, "name", "yearOfBirth")}.')