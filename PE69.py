'''
Author: Walker Kroubalkian
Mathematical Approach to Project Euler Problem #69
'''

import time
from math import sqrt

def isPrime(n):
    if(n<=1):
        return False
    if(n<4):
        return True
    if(n%2==0):
        return False
    c = 3
    while(c<=sqrt(n)):
        if(n%c==0):
            return False
        c+=2
    return True

def projectEulerProblemSixtyNine(n):
    total = 1
    c = 2
    while(total<=n):
        if(isPrime(c)):
            if(total*c>n):
                return total
            total*=c
        c+=1
    return total

start = time.time()
print projectEulerProblemSixtyNine(1000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

510510
--- 1.90734863281e-05 seconds ---

for input of n = 1000000
'''