#takes (X) previous zlomek as input, returns (Y) a jmenovatel of the new one 
def phase1(c, j):
    return 2 * j + c, j

#takes (Y) as argument, returns Z - a new output 
def phase2(c, j):
    return (j + c, c)

bigger = 0
lastTuple = (1, 2)
for i in range(1000):
    tuple = phase1(lastTuple[0], lastTuple[1])
    newTuple = phase2(tuple[0], tuple[1])
    if(len(str(newTuple[0]))) > len(str(newTuple[1])):
        bigger += 1
    lastTuple = (newTuple[0] - newTuple[1], newTuple[1])

print("******************")
print(bigger)