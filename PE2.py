'''
Author: Walker Kroubalkian
Iterative Approach to Project Euler Problem #2
'''

import time

def projectEulerProblemTwo(n):
    total = 0
    first = 1
    second = 1
    while(second<=n):
        temp = second
        second+=first
        first = temp
        if(first%2==0):
            total+=first
    return total

start = time.time()
print projectEulerProblemTwo(4000000)
print("--- %s seconds ---" % (time.time() - start))

'''
Prints

4613732
--- 1.21593475342e-05 seconds ---

for input of n = 4000000
'''