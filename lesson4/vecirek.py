passwords = {"Jiri": "tajne-heslo", "Natalie": "jeste-tajnejsi-heslo", "Klara": "nejtajnejsi-heslo"}
#Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl, že každý z hostů bude mít speciální heslo, které je platné jen pro něj. Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. Hostu na seznamu, který zadá správné heslo, vypíše program text: "Smíš vstoupit."

jmeno = input("zadej jmeno: ")
if jmeno in passwords:
  heslo = input("zadej heslo: ")
  if heslo ==  passwords[jmeno]:
    print("smis vstoupit")