'''
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
hakea jo syötetyn lentoaseman tiedot vai lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja
tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
(ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
Löydät koodeja helposti selaimen avulla.)
'''

# funktio lisää uuden lentoaseman sanakirjaan
def lisaa():
    # kysytään lentoaseman tunnus ja nimi
    tunnus = input("Anna lentoaseman tunnus: ")
    nimi = input("Anna lentoaseman nimi: ")
    # lisätään uusi lentoasema sanakirjaan
    lentoasemat[tunnus] = nimi
    return

# funktio hakee sanakirjasta lentoaseman nimen ICAO-k0odin perusteella
def hae():
    # TODO: toimiva koodi
    print("Kyllä tämäkin valmistuu...")
    return

# xtra: funktio tulostaa sanakiejassa olevien lentoasemien tiedot
# huom: jos tulostus ei kelpaa, niin jokainen alkio sisältää avaimen ja arvon (key, value)...
def tulosta():
    for asema in lentoasemat:
        print(f"{asema}")
    return

# -- pääohjelma alkaa  --
# luon sanakirjan, jolle annan yhden alkion
lentoasemat = {"EFHK" : "Helsinki-Vantaan lentoasema"}

toiminto = -1       # valittu toiminto,
                    # annetaan sellainen alkuarvo että päästään toiston sisään
while toiminto != 3:
    print("0 = tulosta lentoasemien tiedot")
    print("1 = lisää uusi lentoasema")
    print("2 = hae lentoasema")
    print("3 = lopeta")

    toiminto = int(input("Valitse toiminto: "))
    if toiminto == 0:
        tulosta()
    elif toiminto == 1:
        lisaa()
    # TODO: lisää loput toiminnot

print("Kiitos ja näkemiin")