from mymathfunctions import ReturnIntArray 

def ReturnBinaryNum(n):
    return bin(n)[2:]

def CheckPalindrome(array):
    reversedArray = array[:]
    reversedArray.reverse()
    if(array == reversedArray):
        return True 
    return False 

totalSum = 0 
for i in range(0, 1000000):
    if(CheckPalindrome(ReturnIntArray(i)) == True):
        if(CheckPalindrome(ReturnIntArray(ReturnBinaryNum(i))) == True):
            totalSum += i 

print(totalSum)

