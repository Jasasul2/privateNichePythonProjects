number = 9009


numberList = []
reversedNumberList = []

palindromeList = []

for x in range(100, 1000):
    for y in range(100, 1000):
        numberList.clear()
        reversedNumberList.clear()
        number = x * y
        stringNumber = str(number)

        for char in stringNumber:
            numberList.append(char)
            reversedNumberList.append(char)
        reversedNumberList.reverse()

        foundPalindrome = True
        for i in range(len(numberList)):
            if (numberList[i] != reversedNumberList[i]):
                foundPalindrome = False

        if(foundPalindrome):
            palindromeList.append(number)


print(str(max(palindromeList)))

