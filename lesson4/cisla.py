hodnoty = "12.1 1.68 7.45 -11.51"
rozdeleno = hodnoty.split(" ")

print(rozdeleno)

pricteno = float(rozdeleno[3])+0.25
print(pricteno)

rozdeleno[3] = str(pricteno)
print(rozdeleno)
noveHodnoty = " ".join(rozdeleno)
print (noveHodnoty)

hodnoty = ['12', '1', '7', '-11']

hodnoty[2] = str(int(hodnoty[2]) + 4)

print(hodnoty)
