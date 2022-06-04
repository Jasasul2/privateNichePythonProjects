import math 
from mymathfunctions import ReturnIntArray
import time

TARGET = 6

def analyze(n):
    base_array = ReturnIntArray(n)
    ok = True; 
    for multiple in range(1, TARGET):
        ok = check_multiple(base_array, n * (multiple + 1))
        if(ok == False):
            break 
    return ok    

def check_multiple(base_array, multiple):
    multiple_array = ReturnIntArray(multiple)

    if(set(multiple_array) != set(base_array)):
        return False
    
    return True 

i = 0
finished = False
while(finished == False):
    i += 1
    finished = analyze(i)


print("done ", i)