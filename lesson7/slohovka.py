with open('slohovka.txt', encoding='utf-8') as f:
  radky = f.readlines()

slova = [radek.split(' ') for radek in radky]

pocetSlov = 0
for radek in slova:
  try:
    radek.remove('\n')
  except ValueError:
    pass
  pocetSlov += len(radek)
   
print(pocetSlov)
print(slova)
