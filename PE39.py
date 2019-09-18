'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #39
'''

import time
from math import sqrt

def listFactors(n):
    primes = []
    exponents = []
    c = 2
    while(c<=sqrt(n)):
        if(n%c==0):
            primes.append(c)
            t = 0
            while(n%c==0):
                n/=c
                t+=1
            exponents.append(t)
        c+=1
    if(n>1):
        primes.append(n)
        exponents.append(1)
    return sorted(listFactorsGivenFactorization(primes, exponents))

def listFactorsGivenFactorization(p,e):
    total = []
    if(len(p) >= 1):
        for x in range(e[0]+1):
            total.append(p[0]**x)
    else:
        return [1]
    previousTotal = listFactorsGivenFactorization(p[1:], e[1:])
    
    actualTotal = []
    for a in total:
        for b in previousTotal:
            actualTotal.append(a*b)
    
    return actualTotal

def countPythagoreanTriples(n):
    if(n%2==1):
        return -1
    found = []
    possibleD = listFactors(n/2)
    n/=2
    for d in possibleD:
        newProduct = n/d
        lowerBound = int(sqrt(newProduct/2))
        upperBound = int(sqrt(newProduct))
        for m in range(lowerBound, upperBound+1):
            if(m>0 and newProduct%m == 0):
                o = newProduct/m-m
                if(0<o<m):
                    triple = sorted([d*(m*m-o*o), 2*d*m*o, d*(m*m+o*o)])
                    if triple not in found:
                        found.append(triple)
    
    return len(found)

def projectEulerProblemThirtyNine(n):
    maximum = 1
    maxIndex = 12
    for c in range(13,n+1):
        v = countPythagoreanTriples(c)
        if(v>maximum):
            maxIndex = c
            maximum = v
    return maxIndex

start = time.time()
print projectEulerProblemThirtyNine(1000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

840
--- 0.00754904747009 seconds ---

for input of n = 1000
'''