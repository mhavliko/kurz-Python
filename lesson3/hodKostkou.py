import random
import sys

pocetHodu = int(sys.argv[1])

hody = [random.randint(1,12) for i in range(pocetHodu)]
print(hody)

vysledek = ', '.join(str(hod) for hod in hody)

print(vysledek)

with open('hody.txt', mode='w', encoding='utf-8') as vystup:
  vystup.writelines(vysledek)
