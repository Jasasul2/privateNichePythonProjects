from mymathfunctions import IsPandigital, StringInt
import math 

def RangeMultiplyCheck(n, rangeN):
    string = ""
    for i in range(1, rangeN + 1):
        string += str(n * i)
    return string

largestPanNum = 1
i = largestPanNum
rangenum = math.floor(9 / len(str(i)))

while(rangenum > 1):
    rangenum = math.floor(9 / len(str(i)))
    numstring = RangeMultiplyCheck(i, rangenum)
    if(IsPandigital(numstring) == True):
        if(int(numstring) > largestPanNum):
            largestPanNum = int(numstring) 
    i += 1
print("----------------")
print(largestPanNum)




