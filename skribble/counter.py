with open("seznam_slov.txt", "r", encoding = "utf-8") as file:
    x = file.read()
    list = x.split()
    print(len(list))