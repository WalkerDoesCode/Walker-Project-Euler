'''
Author: Walker Kroubalkian
Sieve Approach to Project Euler Problem #10
'''

import time

def sieveEratosthenes(n):
    myPrimes = []
    
    primePossible = [True]*(n+1)
    primePossible[0] = False
    primePossible[1] = False

    for (i,possible) in enumerate(primePossible):
        if(possible):
            for x in range(i*i, (n+1), i):
                primePossible[x] = False
            myPrimes.append(i)

    return myPrimes

def projectEulerProblemTen(n):
    allPrimes = sieveEratosthenes(n)
    total = 0
    for p in allPrimes:
        total+=p
    return total
    

start = time.time()
print projectEulerProblemTen(2000000)
print ("--- %s seconds ---" % (time.time() - start))

'''
Prints

142913828922
--- 0.402328968048 seconds ---

for input of n=2000000
'''