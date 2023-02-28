# Tämä on esimerkin aloitustiedosto (moduuli).
# Esimerkkiin kuuluu myös 2 muuta moduulia: apuA ja apuB.

# Huomataan että kommunikointi eri moduleissa olevien funktioiden välillä toimii
# vastaavasti kuin yhden tiedoston (modulin) tapauksessa.

# Tämä on projektin päätiedosto


# -- esim a --  otetaan käyttöönn vain moduulissa (tiedostossa) apuA oleva
# funktio summaa, modulissaa olevia muita funktioita ei voi kutsua tästä ohjelmasta.
from apuA import summaa

# nyt voin käyttää funktiota summaa pelkästään sen nimellä
vastaus = summaa(3,5)
print(f"Pääohjelma tulostaa: lukujen summa = {vastaus}")

# -- esim b --  nyt otan käyttöön koko modulin (tiedoston) apuB,
# jolloin voin kutsua kaikkia modulin funktioita.
# (vrt. import math)
import apuB

# nyt on ilmoitettava myös modulin nimi.
erotus = apuB.kysy()

print(f"Pääohjelma tulostaa: lukujen erotus = {erotus}")


