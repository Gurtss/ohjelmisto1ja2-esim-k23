# Huom, tentti ap 9.2. (harjoitusmahdollisuus 2.2.)
import random

# globaaleja muuttujia
to_whom = "jollekin"
something = "jotain globaalia"

def say_hello(to_whom):
    print(f"Terve {to_whom}!")
    print(f"ja heippa, {to_whom}")
    # tulostetaan globaalin muuttujan arvo
    print(something)
    return "valmista tuli"

result = say_hello("Kalle")
print(result)
print(say_hello("Viivi"))
# globaalin muuttujan arvo on pysynyt samana
print(to_whom)

def calculateSum(number1, number2):
    return number1 + number2

print(calculateSum(11, 34))

# mod t4 funktion avulla
correct_int = random.randint(1, 10)
# print(correct_int)
def checkGuess(guess):
    if guess < correct_int:
        return 'Liian pieni arvaus'
    elif guess > correct_int:
        return 'Liian suuri arvaus'
    else:
        return 'oikein'
# pääohjelma
game_on = True
while game_on:
    user_guess = int(input("Arvaa luku:"))
    result = checkGuess(user_guess)
    print(result)
    if result == 'oikein':
        print("peli loppui")
        game_on = False
