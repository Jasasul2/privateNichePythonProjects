import math 
from mymathfunctions import ReturnIntArray, CreatePermutations, FixPermutation, IsPrime

usedNumbers = []
primePermLists = []

def CheckPrimePermutations(n):
    permList = CreatePermutations(ReturnIntArray(n))
    primePermList = []
    for perm in permList:
        fixedPerm = FixPermutation(perm)
        if(fixedPerm < 1000):
            continue
        if(fixedPerm not in usedNumbers):
            usedNumbers.append(fixedPerm)
            if(IsPrime(fixedPerm) == True):
                primePermList.append(fixedPerm)
    return primePermList

def CheckSameDifferences(array):
    for i in range(0, len(array) - 2):
        a1 = array[i]
        for y in range(i + 1, len(array)):
            a2 = array[y]
            d = a2 - a1
            a3 = a2 + d
            if(a3 in array):
                return [a1, a2, a3]
    return []

for i in range(1000, 10000):
    if(i not in usedNumbers):
        x = CheckPrimePermutations(i)
        if(len(x) > 2):
            primePermLists.append(x)

answers = []
for list in primePermLists:
    l = CheckSameDifferences(list)
    if(len(l) == 3):
        answers.append(l)

print(answers)