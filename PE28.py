'''
Author: Walker Kroubalkian
Engineer's Induction Approach to Project Euler Problem #28
'''

import time

def projectEulerProblemTwentyEight(n):
    total = 1
    layers = (n+1)/2
    last = 4
    for i in range(1,layers):
        last = last + (32*i-12)
        total+=last
    return total

start = time.time()
print projectEulerProblemTwentyEight(1001)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

669171001
--- 4.72068786621e-05 seconds ---

for input of n = 1001
'''