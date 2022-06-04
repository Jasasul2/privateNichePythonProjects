import math 

def is_pentagonal(n):
    if(n < 1):
        return False 
    k = (math.sqrt(24 * n + 1) + 1) / 6
    return k.is_integer()

def get_pentagonal(n):
    return int(n * (3 * n - 1) / 2) 

dlist = []
pentagonal_list = []
for i in range(1, 10000):
    k = get_pentagonal(i)
    pentagonal_list.append(k)
    for j in pentagonal_list: 
        sum = k + j
        if(is_pentagonal(sum) == True):
            diff = k - j 
            if(is_pentagonal(diff) == True):
                dlist.append([diff, j, k])

print(dlist)