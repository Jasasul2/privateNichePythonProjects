import math 

with open("laaaargenumbers.txt", "r") as file:
    content = file.readlines()
    targetNumber = 0
    for line in content:
        targetNumber += (int(line))
    print(targetNumber)
    



