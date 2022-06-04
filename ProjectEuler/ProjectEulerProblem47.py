import math 
from mymathfunctions import GetPrimeFactors, IsPrime

def CheckDistinction(array):
    if len(array) == len(set(array)):
        return True
    return False 

consecutive = []
target = 4
i = 3
while(len(consecutive) != target):
    if(IsPrime(i) == False):
        factors = set(GetPrimeFactors(i))
        if(CheckDistinction(factors) == True):
            if(len(factors) == target):
                primes = True 
                for x in factors:
                    if(IsPrime(x) == False):
                        primes = False 
                if(primes == True):  
                    consecutive.append([i, factors])
                else:
                    consecutive.clear()
            else:
                consecutive.clear()
        else:
            consecutive.clear()
    else:
        consecutive.clear()
    i += 1 

print(consecutive)