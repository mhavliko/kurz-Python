import wget
import pandas

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

staty = pandas.read_json('staty.json', encoding='utf_8')
evropske_staty = staty[staty['region']=='Europe']
print(evropske_staty.head())
print(evropske_staty.groupby('subregion').count()['name'])
print(evropske_staty.groupby('subregion').sum()[['population']])

hdp = pandas.read_csv('gdp.csv', encoding= 'utf-8').dropna()
staty= staty.rename(columns={'alpha3Code': 'Country Code'})

staty_hdp = pandas.merge(staty,hdp, on='Country Code')
print(staty_hdp.head())
subregiony = staty_hdp.groupby('subregion').sum()[['population','2019']]
print(subregiony.head())
subregiony['GPD 2019/population'] = subregiony['2019']/subregiony['population']
print(subregiony.head())




