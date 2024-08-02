import calendar

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#pocty dni na jednotlive radky
vysledek = '\n'.join(str(pocet) for pocet in pocty_dni)

months_dnum = [[calendar.month_name[i], str(pocty_dni[i-1])] for i in range(1,13)]
print(months_dnum)

# mesic a pocet dni na jednom radku oddelene tabulatorem
vysledek = [('\t'.join(month_num) + '\n') for month_num in months_dnum]
vysledek.insert(0, 'Mesic\tPocet dni\n')
print(vysledek)

with open ('dny.txt', mode='w', encoding='utf-8') as vystup:
  vystup.writelines(vysledek)