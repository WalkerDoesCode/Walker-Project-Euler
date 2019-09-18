'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #71
'''

import time

def projectEulerProblemSeventyOne(d,a,b):
    c = d
    while(c*a%b!=1):
        c-=1
    return (c*a-1)/b

start = time.time()
print projectEulerProblemSeventyOne(1000000, 3, 7)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

428570
--- 9.77516174316e-06 seconds ---

for input of d = 1000000, a = 3, b = 7.
'''