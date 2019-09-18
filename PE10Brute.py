'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #10
'''

import time
from math import sqrt

def isPrime(x):
    c = 2
    while(c<=sqrt(x)):
        if(x%c==0):
            return False
        c+=1
    return True

def projectEulerProblemTen(n):
    total = 0
    for x in range(2,n):
        if isPrime(x):
            total+=x
    return total

start = time.time()
print projectEulerProblemTen(2000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

142913828922
--- 17.6438319683 seconds ---

for input of n = 2000000.
'''