"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan
satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
"""
import random

def roll_die(number_of_sides):
    return random.randint(1, number_of_sides)

def play_game():
    result = 0
    while result != 6:
        result = roll_die(6)
        print(result)

play_game()
