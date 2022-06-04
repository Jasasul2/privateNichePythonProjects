import math 
from mymathfunctions import  IsPrime

def OddNumberGenerator():
    num = 3
    while True:
        yield num
        num += 2 

primes = [2] 

def CheckGoldbach(n):
    print("")
    primeIndex = -1
    prime = 3
    goldbach = False 
    while(primeIndex > len(primes) * -1):
        prime = primes[primeIndex] 
        rem = n - prime
        square = 1
        if(rem > 2):
            square = math.sqrt(rem / 2)
            if(square.is_integer() == True and square > 0):
                goldbach = True 
                break 
        elif(rem == 2):
            goldbach = True 
            break 
        primeIndex -= 1 

    if(goldbach == True):
        print("Number ", n, " is combined from a prime ", prime, " and 2 * ", int(square), " ** 2")
        return True 
    else:
        print("NUMBER ", n , " is a proof this this theory is fake shit")
        return False 

ong = OddNumberGenerator()
oddCompositelist = []
oddNum = 0
conjenctureIsCorrect = True 
i = 0
while(conjenctureIsCorrect == True):
    oddNum = next(ong)
    if(IsPrime(oddNum) == True):
        primes.append(oddNum)
    else:
        conjenctureIsCorrect = CheckGoldbach(oddNum)
    i += 1 