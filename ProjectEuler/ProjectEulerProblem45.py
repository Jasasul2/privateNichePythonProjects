import math 

def hexagonalNumberGenerator():
    num = 1
    inc = 1
    while True:
        yield num
        inc += 4
        num += inc

def isPentagonal(n):
    if(n < 1):
        return False 
    p = (math.sqrt(24 * n + 1) + 1) / 6
    return p.is_integer()

def isTriangular(n):
    if(n < 1):
        return False 
    t = (math.sqrt(8 * n + 1) - 1) / 2
    return t.is_integer() 

hng = hexagonalNumberGenerator()
hlist = []
for i in range(100000):
    hlist.append(next(hng)) #creates pentagonal numbers 

allList = []
for hexNum in hlist:
    if(isPentagonal(hexNum) == True):
        if(isTriangular(hexNum) == True):
            allList.append(hexNum)

print(allList)