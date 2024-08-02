from calendar import month


def mult(a,b):
  return(a*b)

print(mult(3,5))

def totalPrize(persons, breakfast=False):
  return (persons*850+150 if breakfast else persons*850)
def totalPrice(persons, breakfast=False):
  pricePerPerson = 850
  if breakfast:
    pricePerPerson += 125
  return pricePerPerson * persons


print(totalPrize(1,False))


def mathBirth(rc):
  rodne = str(rc)
  mesic = int(rodne[2]+rodne[3])
  if mesic > 50:
    mesic -=50
  return (mesic)

print(mathBirth(8761144172))

def monthOfBirth(birthNumber):
  month = birthNumber[2] + birthNumber[3]
  month = int(month)
  month = month % 50
  return month