class Balik:
  def __init__(self, adresa, hmotnost, doruceno = False):
    self.adresa = adresa
    self.hmotnost = hmotnost
    self.doruceno = doruceno
  
  def deliver(self):
    self.doruceno = True

  def __str__(self):
    informace = f'{self.adresa}, {self.hmotnost}, '
    if self.doruceno:
      informace += 'balik byl dorucen'
    else:
      informace += 'balik nebyl dorucen'
    return informace
    

balik1 = Balik('Brno', '5 kg')
balik2 = Balik('Tisnov', '1 kg', True)

class CennyBalik(Balik):
  def __init__(self, adresa, hmotnost, hodnota, doruceno = False ):
    super().__init__(adresa, hmotnost, doruceno)
    self.hodnota = hodnota
  def __str__(self):
    return f'{super().__str__()}, cena: {self.hodnota}'

balik3 = CennyBalik("Predklasteri", "3 kg", 500)
print(balik3)


