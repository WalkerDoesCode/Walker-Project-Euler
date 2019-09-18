'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #56
'''

import time

def sumDigits(x):
    a = str(x)
    total = 0
    for c in a:
        total+=int(c)
    return total

def projectEulerProblemFiftySix(n):
    maximum = -1
    for a in range(1,n):
        p = 1
        for b in range(1,n):
            p*=a
            v = sumDigits(p)
            if(v>maximum):
                maximum = v
    return maximum

start = time.time()
print projectEulerProblemFiftySix(100)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

972
--- 0.279350042343 seconds ---

for input of n = 100.
'''