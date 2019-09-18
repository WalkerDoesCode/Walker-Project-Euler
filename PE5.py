'''
Author: Walker Kroubalkian
Iterative Approach to Project Euler Problem #5
'''

import time
from math import sqrt

def ifPowerGetPrime(n):
    c = 2
    while(c<=sqrt(n)):
        if(n%c==0):
            while(n%c==0):
                n/=c
            if(n>1):
                return -1
            else:
                return c
        c+=1
    return n

def projectEulerProblemFive(n):
    total = 1
    c = 2
    while(c<=n):
        a = ifPowerGetPrime(c)
        if(a>0):
            total*=a
        c+=1
    return total

start = time.time()
print projectEulerProblemFive(20)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

232792560
--- 2.09808349609e-05 seconds ---

for input of n = 20
'''