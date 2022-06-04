import math 

def ReturnProperDivisors(n):
    divs = []
    d = 1 
    while(d <= math.floor(math.sqrt(n))):
        div = n % d 
        if(div == 0):
            divs.append(d)
            divs.append(int(n / d))
        d += 1 
    if(n in divs):
        divs.remove(n)
    return divs 

amicableDictionary = { }
amicableSum = 0

def CheckAmicability(n):
    a = ReturnProperDivisors(n)
    a.sort()
    b = sum(a)
    asum = 0
    if(n in amicableDictionary or b in amicableDictionary):
        return asum 
    if(sum(ReturnProperDivisors(b)) == n and n != b):
        print("Numbers " + str(n) + " and " + str(b) + " are amicable ")
        amicableDictionary[n] = b 
        asum += n 
        asum += b
    return asum 

for i in range(1, 10000):
    amicableSum += CheckAmicability(i)

print("-------")
print(amicableSum)

