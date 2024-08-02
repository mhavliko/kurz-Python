import pandas
studenti1= pandas.read_csv('studenti1.csv',encoding='utf-8')
studenti2= pandas.read_csv('studenti2.csv',encoding='utf-8')
studenti=pandas.concat([studenti1, studenti2])
print(len(studenti[studenti['ročník'].isnull()]))
print(len(studenti[studenti['kruh'].isnull()]))
print(len(studenti[(studenti['kruh'].isnull()) & (studenti['ročník'].isnull())]))
print(len(studenti))
prezencni_studenti = studenti.dropna()
print(len(prezencni_studenti))
obory = prezencni_studenti[['jméno','příjmení','obor','prospěch']].groupby('obor')
print(obory.count())
print(obory.mean())

jmena = pandas.read_csv('jmena100.csv',index_col='jméno', encoding='utf-8')
spojena_tabulka = pandas.merge(prezencni_studenti, jmena['pohlaví'], on=['jméno'])
print(spojena_tabulka)
print(spojena_tabulka.groupby('pohlaví').count()['jméno'])

import math
def gmean(rada, y=1):
  for x in range(len(rada)):
    y = rada[x] * y
  return math.sqrt(y)

GP = gmean([1, 2, 3, 4, 5])

print(GP)
