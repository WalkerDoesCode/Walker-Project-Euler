'''
Author: Walker Kroubalkian
Sieve Approach to Project Euler Problem #37
'''

import time

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

    return [primePossible,myPrimes]

def projectEulerProblemThirtySeven(n):
    allPrimeInfo = sieveEratosthenes(n)
    primePossible = allPrimeInfo[0]
    myPrimes = allPrimeInfo[1]
    
    truncatablePrimes = []
    
    for p in myPrimes:
        if(p>10):
            s = str(p)
            found = False
            for i in range(1,len(s)):
                if((not primePossible[int(s[i:])]) or (not primePossible[int(s[0:i])])):
                    found = True
                    break
            if not found:
                truncatablePrimes.append(p)
    
    if(len(truncatablePrimes)==11):
        total = 0
        for x in truncatablePrimes:
            total+=x
        return total
    else:
        return -1

start = time.time()
print projectEulerProblemThirtySeven(1000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

748317
--- 0.2643699646 seconds ---

for input of n = 1000000
'''