from calendar import calendar, day_name


import calendar

den = int(input('Zadejte den: '))
mesic = int(input('Zadejte mesic: '))
rok = int(input('Zadejte rok: '))
denVTydnu = calendar.weekday(rok,mesic,den)
print(f'{den}-{mesic}-{rok} was {calendar.day_name[denVTydnu]}')


