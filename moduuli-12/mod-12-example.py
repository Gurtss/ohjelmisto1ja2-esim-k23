import json
import requests

hakusana = input("Anna kaupungin nimi: ")

# Pyynnön malli: https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
pyyntö = "https://api.openweathermap.org/data/2.5/weather?q=" + hakusana + "&appid=laita_tähän_sinun_oma_api_key"

# Testaa tulostuva hakulause selaimella.
# Jos se palauttaa haluttua dataa, niin tämän koodin voi poistaa tai kommentoida
print("Nettiin lähtevä hakulause: ")
print(pyyntö)

# Huomataan selaimen haulla, että yhden kaupungin data ei tule listan sisällä,
# vaan suoraan {...} eli ns. lohkorakenteen sisässä -> avaimiin pöästään suoraan kiinni.

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        # tulostetaan haluttujen data-avaimien arvoja.

        # HUOM: teksti on ympäröity "" merkeillä  ->  hakuavaimien nimet täytyy ympäröidä heittomerkeillä, esim. 'wind'
        print(f"Tuulen nopeus: {json_vastaus['wind'] ['speed']}, mikähän lie on yksikkö?" )

        # Huom: 'Weather'-avain: tämä voi aiheuttaa ongelmia. Huomaatko datasta (esim. selain tai tulosta dump)
        # että Weather-avaimen alla olevat arvot on laitettu listan [...] sisään.
        # Siksi Weather-avaimen sisältöä täytyy käsitellä listana: ['weather'][0] Ks alla
        print(f"Weather-avaimen alta löytyvän id-avaimen arvo: {json_vastaus ['weather'][0] ['id']}")

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
