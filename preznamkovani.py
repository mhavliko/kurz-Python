with open('preznamkovani.txt', encoding='utf-8') as f:
  lines = f.readlines()

preznamkovani = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'F'}

znamky_zaku = [line.replace('\n', '').split('\t') for line in lines]
nove_znamky_zaku = [[preznamkovani[znamka] if znamka in preznamkovani else znamka for znamka in znamky]for znamky in znamky_zaku]
vysledek = [('\t'.join(znamka for znamka in znamky) +'\n') for znamky in nove_znamky_zaku]

with open ('preznamkovano.txt', mode= 'w', encoding='utf-8') as vystup:
  vystup.writelines(vysledek)



