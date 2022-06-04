import math

def isPrime(n):
    if n == 1:
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

limit = 2000000
summice = 5
n = 5

while n <= limit:
    if(isPrime(n)):
        summice += n
    n += 2
    if(n <= limit) and isPrime(n):
        summice += n
    n += 4

print("sum of all primes is " + str(summice))
