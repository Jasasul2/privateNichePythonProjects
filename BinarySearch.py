# Author : Ondřej Maceška 
# Date : 8.8.2020
# Description : naive implementation of the binary search algorithm

arr = []
for i in range(100000):
    arr.append(i)

target = 515

def search(array, target):
    steps = 0
    l = 0
    r = len(array) - 1
    while (l <= r):
        steps += 1
        index = round((l + r) / 2)
        choice = array[index]
        if (choice == target):
            print("steps: " + str(steps))
            return index
        elif target < choice:
            r = index - 1
        else:
            l = index + 1
        print("Index of " + str(choice) + " is " + str(index))
    return -1


print("Index of " + str(target) + " is " + str(search(arr, target)))
