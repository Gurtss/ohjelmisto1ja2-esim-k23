"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen
ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
"""
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game3',
        user='username',
        password='password',
        autocommit=True
    )
connection = connect_db()
#print(connection)

def get_airport(icao):
    query = f"select name, municipality from airport where ident='{icao}'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    #print(result)
    if cursor.rowcount > 0:
        return f"Kentän nimi: {result[0]}, paikkakunta: {result[1]}"
    else:
        return "Ei tuloksia"

# TODO: kysy icao käyttäjältä
result = get_airport("efhk")
print(result)
