import math 
import itertools 

def GetPrimeFactors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
    return factors

def StringInt(n):
    return str(n)

def IsPandigitalN(string):
    list = []
    count = len(string)
    for letter in string:
        if(int(letter) not in list and int(letter) != 0):
            list.append(int(letter))
        else:
            return False 
    
    for i in range(1, count + 1):
        if(i not in list):
            return False 
    return True 
    

def IsPandigital(string): #old version which checked just 9digit numbers 
    list = []
    for letter in string:
        if(int(letter) not in list):
            list.append(int(letter))
        else:
            return False 
            
    if(0 in list or len(list) < 9):
        return False
    return True 

def ReturnBinaryNum(n):
    return bin(n)[2:]

def ReturnIntArray(n):
    array = []
    for letter in str(n):
        array.append(letter)
    return array 

def IntFromList(array):
    string = ""
    for i in array: 
        string += i 
    return int(string) 
        
def IsRightAngleTriangle(a, b, c):
    if(c ** 2 == a ** 2 + b ** 2):
        return True 
    return False 

def DetermineTriangle(a, b, c):
    if(a + b <= c):
        return False 
    if(a + c <= b):
        return False 
    if(b + c <= a):
        return False 
    return True 

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

def GetListOfDivisors(n):
    divisors = [] 
    for i in range(1, math.floor(n / 2)):
        if(n % i == 0):
            divisors.append(i)
    divisors.append(n)
    return divisors

def CreatePermutations(array):
    sortedArray = array[:]
    sortedArray.sort()
    permutations = list(itertools.permutations(sortedArray))
    return permutations

def FixPermutation(perm): #returns permutation as integer
    integer = ""
    for i in perm:
        integer += i 
    return int(integer)

def OddNumberGenerator():
    num = 3
    while True:
        yield num
        num += 2 

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
    
        q += 1
