import math 

def IsPrime(n):
    if n <= 1:
        return False
    elif n < 4:
        return True 
    elif n % 2 == 0:
        return False 
    elif n < 9:
        return True 
    elif n % 3 == 0:
        return False 
    else:
        r = math.floor(math.sqrt(n))
        f = 5 
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True 

largestN = 0
list = [[0, 0, 0]]
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        prime = True 
        while(prime):
            x = n ** 2 + ( a * n ) + b 
            prime = IsPrime(x)
            n += 1 
        if(n > largestN):
            largestN = n 
            list.append([largestN, a, b])

for i in range(len(list)):
    if(list[i][0] == largestN):
        product = list[i][1] * list[i][2]
        print("")
        print(product)