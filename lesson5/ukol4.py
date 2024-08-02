import sys
import random
import string
import math

try:
  if sys.argv[1] == "help":
    print("Strucne instrukce pro vytvoreni registrace:\nProgram si od tebe postupne vyzada osobni udaje (jmeno, prijmeni, datum narozeni) a vytvori ti uzivatelske jmeno. Nasledne se te prepta na tve preference ohledne hesla, ktere ti pote bude vygenerovano. Detailnejsi instrukce pro zadani techto preferenci ti budou sdeleny v prubehu programu")
except IndexError:
  pass

def kontrola(fraze1, fraze2, poradi = 0):
  for fraze in fraze2:
    if poradi == 0:
      if fraze1 in fraze:
        return True
    else:
      if fraze in fraze1:
        return True

print("Pro registraci zadej sve osobni udaje.")
jmeno = input("Krestni jmeno: ")
prijmeni= input("Prijmeni: ")
narozeni = input("Datum narozeni ve formatu dd.mm.rrrr: ")

try:
  uzivatel = jmeno[0] + prijmeni[:7]
except IndexError:
  print("Jmeno a prijmeni jsou povinna pole a musi byt vyplnena.")
  exit()
try:
  den, mesic, rok = narozeni.split(".")
except ValueError:
  print("Datum narozeni je potreba zadat ve formatu dd.mm.rrrr")
  exit()
bydliste = input("zadej misto sveho bydliste (pouze mesto): ")
print()

try:
  delkaHesla = int(input("Nyni si zvol pozadovany pocet znaku hesla (minimalne 8 znaku): "))
  if delkaHesla < 8:
    raise ValueError
except ValueError:
  print("Zvolena delka neni dostatecna, heslo bude vygenerovano v delce 8 znaku.")
  delkaHesla = 8
fraze = input("Pro lepsi zapamatovani hesla si muzes zvolit slovo nebo frazi, ktere bude tve heslo obsahovat. Fraze vsak nesmi byt delsi nez polovina delky hesla, kratsi nez 4 znaky a nesmi obsahovat nic z tvych osobnich udaju: ")

zakazaneFraze = [jmeno, prijmeni, bydliste, den + mesic, den, mesic, rok]

podminka1 = True 
podminka2 = False
podminka3 = False

while podminka1 or podminka2 or podminka3:  
  if fraze == "":
    break
  if  4 <= len(fraze) <= math.ceil(delkaHesla/2):
    podminka1 = False
  else:
    podminka1 = True
    print ("Fraze nema pozadovanou delku.")
    
  if not podminka1:  
    podminka2 = kontrola(fraze, zakazaneFraze)
    podminka3 = kontrola(fraze, zakazaneFraze, 1)
  else:
    podminka2 = False
    podminka3 = False 
  if podminka2 or podminka3:
    print ("Fraze nesmi obsahovat nic z tvych osobnich udaju.")
  if podminka1 or podminka2 or podminka3:
    fraze = input("Zadej novou frazi nebo nech pole prazdne: ")

print("\nHeslo dale musi obsahovat tri z nasledujicich moznosti:\n 1) alespon jeden specialni znak\n 2) alespon jednu cislici\n 3) alespon jedno velke pismeno\n 4) alespon jedno male pismeno")

vyber = input("Zadej nyni, ktere dve varianty (nebo i vice) si prejes pouzit. (Napr. pro vyuziti prvni a treti moznosti, tedy jeden specialni znak a jedno velke pismeno, zadej '1,3'): ")
if str(1) in vyber:
  print (f"Muzes si zvolit znak, ktery znak ma byt v hesle pouzit. Vybirat muzes z nasledujicih: {string.punctuation}..Pokud znak vybirat nechces, nech pole prazdne a pokracuj.")
  print ("Zadej tvuj vybrany znak:")
  znakVyber = input()

znaky = {1:string.punctuation, 2:string.digits, 3:string.ascii_uppercase,4:string.ascii_lowercase}

heslo = []
for znak in znaky:
  if str(znak) in vyber:
    heslo.append(random.choice(znaky[znak]))

delka = len(fraze) + len(heslo)
if fraze!="":
  heslo.append(fraze)
try:
  if znakVyber!="":
    heslo[0] = znakVyber
except NameError:
  pass

for i in range(delkaHesla - delka):
  heslo.append(random.choice(string.ascii_lowercase + string.punctuation + string.ascii_uppercase))

random.shuffle(heslo)
vysledneHeslo = ("")
for znak in heslo:
  vysledneHeslo += znak
print (f"Nasledujici udaje si peclive zapis, budes je potrebovat pri kazdem prihlaseni:\n uzivatelske jmeno: {uzivatel}\n heslo: {vysledneHeslo}")






