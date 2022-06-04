import math 
from mymathfunctions import IsPrime
from collections import deque 

#transforms number into array of its digits 
def CreateArrayFromNumber(n): 
    array = []
    for char in str(n):
        array.append(int(char))
    return array

#creates a list of number rotations 
def CreateNumFromRotation(givenList):
    array = []
    A = deque(givenList)
    for i in range(len(A)):
        A.rotate()
        l = list(deque(A))
        array.append(l)

    return array

#gets an array of arrays and checks prime rotation for each of them 
def CheckPrimeCirculationOfArray(array):
    for x in array:
        num = ""
        for char in x:
            num += str(char)
        number = int(num)
        if(IsPrime(number) == False):
            return False
    return True 

total_count = 0  
for i in range(1, 1000000):
    if(IsPrime(i)):
        array = (CreateNumFromRotation(CreateArrayFromNumber(i)))
        if(CheckPrimeCirculationOfArray(array) == True):
            total_count += 1

print(total_count)


