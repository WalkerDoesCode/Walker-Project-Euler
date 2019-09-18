'''
Author: Walker Kroubalkian
Sieve Approach to Project Euler Problem #7
'''

import time
from math import log

def sieveEratosthenes(n):
    myPrimes = []
    
    primePossible = [True]*(n+1)
    primePossible[0] = False
    primePossible[1] = False
    
    for (i,possible) in enumerate(primePossible):
        if possible:
            for x in range(i*i, (n+1), i):
                primePossible[x] = False
            myPrimes.append(i)

    return myPrimes

def projectEulerProblemSeven(n):
    if(n==1):
        return 2
    elif(n==2):
        return 3
    elif(n==3):
        return 5
    pntLimit = int(n*(log(n)+log(log(n))))
    allPossible = sieveEratosthenes(pntLimit)
    return allPossible[n-1]

start = time.time()
print projectEulerProblemSeven(10001)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

104743
--- 0.0170910358429 seconds ---

for input of n = 10001
'''