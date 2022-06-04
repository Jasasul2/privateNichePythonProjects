testInt = 150

def GetPrimeFactors(integer):
    factors = []
    d = 2
    while integer > 1:
        while integer % d == 0:
            factors.append(d)
            integer /= d
        d += 1

    return factors

primeFactors = GetPrimeFactors(testInt)
print("")
print(primeFactors)
print("")
print("largest is " + str(max(primeFactors)))
