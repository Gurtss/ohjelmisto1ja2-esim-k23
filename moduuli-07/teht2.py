'''
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
syötettiinkö nimi ensimmäistä kertaa.
Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.
'''

# luodaan tyhjä joukko (käytettävä set-toimintoa)
nimet = set()

# kysytään eka nimi ennen toistoa
nimi = input("Anna nimi, tyhjä lopettaa: ")

# toistetaan, kunnes saadaan tyhjä merkkijono
while nimi != "":
    # testataan, onko saatu nimi jo joukossa 'nimet'
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)     # lisätään uusi nimi joukkoon
    # muista kysyä uusi nimi
    nimi = input("Anna nimi, tyhjä lopettaa: ")

# TODO: tulosta joukon alkiot for-toistolla
