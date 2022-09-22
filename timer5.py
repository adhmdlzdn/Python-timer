# Simple Measure Program Execution Time 1.1
# Original Code by Udacity (https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html)

import time, math, random

def binary_search(arr, target):
    arr.sort()

    left = 0
    right = len(arr)

    while left <= right:
        mid = math.floor((left + right) / 2)

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return arr.index(target)

our_list = list(range(1000000))
element = 789879

start = time.time()

binary_search(our_list, element)

end = time.time()

print(end - start)