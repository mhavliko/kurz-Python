import statistics

teploty = [
  [2.1, 5.2, 6.1, -0.1],
  [2.2, 4.8, 5.6, -1.0],
  [3.3, 6.5, 5.9, 1.2],
  [2.9, 5.6, 6.0, 0.0],
  [2.0, 4.6, 5.5, -1.2],
  [1.0, 3.2, 2.1, -2.0],
  [0.4, 2.7, 1.3, -2.8]
]

prumer = [statistics.mean(denniTeploty) for denniTeploty in teploty]
ranni = [denniTeploty[0] for denniTeploty in teploty]
nocni = [denniTeploty[-1] for denniTeploty in teploty]
denANoc = [[denniTeploty[1], denniTeploty[-1]] for denniTeploty in teploty]

print(prumer)
print(ranni)
print(nocni)
print(denANoc)

prumerCelkem = statistics.mean(prumer)
print (prumerCelkem)

#hodnoceni = [7, 9, 6, 7, 9, 8]
#for znamka in hodnoceni:
#  print(str(znamka) +"/10")


