import math 

collatzDictionary = { 4 : 3, 2 : 2, 1 : 1 }

def CountChain(n):
    if(n in collatzDictionary):
        return collatzDictionary[n]
    if(n % 2 == 0):
        collatzDictionary[n] =  int(1 + CountChain(n / 2))
    else:
        collatzDictionary[n] = int(2 + CountChain((3 * n + 1) / 2)) 

    return collatzDictionary[n]

longestChain = [1, 1]

for i in range(500000, 1000000):
    lenght = CountChain(i)
    if (lenght > longestChain[0]):
        longestChain[0] = lenght
        longestChain[1] = i 

print(str(longestChain)) 




