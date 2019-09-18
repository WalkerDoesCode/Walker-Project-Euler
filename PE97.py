'''
Author: Walker Kroubalkian
Square and Multiply Approach to Project Euler Problem #97
'''

import time

def squareAndMultiply(b,e,m):
    l = bin(e)[2:]
    a = len(l)
    exponents = []
    myExponent = b
    while(len(exponents)<a):
        exponents.append(myExponent)
        myExponent = (myExponent**2)%m
    total = 1
    c = l[::-1]
    for x in range(a):
        if(c[x] == '1'):
            total*=exponents[x]
            total%=m
    return total

def projectEulerProblemNinetySeven(a,b,e,c,m):
    return (a*squareAndMultiply(b, e, m) + c)%m

start = time.time()
print projectEulerProblemNinetySeven(28433, 2, 7830457, 1, 10**10)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

8739992577
--- 5.29289245605e-05 seconds ---

for input of a = 28433, b = 2, e = 7830457, c = 1, m = 10**10
'''