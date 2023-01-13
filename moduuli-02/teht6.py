"""
Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
    kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
    nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
"""
import random

random_number1 = random.randint(0, 9)
random_number2 = random.randint(0, 9)
random_number3 = random.randint(0, 9)
# code = str(random_number1) + str(random_number2) + str(random_number3)
code = f"{random_number1}{random_number2}{random_number3}"
print(f"Numerolukon koodi: {code}")
# TODO: nelinumeroinen koodi
