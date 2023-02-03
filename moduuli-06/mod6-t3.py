
def gallons_to_litres(gallons):
    litres = gallons * 3.785
    return litres

program_running = True
while program_running:
    user_input = float(input("Montako gallonaa? "))
    if user_input > 0:
        result = gallons_to_litres(user_input)
        print(f"{user_input} gallonaa on {result:.1f} litraa")
    else:
        print("negatiivinen arvo, lopetetaan ohjelman suoritus")
        program_running = False

