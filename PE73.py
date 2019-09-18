'''
Author: Walker Kroubalkian
Euclidean Algorithm Approach to Project Euler Problem #73
'''

import time

def gcd(a,b):
    if(min(a,b)==0):
        return max(a,b)
    if(a>b):
        return gcd(b,a%b)
    return gcd(a,b%a)

def projectEulerProblemSeventyThree(n):
    total = 0
    for x in range(2,n+1):
        c = 1
        while(c*3<=x):
            c+=1
        while(c*2<x):
            if(gcd(c,x)==1):
                total+=1
            c+=1
    return total

start = time.time()
print projectEulerProblemSeventyThree(12000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

7295372
--- 20.5218679905 seconds ---

for input of n = 12000.
'''