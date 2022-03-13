plates = {"4A2 3000": "František Novák",
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár",
  "1P5 5269": "Marta Nováková",
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}

print("Osoby s auty registrovanymi v plzenskem kraji:")
for znacka, jmeno in plates.items():
  if znacka[1] == "P":
    print(jmeno)

plzen = [jmeno for znacka, jmeno in plates.items() if znacka[1]=="P"]
print(plzen)

