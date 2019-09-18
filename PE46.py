'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #46
'''

import time
from math import sqrt
from math import ceil

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

def projectEulerProblemFortySix(n):
    total = 0
    c = 15
    current = -1
    while(total<n):
        if(not isPrime(c)):
            a = 1
            found = False
            while(a<=ceil(sqrt(c/2))):
                if isPrime(c-2*a*a):
                    found = True
                    break
                a+=1
            if not found:
                total+=1
                current = c
        c+=2
    return current

start = time.time()
print projectEulerProblemFortySix(2)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

5777
--- 0.0163691043854 seconds ---

for input of n = 1
'''