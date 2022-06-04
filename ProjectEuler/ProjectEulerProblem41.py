from mymathfunctions import IsPrime, CreatePermutations, FixPermutation, ReturnIntArray

n = 2143567
permutationList = CreatePermutations(ReturnIntArray(n))
highestPerm = 0
for perm in permutationList:
    truePerm = FixPermutation(perm)
    if(IsPrime(truePerm) == True):
        if(truePerm > highestPerm):
            highestPerm = truePerm 

print(highestPerm)
