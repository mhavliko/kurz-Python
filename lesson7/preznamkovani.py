with open('preznamkovani.txt', encoding='utf-8') as f:
  lines = f.readlines()

preznamkovani = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'F'}

znamky_zaku = [line.replace('\n', '').split('\t') for line in lines]
nove_znamky_zaku = [[preznamkovani[znamka] if znamka in preznamkovani else znamka for znamka in znamky]for znamky in znamky_zaku]
vysledek = [('\t'.join(znamka for znamka in znamky) +'\n') for znamky in nove_znamky_zaku]

with open ('preznamkovano.txt', mode= 'w', encoding='utf-8') as vystup:
  vystup.writelines(vysledek)

#druhe reseni:
with open('preznamkovani.txt', mode='r', encoding='utf-8') as f:
  lines = f.readlines()
 
modified_lines = [lines[0]]
for line in lines[1:]:
    new_line = line.replace('1', 'A') \
                   .replace('2', 'B') \
                   .replace('3', 'C') \
                   .replace('4', 'D') \
                   .replace('5', 'F')
    modified_lines.append(new_line)


#treti reseni:
import csv
 
with open('preznamkovani.txt', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    # nebo reader nize pokud nacitate primo z csv souboru
    # reader = csv.DictReader(f, delimiter=',')
    lines = list(reader)
 
znamky_map = {
    '1' : 'A',
    '2' : 'B',
    '3' : 'C',
    '4' : 'D',
    '5' : 'F',
}
for key in ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5', 'Test 6']:
    for line in lines:
        line[key] = znamky_map[line[key]]

