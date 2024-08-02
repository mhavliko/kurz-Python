x = 'velbloudHoniHada'

vysledek= []
for znak in x:
  if znak.islower():
    vysledek.append(znak)
  else:
    vysledek.append('_')
    vysledek.append(znak.lower())
print(vysledek)

vysledek = ''.join(vysledek)
print(vysledek)