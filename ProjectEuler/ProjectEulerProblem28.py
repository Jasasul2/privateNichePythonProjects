import math 

x = 0 
ran = 1001 

result = 1

current = 0
target = 4
currentIndex = 0
nextIndex = 1

for i in range(2, (ran ** 2) + 1):
    if(currentIndex == nextIndex):
        current += 1 
        currentIndex = 0
        result += i 
        if(current == target):
            current = 0
            nextIndex += 2 
    else:
        currentIndex += 1 


print("result is " + str(result))