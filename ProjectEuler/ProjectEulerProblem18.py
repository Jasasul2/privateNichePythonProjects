def ScanPartOfTheTree(index, x):
    sum1, sum2 = 0, 0

    if(index < len(trianglist)):
        choices = trianglist[index][x : x + 2]
        sum1 += choices[0] + ScanPartOfTheTree(index + 1, x)
        sum2 += choices[1] + ScanPartOfTheTree(index + 1, x + 1)
        return max(sum1, sum2)
    else:
        return 0

with open("triangle.txt", "r") as file:
    triangle = file.readlines()
    trianglist = []
    for line in triangle:
        lineList = line.split()
        trianglist.append(list(map(int, lineList)))
        print(list(map(int, lineList)))

    totalSum = trianglist[0][0]
    totalSum += ScanPartOfTheTree(1, 0)

    print(totalSum)

