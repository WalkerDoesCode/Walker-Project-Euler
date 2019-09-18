'''
Author: Walker Kroubalkian
Semi-Sieve Approach to Project Euler Problem #21
'''

import time
from math import sqrt

def addProperDivisors(n):
    temp = n
    p = []
    e = []
    c = 2
    while(c<=sqrt(n)):
        if(n%c==0):
            t = 0
            while(n%c==0):
                n/=c
                t+=1
            p.append(c)
            e.append(t)
        c+=1
    if(n>1):
        p.append(n)
        e.append(1)
    total = 1
    powers = len(p)
    for x in range(powers):
        powerSum = 0
        for i in range(e[x]+1):
            powerSum+=(p[x]**i)
        total*=powerSum
    return total - temp

def projectEulerProblemTwentyOne(n):
    sums = [0]*n
    i = 1
    while(i<=n/2):
        for c in range(2*i, n, i):
            sums[c]+=i
        i+=1
    
    total = 0
    potential = []
    for x in range(n):
        value = sums[x]
        if(value>=n):
            potential.append(x)
        elif(value>0 and value!=x and sums[value] == x):
            total+=x
    
    for x in potential:
        if(addProperDivisors(addProperDivisors(x)) == x):
            total+=x

    return total

start = time.time()
print projectEulerProblemTwentyOne(10000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

31626
--- 0.0148520469666 seconds ---

for input of n=10000
'''