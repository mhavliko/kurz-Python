import random
tajneCislo = random.randint(0,10)

cislo = int(input("uhodni cislo: "))
while cislo != tajneCislo:
  if cislo > tajneCislo:
    print("zadane cislo je vetsi nez tajne cislo")
  else:
    print("zadane cislo je mensi nez tajne cislo")
  cislo = int(input("hadej znovu: "))

print(f"Bingo, uhodl jsi, tajne cislo je {cislo}.")
