
from requests_html import HTML
with open('dhmo/index.html', encoding='utf-8') as soubor:
  obsah = soubor.read()
html = HTML(html=obsah)

#for odstavec in html.find('p'):
  #print(odstavec.text)

html.find('.sekce1')
for odkaz in html.find('a'):
  print(odkaz.attrs['href'])

html.find('h1, h2')
html.find('ol[type="a"]')
html.find('.sekce1 p')
html.find('.sekce1 > p')
html.find('ol[type="a"] li')

from requests_html import HTMLSession
session = HTMLSession()
stranka = session.get('https://apps.kodim.cz/python-data/scrape')
for odstavec in stranka.html.find('p'):
  print(odstavec.text)
#print(stranka.html.html)

dhmo = HTMLSession()
zdroj_dhmo= dhmo.get('https://apps.kodim.cz/python-data/dhmo')
for nadpis in zdroj_dhmo.html.find('h2'):
  print(nadpis.text)
for odkaz in zdroj_dhmo.html.find('a'):
  print(odkaz.attrs['href'])
for obrazek in zdroj_dhmo.html.find('img'):
  print(obrazek.attrs['src'])

kodim = HTMLSession()
session = kodim.get('https://kodim.cz/czechitas/python-data/zaklady-programovani/prvni-programy')

for cviceni in session.html.find('section[id="doporucene-ulozky-na-doma"] h3, section[id="doporucene-ulozky-na-doma"] .demand-text'):
  print(cviceni.text)


