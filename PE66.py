'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #66
'''

import time
from math import sqrt
from decimal import *

getcontext().prec = 74

def isSquare(n):
    a = int(sqrt(n))
    return a*a==n

def gcd(a,b):
    if(a<0 or b<0):
        return gcd(abs(a),abs(b))
    if(min(a,b)==0):
        return max(a,b)
    if(a>b):
        return gcd(b,a%b)
    return gcd(a,b%a)

def continuedFractionDenominators(n,x):
    a = Decimal(n).sqrt()
    denominators = []
    while(len(denominators)<x):
        v = int(a)
        denominators.append(v)
        a = Decimal(1.)/(a-Decimal(v))
    return denominators

def evaluateContinuedFraction(n,x):
    a = continuedFractionDenominators(n, x)
    b = a[::-1]
    curNumerator = 1
    curDenominator = 0
    for x in b:
        n = curDenominator + curNumerator*x
        d = curNumerator
        g = gcd(n,d)
        curNumerator = n/g
        curDenominator = d/g
    return [curNumerator,curDenominator]


def projectEulerProblemSixtySix(n):
    maxFound = 3
    maxIndex = 2
    for c in range(3,n+1):
        if(not isSquare(c)):
            d = 2
            while(True):
                e = evaluateContinuedFraction(c, d)
                f = e[0]
                g = e[1]
                if(f*f-c*g*g==1):
                    if(f>maxFound):
                        maxFound = f
                        maxIndex = c
                    break
                d+=1
    return maxIndex

start = time.time()
print projectEulerProblemSixtySix(1000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

661
--- 4.85595107079 seconds ---

for input of n = 1000
'''