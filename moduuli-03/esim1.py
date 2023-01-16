# if-rakenne

# kysytään käyttäjän ikä, luetaan se numerona
ika = int ( input('Anna ikäsi '))

# jos täysi-ikäinen, niin kerrotaan kuinka monta vuotta on ollut näin
# Toiminta: jos if-ehto on totta, niin suoritetaan kaikki sen jälkeen olevat sisennetyt rivit
if ika >= 18:
    print('Olet siis täysi-ikäinen')
    aika = ika - 18         # kuinka monta vuotta täysi-ikäisenä?
    print(f"Olet ollut sitä jo {aika} vuotta")

# tämä lause suoritetaan aina (samalla tasolla if-ehdon kanssa)
print('Hyvää päivän jatkoa!')