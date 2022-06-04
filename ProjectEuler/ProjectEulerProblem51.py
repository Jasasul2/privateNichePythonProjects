import math 
import time 
import itertools

groups = {"*1" : [11], "*3" : [13]}
TRESHOLD = 8

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

def find_combinations(input):
    all_combinations = []
    for r in range(len(input)+1):
        combinations_object = itertools.combinations(range(len(input)), r)
        combinations_list = list(combinations_object)
        all_combinations += combinations_list
    all_combinations.pop(0)
    all_combinations.pop(-1)
    return(all_combinations)

def replace(n):
    for combo in replace_something(str(n)):
        search(combo, n)

def replace_something(input):
    all_combinations = []
    kombinace = find_combinations(input)
    for k in kombinace:
        temp = input
        same_value = input[k[0]]
        for index in k:
            if(input[index] != same_value):
                break
            temp = temp[:index] + "*" + temp[index + 1:]
        all_combinations.append(temp)
    return (all_combinations)

def search(list, n):
    string = str(list)
    if(string in groups):
        if(n not in groups[string]):
            groups[string].append(n)
            if(len(groups[string]) == TRESHOLD):
                print("stop")
                print(groups[string])
                time.sleep(15)
    else:
        groups[string] = [n]

d = gen_primes()
for i in range(100000):
    x = (next(d))
    replace(x)

for group in groups:
    print(f'{group} : {groups[group]}')

print("done")
    
