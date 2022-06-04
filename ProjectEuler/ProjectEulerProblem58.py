from mymathfunctions import IsPrime

def SolveProblem(size):
    diagonals = [1]
    found = False
    x = 1
    increaser = 2
    corners = 0
    currentSize = 0
    primesSoFar = 0
    ratio = 1
    while(not found):
        for i in range(currentSize, size * 2 - 2):
            x += increaser
            diagonals.append(x)
            if(IsPrime(x)):
                primesSoFar += 1
            corners += 1
            if(corners == 4):
                corners = 0
                increaser += 2 

        ratio = primesSoFar / len(diagonals)
        #print(size, primesSoFar, len(diagonals), ratio)
        if(ratio <= 0.1):
            found = True 
        size += 2 
        currentSize = len(diagonals)
    
    print("------ Done -------")
    print(size)


SolveProblem(7)


