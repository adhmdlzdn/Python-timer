# Simple Measure Program Execution Time 1.1
# Original Code by Udacity (https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html)

import time, random

our_list = list(range(10000000))
element = 9999999

start = time.time()

random_choice = random.choice(our_list)
while random_choice != element:
    random_choice = random.choice(our_list)

end = time.time()

print(end - start)