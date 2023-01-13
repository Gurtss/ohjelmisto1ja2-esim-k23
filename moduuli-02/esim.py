import math

# print("2")
# print()
print('Hei, "maailma!" 3')

# muuttujan esittely ja arvon sijoittaminen muuttujaan
name = "Matti"
print(name)
name = "Viivi"
print(name)

# syötteen lukeminen käyttäjältä¿
name = input("Anna nimesi: ")
ageString = input("Anna ikäsi: ")
# arvon tyypin muunnos merkkijono (string) => kokonaisluku (int)
# int("3") => 3
age = int(ageString)
age = age + 1
message = "Morjes " + name + ", olet ensi vuonna " + str(age) + "-vuotias."
print(message)
# sama käyttäen f-stringiä
print(f"Morjes {name}, olet ensi vuonna {age:3.0f}-vuotias.")
#print(f"Morjes {name}, olet ensi vuonna {age+10:3d}-vuotias.")

print(f"Piin likiarvo by Python: {math.pi:.5f}")