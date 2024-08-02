import openpyxl
import wget
import pandas
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

#funkce nacte csv soubor z daneho mesta do dataframe a prida sloupec z informaci o tomto meste
def nacti_mesto(mesto):
  data = pandas.read_csv(f'zam_{mesto}.csv', encoding='utf-8')
  data['mesto'] = mesto
  return data

praha = nacti_mesto('praha')
plzen = nacti_mesto('plzeň')
liberec = nacti_mesto('liberec')

zamestnanci = pandas.concat([praha, plzen, liberec],ignore_index=True)
platy = pandas.read_csv('platy_2021_02.csv',encoding='utf-8')

zamestnanci_platy = pandas.merge(zamestnanci, platy, on=['cislo_zamestnance'])
print(zamestnanci.shape)
print(zamestnanci_platy.shape)

print(zamestnanci_platy[['mesto','plat']].groupby('mesto').mean())

zamestnanci_platy_all = pandas.merge(zamestnanci, platy, how='outer' ,on=['cislo_zamestnance'])
byvali_zamestnanci = zamestnanci_platy_all.loc[zamestnanci_platy_all['plat'].isnull()]
print(f'{len(byvali_zamestnanci)} zamestancu jiz pro firmu nepracuje.')

byvali_zamestnanci.to_csv('byvali_zamestnanci.csv')

vykazy = pandas.read_csv('vykazy.csv', encoding='utf-8')
print(vykazy.groupby('project').sum()['hours'])

vykazy = vykazy.rename(columns={'emloyee_id': 'cislo_zamestnance'})

kancelare_vykazy = pandas.merge(vykazy, zamestnanci_platy_all, on='cislo_zamestnance')

print(kancelare_vykazy.groupby('mesto').sum()[['hours']])
print(kancelare_vykazy.groupby(['mesto','project']).sum()[['hours']])

kancelare_vykazy.to_excel('kancelare_vykazy.xlsx')
test = pandas.read_excel('kancelare_vykazy.xlsx')
print(test.head())