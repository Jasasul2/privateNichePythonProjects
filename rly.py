# Author : Ondřej Maceška 
# Date : very long time ago 
# Description : some functions used to solve assignemts our teacher gave us 

import math 

def zonderSum(a, b, c, d):
    print(a + b + c + d)

def zonderCircumference(r):
    print(math.pi * r)

def zonderDetermineNegativity(a, b, c):
    negative = 0
    if(a < 0):
        negative += 1
    if(b < 0):
        negative += 1
    if(c < 0):
        negative += 1
    print(negative)

def zonderDetermineListNegativity(numbers):
    negative = 0
    for i in numbers:
        if (i < 0):
            negative += 1    
    print(negative)

def arithmeticAverage(numbers):
    if(numbers[-1] != 0):
        numbers.append(0)
    
    trueSum = sum(numbers)
    average = trueSum / len(numbers)

    print(average)

def getSmalestNumber(array):
    print(min(array))

def analyzeInput(x):
    if(x == str(x)):
        if(x.upper() == x):
            print("It's a high letter")
        else:
            print("It's a low letter")

    elif(x == int(x)):
        print("it's a number!")
    
    else:
        print("It's bullshit")

def EuklidAlgorithm(x, y):
    d = x % y 
    if(d == 0):
        return y
    return EuklidAlgorithm(y, d)

def CFS(x):
    trueX = str(x)
    ciphers = [char for char in trueX]
    cfs = 0
    for cipher in ciphers:
        cfs += int(cipher)

    return cfs

def GiveMePinCodeBitch():
    pin = input("Give me your pin, bitch ")
    print("your pin - ", pin, " - was confirmed")

d = EuklidAlgorithm(420, 69)
print(d)