
veky = [35, 12, 44, 11, 18, 21, 28, 18]

veky1 = [18-vek for vek in veky]
veky1 = [vek>= 18 for vek in veky]

nazvy = [
  'Někdo to rád horké, extended edition',
  'Adéla ještě nevečeřela',
  'Kulový blesk'
]
delky = [136, 105, 82]
trvani = [(str(delka//60) +":" + str(delka%60)) for delka in delky]

kraje = [
  ['Hlavní město Praha', '1 280 508'],
  ['Jihočeský kraj', '638 782'],
  ['Jihomoravský kraj', '1 178 812'],
  ['Karlovarský kraj', '296 749'],
  ['Kraj Vysočina', '508 952'],
  ['Královéhradecký kraj', '550 804'],
  ['Liberecký kraj', '440 636'],
  ['Moravskoslezský kraj', '1 209 879'],
  ['Olomoucký kraj', '633 925'],
  ['Pardubický kraj', '517 087'],
  ['Plzeňský kraj', '578 629'],
  ['Středočeský kraj', '1 338 982'],
  ['Ústecký kraj', '821 377'],
  ['Zlínský kraj', '583 698']
]

nazvy = [kraj[0]for kraj in kraje]
pocty = [int(kraj[1].replace(" ",""))for kraj in kraje] 

seznam = [nazvy, pocty]

hlasy = [
  [78774, 43179, 225111, 144799, 242854],
  [91062, 22451, 17475, 53391, 46450],
  [179186, 216499, 4493, 156305, 61222],
  [9619, 53476, 926, 64737, 34566],
  [66904, 85730, 27271, 12964, 38041],
  [118755, 1929, 30426, 25178, 31952],
  [64467, 40993, 81181, 39392, 4335],
  [11221, 97970, 26179, 98539, 112578],
  [171064, 7638, 8752, 96666, 39738],
  [74235, 101680, 18920, 45904, 1922],
  [39309, 1505, 10531, 30458, 40228],
  [131584, 1812, 241122, 22267, 99326],
  [194133, 39985, 200997, 28229, 20780],
  [66188, 51607, 15977, 177272, 17664]
]

rows = zip(*hlasy)
transpose = [list(row) for row in rows]

hlasyCelkem = [sum(kandidat) for kandidat in transpose]
print(hlasyCelkem)

max = 0
for hlas in hlasyCelkem:
  if hlas > max:
    max=hlas

print(max)