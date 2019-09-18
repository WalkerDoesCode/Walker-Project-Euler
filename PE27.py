'''
Author: Walker Kroubalkian
Sieve Approach to Project Euler Problem #27
'''

import time
from math import sqrt

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

def isPrime(n):
    if(n>1 and n<4):
        return True
    if(n%2==0 or n<=1):
        return False
    c = 3
    while(c<=sqrt(n)):
        if(n%c==0):
            return False
        c+=2
    return True

def projectEulerProblemTwentySeven(n):
    bPossible = sieveEratosthenes(n)
    aPossible = sieveEratosthenes(2*n)
    maximumSequence = 40
    maxA = 1
    maxB = 41
    for x in bPossible:
        for y in aPossible:
            if abs(y - x - 1)>=n:
                break
            b = x
            a = y-x-1
            i = 2
            while(True):
                if(isPrime(i*i+a*i+b)):
                    i+=1
                else:
                    break
            if(i>maximumSequence):
                maximumSequence = i
                maxA = a
                maxB = b
    return maxA*maxB

start = time.time()
print projectEulerProblemTwentySeven(1000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

-59231
--- 0.0769238471985 seconds ---

for input of n = 1000
'''