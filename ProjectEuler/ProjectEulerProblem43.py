from mymathfunctions import CreatePermutations, FixPermutation, ReturnIntArray, IntFromList

n = 1023456789
permutationList = CreatePermutations(ReturnIntArray(n))
totalSum = 0
for permutation in permutationList:
    if(IntFromList(permutation[1:4]) % 2 == 0):
        if(IntFromList(permutation[2:5]) % 3 == 0):
            if(IntFromList(permutation[3:6]) % 5 == 0):
                if(IntFromList(permutation[4:7]) % 7 == 0):
                    if(IntFromList(permutation[5:8]) % 11 == 0):
                        if(IntFromList(permutation[6:9]) % 13 == 0):
                            if(IntFromList(permutation[7:10]) % 17 == 0):
                                totalSum += IntFromList(permutation)
print(totalSum)
