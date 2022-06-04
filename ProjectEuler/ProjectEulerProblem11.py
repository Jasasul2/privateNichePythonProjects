import numpy as np

def GetProduct(fourNumbers):
    product = 1
    for i in fourNumbers:
        product *= i
    return product 

def HorizontalSearch(line):
    products = []
    for number in range(len(line)): 
        if(number < rowsize - 2):
            products.append(GetProduct(line[number:number + 4]))
    return products

with open("grid.txt", "r") as test_file:
    content = test_file.readlines()
    rowsize = 20
    array = np.ndarray(shape = (rowsize, rowsize), dtype = int)
    for y in range(len(content)): 
        line = content[y].split()
        for x in range(len(line)): 
            array[y][x] = line[x]
    #print(array)

    largestProducts = []
    listToCheck = []

    for y in range(rowsize):
        largestProducts.append(max(HorizontalSearch(array[y]))) #horizontal check 
        lineToCheck1 = []
        lineToCheck2 = []
        for x in range(rowsize):
            lineToCheck1.append(array[x, y]) #vertical check 
        listToCheck.append(lineToCheck1)

    for y in range(rowsize): #Diagonals 
        listToCheck.append(array.diagonal(y).tolist()) 
        listToCheck.append(array.diagonal(-y).tolist())
        listToCheck.append(np.fliplr(array).diagonal(y).tolist())
        listToCheck.append(np.fliplr(array).diagonal(-y).tolist())

    print(listToCheck)
    for lines in listToCheck:
        largestProducts.append(max(HorizontalSearch(lines)))

    print(str(max(largestProducts)))





