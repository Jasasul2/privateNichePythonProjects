import math 

power = 5
dictionary = {}
sum = 0

for i in range(0, 10):
    dictionary[str(i)] = int(math.pow(i, power))
print(dictionary)

for i in range(2, 1000000):
    charsum = 0
    for char in str(i):
        charsum += dictionary[char]
    if(charsum == i):
        sum += i 

print(sum)
