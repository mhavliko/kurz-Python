vysvedceni = {"matematika":1, "cestina":3, "zemepis":1}
print(vysvedceni.values())
print(list(vysvedceni.keys()))
print(vysvedceni)

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales ["nova"] = 0
sales ["Zkus mě chytit"] +=100
print(sales)

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
listek = int(input("Zadej cislo tveho listku:"))

if listek not in tombola:
  print("Bohužel nevyhráváš nic.")
else:
  print(tombola[listek])
  tombola.pop(listek)

print(tombola)




