def GetDigitSum(n):
    x = [char for char in str(n)]
    y = 0
    for digit in x:
        y += int(digit)
    
    return y 

maximum = 0

print("STARTED")
for a in range(100):
    for b in range(100):
        z = GetDigitSum(a ** b)
        if(z > maximum):
            maximum = z

print(maximum)
