class Balik:
  def __init__(self, adresa, hmotnost, doruceno = False):
    self.adresa = adresa
    self.hmotnost = hmotnost
    self.doruceno = doruceno
  
  def deliver(self):
    self.doruceno = True

  def __str__(self):
    informace = f'adresa: {self.adresa}, hmotnost: {self.hmotnost}'
    if self.doruceno:
      informace += ', doruceno'
    else:
      informace += ', nedoruceno'
    return informace
    

class CennyBalik(Balik):
  def __init__(self, adresa, hmotnost, hodnota, doruceno = False ):
    super().__init__(adresa, hmotnost, doruceno)
    self.hodnota = hodnota
  def __str__(self):
    return f'{super().__str__()}, cena: {self.hodnota}'

class Ridic:
  def __init__(self, jmeno):
    self.jmeno = jmeno
    self.seznamBaliku = []

  def __str__(self):
    informace = f"Jmeno: {self.jmeno}, baliky k doruceni: "

    for balik in self.seznamBaliku:
      informace+=  "\n " + balik.adresa
    informace += f"\nCelkem zbyva dorucit {self.zbyvaBaliku()} baliky"
    return informace

  def priradBalik(self, Balik):
    if Balik.doruceno:
      return "Nelze přiřadit, balík již byl doručen."
    else:
      self.seznamBaliku.append(Balik)

  def zbyvaBaliku(self):
    pocetNedorucenych = 0
    for balik in self.seznamBaliku:
      if not balik.doruceno:
        pocetNedorucenych += 1
    return pocetNedorucenych


balik1 = Balik('Cernohorska 522', 480)
balik2 = Balik('Bozetechova 60', 390)
balik3 = CennyBalik("Predklasteri 15", 180, 500)

frantisek = Ridic("Frantisek Cerny")

frantisek.priradBalik(balik1)
frantisek.priradBalik(balik2)
frantisek.priradBalik(balik3)

balik3.deliver
balik1.deliver
print(frantisek)

