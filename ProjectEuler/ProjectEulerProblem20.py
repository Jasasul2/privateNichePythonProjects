import math

target = 100

fac = math.factorial(target)
targetSum = 0
for char in str(fac):
    targetSum += int(char)

print("number " + str(target) + " has factorial " + str(fac) + " which has a sum of " + str(targetSum))