import inflect
p = inflect.engine()

wordCount = 1001
letterCount = 0

for i in range(1, wordCount):
    words = p.number_to_words(i).split()
    for word in words:
        for letter in word:
            if(letter != "-"):
                letterCount += 1 
    print(word)

print("letter count:" + str(letterCount))