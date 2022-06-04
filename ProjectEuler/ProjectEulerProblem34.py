import math

dict = {}
for i in range(0, 10):
    dict[i] = math.factorial(i)

print(dict)

def DigitsFactorial(n):
    list = [char for char in str(n)]
    sum = 0
    for num in list:
        sum += dict[int(num)]
    if(sum == n):
        return True 
    return False 

total_sum = 0
for i in range(3, 1000000):
    if(DigitsFactorial(i) == True):
        total_sum += i 

print(total_sum)