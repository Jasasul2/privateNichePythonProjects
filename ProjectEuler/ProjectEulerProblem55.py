
mapOfPotentialPalindromes = []
mapOfPotentialLychrelness = []

def GetReversedNumber(n):
    m = [char for char in str(n)]
    m.reverse()
    x = ""
    for digit in m:
        x += digit
    x = int(x)
    return x

def IsPalindrome(n):
    if(n == GetReversedNumber(n)):
        return True
    return False

def CheckForLychrelness(n, iteration = 1):
    global mapOfPotentialLychrelness
    global mapOfPotentialPalindromes

    if(iteration >= 50):
        return True 

    if(IsPalindrome(n) and iteration != 1):
        return False 

    m = GetReversedNumber(n)
    x = m + n
    return CheckForLychrelness(x, iteration + 1)

lychrel = 0
for i in range(10000):
    if(CheckForLychrelness(i) == True):
        lychrel += 1
    

print("DONE!!!")
print(lychrel)