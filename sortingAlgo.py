# Author : Ondřej Maceška
# Date : 11.5.2021
# Description : Some sorting algorithms which get an array and return a sorted version


def bubble_sort(array):
    """bubble sort 

    Args:
        array (int[ ]) : input array

    Returns:
        int[ ] : sorted array
    """
    sortedIndex = len(array)
    while(sortedIndex > 0):
        for i in range(sortedIndex - 1):
            a = array[i]
            b = array[i + 1]
            if(a > b):
                array[i] = b
                array[i + 1] = a
        sortedIndex -= 1
    return array


def select_sort(array):
    """selection sort 

    Args:
        array (int[ ]) : input array

    Returns:
        int[ ] : sorted array
    """
    y = 0
    for y in range(len(array)):
        x = array[0]
        index = 0
        for i in range(len(array) - y):
            num = array[i]
            if(num > x):
                x = num
                index = i
        switchedNum = array[-1 - y]
        array[-1 - y] = x
        array[index] = switchedNum 
    return array 

