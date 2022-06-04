import math 

def combination(n, k):
    result = (math.factorial(n)/(math.factorial(n - k) * math.factorial(k)))
    return int(result)

higher_than_milion = 0
for n in range(1, 101):
    for k in range(1, n):
        if(combination(n, k) > 1000000):
            higher_than_milion += 1

print(higher_than_milion)