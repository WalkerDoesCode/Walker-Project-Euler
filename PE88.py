'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #88
'''

import time
from math import sqrt

def projectEulerProblemEightyEight(n):
    answers = [0]*(n+1)
    factorizations = [[],[],[[2]],[[3]],[[2,2],[4]]]
    for c in range(5,2*n+1):
        factors = []
        for x in range(2,int(sqrt(c))+1):
            if(c%x==0):
                a = factorizations[c/x]
                for p in a:
                    possible = True
                    for z in p:
                        if z<x:
                            possible = False
                            break
                    if possible:
                        t = p[:]
                        t.append(x)
                        factors.append(sorted(t))
        factors.append([c])
        factorizations.append(factors)
    for x in range(4,2*n+1):
        factors = factorizations[x]
        for p in factors:
            t = 0
            for y in p:
                t+=y
            if(len(p)>1 and t<=x):
                i = len(p)+x-t
                if(i<=n):
                    v = answers[i]
                    if(v==0):
                        answers[i] = x
    found = []
    total = 0
    for x in answers:
        if x not in found:
            total+=x
            found.append(x)
    return total

start = time.time()
print projectEulerProblemEightyEight(12000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

7587457
--- 0.840548992157 seconds ---

for input of n = 12000
'''