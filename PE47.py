'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #47
'''

import time
from math import sqrt

def countPrimes(n,k):
    total = 0
    if(n%2==0):
        total+=1
        while(n%2==0):
            n/=2
    c = 3
    while(c<=sqrt(n)):
        if(n%c==0):
            total+=1
            if(total>k):
                return False
            while(n%c==0):
                n/=c
        c+=2
    if(n>1):
        total+=1
    return total == k

def projectEulerProblemFortySeven(n,k):
    c = 14
    streak = 0
    while(streak<n):
        if(countPrimes(c,k)):
            streak+=1
            if(streak==n):
                return (c-n+1)
        else:
            streak = 0
        c+=1
    return "HOW"

start = time.time()
print projectEulerProblemFortySeven(4, 4)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

134043
--- 0.572690010071 seconds ---

for input of n = 4, k = 4
'''
