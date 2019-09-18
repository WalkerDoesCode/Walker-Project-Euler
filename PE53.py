'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #53
'''

import time

def combination(n,r):
    numerator = 1
    denominator = 1
    for x in range(r):
        numerator*=(n-x)
        denominator*=(x+1)
    return numerator/denominator

def projectEulerProblemFiftyThree(n, m):
    total = 0
    for c in range(1,n+1):
        for x in range(0,c/2+1):
            if(combination(c,x)>m):
                total+=(c-2*x+1)
                break
    return total

start = time.time()
print projectEulerProblemFiftyThree(100, 1000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

4075
--- 0.000518083572388 seconds ---

for input of n = 100, m = 1000000
'''