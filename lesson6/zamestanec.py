class Zamestnanec:
  def __init__(self, jmeno, pozice):
    self.jmeno = jmeno
    self.pozice = pozice
    self.dovolena = 160

  def __str__(self):
    return f"{self.jmeno} a pracuje na pozici {self.pozice}"
  
  def cerpej_dovolenou(self, pocet_hodin):
    if self.dovolena >= pocet_hodin:
      self.dovolena -= pocet_hodin
      return "Užij si to."
    else:
      return f"Máš nárok je na {self.dovolena} hodin."
  

class Manazer(Zamestnanec):
  def __init__(self, jmeno, pozice, pocet_podrizenych):
    super().__init__(jmeno, pozice)
    self.pocet_podrizenych = pocet_podrizenych

  def __str__(self):
    text = super().__str__()
    text = text + f" Počet podřízených: {self.pocet_podrizenych}"
    return text


frantisek = Zamestnanec("František Novák", "konstruktér")
klara = Zamestnanec("Klára Nová", "konstruktérka")
marian = Manazer("Marian Přísný", "vedoucí", 2)

class Brigadnik(Zamestnanec):
  def __init__(self, jmeno, pozice, uvazek):
    super().__init__(jmeno, pozice,)
    self.uvazek = uvazek

  def __str__(self):
    return f'{super().__str__()}, uvazek: {self.uvazek}'

martin = Brigadnik("Martin Divny", "klaun", 0.5)
print(martin)