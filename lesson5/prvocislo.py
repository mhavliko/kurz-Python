cislo = int(input("zadej cele cislo: "))
prvocislo = True
for i in range(2,cislo):
  if cislo%i ==0:
    print("zadane cislo neni prvocislo")
    prvocislo = False
    break

if prvocislo:
  print("zadane cislo je prvocislo")