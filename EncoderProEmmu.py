# Author : Ondřej Maceška 
# Date : 14.11.2020
# Description : Some random code used to generate a ciphered text 
#               to test a decoding algorithm of my friend  

import random 

alphabet = "abcdefghijklmnopqrstuvxywz"
alpha_dict = {}
for i in range(0, len(alphabet)):
    alpha_dict[i] = alphabet[i]

dick_list = [char for char in alphabet]
random.shuffle(dick_list)

code_alpha_dict = {}
x = 0
for dick in dick_list:
    code_alpha_dict[dick] = x
    x += 1

with open("englishtext.txt", "r", encoding = "utf-8") as text:
    input_text = text.read()
    print(input_text)
    print(len(input_text))
    output_text = ""
    input_text = input_text.lower()
    for char in input_text:
        new_char = char
        if(char in dick_list):
            index = code_alpha_dict[char]
            new_char = alpha_dict[index]
        output_text += new_char

    print("")
    print(output_text)