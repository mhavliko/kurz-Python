with open('pasazeri.txt', encoding= 'utf-8') as f:
  dny = f.readlines()

dnyJizdy = [den.replace('\n','').split(' ') for den in dny]

rozdeleneJizdy = [[jizda.split(',') for jizda in jizdy] for jizdy in dnyJizdy]
cisla=[[[int(cislo) for cislo in jizda] for jizda in dny] for dny in rozdeleneJizdy]

print(cisla)

monTam = sum(cislo[0] for cislo in cisla[0])
monZpet = sum(cislo[1] for cislo in cisla[0])
print(monTam)
print(monZpet)

celkemTam = sum(sum(cislo[0] for cislo in jizdy) for jizdy in cisla)
print(celkemTam)