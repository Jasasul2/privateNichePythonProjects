
def TryToSimplify(n1, n2):
    if(n1 == n2):
        return False
    result1 = (n1 / n2)

    array1 = [char for char in str(n1)]
    array2 = [char for char in str(n2)]
    foundSimp = False

    for char in array1:
        if(foundSimp):
            break 
        for char2 in array2:
            if char == char2 and char != "0":
                array1.remove(char)
                array2.remove(char2)
                foundSimp = True
                break 

    if(len(array1) == 1):
        nn1 = int(array1[0])
        nn2 = int(array2[0])
        if(nn2 == 0):
            return False
        result2 = nn1 / nn2 
        if(result1 == result2):
            return True 
    return False 

cancellingFractions = []
for n1 in range(10, 100):
    for n2 in range(10, 100):
        if(TryToSimplify(n1, n2) == True):
            if([n2, n1] not in cancellingFractions):
                cancellingFractions.append([n1, n2])

print(cancellingFractions)
result1 = 1
result2 = 1
for x in cancellingFractions:
    result1 *= x[0]
    result2 *= x[1]

print([result1, result2])