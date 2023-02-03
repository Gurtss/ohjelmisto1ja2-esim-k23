import math

def pizzalaskuri(halkaisija, hinta):
    # pinta-ala pi*r^2
    pinta_ala = math.pi * (halkaisija/100.0/2.0)**2
    hinta_ala = hinta / pinta_ala
    return hinta_ala

def kysy_pizzan_tiedot():
    halk = float(input("Anna pizzan halkaisija (cm): "))
    hint = float(input("Anna pizzan hinta (€): "))
    return {'hinta': hint, 'halkaisija': halk}

pizzat = []
hinnat_m2 = []
for i in range(2):
    print(f"{i+1}. pizza:")
    pizza = kysy_pizzan_tiedot()
    pizzat.append(pizza)
    hinnat_m2.append(pizzalaskuri(pizza["halkaisija"], pizza["hinta"]))
print(pizzat)
print(hinnat_m2)


print(f"Eka pizza = {round(hinnat_m2[0], 3)} €/m^2 \nToka pizza = {round(hinnat_m2[1], 3)} €/m^2")
if hinnat_m2[0] < hinnat_m2[1]:
    print("Eka pizza on parempi vastine rahalle.")
elif hinnat_m2[1] < hinnat_m2[0]:
    print("Toka pizza on parempi vastine rahalle.")
else:
    print("Pizzat ovat yhtä hyviä vastineita rahalle.")