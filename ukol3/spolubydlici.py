purchaseList = [
  {"person": "Petr", "item": "Prací prášek", "value": 399},
  {"person": "Ondra", "item": "Savo", "value": 80},
  {"person": "Petr", "item": "Toaletní papír", "value": 65},
  {"person": "Libor", "item": "Pivo", "value": 124},
  {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
  {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
  {"person": "Ondra", "item": "Toaletní papír", "value": 120},
  {"person": "Míša", "item": "Pečící papír", "value": 30},
  {"person": "Zuzka", "item": "Savo", "value": 80},
  {"person": "Pavla", "item": "Máslo", "value": 50},
  {"person": "Ondra", "item": "Káva", "value": 300}
]
sum_per_person = {}
for item in purchaseList:
  person = item["person"]
  value = item["value"]
  if person in sum_per_person:
    sum_per_person[person] += value
  else:
    sum_per_person[person] = value

total_value = 0
for person, value in sum_per_person.items():
  total_value += value
  print(f"{person} utratil(a) za společné nákupy {value} Kč.")

average_value = total_value / len(sum_per_person)
print(f"Průměrná hodnota na osobu je {round(average_value)} Kč.")

for person, value in sum_per_person.items():
  if value - average_value >= 0:
    dif = "preplatek"
  else:
    dif = "doplatek"
  print (f'{person} - {dif} {round(abs(value - average_value))} Kc')