# Huom, tentti ap 9.2. (harjoitusmahdollisuus 2.2.)
import random

# globaaleja muuttujia
to_whom = "jollekin"
something = "jotain globaalia"

def say_hello(to_whom):
    to_whom = to_whom.upper()
    print(f"Terve {to_whom}!")
    print(f"ja heippa, {to_whom}")
    # tulostetaan globaalin muuttujan arvo
    print(something)
    return "valmista tuli"

to_whom = "Kalle"
result = say_hello(to_whom)
print(result)
print(say_hello("Viivi"))
# globaalin muuttujan arvo on pysynyt samana
print(to_whom)

def calculate_sum(number1, number2):
    return number1 + number2

print(calculate_sum(11, 34))

# mod t4 funktion avulla
correct_int = random.randint(1, 10)
# print(correct_int)
def check_guess(guess):
    if guess < correct_int:
        return 'Liian pieni arvaus'
    elif guess > correct_int:
        return 'Liian suuri arvaus'
    else:
        return 'oikein'
# pääohjelma (arvauspeli) omassa funktiossaan
def guess_game():
    game_on = True
    while game_on:
        user_guess = int(input("Arvaa luku:"))
        result = check_guess(user_guess)
        print(result)
        if result == 'oikein':
            print("peli loppui")
            game_on = False
# guess_game()

# Lista parametrina (materiaalista)
def inventaario(tavarat):
    tavarat.append("tussi")
    print("Sinulla on seuraavat tavarat:")
    for tavara in tavarat:
        print("- " + tavara)

koulureppu = ["kynä", "kumi", "viivotin"]
inventaario(koulureppu)
print(koulureppu)

# listajuttuja
# tulostetaan kaikki alkiot: for in
lista = [1, 3, 4, 5, 6]
for numero in lista:
    print(numero)
print("--------------")
# tulostetaa joka toisen alkion arvon
for i in range(len(lista)):
    if i%2 == 0:
        print(lista[i])
# listan kopiointi
lista2 = lista.copy()
lista2.remove(3)
print(lista)