'''
Uuden käyttäjän luominen MariaDB tietokantaan.
Annetaan käyttäjälle myös tarvittavat oikeudet kaikkiin valitun tietokannan tauluihin.

Sinun täytyy kirjautua tietokantaan pääkäyttäjänä (admin/root/superuser),
jotta sinulla on oikeudet tehdä nämä jutut.

'''

# 1. Kirjaudu MariaDB:n pääkäyttäjänä

# 2. Luo uusi käyttäjä ja määritä hänen salasana (nyt: tunnus on user1 ja salasana sala1)
# komento: CREATE USER 'user1'@localhost IDENTIFIED BY 'sala1';

# 3. Anna käyttäjälle user1 grant-komennossa luetellut oikeudet (select jne) kaikkiin flight_game -tietokannan tauluihin.
# Komento:
# GRANT SELECT, INSERT, UPDATE, DELETE
# ON flight_game.*
# TO 'user1'@'localhost';