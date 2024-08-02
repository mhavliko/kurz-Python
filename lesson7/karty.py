import random
barvy = ['kary', 'piky', 'krize','srdce']
hodnoty = [2,3,4,5,6,7,8,9,10,'kluk','dama','kral','eso']

barva = random.sample(barvy, 1)
hodnota = random.sample(hodnoty, 1)

karta = barva + hodnota

with open('karty.txt', encoding='utf-8') as f:
  lines = f.readlines()
balicekKaret = [line.replace('\n','') for line in lines]
print(balicekKaret)

karty = []
for i in range(4):
  karta = (random.sample(balicekKaret, 1))
  karty.append(karta)
  balicekKaret.remove(karta[0])

print(karta)
print(karty)
