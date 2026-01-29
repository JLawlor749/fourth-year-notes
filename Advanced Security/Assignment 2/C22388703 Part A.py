import random

def test(n):
    q = n-1
    k = 0

    while q % 2 == 0:
        q //= 2
        k += 1


    a = random.randint(2, n-1)

    if (pow(a, q) % n) == 1:
        return "Inconclusive"
    

    for i in range(0, k):
        power = pow(2, i) * q

        if pow(a, power) % n == n - 1:
            return "Inconclusive"
        
    return "Composite"
        


def miller_rabin(n, rounds):
    
    if n == 2:
        return("Prime")

    if n <= 1:
        return("Not prime")
    
    if n % 2 == 0:
        return("Composite")

    for i in range(rounds):
        if test(n) == "Composite":
            return "Composite"
        
    return "Inconclusive"




#var = int(input("Choose a number to test: "))
#print(test(var))

rounds = int(input("Choose a number of rounds: "))

notPrime = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 33, 35, 39, 49, 51, 55, 57, 63, 65, 77, 85, 91]
prime = [2, 23, 19, 17, 101, 113, 127, 131, 137, 149, 157, 163, 173, 179, 193, 199, 223, 227, 257, 263, 281, 307, 331, 353, 383, 401, 421, 457, 499]

print("Primes:")
for i in prime:
    print(miller_rabin(i, rounds))

print("\n\n")

print("Non-Primes:")
for i in notPrime:
    print(miller_rabin(i, rounds))