import calendar

file = open('mereni.txt', encoding='utf-8')
lines = file.readlines()
file.close()

with open('mereni.txt', encoding='utf-8') as file2:
  lines = file2.readlines()
  
with open('vyplata.txt',encoding='utf-8') as file:
  vykaz = [int(hodiny) for hodiny in file.readlines()]
 
print(vykaz)


hodinovaMzda = int(input('zadej hodinovou mzdu: '))
vyplaty =[hodiny * hodinovaMzda for hodiny in vykaz]

print(f'Vydelek za cely rok cini {sum(vyplaty)}\nPrumerna mesicni vyplata cini {sum(vyplaty)/12}')

print(vyplaty)
proVystup = ''
for i in range(12):
  print(f'{calendar.month_name[i+1]} - {vyplaty[i]} Kc')
  vyplata = f'{calendar.month_name[i+1]}\t{vyplaty[i]}\n'
  proVystup += vyplata

with open('vyplata_Mesice', mode = 'w', encoding = 'utf-8') as vystup:
  vystup.writelines(proVystup)




