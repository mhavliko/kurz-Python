import wget
import pandas
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")

data = pandas.read_csv('country_vaccinations.csv', encoding='utf-8')
print(data.loc[data['date']=='2021-03-10',['country','total_vaccinations']])
data.loc[(data['date']=='2021-03-10')& (data['total_vaccinations']>1000000)]
data.loc[(data['daily_vaccinations']<100) | (data['daily_vaccinations']>100000)]
data.loc[(data['country'].isin(['United Kingdom', 'Finland', 'Italy']))&(data['date'].isin(['2021-03-10','2021-03-11']))]
data.loc[(data['country']=='Japan')&(data['date']>= '2021-03-03')&(data['date']<= '2021-03-09')]

