import math 

target = 1000
total = 0
for i in range(1, target + 1):
    n = i ** i
    total += n

print(total)