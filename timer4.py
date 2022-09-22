# Simple Measure Program Execution Time 1.2
# Original Code by Udacity (https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html)

import time 

our_list = list(range(1000000))
element = 898989

start = time.time()

for el in our_list:
    if el == element:
        break

end = time.time()
print(end - start)