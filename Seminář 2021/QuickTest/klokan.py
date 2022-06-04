array = []
for i in range(1, 1001):
    array.append(i)

for x in range(len(array) - 2):
    add = array[x] + array[x + 1] + array[x + 2] 
    print(x)
