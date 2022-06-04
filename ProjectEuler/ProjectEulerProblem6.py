numberRange = 100

sumOfSquares = 0

theSum = 0
squareOfTheSum = 0

for i in range(1, numberRange + 1):
    sumOfSquares += (i ** 2)
    print(i ** 2)
    theSum += i

print("-------")
print("sum of the squares: " + str(sumOfSquares))
squareOfTheSum = theSum ** 2
print("-------")
print("square of the sum: " + str(squareOfTheSum))
print("*******")
print(str(squareOfTheSum - sumOfSquares))
