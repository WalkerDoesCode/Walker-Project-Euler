'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #12
'''

import time
from math import sqrt

def numberDivisors(n):
    total = 1
    c = 2
    while(c<=sqrt(n)):
        if(n%c==0):
            t = 0
            while(n%c==0):
                n/=c
                t+=1
            total*=(t+1)
        c+=1
    if(n>1):
        total*=2
    return total

def projectEulerProblemTwelve(n):
    last = 1
    if(n==1):
        return 1
    c = 3
    while(True):
        if(c%2==0):
            a = numberDivisors(c/2)
        else:
            a = numberDivisors(c)
        if(a*last>n):
            return c*(c-1)/2
        last = a
        c+=1

start = time.time()
print projectEulerProblemTwelve(500)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

76576500
--- 0.0434160232544 seconds ---

for input of n=500
'''