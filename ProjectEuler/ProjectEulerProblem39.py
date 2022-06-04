
import math   

def CalculateCombinationsForTrainglesInRange(n):
    triangles = {}
    for a in range(1, math.floor(n / 2)):
        for b in range(a, math.floor(n / 2)):
            pythagoras = (a ** 2 + b ** 2) ** (1 / 2)
            for c in range(b, math.floor(n / 2)):
                perimeter = a + b + c
                if pythagoras == c and perimeter <= n:
                    if triangles.get(perimeter): triangles[perimeter] += 1
                    else: triangles[perimeter] = 1
    return triangles

tris = CalculateCombinationsForTrainglesInRange(1000)
mx = max(tris.values())
for k in tris:
    if tris[k] == mx: print(k)