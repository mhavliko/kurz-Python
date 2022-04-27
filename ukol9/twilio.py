import wget
import pandas as pd
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

akcie = pd.read_csv('twlo.csv',index_col=0, encoding='utf-8')
print(akcie.shape)
pocet_radku = akcie.shape[0]
print(akcie.iloc[:5])
print(akcie.head())
print(akcie.tail(1))
print(f'Pocet radku = {pocet_radku}')
print(type(pocet_radku))

prvni_cena = akcie.iloc[0][4]
posledni_cena = akcie.iloc[-1][4]
print(f'Cena akcie vzrostla o {round(posledni_cena/prvni_cena*100)} %.')

maximalni_cena = akcie.loc[:,'High'].max()
minimalni_cena = akcie.loc[:,'Low'].min()
price_range = maximalni_cena-minimalni_cena
print(f'Price range = {price_range}')
