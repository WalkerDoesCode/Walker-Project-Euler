'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #30
'''

import time

def sumDigitPower(n,p):
    total = 0
    a = str(n)
    for x in a:
        total+=(int(x)**p)
    return total

def projectEulerProblemThirty(p):
    a = 1
    while((10**a) - 1 <= a*(9**p)):
        a+=1
    total = 0
    for x in range(2,(9**p)*a+1):
        if(x == sumDigitPower(x,p)):
            print x
            total+=x
    return total


start = time.time()
print projectEulerProblemThirty(5)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

443839
--- 0.88481593132 seconds ---

for input of p = 5
'''