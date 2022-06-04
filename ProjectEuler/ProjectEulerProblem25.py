
def CountDigits(n):
    return len(str(n))

n1 = 1 
n2 = 1
n3 = 0
index = 3

while(CountDigits(n3) != 1000):
    n3 = n1 + n2
    n1 = n2
    n2 = n3 
    index += 1 

print("------")
print(CountDigits(n3))
print(index)


