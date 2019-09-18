'''
Author: Walker Kroubalkian
The Iterative Approach to Project Euler Problem #1
'''

import time

def projectEulerProblemOne(n):
    total = 0
    for i in range(1,n):
        if(i%3==0 or i%5==0):
            total+=i
    return total

start = time.time()
print projectEulerProblemOne(1000)
print("--- %s seconds ---" % (time.time() - start))

'''
Prints

233168
--- 0.000103950500488 seconds ---

for input of n = 1000
'''