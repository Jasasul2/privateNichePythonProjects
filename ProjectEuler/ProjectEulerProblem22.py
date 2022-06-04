alphabet = { "A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8, "I" : 9, "J" : 10, 
"K" : 11, "L" : 12, "M" : 13, "N" : 14, "O" : 15, "P" : 16, "Q" : 17, "R" : 18, "S" : 19, "T" : 20, "U" : 21, 
"V" : 22, "W" : 23, "X" : 24, "Y" : 25, "Z" : 26 }

totalScore = 0

with open("names.txt", "r") as names:
    content = names.readlines()
    nameList = []
    for line in content:
        nlist = line.split()
        for n in nlist:
            nameList.append(n)

    nameList.sort()
    print(nameList)

    for i in range(len(nameList)):
        skore = 0
        for char in nameList[i]:
            skore += alphabet[char]
        skore *= (i + 1) 
        print(nameList[i] + " has score " + str(skore))
        totalScore += skore

print("TotalScore is " + str(totalScore))
