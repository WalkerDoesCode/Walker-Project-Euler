'''
Author: Walker Kroubalkian
Engineer's Induction Approach to Project Euler Problem #58
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

def projectEulerProblemFiftyEight(p):
    total = 5
    found = 3
    c = 3
    while(found*100>=total*p):
        t = c*c+c+1
        for a in range(3):
            if isPrime(t):
                found+=1
            total+=1
            t+=(c+1)
        total+=1
        c+=2
    return c

start = time.time()
print projectEulerProblemFiftyEight(10)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

26241
--- 3.82181882858 seconds ---

for input of p = 10
'''