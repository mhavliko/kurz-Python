import sys

desserts = [["trubicka",40],["dort",20],["kremrole", 50]]
drinks = [["kava",30],["cappucino", 50],["voda", 20]]

if sys.argv[1] == "help":
  print ("Nabidka zakusku:")
  for dessert in desserts:
     print (f'{dessert[0]} - {dessert[1]} Kc')
  print()
  print ("Nabidka napoju (cena za maly/velky napoj):")
  for drink in drinks:
    print (f'{drink[0]} - {drink[1]}/{int(int(drink[1])*1.5)} Kc')
  exit()
else:
  noPeople, tip, toGo = sys.argv[3:]
  drinkSize = sys.argv[2].split("-")

  prizeFood = [dessert[1] for dessert in desserts if dessert[0] == sys.argv[1]]
  prizeDrink = [drink[1] for drink in drinks if drink[0] == drinkSize[0]]
  prizeFood = int(prizeFood[0])
  prizeDrink = int(prizeDrink[0])
  if drinkSize[1] == "big":
    prizeDrink = int(prizeDrink * 1.5)

  cena = (int(noPeople) * (prizeFood + int(toGo) * 10 + prizeDrink))
  cena += int(tip) * 0.1 * cena
  
  print(f"Objednali jste si {noPeople}x {sys.argv[1]} a {sys.argv[2]}.")
  print(f"Cena je {int(round(cena))} korun.")