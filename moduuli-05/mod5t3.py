#number = 15

def isPrimeNumber(number):
    for iterator in range(2, number):
        print(f"testataan lukua {number} jakamalla se arvolla {iterator}")
        print(f"jakojäännös: {number % iterator}")
        if number % iterator == 0:
            #print(f"{number} ei ole alkuluku")
            #return False
            return f"{number} ei ole alkuluku"
    #return True
    return f"{number} on alkuluku"

print(isPrimeNumber(15))
print(isPrimeNumber(17))
print(isPrimeNumber(13))