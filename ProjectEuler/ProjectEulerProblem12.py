import math 

def ReturnDivisors(n):
    divs = []
    d = 1 
    while(d < math.floor(math.sqrt(n))):
        div = n % d 
        if(div == 0):
            divs.append(d)
            divs.append(int(n / d))
        d += 1 
    return divs 

targetDiv = 500
divisors = []
n = 0 
triangle = 1 

while(len(divisors) <= targetDiv):
    n += triangle 
    triangle += 1 
    if (n % 2 == 0):
        divisors = ReturnDivisors(n)

divisors.sort()
print("Number " + str(n) + " has " + str(len(divisors)) + " divisors : " + str(divisors))
