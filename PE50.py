'''
Author: Walker Kroubalkian
Sieve Approach to Project Euler Problem #50
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

    return myPrimes

def projectEulerProblemFifty(n):
    allPrimes = sieveEratosthenes(n)
    maxPrime = 41
    c = 7
    while(c<=n):
        total = 0
        for x in range(c):
            total+=allPrimes[x]
        if(total>n):
            return maxPrime
        if(total in allPrimes):
            maxPrime = total
        a = c
        while(a<n):
            total+=allPrimes[a]
            total-=allPrimes[a-c]
            if(total > n):
                break
            elif(total in allPrimes):
                maxPrime = total
            a+=1
        c+=1
    return maxPrime

print projectEulerProblemFifty(1000000)