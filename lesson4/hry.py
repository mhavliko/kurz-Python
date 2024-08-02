hry = [
  ["Ňadro na ňadru na nádru", 180],
  ["Útok plyšových krokodýlů", 95],
  ["Cesta do říše zelí", 128],
  ["Romance na zdymadle", 144],
  ["Zátiší s mimozemšťanem", 135],
  ["Čtyři facky a dortík", 100],
  ["Motorová okurka", 165],
  ["Johnny Noir", 140],
  ["Pražská kavárna vrací úder", 130],
  ["Pět sester ve vratech", 111],
  ["Stařec a krajta", 187],
  ["Růžová nemoc", 210],
  ["Smrt v přímém přenosu", 265],
]

for hra in hry:
  if hra[1]>120:
    hodin = hra[1]//60
    minut = hra[1]%60
    if minut !=0:
      print (f'{hra[0]} - trvani {hodin} hod a {minut} min ')
    else:
      print (f'{hra[0]} - trvani {hodin} hod')