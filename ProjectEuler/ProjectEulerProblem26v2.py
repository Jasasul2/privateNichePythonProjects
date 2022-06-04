
def AnalyzeReccurence(f):
    cycle = str(f)
    list = []
    checklist = []
    for i in str(f)[2:]:
        list.append(i)
        checklist.append(i)

    reccurenceString = CheckReccurence(list, checklist)
    return reccurenceString

def CheckReccurence(list, dict):
    reccurenceList = []
    for i in dict:
        if(dict.count(i) > 1): 
            reccurenceList.append(i)
        else:
            for l in list: 
                if (l == i):
                    list.remove(l)

    if(len(reccurenceList) > 0):
        recString = ""
        for i in reccurenceList:
            recString += str(i) 
        if(LastReccurenceCheck(list, reccurenceList) == True):
            return(recString)
    
    return("N")

def LastReccurenceCheck(list, reclist):
    reccurence = 0
    print(list)
    print(reclist)
    for i in range(len(list) - len(reclist) + 1):
        reccurenceFound = True
        for r in range(len(reclist)):
            if(list[i + r] != reclist[r]):
                reccurenceFound = False 
        if(reccurenceFound):
            reccurence += 1 
    if(reccurence >= 1):
        return True 
    else:
        return False 

dick = []

for d in range(2, 50):
    x = 1 / d
    print("")
    string = AnalyzeReccurence(x)
    print(str(d) + " " + str(x) + "  " + string)
    if(string != "N"):
        dick.append([d, string])

print("")
print(dick)
maxLen = 0 
maxInt = 0
for d in dick:
    if(len(d[1]) > maxLen):
        maxLen = len(d[1])
        maxInt = d[0]
print(str(maxLen) + " ... " + str(maxInt))
