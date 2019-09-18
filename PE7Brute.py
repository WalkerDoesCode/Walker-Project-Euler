'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #7
'''

import time
from math import sqrt

def isPrime(n):
    c = 2
    while(c<=sqrt(n)):
        if(n%c==0):
            return False
        c+=1
    return True

def projectEulerProblemSeven(n):
    total = 0
    c = 2
    while(total<n):
        if(isPrime(c)):
            total+=1
        c+=1
    return c-1

start = time.time()
print projectEulerProblemSeven(100)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

104743
--- 0.310272932053 seconds ---

for input of n = 10001
'''