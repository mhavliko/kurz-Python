seznam = [0.5, 2.5, 4]
# Napište cyklus, který projde zadaný seznam desetinných čísel a spočítá jejich průměr. Seznam čísel si vytvořte na začátku programu.
# Napište cyklus, který projde zadaný seznam celých čísel a najde v něm největší hodnotu.

soucet1 = sum(seznam)
print (soucet1)

soucet = 0
pocet = 0
for cislo in seznam:
  soucet += cislo
  pocet += 1

prumer = soucet/pocet
print (str(soucet) + str(pocet) + " => prumer je: "  + str(prumer))

hodnota = seznam[0]
for cislo in seznam:
  if cislo > hodnota:
    hodnota = cislo
print (hodnota)
