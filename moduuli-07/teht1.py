'''
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
'''

# määritellään monikkorakenne
vuodenajat = ("kevät", "kesä", "syksy", "talvi")

# kysytään käyttäjältä kuukauden numeron (1-12)
kkNro = int(input("Anna kuukauden numero (1-12: "))

# TODO: täydennä koodi täysin toimivaksi, muista myös joulukuu
# määritellään, mihin vuodenaikaan kuukausi kuuluu.
# hyödynnetään monikkoa.
if (kkNro == 1 or kkNro == 2):
    vuodenaika = vuodenajat[3]
elif (kkNro >= 3 and kkNro <= 5):
    vuodenaika = vuodenajat[0]
else:
    vuodenaika = "tuntematon"

# tulostetaan vastaus
print(f"{kkNro}. kuukausi kuuluu vuodenaikaan: {vuodenaika}")