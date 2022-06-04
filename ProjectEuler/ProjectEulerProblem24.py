import math 
import itertools 

def CreatePermutations(array):
    sortedArray = array[:]
    sortedArray.sort()
    permutations = list(itertools.permutations(sortedArray))
    return permutations

testArray = [n for n in range(10)]
testPermutations = CreatePermutations(testArray)
print(testPermutations[999999])
