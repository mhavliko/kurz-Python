import wget
import pandas
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

postavy = pandas.read_csv('character-deaths.csv', index_col='Name', encoding='utf-8')
sloupce = postavy.columns
print(sloupce)
hali_death = postavy.loc[['Hali'],['Death Year']]
print(postavy.loc['Gevin Harlaw': 'Gillam'])
print(postavy.loc['Gevin Harlaw':'Gillam','Death Year'])
print(postavy.loc['Gevin Harlaw':'Gillam','GoT':'DwD'])