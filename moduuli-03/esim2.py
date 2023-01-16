# useita loogisia ehtoja yhdessä
# if - else eli joko tai -rakenne.

print("Yritä antaa parillinen kokonaisluku väliltä 11 .. 20")
luku = int (input('Anna lukusi: '))

# testataan että täyttääkö luku ehdot vai ei
if (11 <= luku <= 20)  and  (luku % 2 == 0) :
    print('Kato osasit!')
else:
    print('Tollo!')

# tämä tulostetaan aina
print('Ohjelma loppui')

# Huomautus:
# if-lause voidaan kirjoittaa kokonaan ilman sulkuja
#       if 11 <= luku <= 20  and  luku % 2 == 0:
# sulut ehkä selkeyttävät ehdon hahmottamista.
