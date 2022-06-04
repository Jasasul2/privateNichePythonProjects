from mymathfunctions import IsPrime, ReturnIntArray

def CheckTruncatibility(array):
    string = ""
    for i in range(len(array)): #from right to left 
        string += str(array[i])
        if(IsPrime(int(string)) == False):
            return False 

    for i in range(len(array) - 1):
        string = string.replace(str(array[i]), "", 1)
        if(IsPrime(int(string)) == False):
            return False 

    return True 
        
def CheckDualTruncatibility(n):
    if(IsPrime(n)):
        array = ReturnIntArray(n)
        return CheckTruncatibility(array)

i = 11
truncatablePrimes = []
while(len(truncatablePrimes) < 11):
    if(CheckDualTruncatibility(i) == True): 
        truncatablePrimes.append(i)
    i += 2
    
print(truncatablePrimes)
print(sum(truncatablePrimes))
