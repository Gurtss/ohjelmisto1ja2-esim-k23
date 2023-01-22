'''
    Listan peruskäsittelyä.
    Kysytään käyttäjältä numeroita kunnes hän antaa tyhjän.
    Tulostetaan lopuksi käyttäjän 3 pienintä lukua.
'''

# luodaan tyhjä lista käyttäjän lukuja varten.
kokonaisLuvut = []

# luetaan käyttäjän luku merkkijonona, jotta voidaan verrata sitä tyhjään merkkijonoon.
lukuStr = input('Anna kokonaisluku (tyhjä lopettaa): ')

# toistetaan, kunnes saadaan tyhjä
while lukuStr != "":
    # muutetaan saatu merkkijono kokonasluvuksi
    luku = int(lukuStr)
    # lisätään saatu kokonaisluku listan loppuun
    kokonaisLuvut.append(luku)
    # muista kysyä uusi luku (merkkijonona)
    lukuStr = input('Anna kokonaisluku (tyhjä lopettaa): ')

# kokeillaan muutamia listan valmiita toimintoja
print(f"Annoit {len(kokonaisLuvut)} lukua")
if kokonaisLuvut.__contains__(10):
    print("Annoit ainakin kerran luvun 10")
    print("Poistan luvuistasi eka kympin")
    kokonaisLuvut.remove(10)

print("Tallentamani luvut tällä hetkellä")
print(kokonaisLuvut)

# järjestetään luvut suuruusjärjestykseen
kokonaisLuvut.sort()

# muuttuja index saa for-toistossa arvot 0, 1 ja 2
print("Kolme pinintä lukuasi ovat: ")
for index in range(0, 3):
    print(kokonaisLuvut[index])


