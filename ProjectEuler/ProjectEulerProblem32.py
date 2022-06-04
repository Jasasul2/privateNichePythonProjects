from mymathfunctions import IsPandigital 

def CheckPandigitalcy(multi, multi2, product):
    list = []
    joint = str(multi) + str(multi2) + str(product)
    return IsPandigital(joint)

def CheckUniqueness(number):
    letters = []
    for letter in str(number):
        if(letter not in letters):
            letters.append(letter)
        else:
            return False 
    if("0" in letters):
        return False 
    return True 


pandigitalNumbers = set()
for multiplier in range(1, 10000):
    if(CheckUniqueness(multiplier) == True):
        for multiplicand in range(2, 10000):
            if(CheckUniqueness(multiplicand) == True):
                if(multiplier != multiplicand):
                    product = multiplicand * multiplier 
                    if(CheckPandigitalcy(multiplier, multiplicand, product) == True):
                        pandigitalNumbers.add(product)

print(pandigitalNumbers)
print(sum(pandigitalNumbers))



