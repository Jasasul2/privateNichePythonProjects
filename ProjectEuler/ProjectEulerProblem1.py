
target = 1000
currentCount = 0

for i in range(1, target):
    x = i / 5
    y = i / 3
    if(x.is_integer() or y.is_integer()):
        currentCount += i

print(currentCount)
