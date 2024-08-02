import csv
with open('csv.csv', encoding= 'utf-8') as f:
  lines = f.readlines()

line = lines[0]
#print(lines)

with open('testik.csv', mode='w', encoding='utf-8') as vystup:
  vystup.writelines(lines)

with open('csv.csv', newline= '', encoding='utf-8') as file:
  reader = csv.DictReader(file, delimiter=',')
  rows = list(reader)

print (rows)
