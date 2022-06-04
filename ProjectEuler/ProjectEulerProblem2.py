
lastNumber = 1
currentNumber = 2
totalSum = 0

while(currentNumber <= 4000000):
    newNumber = currentNumber + lastNumber
    lastNumber = currentNumber
    currentNumber = newNumber
    if(currentNumber <= 4000000):
        if((currentNumber / 2).is_integer()):
            totalSum += currentNumber
            print(currentNumber)
print("")
print(totalSum + 2)
