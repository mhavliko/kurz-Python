from datetime import date
from unidecode import unidecode
import json

#funkce vrati vek ze zadaneho rodneho cisla
def vek_z_rc(rc):
  return(date.today().year-int('19' + rc[0] + rc[1]))

#funkce vrati pohlavi ze zadaneho rodneho cisla
def pohlavi_z_rc(rc):
  if int(rc[2]) in{5,6}:
    return('zena')
  else:
    return('muz')

#funkce vrati email ze zadaneho jmena, prijmeni a domeny
def email(jmeno, prijmeni, domena):
  return(f'{unidecode(prijmeni[:5])}{unidecode(jmeno[:3])}@{domena}')

with open('studenti.txt', encoding='utf-8') as f:
  radky = f.readlines()

seznam_radku=[student.split('\t') for student in radky]
studenti = [[hodnota.replace('\n','') for hodnota in student] for student in seznam_radku]

for student in studenti:
  try:
    student.append(vek_z_rc(student[-1]))
    student.append(pohlavi_z_rc(student[-2]))
    student.append(email(student[0],student[1],'hybrid.edu'))
  except ValueError:
    pass

studenti[0].append('vek')
studenti[0].append('pohlavi')
studenti[0].append('email')

keys = studenti[0]
studenti_slovnik = [{k:v for k,v in zip(keys, i)} for i in studenti[1:] ]

with open('studenti.json', mode='w', encoding='utf-8') as f:
  json.dump(studenti_slovnik,f)

print(studenti_slovnik)
 
