import math 
from decimal import *

def AnalyzeReccurence(f):
    cycle = str(f)
    list = []
    dict = {}
    for i in str(f)[2:]:
        list.append(i)
        if(i in dict):
            dict[i] += 1 
        else:
            dict[i] = 1

    reccurenceLenght = CheckReccurence(list, dict)
    return reccurenceLenght

def CheckReccurence(list, dict):
    reccurenceList = []
    for i in dict:
        if(dict[i] > 1): 
            reccurenceList.append(i)
        else:
            for l in list: 
                if (l == i):
                    list.remove(l)

    guess = 1
    maxLen = math.floor(len(list) / 2)
    for x in range(2, maxLen):
        if list[0:x] == list[x:2*x] :
            return x

    return guess - 1

dick = []

for d in range(2, 1000):
    getcontext().prec = 10000
    x = Decimal(1) / Decimal(d)
    #print("")
    lenght = AnalyzeReccurence(x)
    #print(str(d) + " " + str(x) + "  " + str(lenght))
    if(lenght > 1):
        dick.append([d, lenght])

print("")
print(dick)
maxLen = 0 
maxInt = 0
for d in dick:
    if(d[1] > maxLen):
        maxLen = d[1]
        maxInt = d[0]

print(str(maxLen) + " ... " + str(maxInt))
