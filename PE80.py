'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #80
'''

import time
from decimal import *
from math import sqrt

getcontext().prec = 200

def sumDigitSquareRoot(n,x):
    a = Decimal(n).sqrt()
    s = str(a)
    t = 0
    for y in range(x+1):
        if(s[y]!="."):
            t+=int(s[y])
    return t

def isSquare(n):
    a = int(sqrt(n))
    return a*a==n

def projectEulerProblemEighty(n,e):
    total = 0
    for c in range(2,n+1):
        if not isSquare(c):
            total+=sumDigitSquareRoot(c, e)
    return total

start = time.time()
print projectEulerProblemEighty(100, 100)
print ("--- %s seconds ---" % (time.time() - start))

'''
Prints

40886
--- 0.00751686096191 seconds ---

for input of n = 100, e = 100.
'''