'''
Author: Walker Kroubalkian
Sieve Approach to Project Euler Problem #87
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

def projectEulerProblemEightySeven(n):
    primes = sieveEratosthenes(int(sqrt(n)))
    squares = []
    cubes = []
    fourths = []
    cubeDone = False
    fourthDone = False
    for p in primes:
        squares.append(p*p)
        if not cubeDone:
            c = p*p*p
            if(c>n):
                cubeDone = True
            else:
                cubes.append(c)
        if not fourthDone:
            f = p*p*p*p
            if(f>n):
                fourthDone = True
            else:
                fourths.append(f)
    found = [False]*(n+1)
    for a in squares:
        for b in cubes:
            if (b+a)>n:
                break
            for c in fourths:
                s = a+b+c
                if s>n:
                    break
                else:
                    found[s] = True
    total = 0
    for x in found:
        if x:
            total+=1
    return total
                

start = time.time()
print projectEulerProblemEightySeven(50000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

1097343
--- 0.985231161118 seconds ---

for input of n = 50000000.
'''