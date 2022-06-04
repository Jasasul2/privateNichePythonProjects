import math 
from mymathfunctions import IsPrime 

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

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

primeList = []
d = gen_primes()
for i in range(10):
    x = (next(d))
    if(x > 1000000):
        break
    primeList.append(x)

print(len(primeList))

longest_chain = 0
for start in range(len(primeList)): #prime at which the chain starts 
    value = 0 
    chain = [] #currentChain 
    for end in range(start, len(primeList)):
        currentPrime = primeList[end]
        value += currentPrime
        chain.append(currentPrime)
        if((value in primeList) and len(chain) > longest_chain):
            print("")
            print("")
            print(f'value {value} is a prime built from this {len(chain)} units long chain: {chain}')
            longest_chain = len(chain)
        if(value > 1000000):
            break

