
#values = [200, 100, 50, 20, 10, 5, 2, 1]
values = [1, 2, 5, 10, 20, 50, 100, 200]

targetValue = 200

def Combine(remainingValue, ran):
    waysToSolve = 0
    for i in range(ran, len(values)): 
        subst = remainingValue - values[i]
        if(subst) > 0:
            waysToSolve += Combine(subst, i)
        elif (subst) == 0:
            waysToSolve += 1 
            return waysToSolve 
    return waysToSolve

print(Combine(targetValue, 0))