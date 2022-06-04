import math 

border = 28123 
abundantNumbers = []
reversedAbNumbers = []
nonConstructubleSum = 0

def ReturnProperDivisors(n):
    divs = []
    d = 1 
    while(d <= math.floor(math.sqrt(n))):
        div = n % d 
        if(div == 0):
            divs.append(d)
            dev = int(n / d)
            if(dev != d):
                divs.append(dev)
        d += 1 
    if(n in divs):
        divs.remove(n)
    return divs 

def IsAbundant(n):
    if(sum(ReturnProperDivisors(n)) > n):
        return True
    else:
        return False

def CanBeConstructedFromAbundant(n):
    for num1 in abundantNumbers:
        num2 = int(n - num1)
        if(num2 < 0):
            return False 
        if(IsAbundant(num2)):
            return True 
        if(num1 >= n):
            return False 

for i in range(11, border): #constructing abundant 
    if(IsAbundant(i)):
        abundantNumbers.append(i)

reversedAbNumbers = abundantNumbers[:]
reversedAbNumbers.reverse()


for i in range(1, border):
    if(CanBeConstructedFromAbundant(i) == False):
        nonConstructubleSum += i 

print("sum of non bla bla numbers is " + str(nonConstructubleSum))