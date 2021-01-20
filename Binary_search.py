#二分探索

my_list = []
for i in range(100000000):
    my_list.append(i)

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) //2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1

    return None



#Numpyを使用した場合

import numpy as np

my_list = np.array([i for i in range(100000000)])

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) //2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1

    return None

