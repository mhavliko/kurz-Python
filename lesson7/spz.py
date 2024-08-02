import sys

soubor = sys.argv[1]
with open(soubor, encoding='utf-8') as f:
  auta = f.readlines()
autaSplitted = []
for auto in auta:
  auto = auto.replace('\n', '')
  autoInfo = auto.split(' ')
  autaSplitted.append(autoInfo)
  

kms = [auto[1] for auto in autaSplitted]

kilometry = []
for km in kms:
  km = km.replace(',','.')
  km = float(km)
  kilometry.append(km)
print(sum(kilometry))