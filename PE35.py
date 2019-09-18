'''
Author: Walker Kroubalkian
Sieve Approach to Project Euler Problem #35
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

def projectEulerProblemThirtyFive(n):
    allPrimeInfo = sieveEratosthenes(n)
    primePossible = allPrimeInfo[0]
    myPrimes = allPrimeInfo[1]
    
    total = 0
    
    for myPrime in myPrimes:
        theString = str(myPrime)
        found = False
        for x in range(len(theString)):
            if(not primePossible[int(theString[x:]+theString[0:x])]):
                found = True
                break
        if(not found):
            total+=1
    return total

start = time.time()
print projectEulerProblemThirtyFive(1000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

55
--- 0.270114898682 seconds ---

for input of n = 1000000
'''