cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
cisla2 = [cislo*2 for cislo in cisla]
cisla3 = [cislo*(-1) for cislo in cisla]
cisla4= [cislo**2 for cislo in cisla]
cisla5= [str(cislo) for cislo in cisla]

print(cisla2)
print(cisla3)
print(cisla4)
print(cisla5)

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
pocty = [len(jmeno) for jmeno in jmena]
velka = [jmeno.upper () for jmeno in jmena]
zenska = [jmeno + "a" for jmeno in jmena]
maily = [jmeno.lower() + "@email.cz" for jmeno in jmena]

print(pocty)
print(velka)
print(zenska)
print(maily)