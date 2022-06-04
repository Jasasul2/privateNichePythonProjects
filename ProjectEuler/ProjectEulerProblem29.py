
border = 100 
list = []
for a in range(2, border + 1):
    for b in range(2, border + 1):
        result = a ** b
        if(result not in list):
            list.append(result)

list.sort()
print("there are " + str(len(list)) + " different shit numbers")