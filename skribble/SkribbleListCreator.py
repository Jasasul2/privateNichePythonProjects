# Author : Ondřej Maceška 
# Date : 30.11.2020
# Description : Used to generate a list of words for an online game https://skribbl.io

import random 

abeceda = "ABCDEFGHJKLMNOPQRSTUVXYZW"
shit_to_remove = ["chlor", "fosfát", "metyl", "propyl", "butyl", "brom", "methyl", "uhl", "fluor", "oxid"]

sex = 1500

adjective_modifiers = ["ne", "polo", "anti"]

with open("all_words_updated.txt", "w", encoding = "utf-8") as new_words: 
    with open("female_words.txt", "r",  encoding = "utf8") as female_file:
        with open("all_words.txt", "r",  encoding = "utf8") as all_file:
            with open("male_words.txt", "r",  encoding = "utf8") as male_file:
                with open("adjectives.txt", "r", encoding = "utf8") as adjectives_file:
                    content1 = female_file.read()
                    female_words = content1.split()
                    content2 = male_file.read()
                    male_words = content2.split()
                    adjectives_content = adjectives_file.read()
                    adjectives = adjectives_content.split()

                    random_female_words = random.sample(female_words, int(sex/2))
                    for female_word in random_female_words:
                        if(random.randint(0, 1) == 0):
                            adjective = random.choice(adjectives)
                            split_adjective = [char for char in adjective]

                            if(split_adjective[-1] == "ý"):
                                adjective = adjective[:-1] + "á"

                            if(random.randint(0, 6) == 0):
                                adjective = random.choice(adjective_modifiers) + adjective 
                            female_word = adjective + " " + female_word
                        if(len(female_word) <= 30):
                            new_words.write(female_word + ",\n")


                    random_male_words = random.sample(male_words, int(sex/2))
                    for male_word in random_male_words:
                        if(random.randint(0, 1) == 0):
                            adjective = random.choice(adjectives)
                            split_adjective = [char for char in adjective]

                            if(random.randint(0, 6) == 0):
                                adjective = random.choice(adjective_modifiers) + adjective 
                            male_word = adjective + " " + male_word

                        new_words.write(male_word + ",\n")

                """                     creating different lists
                print(len(words))
                for word in words:
                    to_be_removed = False
                    for shit in shit_to_remove:
                        if(shit in word):
                            to_be_removed = True 

                    if(to_be_removed == True):
                        continue
        
                    split_word = [char for char in word]
                    s = split_word[-1]
                    if(s == "a" or s == "e" or s == "ě" or s == "ž" or s == "ť" or s == "y" or (s == "č" and split_word[-2] == "u") or (s == "ř" and split_word[-2] == "ě")):
                        female_file.write(word + "\n")
                    else:
                        male_file.write(word + "\n")
                """

print("Done")