import pandas
jmena = pandas.read_csv('jmena100.csv', encoding='utf-8')
print(jmena[jmena['vek']>60])
print(jmena[(jmena['četnost']>80000) & (jmena['četnost']<100000)])
cetnost = jmena[(jmena['četnost']>80000) & (jmena['četnost']<100000)]
print(cetnost['jmeno'])
slovansky_hebrejsky = jmena[(jmena['původ']=='slovanský') | (jmena['původ']=='hebrejský')]
print(slovansky_hebrejsky[['jmeno','četnost']])
slovansky_hebrejsky.info()
svatek_do_7unora = jmena[jmena['svátek'].isin(['1.2','2.2','3.2','4.2','6.2','7.2','7.2'])]
print(svatek_do_7unora['jmeno'])
