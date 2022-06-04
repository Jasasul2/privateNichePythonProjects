# Author : Ondřej Maceška 
# Date : 20.10.2020
# Description : Encodes a given string with the ability to decode it 

import math 
import random

index = 0
alphabetString = "a]b0cBd1CeůD2fEóšg3F÷×h G(4ůiHjI5k*/-+Jl6KmL7čnM[ož8NýpOqř9PrěQsRt;SéuTvU)wVxX_:.,yYzZ"
alphabet = {}
reversedAlphabet = {} 
for char in alphabetString:
    alphabet[char] = index
    reversedAlphabet[index] = char
    index += 1 

def Move(list, value):
    newlist = []
    for char in list:
        if(char in alphabet):
            index = alphabet[char]
            index += value
            correctIndex = index
            if(index >= len(reversedAlphabet)):
                correctIndex = index - len(reversedAlphabet)
            elif(index < 0):
                correctIndex = index + len(reversedAlphabet)
            char = reversedAlphabet[correctIndex]
        newlist.append(char)
    return newlist

def GetString(list):
    string = ""
    for char in list:
        string += char
    return string 

def SwitchUpper(list):
    for i in range(len(list)):
        char = list[i]
        if(char.isupper() == True):
            list[i] = char.lower()
        elif(char.islower() == True):
            list[i] = char.upper()
    return list 

def Encode(message):
    chars = [char for char in message]
    #step 1 - check parity 
    if(len(message) % 2 != 0):
        chars.insert(0, " ")

    #step 2 - split in halves 
    firstHalf = chars[0 : math.floor(len(chars) / 2)]
    secondHalf = chars[math.floor(len(chars) / 2) : len(chars)]

    #step 3 - moves symbols in halves by their randomMoveIndexes 
    moveIndex1 = random.randint(1, 9)
    moveIndex2 = random.randint(1, 9)
    firstHalf = Move(firstHalf, moveIndex1)
    secondHalf = Move(secondHalf, moveIndex2)

    #step 4 - splits halves into quarters 
    firstQuarter = firstHalf[0 : math.floor(len(firstHalf) / 2)]
    secondQuarter = firstHalf[math.floor(len(firstHalf) / 2) : len(firstHalf)]
    thirdQuarter = secondHalf[0 : math.floor(len(secondHalf) / 2)]
    fourthQuarter = secondHalf[math.floor(len(secondHalf) / 2) : len(secondHalf)]

    #step 4 - rearranges the quarters (4 - 2 - 3 - 1) instead of (1 - 2 - 3 - 4)
    #step 4.5 - switch lowercase and uppercase letters 
    s1 = GetString(SwitchUpper(firstQuarter))
    s2 = GetString(SwitchUpper(secondQuarter))
    s3 = GetString(SwitchUpper(thirdQuarter))
    s4 = GetString(SwitchUpper(fourthQuarter))
    #step 5 - add moveIndexes on the start and end 
    string = str(moveIndex1) + s4 + s2 + s3 + s1 + str(moveIndex2)
    print("ciphered message: ", string)
    return(string)

def Decode(cipher):
    #print("message to decipher: ", cipher)
    #step 1 - turn cipher into list, get move indexes and remove them 
    list = [char for char in cipher]
    moveIndex1 = -1 * int(list[0])
    moveIndex2 = -1 * int(list[-1])
    newList = list[1 : len(list) - 1]
    charCount = len(newList)
    
    #step 2 - split into halves or quarters, change uppercase/lowercase, move and concacenate 
    string = ""
    if(charCount == 2):
        firstHalf = Move(SwitchUpper([newList[1]]), moveIndex1)
        secondHalf = Move(SwitchUpper([newList[0]]), moveIndex2)
        string = GetString(firstHalf) + GetString(secondHalf)
    else:
        splitter = math.ceil(charCount / 4)
        splitter2 = 0
        if(charCount % 4 != 0): #asymetric 
            splitter2 = splitter - 1
        else:
            splitter2 = splitter 
        fourthQuarter = Move(SwitchUpper(newList[0 : splitter]), moveIndex2)
        secondQuarter = Move(SwitchUpper(newList[splitter : splitter * 2]), moveIndex1)
        thirdQuarter = Move(SwitchUpper(newList[splitter * 2 : splitter * 2 + splitter2]), moveIndex2)
        firstQuarter = Move(SwitchUpper(newList[splitter * 2 + splitter2 : len(newList)]), moveIndex1)
        string = GetString(firstQuarter) + GetString(secondQuarter) + GetString(thirdQuarter) + GetString(fourthQuarter)

    print("                                                                                 (deciphered message:", string, ")")
    return string 

while(True):
    string = str(input("enter your message: "))
    cipher = Encode(string)
    Decode(cipher)
    print("")
    print("")

